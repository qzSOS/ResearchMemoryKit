# Experiment Log

## EXP-001: Leakage-Safe Baseline Gate

| Field | Value |
|---|---|
| Date | 2026-07-14 |
| Status | FINAL/pass |
| Hypothesis | A simple baseline can run on the leakage-safe toy split and produce stable reference outputs. |
| Gate | Metrics file exists, preview artifacts are reviewed, and split hashes contain no overlap. |
| Code commit | `example-commit-001` |
| Config | `registry/config/EXP-001.yaml` |
| Output | `outputs/EXP-001/` |
| Metrics | Synthetic score: 20.0; overlap count: 0. |
| Evidence review | The score is only a control reference, not a publishable improvement claim. |
| Conclusion | Baseline protocol is valid enough to support one reliability gate. |
| Follow-up | Register `EXP-002` reliability defer gate. |

## Entry Template

```markdown
## EXP-NNN: Title

| Field | Value |
|---|---|
| Date |  |
| Status | FINAL/pass, FINAL/fail, FAILED, VALIDATING, DEPRECATED |
| Hypothesis |  |
| Gate |  |
| Code commit |  |
| Config |  |
| Output |  |
| Metrics |  |
| Evidence review |  |
| Conclusion |  |
| Follow-up |  |
```
