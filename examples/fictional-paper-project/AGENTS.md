# Fictional Paper Project Agent Instructions

## Startup

1. Read `memory/CURRENT_STATE.md`.
2. Read `memory/README.md`.
3. Inspect git status.
4. Read `memory/WORKFLOW.md` before experiments.

## Project Rule

This project advances only through gates. Running code is not enough.

Any experiment must close one of these states:

- `FINAL`: evidence supports the conclusion;
- `FAILED`: evidence closes the route;
- `VALIDATING`: evidence exists but needs independent review;
- `DEPRECATED`: superseded by a later, better-controlled record.

## Router Discipline

Do not store current mutable truth in this file. Put active status in `memory/CURRENT_STATE.md`.
