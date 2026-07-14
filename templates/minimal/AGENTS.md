# Project Agent Router

New session? Read in this order:

1. `CURRENT_STATE.md` - current snapshot
2. `AGENTS.md` - this file, project rules and routing
3. `DECISIONS.md` - rationale for important choices
4. `SESSION_LOG.md` - recent significant activity if the state is stale

If `CURRENT_STATE.md` is older than seven days, treat it as stale and read `SESSION_LOG.md` plus recent git history.

## File Semantics

| File | Semantics | Update rule |
|---|---|---|
| `CURRENT_STATE.md` | Overwriteable current snapshot | Replace after major state changes |
| `DECISIONS.md` | Append-only decisions | Append when direction, scope, or method changes |
| `SESSION_LOG.md` | Append-only activity | Append after significant work |
| `AGENTS.md` | Low-volatility router | Update only when structure or rules change |

## Rules

- Keep the router low-volatility. Do not store current results here.
- One mutable fact has one authoritative source.
- Do not let important findings live only in chat history.
- A task is not complete until the memory files reflect what changed.
- Use git history for provenance; commit the memory layer early.
