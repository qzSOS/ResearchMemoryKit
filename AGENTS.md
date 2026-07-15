# ResearchMemoryKit Agent Instructions

These instructions apply to this repository.

## Session Startup

Before non-trivial work:

1. Read `memory/CURRENT_STATE.md`.
2. Read `memory/README.md` and the task-specific routed files.
3. Read `memory/WORKFLOW.md` before implementation or release work.
4. Inspect `git status` and preserve unrelated changes.

Do not treat a phase as complete until its gate passes and the memory layer
reflects the new state.

## Repository Rules

- Keep current mutable truth in `memory/CURRENT_STATE.md`.
- Keep this router low-volatility.
- Append decisions and significant sessions; do not silently rewrite history.
- Keep the Python runtime dependency-free.
- Prefer explicit contracts over heuristics when checking project structure.
- Preserve public-release validation and strict desensitization.

