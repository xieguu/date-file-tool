import sys,time,pathlib as p;a=(sys.argv+[""])[1];((p.Path(a).expanduser() if a.strip() else p.Path(__file__).resolve().parent)/time.strftime("%Y.%m.%d")).mkdir(exist_ok=1)
