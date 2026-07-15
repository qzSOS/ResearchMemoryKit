# AI 科研 Agent 需要的不只是记忆，而是门控

> A practical note on making AI-assisted research auditable, reproducible, and recoverable.

很多人在使用 AI 编程 Agent 做科研时，第一反应是给 Agent 增加“记忆”：把聊天记录保存下来，把实验结果写进笔记，把项目状态放到一个 Markdown 文件里。

这当然有用。但如果项目真的持续数周甚至数月，只靠记忆很快不够。

长期科研项目的问题不是“Agent 忘了什么”这么简单。更常见的问题是：

- 当前状态埋在几万字聊天记录里；
- 同一个结论在多个文件中重复出现，后来彼此不一致；
- 失败实验没有被记录，几周后又被重复；
- 生成图片、日志、表格和 checkpoint 越堆越多，但没人知道哪些能作为证据；
- Agent 持续执行任务，却没有证明项目真的向前推进；
- 一个看似合理的方向被惯性推进，直到很晚才发现门控根本没过。

所以，AI 科研 Agent 需要的不只是 memory，而是 gates。

## Chat History 不是 Project Memory

聊天记录适合保存对话，但不适合作为项目记忆。

原因很简单：聊天记录是线性的，而科研项目不是。

一个真实项目里同时存在：

- 当前应该做什么；
- 为什么选择这个方向；
- 哪些实验已经关闭；
- 哪些路线失败了；
- 哪些坑不能再踩；
- 哪些结果可以支撑结论；
- 哪些结果只能作为诊断产物；
- 下一步如果失败，应该怎么停。

如果这些信息全都留在聊天记录里，新会话恢复上下文就会变成考古。Agent 可能读到旧结论，也可能跳过关键失败记录。更糟的是，旧信息和新信息会混在一起，没有明确的可信边界。

项目记忆应该是结构化的，而不是聊天记录的堆积。

## Current State 是入口，但不是全部

一个短小的 `CURRENT_STATE.md` 很有价值。

它应该回答：

- 现在项目在哪个阶段；
- 当前目标是什么；
- 当前最可信的结果是什么；
- 什么正在阻塞；
- 下一步具体做什么；
- 什么情况下应该停止或转向。

这个文件应该是可覆盖的。它不是历史档案，而是驾驶舱。

但 Current State 只能回答“现在怎样”。它不能单独回答“为什么会这样”。所以它需要配套的历史记录：

- `DECISIONS.md`：记录方向选择、理由、备选方案、复盘条件；
- `EXPERIMENT_LOG.md`：记录实验结论和证据；
- `FAILED_ATTEMPTS.md`：记录失败路线和保留教训；
- `PITFALLS.md`：记录可复现的 bug、环境坑和诊断方法；
- `SESSION_LOG.md`：记录重要会话活动；
- `WORKFLOW.md`：定义什么叫完成。

Current State 负责恢复，append-only records 负责可信。

## 关键不是文件，而是完成门

很多模板失败，不是因为文件设计错了，而是因为 Agent 不会自动维护它们。

如果“更新记忆”只是一个建议，Agent 很容易跳过它。尤其在科研项目里，GPU 时间窗、截止日期、远程环境和实验压力都会把工作流压缩成最短路径。

所以需要 completion gate。

例如，一个实验不应该在“代码跑完”时就算完成。它应该在以下条件满足后才算完成：

- registry 里有实验 ID、配置、输入角色、输出路径；
- 结果或失败已经写入日志；
- 新发现的坑已经加入 pitfall catalog；
- 当前状态已经更新；
- 不被结果支持的结论被明确排除。

换句话说：

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

这时 Agent 的工作才从“执行了很多命令”变成“通过了一个可审计的研究步骤”。

## 失败实验应该是一等记录

科研中的失败不是垃圾信息。

失败路线至少有三种价值：

1. 它告诉未来的 Agent 不要重复同一个方向；
2. 它定义了方法的边界；
3. 它可能在论文或报告中成为可信的 negative evidence。

问题在于，失败经常只存在于聊天里，或者被一句“这个不行”带过。几周后，另一个 Agent 或同一个人又会重新尝试。

更好的做法是把失败记录成结构化条目：

```markdown
### F-001: Validation Split Leakage

| Field | Value |
|---|---|
| Route | Random patch-level split |
| What failed | Validation samples overlapped training sources |
| Evidence | Duplicate source IDs across roles |
| Preserved lesson | Split by source before extracting patches |
| Do not repeat unless | A leakage-safe manifest is generated |
```

这样失败就不再是情绪，而是项目资产。

## Router 不应该承载当前真相

很多项目会在 `README.md` 或 `AGENTS.md` 顶部写“当前结论”“最新结果”“当前最佳配置”。

短期看方便，长期看危险。

Router 文件应该低波动：告诉 Agent 该读什么文件、遵守什么规则、哪里是权威来源。它不应该承载会变化的当前真相。

因为一旦 Router 和 Current State 同时写了“最新结论”，它们就会漂移。后来的人或 Agent 不知道该信谁。

一个简单原则是：

> Router tells you where to read. Current State tells you what is true now.

## 可信科研依赖闭环

AI Agent 可以很快地产生代码、图、表和报告。但这些产物本身不等于可信科研。

可信来自闭环：

- 为什么做这个方向；
- 运行了什么；
- 用了什么配置；
- 结果如何验证；
- 失败如何记录；
- 哪些结论不能说；
- 当前状态如何变化。

ResearchMemoryKit 的核心不是“保存更多文本”，而是让每一步都有门控、有来源、有停止条件。

这对可复现工程也很重要。一个实验结果如果没有 commit、配置、输入角色、输出路径和证据边界，就很难被复现，也很难被信任。

## 固定模板不够，Agent 也应该能自适应设计记忆层

不同项目需要不同结构。

一个论文项目可能需要 `registry/`、`EXPERIMENT_LOG.md`、`FAILED_ATTEMPTS.md`。一个工程交付项目可能更需要 `DELIVERY_INDEX.md` 和证据边界。一个创作管线项目则可能需要 asset metadata 和版本化 prompt。

所以最好的方式不是强迫所有项目套同一个模板，而是给 Agent 一个元提示词，让它根据项目目标设计目录和记忆层。

例如：

```text
I want this project to use ResearchMemoryKit, but the project may need a custom structure.

Please inspect the project goal, expected artifacts, experiment or delivery workflow, privacy constraints, and collaboration pattern. Then design a project directory and memory layer that fits this project.

Requirements:
1. Create a low-volatility router file such as AGENTS.md.
2. Create an overwriteable Current State file as the first session recovery target.
3. Create append-only records for decisions, failed attempts, pitfalls, and significant activity.
4. If the project has experiments, create a metadata-only registry and an experiment completion gate.
5. If the project has deliverables, create a delivery index and evidence-boundary rules.
6. Define what counts as "done" for the project.
7. Keep mutable facts in one authoritative source.
8. Ask whether the project is private, shared, or being prepared for publication.
9. Preserve operational paths when a private project needs them, but prefer repository-relative paths or named environment roots in shared records.
10. Keep per-machine mappings in gitignored local files when practical. Never store credentials or secrets in project memory.
11. Apply anonymization only to material that will be public.
```

这样，ResearchMemoryKit 就不是一个死模板，而是一套设计原则。

## 什么时候不需要它

不是所有项目都需要这种结构。

如果一个任务一小时内能完成，不需要它。  
如果团队已经有完整实验平台，也不应该用它替代平台。  
如果项目只需要任务列表，项目管理工具更合适。

ResearchMemoryKit 适合的是这类项目：

- 会持续数周或数月；
- 会被多个 Agent 或多次会话接手；
- 失败实验本身有价值；
- 结论必须可追溯；
- 项目方向需要门控，而不是靠惯性推进。

## 小结

AI 科研 Agent 的问题不只是记忆长度不够。

真正的问题是：项目如何在长期不确定性中保持可信推进。

一个好的研究记忆层应该同时做到：

- 快速恢复上下文；
- 保留决策来源；
- 记录失败边界；
- 约束证据强度；
- 定义完成门；
- 让 Agent 能自主推进，但不能跳过审计。

这就是 ResearchMemoryKit 想解决的问题。

项目地址：

https://github.com/qzSOS/ResearchMemoryKit
