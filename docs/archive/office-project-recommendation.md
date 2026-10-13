pdfme：把办公表单做成可重复使用的 PDF 模板

调研日期：2026-10-08。
官方仓库：[pdfme/pdfme](https://github.com/pdfme/pdfme)，MIT 许可证；官方体验：[Playground](https://playground.pdfme.com/)。

已核实的库与 UI 能力：

- 模板由固定底稿 `basePdf` 与可变字段 `schemas` 组成，可保存为 JSON。[Template](https://pdfme.com/docs/getting-started#template)
- `Designer` 编辑模板；`Form` 录入字段；`Viewer` 预览。`Form.getInputs()` 的结果可交给生成器。[UI](https://pdfme.com/docs/getting-started#ui)
- `@pdfme/generator` 提供 `await generate({ template, inputs })`，可在浏览器和 Node.js 中运行。[Generator](https://pdfme.com/docs/getting-started#generator)
- `inputs` 接受多条字段数据；官方单页模板示例说明，多条输入可生成一份多页 PDF。它并不意味着每条记录自动导出一个独立文件。[批量输入说明](https://pdfme.com/docs/getting-started#generator)

建议开发的办公流程：

- 导入 Excel 名单 → 校验并映射姓名、部门等列 → 选择证明或通知模板 → 预览 → 生成 PDF。
- Excel 解析、列映射、数据校验、按人独立导出与打包，是需要另外开发的业务功能；模板设计与 PDF 生成可直接复用 pdfme。
- 推荐先做“一个模板＋一张名单”，验证排版和字段对应后再增加模板种类。以上是项目构想，不代表现成的 Excel 办公套件。

本次仅核实官方接口并记录建议，未安装、部署或生成 PDF。
