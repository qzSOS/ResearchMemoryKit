# ResearchMemoryKit

一个面向长期 AI 辅助科研项目的轻量级 Markdown 记忆系统。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No dependencies](https://img.shields.io/badge/dependencies-none-blue.svg)](scripts/init_memory.py)
[![Validation](https://img.shields.io/badge/validation-scripted-blue.svg)](scripts/validate_public_repo.py)
[![Bilingual](https://img.shields.io/badge/docs-EN%20%7C%20ZH-lightgrey.svg)](README.md)

ResearchMemoryKit 不是 agent runtime、实验管理平台、数据库或工作流引擎。它是一组很小的文件模板和维护规则，用来帮助研究者和代码 Agent 在多次会话之间恢复上下文、保留决策依据、记录失败分支，并持续推进项目。

English: [README.md](README.md)

## 30 秒试用

```bash
git clone https://github.com/qzSOS/ResearchMemoryKit.git
cd ResearchMemoryKit
python scripts/init_memory.py research-project /tmp/my-research-project
cd /tmp/my-research-project
find . -maxdepth 3 -type f | sort
```

你会得到一套项目记忆层：当前状态、决策日志、实验日志、失败尝试、坑位目录、工作流完成门和只保存元数据的 registry。

只想阅读示例的话，可以看 [examples/toy-research-project](examples/toy-research-project)。

## 为什么需要它

AI 编程 Agent 擅长局部执行，但长期科研项目通常不是因为“不会写代码”而失败，而是因为：

- 当前状态埋在很长的聊天记录里；
- 同一个事实被复制到多个文件，后来彼此漂移；
- 失败实验没有沉淀，几周后又被重复；
- 临时笔记堆积成永久噪声；
- Agent 会更新熟悉文件，却跳过新的记忆结构；
- 生成产物增长速度超过项目解释它们的速度。

ResearchMemoryKit 把这些问题视为正常的科研工程失败模式。它的目标不是自动化一切，而是在足够小的维护成本下，保证新会话能恢复工作。

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

> 任务不算完成，直到记忆层反映了这次变化。

## 关键原则

- **先读 Current State**：短小、可覆盖的当前快照是每次会话入口。
- **历史只追加**：决策、失败、结论要保留可信来源。
- **Router 保持低波动**：路由文件只告诉你去哪读，不承载最新结论。
- **一个事实一个真源**：可变事实重复出现就是潜在 bug。
- **完成门激活行为**：模板本身不够，必须把记忆更新纳入完成定义。
- **证据边界要清楚**：不要把初步结果写成超过证据强度的结论。

## 快速开始

使用初始化脚本：

```bash
python scripts/init_memory.py minimal /path/to/project
python scripts/init_memory.py research-project /path/to/project
python scripts/init_memory.py delivery-project /path/to/project
```

也可以手动复制模板。

小项目：

```text
templates/minimal/
```

实验密集型科研项目：

```text
templates/research-project/
```

工程交付类项目：

```text
templates/delivery-project/
```

然后先提交一次 git，再开始正式工作。这个系统依赖版本历史来维持可信度。

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

## 仓库结构

```text
templates/                 可复用记忆层模板
examples/                  完全脱敏的玩具示例
docs/theory.md             设计原则和失败模式
docs/case-studies/         匿名化案例
docs/desensitization.md    公开发布脱敏检查表
docs/portfolio-plan.md     作品集呈现建议
docs/agent-prompts.md      常见 coding agent 启动提示词
scripts/init_memory.py     零依赖模板初始化脚本
scripts/validate_public_repo.py 公开发布校验脚本
```

## 适用场景

适合：

- 项目持续数周或数月；
- 多个 Agent 或多次会话会接手；
- 失败实验本身有价值；
- 决策需要理由和复盘条件；
- 需要不读完整聊天记录就恢复上下文。

不适合：

- 一次短会话能完成的任务；
- 已经必须使用正式实验追踪平台；
- 团队需要权限、仪表盘或数据库级工作流。

## 作者

本项目由 [qzSOS](https://github.com/qzSOS) 创建，是一个面向公开作品集的脱敏版本，用来展示长期 AI 辅助科研项目中的记忆连续性设计。

公开仓库只包含匿名化示例和模板，不包含私人项目名、未发表结果、服务器路径、合作者信息、客户信息或数据集相关敏感细节。

## Roadmap

- `rmk check`：更强的状态过期和 Router 真源重复检查；
- 为超大只追加文件增加可选活动索引；
- 增加论文写作和 benchmark packaging 的脱敏示例；
- 建一个小型 GitHub Pages 文档站；
- 为常见 coding agent 增加启动提示词。

## 许可证

MIT License。见 [LICENSE](LICENSE)。
