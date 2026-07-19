# Coding Agent 起始提示词

这些提示词帮助 Coding Agent 一致地使用 ResearchMemoryKit。

英文对应版本见 [agent-prompts.md](agent-prompts.md)。

## 自适应记忆层设计

当固定模板不够用、需要 Agent 根据项目实际情况设计目录和记忆层时使用。

```text
我希望这个项目使用 ResearchMemoryKit，但项目可能需要自定义结构。

请检查项目目标、预期 artifact、实验或交付工作流、隐私约束和协作方式，
然后设计适合这个项目的目录和记忆层。

要求：
1. 创建低波动的 router 文件，例如 AGENTS.md。
2. 创建可覆盖的 Current State 文件，作为每次会话的第一个恢复入口。
3. 创建只追加的决策、失败尝试、坑位和重要活动记录。
4. 如果项目包含实验，创建只记录元数据的 registry 和实验完成门。
5. 如果项目包含交付物，创建交付索引和证据边界规则。
6. 定义项目的“完成”含义：任务、实验、转向或交付关闭前必须更新哪些记忆文件。
7. 每类可变事实只保留一个权威来源；router 应该链接到 Current State，
   而不是重复当前真相。
8. 如果结构化自动检查有帮助，创建 rmk.json，声明 router、Current State、
   必需文件、只追加文件、路由目标、过期阈值和门控标题。
9. 如果创建了这个可选契约且命令可用，运行 rmk check。
10. 询问项目是私有、共享还是准备公开。
11. 保留恢复工作所需的操作信息。私有项目必要时可以使用精确机器路径，
    但共享文件优先使用仓库相对路径或命名环境根目录。
12. 具体机器映射可放在 gitignored 本地文件中。永远不要把凭据或 secret
    写进项目记忆。
13. 只有准备公开的文件或导出物才应用匿名化和公开限制。

创建结构后，请说明：
- 每个文件为什么存在；
- 每类事实由哪个文件作为权威来源；
- 第一份 Current State；
- 第一条决策记录；
- 后续 Agent 必须遵守的完成门；
- 如果启用了可选契约，说明 rmk check 结果。
```

## 新会话

```text
这个项目使用 ResearchMemoryKit。

开始非平凡工作前：
1. 阅读 AGENTS.md。
2. 首先阅读 memory/CURRENT_STATE.md。
3. 阅读 memory/README.md 和任务所需的路由文件。
4. 检查 git status。
5. 遵守 memory/WORKFLOW.md。
6. 如果仓库使用 rmk.json，在关闭重要任务前运行 rmk check。

在记忆层反映重大状态变化之前，不要把任务视为完成。
```

## 研究阶段、阻塞和 Artifact 语义

当科研任务会产生证据、使用 artifact、改变研究方向或因某个条件暂停时使用。

```text
这个项目使用 ResearchMemoryKit。开始前，检查当前研究阶段和书面门控。

1. 判断当前工作属于 EXPLORATORY、CONFIRMATORY 还是 PAPER，并说明任务是
   探索、确认还是论文准备。
2. 将研究阶段与证据等级分开。测试通过不能自动晋级探索结果。
3. 遇到阻塞时使用一个标准 blocker code：
   ACCESS_BLOCKED、INPUT_MISSING、LICENSE_BLOCKED、IDENTITY_DRIFT、
   CONTRACT_INCOMPLETE、RESOURCE_BUSY、DATE_NOT_DUE、BUDGET_LIMITED、
   HUMAN_APPROVAL_REQUIRED 或 SCIENTIFIC_GATE_FAILED。
4. 记录 blocker_code、summary、recoverable、owner、recovery_condition、
   safe_next_action、scientific_impact、完整 ISO-8601 的 observed_at，以及
   只能引用仓库相对路径、commit、Goal ID 或 artifact ID 的 evidence_reference。
5. 将 artifact identity 与 artifact availability 分开。区分 REGISTERED、
   LOCATABLE、ACCESSIBLE、HASH_VERIFIED、STAGED、LOAD_VERIFIED 和
   EVALUATED。登记、hash、checkpoint identity 或 metadata-only 检查都不能
   证明文件可用或已经加载。
6. 探索性重新生成 artifact 时创建新的 artifact identity，并标注
   newly_generated provenance。绝不覆盖历史 hash 或 provenance。
7. 记录恢复条件和下一步安全动作。一个局部动作阻塞时，不要冻结无关的
   文档、验证或只读审计工作。
8. 不要把探索结果写成论文主张。区分观察、失败、解释、证据边界和不受支持
   的主张。
9. 跨日或跨时区工作记录 governing_date、date_authority、timezone、
   observed_at、eligible_after 和 date_conflict_policy。Current State 的
   Date 是项目快照日期，不自动是会话日期权威。
10. 关闭任务前更新 memory/CURRENT_STATE.md，并追加相关决策、结论、失败、
    坑位或会话记录。保留人工科学判断，以及作者、投稿和 release 的最终人工批准。
```

## 实验结束

```text
请使用 ResearchMemoryKit 完成门关闭这个实验：
1. 更新 registry 状态和指标；
2. 将结论写入 memory/EXPERIMENT_LOG.md，或将失败写入 memory/FAILED_ATTEMPTS.md；
3. 将可复现 bug 加入 memory/PITFALLS.md；
4. 追加 memory/SESSION_LOG.md；
5. 如果活动状态变化，替换 memory/CURRENT_STATE.md。
```

## 改造现有项目

```text
请为这个现有项目初始化 ResearchMemoryKit。

约束：
- 保持 AGENTS.md 为低波动 router。
- 只把当前可变事实放在 memory/CURRENT_STATE.md。
- 添加一条决策，说明为什么需要这层记忆。
- 在 memory/WORKFLOW.md 中加入完成门。
- 如果结构化自动检查有帮助，创建或更新 rmk.json 并运行 rmk check。
- 保留私有项目恢复工作所需的操作路径。
- 项目跨机器共享时，优先使用命名环境根目录或 gitignored 本地映射。
- 永远不要把凭据写进项目记忆。
```

## 公开发布审计

```text
请在公开发布前审计这个仓库。

检查：
- 没有私有项目名称；
- 没有未发表指标或主张；
- 没有本地路径、服务器 alias、邮箱、token 或凭据；
- Markdown 链接可解析；
- JSON 文件可解析；
- 示例是虚构的或已经充分匿名化。

如果存在，运行 scripts/validate_public_repo.py。
如果仓库有 rmk.json，运行 rmk check . --strict。
```
