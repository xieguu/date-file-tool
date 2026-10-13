# 今日文件夹创建器

在指定目录下创建当天日期命名的文件夹，格式为 `yyyy.MM.dd`，例如 `2026.10.05`。

仓库：[xieguu/date-file-tool](https://github.com/xieguu/date-file-tool)。

## 文件说明

- `创建今日文件夹.ps1`：推荐入口，支持传入目标目录。
- `创建今日文件夹.bat`：Windows 双击/快捷方式入口，内部调用 PowerShell 脚本。
- `main.py`：Python 入口，行为与 PowerShell 版保持一致。
- `tests/test_today_folder.py`：标准库回归测试，覆盖三个入口的路径处理与并发创建。
- `.editorconfig`：约定文件编码与换行符，避免编辑后再次出现中文乱码。
- `docs/project-improvement-research.md`：本工具的改进记录与相关方案调研。
- `docs/archive/`：其他项目方向的历史调研，不属于本工具已实现的功能。

自动生成的日期目录及 Python 缓存不纳入版本管理。

## 运行环境

- PowerShell / BAT 入口：Windows PowerShell 5.1，无需安装第三方模块。
- Python 入口：Python 3.10 或更新版本，仅使用标准库，无需安装依赖。

## 使用方式

默认在脚本所在目录创建今日文件夹：

```powershell
.\创建今日文件夹.ps1
```

在指定目录创建今日文件夹：

```powershell
.\创建今日文件夹.ps1 "C:\Users\29718\Desktop"
```

使用批处理入口：

```bat
创建今日文件夹.bat "C:\Users\29718\Desktop"
```

使用 Python 入口：

```powershell
python .\main.py "C:\Users\29718\Desktop"
```

## 编码约定

- `.ps1` 文件使用 **UTF-8 with BOM**，确保 Windows PowerShell 5.1 正确读取中文源码；仅设置控制台代码页无法修复源码解码错误。
- `.bat` 文件使用无 BOM 的 UTF-8 和 CRLF 换行；其他文本文件使用无 BOM 的 UTF-8 和 LF 换行。
- 支持 EditorConfig 的编辑器会按 `.editorconfig` 应用这些设置。

## 行为约定

- 不传目标目录，或参数仅含空白：使用脚本所在目录，与调用时的工作目录无关。
- 目标目录不存在：返回失败。
- 目标路径不是文件夹：返回失败。
- 今日文件夹已存在：返回成功。
- 今日名称被同名文件占用：返回失败。
- 创建成功：返回成功。
- 多个实例同时创建同一天的文件夹：均返回成功；若被同名文件占用，仍返回失败并保留该文件。
- 成功时不输出；失败时由 Python 或 PowerShell 输出原生错误。
- 最小入口仅接收目标目录，不提供 `--help` 等选项。

## 退出码

- `0`：创建成功，或目标日期文件夹已存在。
- `1`：目标路径无效、同名文件占用、权限不足或其他创建失败。

## 回归验证

在项目根目录运行，无需安装测试依赖：

```powershell
python -m unittest discover -s tests -v
```

测试在临时目录中运行，覆盖空白参数、不同工作目录、中文及特殊字符路径、重复创建、文件冲突、创建失败和并发调用。Windows 下实际运行 Python、PowerShell 和 BAT 三个入口；其他平台验证 Python 入口。
