# Starter Prompts for Coding Agents

These prompts help a coding agent use ResearchMemoryKit consistently.

## Adaptive Memory Layer Design

Use this when a fixed template is not enough and you want the agent to design the project structure and memory layer from the actual project needs.

```text
I want this project to use ResearchMemoryKit, but the project may need a custom structure.

Please inspect the project goal, expected artifacts, experiment or delivery workflow, privacy constraints, and collaboration pattern. Then design a project directory and memory layer that fits this project.

Requirements:
1. Create a low-volatility router file such as AGENTS.md.
2. Create an overwriteable Current State file as the first session recovery target.
3. Create append-only records for decisions, failed attempts, pitfalls, and significant activity.
4. If the project has experiments, create a metadata-only registry and an experiment completion gate.
5. If the project has deliverables, create a delivery index and evidence-boundary rules.
6. Define what counts as "done" for the project: which memory files must be updated before a task, experiment, pivot, or delivery is complete.
7. Keep mutable facts in one authoritative source; routers should link to Current State instead of restating current truth.
8. Do not include private paths, credentials, unpublished sensitive details, or personal information.

After creating the structure, explain:
- why each file exists;
- which file is authoritative for each kind of fact;
- the first Current State;
- the first decision record;
- the completion gate that future agents must follow.
```

## New Session

```text
This project uses ResearchMemoryKit.

Before doing non-trivial work:
1. Read AGENTS.md.
2. Read memory/CURRENT_STATE.md first.
3. Read memory/README.md and any routed files needed for the task.
4. Inspect git status.
5. Follow memory/WORKFLOW.md.

Do not treat the task as complete until the memory layer reflects any major state change.
```

## End of Experiment

```text
Please close this experiment using the ResearchMemoryKit completion gate:
1. update registry status and metrics;
2. record the conclusion in memory/EXPERIMENT_LOG.md or the failure in memory/FAILED_ATTEMPTS.md;
3. add any reproducible bug to memory/PITFALLS.md;
4. append memory/SESSION_LOG.md;
5. replace memory/CURRENT_STATE.md if the active state changed.
```

## Retrofitting an Existing Project

```text
Please initialize ResearchMemoryKit for this existing project.

Constraints:
- Keep AGENTS.md as a low-volatility router.
- Put current mutable facts only in memory/CURRENT_STATE.md.
- Add one decision explaining why the memory layer exists.
- Add a completion gate to memory/WORKFLOW.md.
- Do not copy private paths, credentials, or unpublished sensitive details into public-facing files.
```

## Public Release Audit

```text
Please audit this repository before public release.

Check:
- no private project names;
- no unpublished metrics or claims;
- no local paths, server aliases, emails, tokens, or credentials;
- Markdown links resolve;
- JSON files parse;
- examples are fictional or fully anonymized.

Run scripts/validate_public_repo.py if available.
```
