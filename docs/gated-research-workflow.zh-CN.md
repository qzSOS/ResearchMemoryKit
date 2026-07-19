# 门控科研工作流

ResearchMemoryKit 不只是用于恢复上下文。它更重要的用途，是让 AI 辅助科研
过程可审计。

核心原则是：

> Agent 可以自主执行，但只有在门控关闭后，项目进展才算可信。

本文与[英文版本](gated-research-workflow.md)保持对应。

## 工作闭环

```text
Current State
  -> 决策
  -> 登记工作
  -> 执行
  -> 验证
  -> 结论或失败
  -> 更新坑位记录
  -> 会话日志
  -> 替换 Current State
```

这样，“Agent 做了很多工作”才会转化为“项目通过了一个有记录的门控”。

## 书面门控与自动检查

`WORKFLOW.md` 中的门控定义项目认为什么算完成。需要自动结构检查的项目可以
使用 `rmk check`，确认声明的门控及其支撑结构仍然存在。P0 不检查实验
证据，也不判断科学条件是否满足。

可以用可选检查器发现契约漂移；书面门控仍需通过证据审阅和人工判断关闭。

## 研究阶段

当前研究活动使用以下阶段之一：

| 阶段 | 用途 | 证据态度 |
|---|---|---|
| `EXPLORATORY` | 判断某个现象、实现路线或测量是否值得继续。 | 可以使用不完整或初步证据，但必须明确标注。 |
| `CONFIRMATORY` | 在冻结的协议和独立验证计划下检验预先定义的问题。 | 结果必须对照已登记的晋级门解释。 |
| `PAPER` | 准备能够接受正式审查的主张和公开材料。 | 必须具备完整 provenance、claim-to-evidence 审查和人工批准。 |

### `EXPLORATORY`

探索阶段可以使用单个序列或有限样本、短跑、smoke 检查、初步指标、不完整
数据和重新生成的 artifact。它适合排查某个观察是否存在，也可以使用新的
artifact identity。

探索结果不得自动声称方法有效、跨序列泛化、统计显著、具有临床价值或已经
构成正式论文证据。新生成的 artifact 也不能被写成历史 artifact。

### `CONFIRMATORY`

确认阶段要求冻结输入、代码、配置、评估协议和输出路径；预先定义晋级门，
并明确独立来源或独立序列。必须同时记录 artifact identity 和 availability，
并区分观察结果、失败结果和解释。

在把确认结果当作论文证据之前，应排除明显的坐标、视场（FoV）、reference
support 和数据污染解释。工程测试通过本身不等于科学晋级。

### `PAPER`

论文阶段要求完整 provenance；明确数据来源、访问边界和许可边界；完整实验
记录；预先定义的对照和统计分析；必要的多序列或 held-out 验证；
claim-to-evidence 审查；以及作者、投稿和公开材料的人工审阅。

### 阶段与主张边界

三个阶段是工作流状态，不是证据等级。阶段晋级必须显式记录阶段变更日期、
日期权威、决定、证据引用和人工负责人。测试通过不能自动把 `EXPLORATORY`
晋级为 `CONFIRMATORY` 或 `PAPER`，证据等级也不能自动升级。

探索模式不会降低论文级标准，只是把这些标准延后到正式提出论文主张之前。
严格度应随主张强度增加，而不是在探索开始前就要求所有论文条件。

## 标准阻塞原因

`BLOCKED` 是状态，具体原因必须使用稳定的 blocker code。不要使用
`DATA_BLOCKED` 把访问、输入、日期、许可、资源或科学失败混为一谈。

每条阻塞记录至少包含：

```yaml
blocker_code: ACCESS_BLOCKED
summary: 当前授权范围内无法读取来源元数据。
recoverable: true
owner: project maintainer
recovery_condition: 获得授权且读取检查成功。
safe_next_action: 不读取来源，先验证协议并更新 registry。
scientific_impact: data
observed_at: 2026-01-15T09:30:00Z
evidence_reference: memory/SESSION_LOG.md#B-001
```

这些字段分别表示：`blocker_code` 是稳定枚举；`summary` 是简短原因；
`recoverable` 表示是否存在明确恢复路径；`owner` 表示负责解除阻塞的角色；
`recovery_condition` 是可验证的恢复条件；`safe_next_action` 是无需额外批准
即可执行的动作；`scientific_impact` 说明阻塞影响数据、工程、解释还是论文
主张；`observed_at` 记录观测时间；`evidence_reference` 指向支持该判断的记录。

`observed_at` 必须是完整 ISO-8601 时间戳。`evidence_reference` 只能引用
仓库相对路径、commit、Goal ID 或 artifact ID，不能包含绝对路径、主机名、
SSH alias、用户名或凭据。

| Code | 含义与边界 |
|---|---|
| `ACCESS_BLOCKED` | 当前授权范围内无法访问所需来源或服务。这不是科学失败。 |
| `INPUT_MISSING` | 所需输入、manifest 或声明的 artifact 不存在。这不是方法失败。 |
| `LICENSE_BLOCKED` | 当前许可或公开边界不允许预期使用或再分发。它可以阻止公开再分发，但没有进一步规定时不自动禁止内部科研。 |
| `IDENTITY_DRIFT` | 实际输入、代码、配置或 artifact identity 与登记的身份或 provenance 不一致。 |
| `CONTRACT_INCOMPLETE` | 所需协议、门控、字段或验收规则没有定义到足以继续执行。 |
| `RESOURCE_BUSY` | CPU、GPU、存储或远端执行资源不可用或正在被占用。 |
| `DATE_NOT_DUE` | 依赖日期的动作尚未满足资格。必须记录恢复日期或条件，只暂停该动作。 |
| `BUDGET_LIMITED` | 时间、算力、存储或经费不足以执行计划动作。这不是实验失败。 |
| `HUMAN_APPROVAL_REQUIRED` | 动作或主张在继续前需要指定人工决策。 |
| `SCIENTIFIC_GATE_FAILED` | 在当前协议和阈值下，科学问题或晋级门没有通过。 |

这些代码分别表达访问与权限、输入与 artifact、许可与公开边界、
provenance/hash 漂移、协议不完整、资源占用、日期或预算限制、人工批准和
科学失败。特别是，`ACCESS_BLOCKED` 不等于 `SCIENTIFIC_GATE_FAILED`；
`INPUT_MISSING` 不等于“方法失败”；`DATE_NOT_DUE` 只阻塞日期相关动作；
`BUDGET_LIMITED` 不表示实验失败。

## Artifact 身份与可用性

Artifact identity、provenance、availability、hash verification 和 load
verification 是不同字段。有 hash 不证明文件可访问；有 checkpoint identity
不证明 checkpoint 内容已经加载。metadata-only 检查不能记录成 load
verification；`REGISTERED` 也绝不能被下游解释成 `AVAILABLE`。

使用以下生命周期：

| 状态 | 含义 |
|---|---|
| `REGISTERED` | 已记录 artifact identity、来源或预期用途；不声明文件存在。 |
| `LOCATABLE` | 已知可能的路径、来源或检索位置。 |
| `ACCESSIBLE` | 在授权边界内可以读取文件元数据或内容。 |
| `HASH_VERIFIED` | 实际文件字节与登记的 hash 一致。 |
| `STAGED` | 文件已复制到授权的本地 staging 位置。 |
| `LOAD_VERIFIED` | 文件已通过规定的解析器或 loader 检查。 |
| `EVALUATED` | 文件已在明确的评估协议下使用。 |

必要时使用以下失败或阻塞状态：

`ACCESS_BLOCKED`、`MISSING`、`HASH_MISMATCH`、`LICENSE_BLOCKED` 和
`LOAD_FAILED`。

这些状态的边界是：

| 状态 | 含义 |
|---|---|
| `ACCESS_BLOCKED` | artifact 可以已经登记或定位，但当前授权不允许读取。 |
| `MISSING` | 在声明的位置或可定位来源中找不到预期 artifact。 |
| `HASH_MISMATCH` | 可访问文件的字节与登记的 hash 不一致。 |
| `LICENSE_BLOCKED` | 已知许可边界不允许按当前目的使用或再分发 artifact。 |
| `LOAD_FAILED` | 文件可访问，但未通过规定的解析器或 loader 检查。 |

探索性重新生成必须创建新的 artifact identity，并标注
`stage: EXPLORATORY` 与 `provenance: newly_generated`。新 artifact 不能
覆盖旧 artifact 的 hash 或历史 provenance，artifact availability 也不能
自动升级为科学主张。

例如，一个完全虚构的记录可以写成：

```text
artifact: fictional_sequence_a_estimate
REGISTERED -> ACCESS_BLOCKED
```

之后的探索实验可以生成：

```text
artifact: fictional_sequence_a_estimate_v2
stage: EXPLORATORY
provenance: newly_generated
```

第二条记录可用于探索，但不能写回第一条 artifact 的 hash 或历史
provenance。artifact 缺失或不可访问，也不能自动解释为方法失败。

## 日期语义

`memory/CURRENT_STATE.md` 中的 `Date` 是项目快照日期，不自动等于会话、
实验或日期门禁的权威日期。系统会话日期、项目文件日期和机器时钟观测必须
分开记录。

每个日期门禁都应记录：

```yaml
governing_date: 2026-01-15T00:00:00Z
date_authority: registered protocol
timezone: UTC
observed_at: 2026-01-15T09:30:00Z
eligible_after: 2026-01-16T00:00:00Z
date_conflict_policy: use the registered protocol authority and record conflicting observations
```

主机时钟、远端时钟和 NTP 状态只能作为观测证据，不能自动成为权威。日期
冲突时要记录具体日期和时间，不能用“今天”“昨天”“明天”替代。跨日或跨
时区判断优先使用完整 ISO-8601 时间戳，而不是只有日期的字段。

过期的提示词或旧项目记录不能覆盖当前会话的权威日期。如果日期只影响一项
实验，只暂停该实验；无关文档、CPU 验证和只读审计仍可继续。
`DATE_NOT_DUE` 必须说明恢复日期或可验证的恢复条件。

## 科研门控

一个科研实验只有在以下条件满足后才算完成：

1. 阶段、假设和晋级门已在执行前或执行中登记；
2. 精确的代码、配置、输入角色、artifact identity、availability 和输出路径
   已知；
3. 指标或验证证据已记录；
4. 结果已分类为 final、failed、deprecated 或 still validating；
5. 每条阻塞都有 code、owner、恢复条件、安全下一步和证据引用；
6. 可复现 bug 已加入坑位目录；
7. 如果活动路线或证据边界发生变化，已替换 Current State。

## 方向门控

项目转向只有在以下条件满足后才接受：

1. 总结当前路线的证据边界；
2. 记录停止或继续的理由；
3. 列出替代方案；
4. 明确复盘条件；
5. 下一条路线出现在 Current State；
6. 阶段晋级或降级已显式记录。

这可以避免依靠惯性漂移。项目可以停止弱路线，不必假装每条失败分支都没有
价值。

## 交付门控

交付 artifact 只有在以下条件满足后才接受：

1. artifact identity 和 availability 状态已列入交付索引；
2. 证据边界明确；
3. 生成产物已分类为 accepted、diagnostic、archive 或 external；
4. 图像或报告 artifact 已实际审阅；
5. 不受支持的主张已明确写出；
6. 最终人工 release approval 已记录。

## 为什么对 Agent 有帮助

Coding Agent 可以执行很多局部步骤，但没有门控时，也很容易制造进展假象。

ResearchMemoryKit 为 Agent 提供项目级契约：

- 首先读什么；
- 当前适用哪个阶段；
- 需要更新什么；
- 如何命名阻塞；
- 实际知道哪个 artifact 状态；
- 何时应安全停止或继续；
- 什么证据才足够；
- 当前还不能声称什么。

这不是完全自动化，而是带有持久审计轨迹和人工科学判断边界的受监督自主。

## 最小门控模板

```markdown
## Completion Gate

This task is complete only if:

- [ ] 当前研究阶段和晋级边界已记录；
- [ ] 权威 Current State 已反映结果；
- [ ] 已存在决策、结论、失败或交付记录；
- [ ] 复现所需的命令、配置、artifact identity、availability 和路径已记录；
- [ ] 阻塞包含 code、恢复条件、安全下一步和证据引用；
- [ ] 新坑位已记录；
- [ ] 不受支持的主张已明确排除；
- [ ] 准备公开主张或 release 时，已记录最终人工批准。
```
