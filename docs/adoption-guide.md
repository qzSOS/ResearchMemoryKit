# Adoption Guide

This guide describes how to introduce ResearchMemoryKit into a real project.

## New Projects

1. Choose a template.
2. Copy it with `scripts/init_memory.py`.
3. Fill in `CURRENT_STATE.md`.
4. Record the initial scope decision.
5. Run `rmk check`.
6. Commit the memory layer before project work starts.

Recommended:

```bash
python -m pip install -e /path/to/ResearchMemoryKit --no-deps
python scripts/init_memory.py research-project /path/to/new-project
cd /path/to/new-project
rmk check .
git add .
git commit -m "Initialize project memory layer"
```

An untouched template intentionally fails until its Current State date is
initialized.

## Existing Projects

Retrofitting is harder because agents and humans already have habits.

Use this sequence:

1. Copy the template.
2. Write `CURRENT_STATE.md` from the actual current state.
3. Add one decision explaining why the memory layer exists.
4. Add a completion gate to the workflow.
5. Make `rmk.json` describe the authoritative files and gates.
6. Run `rmk check` and resolve contract errors.
7. During the next real task, explicitly update memory before calling the task done.

Do not just add files and expect behavior to change.

## Team Use

For small teams:

- keep one memory layer in the repository;
- assign one file as the source of truth for each mutable fact;
- review Current State in handoffs;
- keep generated artifacts outside git unless curated.

## Warning Signs

Add an index or simplify when:

- Current State exceeds 35 lines;
- the router repeats current results;
- decisions lack revisit conditions;
- failed attempts are only mentioned in chat;
- generated outputs cannot be classified;
- append-only logs are too large to scan.

## Maintenance Rhythm

Daily or per session:

- replace Current State when active status changes;
- append significant session activity.
- run `rmk check` before calling a substantial task complete.

Per experiment:

- update registry;
- record conclusion or failure;
- add pitfalls;
- replace Current State.

Per milestone:

- audit duplicate truth;
- archive or classify outputs;
- add indexes for large logs.
