# Research Project Agent Instructions

These instructions apply to this repository.

## Mandatory Session Startup

Before any non-trivial task:

1. Read `memory/CURRENT_STATE.md`.
2. Read this file.
3. Read `memory/README.md` and the task-specific routed files.
4. Inspect `git status` and preserve unrelated user changes.
5. Before coding, read `memory/WORKFLOW.md` and `memory/PITFALLS.md`.
6. Before remote or GPU work, read `memory/ENVIRONMENT.md` if present.

Never assume remembered context is current. Re-read and verify.

## Memory Semantics

- `memory/CURRENT_STATE.md`: overwriteable snapshot.
- `memory/DECISIONS.md`: append-only decisions with rationale and revisit conditions.
- `memory/EXPERIMENT_LOG.md`: conclusions are append-only; presentation can be reorganized without deleting conclusions.
- `memory/FAILED_ATTEMPTS.md`: append-only failed routes and preserved lessons.
- `memory/PITFALLS.md`: append-only high-risk bugs and diagnostics.
- `memory/SESSION_LOG.md`: append-only significant session activity.
- `memory/WORKFLOW.md`: reusable execution and validation rules.
- `registry/`: experiment metadata only. Large outputs stay outside git.

## Current-State Activation

The Current State pattern is active from Day 0 and mandatory.

- Keep it under 35 lines.
- Replace the snapshot rather than appending history.
- If older than seven days, treat it as stale.
- A major state change is not complete until Current State reflects it.

## Experiment Lifecycle

No expensive experiment should run without a registry entry.

Lifecycle:

`PLANNED -> REGISTERED -> RUNNING -> VALIDATING -> FINAL | FAILED | DEPRECATED`

Each experiment should have:

- a unique ID;
- hypothesis and promotion gate;
- code commit;
- dataset or input role;
- exact config;
- output path;
- status and final metrics.

## Router Discipline

Keep this file low-volatility. Do not store mutable project truth here. Link to `memory/CURRENT_STATE.md` instead.
