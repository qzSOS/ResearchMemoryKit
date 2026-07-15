# ResearchMemoryKit

一套面向长期 AI 辅助科研与复杂工程、以 Markdown 为核心的项目记忆与门控工作流。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No runtime dependencies](https://img.shields.io/badge/runtime_dependencies-none-blue.svg)](pyproject.toml)
[![Validate](https://github.com/qzSOS/ResearchMemoryKit/actions/workflows/validate.yml/badge.svg)](https://github.com/qzSOS/ResearchMemoryKit/actions/workflows/validate.yml)
[![Bilingual](https://img.shields.io/badge/docs-EN%20%7C%20ZH-lightgrey.svg)](README.md)
[![LINUX DO](https://img.shields.io/badge/LINUX-DO-ffb000.svg)](https://linux.do)

ResearchMemoryKit 是一种轻量、Git 原生的长期 AI 辅助科研与工程项目工作
方法。它的核心有意保持简单：用少量 Markdown 文件记录当前状态、关键决策、
失败路线、证据边界和完成门控。

人和 Agent 通过读写这些文件恢复上下文、控制项目走向、保留审计轨迹，并判断
一项工作是否真正完成。采用这套方法不需要安装服务或 Python 包。模板和提示词
可以帮助你按真实项目调整结构；可选的 `rmk.json` 与 `rmk check` 用于发现
结构漂移。

```text
Current State
  -> Decision / Gate
  -> Registered work
  -> Execution
  -> Evidence review
  -> Conclusion or failure
  -> Pitfall / Session update
  -> Current State replacement
```

English: [README.md](README.md)

## 它能帮助什么

- **上下文恢复**：新的人或 Agent 可以从短小的 Current State 重新开始。
- **项目走向控制**：决策记录理由、备选方案和复盘条件，让项目能停止弱路线，而不是惯性漂移。
- **可信科研工作流**：书面完成门要求在关闭任务前审阅结果、失败、坑位和状态变化。
- **可复现工程**：元数据、命令、输出和证据边界保持连接。
- **带护栏的 Agent 自主推进**：Agent 可以推进工作，但门控定义什么才算真实进展。

## 从 Markdown 开始

使用这套模式不需要安装任何东西。你可以复制并调整一个模板，也可以让 Agent
根据项目的真实目标和工作流设计最小但够用的记忆层。

仓库内的初始化脚本只是一个便捷入口：

```bash
git clone https://github.com/qzSOS/ResearchMemoryKit.git
cd ResearchMemoryKit
python scripts/init_memory.py research-project /tmp/my-research-project
```

如果项目更适合轻量或交付场景，可把 `research-project` 换成 `minimal` 或
`delivery-project`。随后填写 Current State、定义书面完成门控，并把这些
Markdown 文件和项目一起提交。

只想阅读示例的话，可以看：

- [examples/toy-research-project](examples/toy-research-project)：最小完整记忆层；
- [examples/fictional-paper-project](examples/fictional-paper-project)：带门控的论文式工作流示例。

## 可选：30 秒结构检查

![ResearchMemoryKit 发现断开的 Current State 路由和缺失门控，修复后通过](docs/assets/rmk-gate-demo.gif)

这个动画来自一个可执行的纯虚构案例。第一次检查会发现 Current State
路由断开、门控标题缺失；修复契约后，同一个项目通过检查。

```bash
git clone https://github.com/qzSOS/ResearchMemoryKit.git
cd ResearchMemoryKit
python scripts/demo_gate.py
```

完整输出和 P0 能力边界见 [docs/gate-demo.md](docs/gate-demo.md)。

如需给自己的项目增加可选检查器：

```bash
python -m pip install -e . --no-deps
rmk check /tmp/my-research-project
```

检查器会报告缺失文件、路由断开、状态过期、未解决占位符和缺失的门控标题。
它不会判断科研结论是否真实，也不会判断证据是否充分。

## 为什么需要它

AI 编程 Agent 擅长局部执行，但长期科研项目通常不是因为“不会写代码”而失败，而是因为：

- 当前状态埋在很长的聊天记录里；
- 同一个事实被复制到多个文件，后来彼此漂移；
- 失败实验没有沉淀，几周后又被重复；
- 临时笔记堆积成永久噪声；
- Agent 会更新熟悉文件，却跳过新的记忆结构；
- Agent 持续执行任务，却没有证明研究门控真的通过；
- 生成产物增长速度超过项目解释它们的速度。

ResearchMemoryKit 把这些问题视为正常的科研工程失败模式。它的目标不是自动化一切，而是在足够小的维护成本下，保证新会话能恢复工作，也保证关键步骤有可审计的完成条件。

## 核心模式

每个项目从少量文件开始：

```text
AGENTS.md or README.md       恢复入口和项目规则
memory/CURRENT_STATE.md      可覆盖的当前状态快照
memory/DECISIONS.md          只追加的决策记录
memory/EXPERIMENT_LOG.md     结论只追加，展示格式可重排
memory/FAILED_ATTEMPTS.md    只追加的失败路线和保留教训
memory/PITFALLS.md           只追加的高风险坑位和诊断方法
memory/SESSION_LOG.md        只追加的重要会话活动
memory/WORKFLOW.md           完成门和操作规则
registry/                    可选，只保存实验元数据
```

最重要的规则：

> 任务不算完成，直到门控通过，并且记忆层反映了这次变化。

## 可选的结构检查

Markdown 记录和书面门控才是项目的事实来源。需要 CI 约束的项目还可以增加
显式的 `rmk.json` 契约。P0 检查器会验证必需文件、路径安全、Router 可达性、
门控标题、Current State 日期、状态过期和未解决占位符。

```bash
rmk check /path/to/project
rmk check /path/to/project --strict
rmk check /path/to/project --format json
```

普通模式在契约破损时失败；`--strict` 还会让 warning 导致失败，适合接入
CI。可选 Manifest 和稳定错误码见 [docs/rmk-check.md](docs/rmk-check.md)。

P0 检查的是契约健康度，不判断证据质量、科研方法是否合理或结论是否真实。
这些仍然属于工作流执行和人工审阅的责任。

## 关键原则

- **先读 Current State**：短小、可覆盖的当前快照是每次会话入口。
- **历史只追加**：决策、失败、结论要保留可信来源。
- **Router 保持低波动**：路由文件只告诉你去哪读，不承载最新结论。
- **一个事实一个真源**：可变事实重复出现就是潜在 bug。
- **完成门激活行为**：模板本身不够，必须把记忆更新纳入完成定义。
- **门控指导项目走向**：实验、转向和交付都有明确通过/失败或复盘条件。
- **证据边界要清楚**：不要把初步结果写成超过证据强度的结论。

## 和 Agent 一起使用

对于私人或内部项目，可以直接给 coding agent 这段简短指令：

```text
请在这个项目中采用 ResearchMemoryKit 的方法。先检查项目目标和工作流，再创建最小但够用的 Markdown 记忆层，定义书面完成门控、权威文件和会话恢复顺序。保留恢复工作所需的操作信息。共享文件优先使用仓库相对路径或环境别名；具体机器映射可放在 gitignored 本地文件中。不要把凭据写进项目记忆。如果项目需要自动检查结构，再创建 rmk.json 并运行 rmk check。准备任何公开内容前先询问我。
```

更完整的提示词见 [docs/agent-prompts.md](docs/agent-prompts.md)。
不适合固定模板的项目可以使用其中的自适应提示词。

## 应该选哪个模板？

| 模板 | 适合场景 | 包含内容 |
|---|---|---|
| `minimal` | 小项目、阅读笔记、个人原型 | Current State、Decisions、Session Log |
| `research-project` | 机器学习/AI 科研、实验、论文、长期 baseline | memory router、实验日志、失败尝试、坑位目录、完成门、registry |
| `delivery-project` | 工程报告、对外交付、生成图片/视频 | project state、delivery index、decision log、work log、证据边界规则 |

## 和其他工具有什么不同？

| 工具类别 | 擅长什么 | ResearchMemoryKit 的差异 |
|---|---|---|
| Agent 记忆数据库 | 存储和检索 agent memory | 文件化、可检查、git-native、不需要服务 |
| 实验追踪平台 | 指标、dashboard、run、artifact | 记录理由、失败路线、当前状态和证据边界 |
| 项目管理工具 | 任务、负责人、截止日期 | 面向科研不确定性和多会话 agent 接力 |
| 笔记软件 | 灵活的人类笔记 | 增加生命周期语义和完成门 |

更详细说明见 [docs/comparison.md](docs/comparison.md)。

## 文档导航

| 需求 | 文档 |
|---|---|
| 在新项目或现有项目中采用 Markdown 工作流 | [接入指南](docs/adoption-guide.md) |
| 给 Agent 一段符合真实项目的提示词 | [Agent 提示词](docs/agent-prompts.md) |
| 查看真实的失败与修复过程 | [门控演示](docs/gate-demo.md) |
| 理解 `rmk.json` 和错误码 | [`rmk check` 参考](docs/rmk-check.md) |
| 设计科研、方向和交付门控 | [门控科研工作流](docs/gated-research-workflow.md) |
| 在 GitHub Actions 中检查契约 | [CI 指南](docs/ci.md) |
| 安全公开一个私人项目 | [安全发布指南](docs/publishing-safely.md) |
| 理解设计取舍 | [理论](docs/theory.zh-CN.md)与[工具比较](docs/comparison.md) |

根目录的 `memory/` 是有意提交的。它只记录 ResearchMemoryKit 自身的开发，
是这套 Markdown 工作流的公开自托管示例；本仓库还在其上使用了可选的契约
检查器。这里不包含从任何私人科研项目复制的记忆内容。

## 延伸阅读

- [AI 科研 Agent 需要的不只是记忆，而是门控](docs/blog/ai-research-agents-need-gates-zh.md)
- [AI Research Agents Need Gates, Not Just Memory](docs/blog/ai-research-agents-need-gates.md)

## 适用场景

适合：

- 项目持续数周或数月；
- 多个 Agent 或多次会话会接手；
- 失败实验本身有价值；
- 决策需要理由和复盘条件；
- 需要不读完整聊天记录就恢复上下文；
- 项目需要在接受结论、转向或交付前通过明确门控。

不适合：

- 一次短会话能完成的任务；
- 已经必须使用正式实验追踪平台；
- 团队需要权限、仪表盘或数据库级工作流。

## 作者

本项目由 [qzSOS](https://github.com/qzSOS) 创建。公开示例均为虚构内容；
私人项目如何准备公开材料单独写在
[docs/publishing-safely.md](docs/publishing-safely.md) 中。

## Roadmap

- registry 生命周期和实验交叉引用检查；
- 基于 git 的只追加删除检测；
- claim 证据和人工审核状态；
- 保守的 Router 真源重复检查；
- 为超大只追加文件增加可选活动索引；
- 增加更多可执行的虚构案例；
- 发布 PyPI 包并降低安装门槛；
- 建一个小型 GitHub Pages 文档站；
- 为常见 coding agent 增加启动提示词。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
