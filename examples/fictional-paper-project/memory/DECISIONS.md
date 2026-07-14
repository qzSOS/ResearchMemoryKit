# Decision Log

## D-001: Scope the Paper Around Deferral, Not a New Model

| Field | Value |
|---|---|
| Date | 2026-07-14 |
| Status | Active |
| Question | Should the paper propose a new restoration model or a reliability-controlled deferral protocol? |
| Decision | Study the deferral protocol. |
| Rationale | The project needs a controlled, auditable contribution. A new model would add uncontrolled variables. |
| Alternatives | Train a larger model; add a new loss; build a new dataset. |
| Revisit condition | If the baseline cannot produce stable outputs under a leakage-safe split. |
| Source | Project bootstrap. |

## D-002: Require Split Validation Before Reliability Claims

| Field | Value |
|---|---|
| Date | 2026-07-14 |
| Status | Active |
| Question | Can reliability experiments start before split leakage is ruled out? |
| Decision | No. The split validation gate must pass first. |
| Rationale | Reliability signals are meaningless if validation data overlaps training data. |
| Alternatives | Run reliability experiments immediately and audit later. |
| Revisit condition | None; this is a hard validity gate. |
| Source | `F-001`, `P-001`. |
