# Project Memory Router

Read `CURRENT_STATE.md` first in every new session.

| Need | Authoritative file |
|---|---|
| Recover current project state | `CURRENT_STATE.md` |
| Understand design decisions | `DECISIONS.md` |
| Follow development and release gates | `WORKFLOW.md` |
| Review significant implementation sessions | `SESSION_LOG.md` |

## Semantics

- `CURRENT_STATE.md` is overwriteable.
- `DECISIONS.md` and `SESSION_LOG.md` are append-only.
- `WORKFLOW.md` changes only when the development contract changes.
- Chat history is not an authoritative project record.
