新项目方向调研

调研日期：2026-10-08。来源限官方仓库与文档；以下区分现有能力与首版建议。

**优先方向：个人网页变化监控**

- 官方仓库：[dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io)；许可证：[Apache-2.0](https://github.com/dgtlmoon/changedetection.io/blob/master/LICENSE)。
- 官方现有：按间隔检测网页变化，可用 CSS/XPath 选区域、关键词和正则过滤内容。[功能列表](https://github.com/dgtlmoon/changedetection.io#key-features)
- 官方现有：按词、行、字符查看差异；API 可列出变化时间并读取历史文本快照。[差异展示](https://github.com/dgtlmoon/changedetection.io#easily-see-what-changed-examine-by-word-line-or-individual-character)、[历史与快照 API](https://github.com/dgtlmoon/changedetection.io/blob/master/docs/api-spec.yaml)
- 官方现有：通过 Apprise 发邮件、Discord、Webhook 等通知，并可自定义通知模板。[通知说明](https://github.com/dgtlmoon/changedetection.io#notifications)
- 官方现有：支持 JavaScript 动态页面抓取；浏览器交互步骤需要启用 Playwright。[浏览器步骤与抓取方式](https://github.com/dgtlmoon/changedetection.io#perform-interactive-browser-steps)
- 复用判断（本次建议）：适合作为监控后端，复用抓取、调度、差异和通知，通过已有 REST API 接自己的操作入口。[官方 API 支持](https://github.com/dgtlmoon/changedetection.io#api-support)
- 建议首版范围（尚未实施）：添加网址、设检查间隔、选关注区域、看变化记录、收邮件；先围绕招聘公告、软件更新或商品价格选一种场景。
- 建议新增：Windows 托盘入口、常用监控规则模板；这两项是项目构想，不代表官方现成功能。
- 历史边界：官方 API 说明文本快照可按时间读取，原始 HTML 只保留最近两份，不能据此承诺完整网页永久归档。[快照定义](https://github.com/dgtlmoon/changedetection.io/blob/master/docs/api-spec.yaml)

**备选方向：收藏整理与网页存档**

- 官方仓库：[linkwarden/linkwarden](https://github.com/linkwarden/linkwarden)；许可证：[AGPL-3.0](https://github.com/linkwarden/linkwarden/blob/main/LICENSE.md)。
- 官方现有：按集合、子集合和标签整理收藏，支持全文搜索、筛选与排序。[功能列表](https://github.com/linkwarden/linkwarden#features)
- 官方现有：自动保存网页截图、PDF 和单文件 HTML；提供阅读视图、划线与批注。[功能列表](https://github.com/linkwarden/linkwarden#features)
- 官方现有：浏览器扩展、共享集合、成员权限；支持自行部署。[仓库功能与安装入口](https://github.com/linkwarden/linkwarden#features)
- 复用判断（本次建议）：适合做个人资料库，直接复用收藏、搜索与存档功能；项目增量可放在按工作项目归档和定期回顾流程。
- 建议首版范围（尚未实施）：保存链接、标签分类、搜索、查看已存副本；按项目自动归档和回顾提醒属于后续新增构想。

**备选方向：个人常用工具页面**

- 官方现有：[IT-Tools](https://github.com/CorentinTh/it-tools) 是 Vue/TypeScript 工具集合，支持 Docker 自托管，提供 `pnpm run script:create:tool` 扩展入口，采用 GPL-3.0。
- 建议首版范围（尚未实施）：整理自己高频使用的工具入口，添加少量专用工具；预计扩展难度较低。

**备选方向：可搜索的文档资料库**

- 官方现有：[Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) 支持文档扫描、索引、归档及搜索，推荐 Docker Compose 部署，采用 GPL-3.0。
- 建议首版范围（尚未实施）：本地文档导入、检索、分类。

**备选方向：局域网文件接收与自动归档**

- 官方现有：[LocalSend](https://github.com/localsend/localsend) 可在局域网内跨平台传文件与消息，支持 Windows，采用 Apache-2.0；当前源码构建需要 Flutter 和 Rust。
- 建议首版范围（尚未实施）：接收文件后按日期归档；预计扩展难度较高。

选型建议：优先网页变化监控；想最快形成定制成果，可选 IT-Tools。难度属于本次估计。
本次产物仅为方向调研；未安装、运行或部署上述应用，未评价版本新旧或维护活跃度。
