办公工作流项目调研

调研日期：2026-10-08。首选建议：Activepieces，适合把表格、邮件和人工处理连接成可视化流程。

**Activepieces：首选**

- 官方仓库：[activepieces/activepieces](https://github.com/activepieces/activepieces)。
- 社区版核心采用 MIT；企业功能另用 Commercial License，不能把整个产品的所有功能都算作 MIT。[官方许可说明](https://github.com/activepieces/activepieces#license)
- 可视化流程编排支持分支、循环、HTTP、代码步骤、表单输入及人工介入。[官方功能列表](https://github.com/activepieces/activepieces#-builder-features)
- 支持自托管，官方安装文档提供 Docker Compose、PostgreSQL 与 Redis 方案。[安装选项](https://www.activepieces.com/docs/install/overview)
- Excel 365 连接器支持新增行触发、读取和写入表格；需要连接 Microsoft 账户。[官方 Excel 365 连接器](https://www.activepieces.com/pieces/microsoft-excel-365)
- Outlook 与 Excel 365 可连接处理邮件和表格数据。[官方连接说明](https://www.activepieces.com/pieces/microsoft-outlook/microsoft-excel-365)

**n8n：许可区别**

- n8n 官方称其为 fair-code，采用 Sustainable Use License 和企业许可，不应与 MIT 等严格开源许可混称。[官方 README](https://github.com/n8n-io/n8n/blob/master/README.md)
- SUL 允许内部业务、非商业或个人用途，但对分发和其他用途设有限制；`.ee.` 文件／`.ee` 目录需相应企业许可。[许可原文](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)

**NocoBase：适合内部业务系统，但需区分审批插件**

- 基础工作流属于 Community Edition+，内置且默认启用。[基础工作流插件](https://docs.nocobase.com/plugins/%40nocobase/plugin-workflow)
- 专用审批节点标注 Professional Edition+，不能承诺免费社区版直接包含完整审批插件。[审批节点](https://docs.nocobase.com/workflow/nodes/approval)

建议办公流程：表单提交采购申请 → 按金额分支 → 人工确认 → 写入 Excel 365 台账 → 通过 Outlook 通知申请人。
这是基于现有节点与连接器提出的组装方案，需要配置账户、字段和规则；本次未核实存在同名即用模板。

本次只调研与记录，未安装、部署或修改应用代码。
