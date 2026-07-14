# Memory Router

Read `CURRENT_STATE.md` first in every new session.

| Task | Authoritative file |
|---|---|
| Recover current status | `CURRENT_STATE.md` |
| Check why a direction was chosen | `DECISIONS.md` |
| Check completed experiment conclusions | `EXPERIMENT_LOG.md` |
| Avoid repeating failed work | `FAILED_ATTEMPTS.md` |
| Diagnose recurring bugs | `PITFALLS.md` |
| Follow execution and validation rules | `WORKFLOW.md` |
| Review recent significant activity | `SESSION_LOG.md` |

## Lifecycle Rules

- Current facts live in `CURRENT_STATE.md`.
- Decisions, failures, pitfalls, and conclusions are append-only.
- Temporary scratch notes should not become a second truth source.
- Large append-only files should gain an index or summary when retrieval becomes slow.
