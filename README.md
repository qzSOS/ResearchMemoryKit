# ResearchMemoryKit

A gated memory layer for trustworthy AI-assisted research workflows.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No runtime dependencies](https://img.shields.io/badge/runtime_dependencies-none-blue.svg)](pyproject.toml)
[![Validate](https://github.com/qzSOS/ResearchMemoryKit/actions/workflows/validate.yml/badge.svg)](https://github.com/qzSOS/ResearchMemoryKit/actions/workflows/validate.yml)
[![Bilingual](https://img.shields.io/badge/docs-EN%20%7C%20ZH-lightgrey.svg)](README.zh-CN.md)
[![LINUX DO](https://img.shields.io/badge/LINUX-DO-ffb000.svg)](https://linux.do)

ResearchMemoryKit is not an agent runtime, experiment tracker, database, or workflow engine. It is a small Markdown-based layer that helps a human researcher and coding agents recover context, preserve decisions, gate project progress, and keep evidence reproducible across many sessions.

It is more than a context note template. The goal is to turn long AI-assisted research into a **gated, auditable operating loop**: every direction change has rationale, every experiment has a completion gate, every failure preserves a lesson, and every new session starts from a credible current state.

```text
Current State
  -> Decision / Gate
  -> Registered work
  -> Execution
  -> Evidence review
  -> Conclusion or failure
  -> Pitfall / Session update
  -> Current State replacement
```

中文说明: [README.zh-CN.md](README.zh-CN.md)

## 30-Second Demo

```bash
git clone https://github.com/qzSOS/ResearchMemoryKit.git
cd ResearchMemoryKit
python -m pip install -e . --no-deps
rmk check . --strict
python scripts/init_memory.py research-project /tmp/my-research-project
```

The repository validates its own memory contract, then initializes a project
with a current snapshot, decision log, experiment log, failed-attempt record,
pitfall catalog, workflow gate, metadata-only registry, and `rmk.json`.

Fill the generated Current State before running:

```bash
rmk check /tmp/my-research-project
```

An uninitialized `YYYY-MM-DD` date is intentionally reported as an error.

For read-only examples, open:

- [examples/toy-research-project](examples/toy-research-project) for the smallest complete memory layer;
- [examples/fictional-paper-project](examples/fictional-paper-project) for a gated paper-style workflow.

## What It Helps With

- **Context recovery**: a new human or agent can restart from a short Current State file.
- **Project steering**: decisions include rationale, alternatives, and revisit conditions, so the project can stop weak routes instead of drifting.
- **Trusted research**: experiments close only after results, failures, pitfalls, and state changes are recorded.
- **Reproducible engineering**: metadata, commands, outputs, and evidence boundaries stay connected.
- **Agent autonomy with guardrails**: agents can push work forward, but gates define what counts as real progress.

## Why This Exists

AI coding agents are good at local execution, but long research projects fail in different ways:

- the current status is buried in a long chat history;
- decisions are copied into multiple files and drift;
- failed experiments disappear, then get repeated;
- "temporary" notes become permanent clutter;
- agents update familiar files but skip the new memory structure;
- agents keep executing tasks without proving that a research gate passed;
- generated outputs grow faster than the project can explain them.

ResearchMemoryKit treats these as normal research-engineering failure modes. It keeps the system small enough to maintain by hand, while giving every new session a reliable recovery path and every major step an auditable completion condition.

## Core Pattern

Every project starts with a few files:

```text
AGENTS.md or README.md       recovery router and project rules
memory/CURRENT_STATE.md      overwriteable current snapshot
memory/DECISIONS.md          append-only decisions
memory/EXPERIMENT_LOG.md     append-only conclusions, reformattable presentation
memory/FAILED_ATTEMPTS.md    append-only failed routes and preserved lessons
memory/PITFALLS.md           append-only recurring bugs and diagnostics
memory/SESSION_LOG.md        append-only significant activity
memory/WORKFLOW.md           completion gates and operating rules
registry/                    optional experiment metadata only
```

The critical rule is simple:

> A task is not complete until its gate has passed and the memory layer reflects what changed.

## Machine-Verifiable Gates

Each managed project includes an explicit `rmk.json` contract. The P0 checker
validates required files, path safety, router reachability, gate headings,
Current State dates, staleness, and unresolved placeholders.

```bash
rmk check /path/to/project
rmk check /path/to/project --strict
rmk check /path/to/project --format json
```

Normal mode fails on broken contracts. `--strict` also fails on warnings, which
makes it suitable for CI. See [docs/rmk-check.md](docs/rmk-check.md) for the
manifest and stable finding codes.

## Key Ideas

- **Current State first**: a short, overwriteable snapshot is the entry point for every session.
- **History is append-only**: decisions, failures, and conclusions preserve provenance.
- **Routers stay boring**: routers describe where to read, not what the current result is.
- **One fact, one source**: duplicate mutable truth is treated as a bug.
- **Completion gates activate behavior**: templates only work when memory updates are part of the definition of done.
- **Gates steer the project**: experiments, pivots, and deliverables have explicit pass/fail or revisit conditions.
- **Evidence boundaries matter**: do not turn preliminary results into stronger claims than the evidence supports.

## Quick Start

Use the initialization script:

```bash
python -m pip install -e . --no-deps
python scripts/init_memory.py minimal /path/to/project
python scripts/init_memory.py research-project /path/to/project
python scripts/init_memory.py delivery-project /path/to/project
rmk check /path/to/project
```

Or copy a template manually.

For a small project:

```text
templates/minimal/
```

For an experiment-heavy research project:

```text
templates/research-project/
```

For an engineering or client-delivery project:

```text
templates/delivery-project/
```

Then make the first commit before doing project work. The memory layer depends on version history for trust.

The generated contract will fail until the Current State date is initialized.
This prevents an untouched template from appearing healthy.

If your project does not fit a fixed template, use the adaptive prompt in [docs/agent-prompts.md](docs/agent-prompts.md#adaptive-memory-layer-design). It asks an agent to inspect the project needs and design a tailored directory plus memory layer.

## Use With an Agent

For a new project, you can give a coding agent this short instruction:

```text
Initialize this project with ResearchMemoryKit. Read the project goal and expected workflow, then create the smallest useful directory and memory layer. Define the completion gate that future work must pass before it is considered done. Do not include private paths, unpublished results, credentials, or personal information.
```

Longer prompts are available in [docs/agent-prompts.md](docs/agent-prompts.md).

## Which Template Should I Use?

| Template | Best for | Includes |
|---|---|---|
| `minimal` | small projects, reading notes, one-person prototypes | Current State, Decisions, Session Log |
| `research-project` | ML/AI research, experiments, paper work, long baselines | memory router, experiment log, failed attempts, pitfalls, workflow gate, registry |
| `delivery-project` | engineering reports, client-facing artifacts, generated figures/videos | project state, delivery index, decision log, work log, evidence-boundary rules |

## How It Compares

| Tool category | What it is good at | ResearchMemoryKit difference |
|---|---|---|
| Agent memory databases | storing and retrieving agent memories | file-based, inspectable, git-native, no service required |
| Experiment trackers | metrics, dashboards, runs, artifacts | captures rationale, failed routes, current state, and evidence boundaries |
| Project management tools | tasks, owners, deadlines | designed for research uncertainty and multi-session agent handoff |
| Notes apps | flexible human notes | adds lifecycle semantics and completion gates |

See [docs/comparison.md](docs/comparison.md) for the longer version.

## Repository Layout

```text
templates/                 reusable gated memory templates
examples/                  fully sanitized toy examples
examples/fictional-paper-project gated paper-style example
researchmemorykit/          dependency-free checker and CLI
tests/                      standard-library regression tests
rmk.json                    this repository's self-hosted contract
memory/                     public-safe memory for this repository itself
docs/theory.md             design principles and failure modes
docs/rmk-check.md           checker contract and stable finding codes
docs/gated-research-workflow.md trusted research and reproducible engineering loop
docs/case-studies/         anonymized case studies
docs/desensitization.md    public-release checklist
docs/agent-prompts.md      starter prompts for coding agents
docs/blog/                 publishable essays and project introductions
docs/github-actions/       optional CI workflow template
scripts/init_memory.py     dependency-free template initializer
scripts/validate_public_repo.py public-release validation checks
scripts/enable_github_actions.py local helper to install the optional workflow
```

The root `memory/` directory is intentional. It records only the development
of ResearchMemoryKit itself and acts as a sanitized self-hosting example for
the contract checked by `rmk check . --strict`. It contains no memory copied
from private research projects.

## Further Reading

- [AI Research Agents Need Gates, Not Just Memory](docs/blog/ai-research-agents-need-gates.md)
- [AI 科研 Agent 需要的不只是记忆，而是门控](docs/blog/ai-research-agents-need-gates-zh.md)

## When To Use This

Use ResearchMemoryKit when:

- a project spans weeks or months;
- multiple agents or sessions will touch it;
- failed experiments are useful evidence;
- decisions need rationale and revisit conditions;
- current status must be recoverable without reading the whole chat history.
- the project needs gates before claims, pivots, or deliverables are accepted.

Do not use it when:

- the task fits in one short session;
- a real experiment tracking platform is already required;
- the team needs permissions, dashboards, or a database-backed workflow.

## About

This project was created by [qzSOS](https://github.com/qzSOS) as a public reference implementation distilled from a gated memory layer used across multiple long-running AI-assisted projects.

The public repository intentionally uses anonymized examples and templates. It does not include private project names, unpublished results, server paths, collaborators, client information, or dataset-specific confidential details.

## Roadmap

- registry lifecycle and experiment cross-reference checks;
- git-aware append-only deletion detection;
- claim evidence and human-review status;
- conservative router-truth-duplication checks;
- optional active indexes for very large append-only files;
- more sanitized examples for paper writing and benchmark packaging;
- a small GitHub Pages documentation site;
- starter prompts for common coding agents.

## License

MIT License. See [LICENSE](LICENSE).
