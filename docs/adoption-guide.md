# Adoption Guide

This guide describes how to introduce ResearchMemoryKit into a real project.

## New Projects

1. Choose a template or ask an agent to design a project-specific structure.
2. Copy or create the Markdown memory files.
3. Fill in `CURRENT_STATE.md`.
4. Record the initial scope decision.
5. Define the written completion gate.
6. Commit the memory layer before project work starts.
7. Optionally add `rmk.json` and run `rmk check` when automated structural
   checks would help.

No package installation is required for the core workflow:

```bash
python scripts/init_memory.py research-project /path/to/new-project
cd /path/to/new-project
git add .
git commit -m "Initialize project memory layer"
```

To enable the optional checker:

```bash
python -m pip install -e /path/to/ResearchMemoryKit --no-deps
rmk check .
```

An untouched template intentionally fails until its Current State date is
initialized when the optional checker is used.

## Existing Projects

Retrofitting is harder because agents and humans already have habits.

Use this sequence:

1. Copy the template.
2. Write `CURRENT_STATE.md` from the actual current state.
3. Add one decision explaining why the memory layer exists.
4. Add a completion gate to the workflow.
5. During the next real task, explicitly update memory before calling the task done.
6. If CI or repeated structural drift is a concern, make `rmk.json` describe
   the authoritative files and gates, then run `rmk check`.

Do not just add files and expect behavior to change.

## Team Use

For small teams:

- keep one memory layer in the repository;
- assign one file as the source of truth for each mutable fact;
- review Current State in handoffs;
- keep generated artifacts outside git unless curated.

## Paths, environments, and secrets

ResearchMemoryKit does not require a private project to hide information that
is needed to run the project.

- Paths inside `rmk.json` are repository-relative because they describe files
  in the project contract.
- Experiment and environment records may use exact local or server paths when
  the repository is private and those paths are operationally necessary.
- For a shared repository, prefer stable environment roles and path keys.
  Keep per-machine mappings in a gitignored file such as
  `memory/ENVIRONMENT.local.md`.
- Add `*.local.md` to the target project's `.gitignore` before relying on that
  convention.
- Credentials never belong in memory files, even in a private repository.

Apply the stricter rules in
[publishing-safely.md](publishing-safely.md) only when material will be made
public.

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
- run `rmk check` before calling a substantial task complete when the project
  uses the optional contract.

Per experiment:

- update registry;
- record conclusion or failure;
- add pitfalls;
- replace Current State.

Per milestone:

- audit duplicate truth;
- archive or classify outputs;
- add indexes for large logs.
