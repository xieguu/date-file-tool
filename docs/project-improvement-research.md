# 修改建议与相关开源项目

调研日期：2026-10-08。

当前工具适合继续作为轻量命令行入口使用。若希望在资源管理器中按日期创建文件夹，本次查到的现成方案中，PowerToys New+ 与需求最接近：支持文件夹模板、右键创建及日期变量替换。[官方说明](https://learn.microsoft.com/en-us/windows/powertoys/newplus)

## 当前实现状态（2026-10-13 更新）

- `main.py` 与 `创建今日文件夹.ps1` 是两套实现；BAT 调用 PowerShell，合计三个入口。
- 省略目标目录或传入纯空白参数时，三个入口均使用脚本目录。
- Python 使用 `Path.mkdir(exist_ok=True)`；PowerShell 校验父目录后使用 `DirectoryInfo.CreateSubdirectory`。重复及并发创建已有目录均成功，同名文件冲突则失败。
- 已保留 [回归测试](../tests/test_today_folder.py)，2026-10-13 在 Windows 下运行 4 项测试全部通过，覆盖三个入口的路径、空白参数、重复创建、冲突和并发调用。
- 旧版 `resolve_base_path` 函数已不存在，不应再使用早期调研中的导入调用命令；当前入口直接执行创建操作。

验证命令：

```powershell
python -m unittest discover -s tests -v
```

## 尚未实现的扩展方向

指定日期、名称后缀、创建后打开目录，以及资源管理器模板集成均属于扩展建议，当前版本没有这些功能。以下开源项目比较保留 2026-10-08 的调研结论，本次未重新核验其外部版本与能力。

## 相关项目对比

| 项目 | 与本项目的关系 | 官方确认的能力 | 使用条件与许可证 |
|---|---|---|---|
| [PowerToys New+](https://learn.microsoft.com/en-us/windows/powertoys/newplus) | 最接近当前的交互式创建需求 | 资源管理器右键按模板创建文件或文件夹，支持日期变量替换 | 安装 PowerToys；Windows 10 2004+ / Windows 11，x64 或 ARM64；[安装条件](https://learn.microsoft.com/en-us/windows/powertoys/install)，[MIT 源码](https://github.com/microsoft/PowerToys) |
| [organize](https://github.com/tfeldmann/organize) | 扩展到自动整理现有文件时适合复用 | 规则配置、移动、复制、重命名、冲突处理和模拟执行；支持 Windows、macOS、Linux | Python 工具，包名 `organize-tool`；MIT；能力与安装方法见官方仓库 |
| [date2name](https://github.com/novoid/date2name) | 日期命名的相邻工具 | 为已有文件或目录添加日期前缀，默认取修改时间；支持多种日期格式和预演 | 需要 Python；官方提供 Windows Explorer 集成说明；GPL-3.0 |
| [Cookiecutter](https://github.com/cookiecutter/cookiecutter) | 扩展到生成整套目录结构时适合复用 | 根据本地或远程模板及输入变量生成项目；支持 Windows、macOS、Linux | Python 工具；BSD-3-Clause；当前需求下属于扩展选项 |

New+ 的日期目录模板可以按官方变量规则命名为 `$YYYY.$MM.$DD`，并启用 **Replace variables in template filename**；该选项默认关闭。随后通过资源管理器右键菜单选择该模板。[变量及启用方式](https://learn.microsoft.com/en-us/windows/powertoys/newplus#replace-variables-in-template-filename)

本次对外部工具的能力核对基于其官方文档与仓库，未安装运行这些工具。日期模板是否足够、是否还需要命令行退出码和本项目的冲突语义，应按实际使用场景选择；不将其他工具视为命令行行为完全一致的替换品。
