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

## Public Boundary

This directory is intentionally versioned as ResearchMemoryKit's own
self-hosted memory layer. It may record public development decisions, release
gates, and validation results for this repository only.

Do not place private project names, unpublished results, personal contact
details, local or server paths, collaborators, clients, patients, or
institution-specific data here.
