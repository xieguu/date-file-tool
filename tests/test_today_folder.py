from concurrent.futures import ThreadPoolExecutor
from datetime import date
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from threading import Barrier
import unittest


ROOT = Path(__file__).resolve().parents[1]
PS_SCRIPT = "创建今日文件夹.ps1"
BAT_SCRIPT = "创建今日文件夹.bat"
TODAY = f"{date.today():%Y.%m.%d}"


class EntryPointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scratch = TemporaryDirectory(prefix="today-folder-tests-")
        cls.addClassCleanup(cls.scratch.cleanup)
        cls.base = Path(cls.scratch.name)
        cls.scripts = cls.base / "脚本 [scripts] & tools"
        cls.scripts.mkdir()
        cls.caller = cls.base / "caller"
        cls.caller.mkdir()
        for name in ("main.py", PS_SCRIPT, BAT_SCRIPT):
            shutil.copy2(ROOT / name, cls.scripts / name)
        cls.entries = ("python", "powershell", "bat") if os.name == "nt" else ("python",)

    def invoke(self, entry, target=None, caller=None):
        if entry == "python":
            command = [sys.executable, str(self.scripts / "main.py")]
        elif entry == "powershell":
            command = [
                "powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass",
                "-File", str(self.scripts / PS_SCRIPT),
            ]
        else:
            arguments = [str(self.scripts / BAT_SCRIPT)]
            if target is not None:
                arguments.append(str(target))
            quoted = " ".join(f'"{argument}"' for argument in arguments)
            command = f'cmd.exe /d /s /c "{quoted}"'
        if entry != "bat" and target is not None:
            command.append(str(target))
        return subprocess.run(
            command, cwd=caller or self.caller, capture_output=True, timeout=30,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
        )

    def test_default_and_blank_targets_use_script_directory(self):
        for entry in self.entries:
            for index, argument in enumerate((None, "", " ", "\t")):
                with self.subTest(entry=entry, argument=argument):
                    caller = self.caller / f"{entry}-{index}"
                    caller.mkdir()
                    result = self.invoke(entry, argument, caller)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, b"")
                    self.assertTrue((self.scripts / TODAY).is_dir())
                    self.assertFalse((caller / TODAY).exists())

    def test_create_and_repeat_with_literal_unicode_paths(self):
        for entry in self.entries:
            with self.subTest(entry=entry):
                base = self.base / f"{entry} 中文 [资料] & data"
                base.mkdir()
                for _ in range(2):
                    result = self.invoke(entry, base)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(result.stderr, b"")
                self.assertTrue((base / TODAY).is_dir())

    def test_invalid_targets_and_collisions_preserve_files(self):
        for entry in self.entries:
            with self.subTest(entry=entry):
                missing = self.base / f"missing-{entry}"
                result = self.invoke(entry, missing)
                self.assertEqual(result.returncode, 1)
                self.assertTrue(result.stderr)
                self.assertFalse(missing.exists())

                file = self.base / f"file-{entry}"
                file.write_bytes(b"base file")
                result = self.invoke(entry, file)
                self.assertEqual(result.returncode, 1)
                self.assertTrue(result.stderr)
                self.assertEqual(file.read_bytes(), b"base file")

                base = self.base / f"collision-{entry}"
                base.mkdir()
                target = base / TODAY
                target.write_bytes(b"existing date file")
                result = self.invoke(entry, base)
                self.assertEqual(result.returncode, 1)
                self.assertTrue(result.stderr)
                self.assertEqual(target.read_bytes(), b"existing date file")

    def test_parallel_entrypoints_create_one_directory(self):
        base = self.base / "parallel"
        base.mkdir()
        entries = self.entries * 2
        barrier = Barrier(len(entries))

        def invoke_together(entry):
            barrier.wait(timeout=10)
            return self.invoke(entry, base)

        with ThreadPoolExecutor(max_workers=len(entries)) as pool:
            results = list(pool.map(invoke_together, entries))
        for entry, result in zip(entries, results):
            with self.subTest(entry=entry):
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, b"")
        self.assertEqual(list(base.iterdir()), [base / TODAY])


if __name__ == "__main__":
    unittest.main()
