# Starter Prompts for Coding Agents

These prompts help a coding agent use ResearchMemoryKit consistently.

The Chinese counterpart is [agent-prompts.zh-CN.md](agent-prompts.zh-CN.md).

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
8. If automated structural checks would help this project, create an `rmk.json` contract for the router, Current State, required files, append-only files, routed targets, stale threshold, and gate headings.
9. If that optional contract is created and the command is available, run `rmk check`.
10. Ask whether the project is private, shared, or being prepared for public release.
11. Preserve operational facts needed to resume the work. Exact machine paths are allowed when necessary in a private project, but prefer repository-relative paths or named environment roots in shared files.
12. Keep per-machine mappings in a gitignored local file when practical. Never store credentials or secrets in project memory.
13. Apply anonymization and publication restrictions only to files or exports that will be public.

After creating the structure, explain:
- why each file exists;
- which file is authoritative for each kind of fact;
- the first Current State;
- the first decision record;
- the completion gate that future agents must follow;
- the `rmk check` result, if the optional contract was enabled.
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
6. Run `rmk check` before closing a substantial task if the repository uses `rmk.json`.

Do not treat the task as complete until the memory layer reflects any major state change.
```

## Research Stage, Blocker, and Artifact Semantics

Use this prompt for research tasks that can produce evidence, consume
artifacts, change a research direction, or pause on a condition.

```text
This project uses ResearchMemoryKit. Before starting, inspect the current
research stage and the written gate.

1. Decide whether the current work is EXPLORATORY, CONFIRMATORY, or PAPER.
   State whether the task is exploration, confirmation, or paper preparation.
2. Keep the stage separate from evidence grade. Do not automatically promote
   an exploratory result because a test passes.
3. If work is blocked, use one standard blocker code:
   ACCESS_BLOCKED, INPUT_MISSING, LICENSE_BLOCKED, IDENTITY_DRIFT,
   CONTRACT_INCOMPLETE, RESOURCE_BUSY, DATE_NOT_DUE, BUDGET_LIMITED,
   HUMAN_APPROVAL_REQUIRED, or SCIENTIFIC_GATE_FAILED.
4. Record blocker_code, summary, recoverable, owner, recovery_condition,
   safe_next_action, scientific_impact, observed_at as a full ISO-8601
   timestamp, and evidence_reference as a repository-relative path, commit,
   Goal ID, or artifact ID.
5. Keep artifact identity separate from artifact availability. Distinguish
   REGISTERED, LOCATABLE, ACCESSIBLE, HASH_VERIFIED, STAGED, LOAD_VERIFIED,
   and EVALUATED. Do not treat a registration, hash, checkpoint identity, or
   metadata-only check as proof that a file is available or loadable.
6. If an exploratory run regenerates an artifact, create a new artifact
   identity with newly_generated provenance. Never overwrite historical hash or
   provenance.
7. Record the recovery condition and the next safe action. Do not freeze
   unrelated documentation, validation, or read-only audit work because one
   local action is blocked.
8. Do not turn exploratory results into paper claims. Keep observations,
   failures, interpretations, evidence boundaries, and unsupported claims
   distinct.
9. For cross-day or cross-time-zone work, record governing_date,
   date_authority, timezone, observed_at, eligible_after, and
   date_conflict_policy. Treat the Current State Date as a project snapshot,
   not automatically as the session date authority.
10. Before closing the task, update memory/CURRENT_STATE.md and append the
    relevant decision, conclusion, failure, pitfall, or session record.
    Preserve human scientific judgment and final authorship, submission, and
    release approval.
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
- If automated structural checks are useful, create or update rmk.json and run rmk check.
- Preserve operational paths needed by the private project.
- Prefer named environment roots or gitignored local mappings when the project is shared across machines.
- Never write credentials into project memory.
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
Run rmk check . --strict if the repository has rmk.json.
```
