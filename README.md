# ResearchMemoryKit

A lightweight Markdown memory system for long-running AI-assisted research projects.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![No dependencies](https://img.shields.io/badge/dependencies-none-blue.svg)](scripts/init_memory.py)
[![Validation](https://img.shields.io/badge/validation-scripted-blue.svg)](scripts/validate_public_repo.py)
[![Bilingual](https://img.shields.io/badge/docs-EN%20%7C%20ZH-lightgrey.svg)](README.zh-CN.md)

ResearchMemoryKit is not an agent runtime, experiment tracker, database, or workflow engine. It is a small set of files and rules that help a human researcher and coding agents recover context, preserve decisions, and keep experiments moving across many sessions.

中文说明: [README.zh-CN.md](README.zh-CN.md)

## 30-Second Demo

```bash
git clone https://github.com/qzSOS/ResearchMemoryKit.git
cd ResearchMemoryKit
python scripts/init_memory.py research-project /tmp/my-research-project
cd /tmp/my-research-project
find . -maxdepth 3 -type f | sort
```

You now have a project memory layer with a current snapshot, decision log, experiment log, failed-attempt record, pitfall catalog, workflow gate, and metadata-only registry.

For a read-only example, open [examples/toy-research-project](examples/toy-research-project).

## Why This Exists

AI coding agents are good at local execution, but long research projects fail in different ways:

- the current status is buried in a long chat history;
- decisions are copied into multiple files and drift;
- failed experiments disappear, then get repeated;
- "temporary" notes become permanent clutter;
- agents update familiar files but skip the new memory structure;
- generated outputs grow faster than the project can explain them.

ResearchMemoryKit treats these as normal research-engineering failure modes. It keeps the system small enough to maintain by hand, while giving every new session a reliable recovery path.

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

> A task is not complete until the memory layer reflects what changed.

## Key Ideas

- **Current State first**: a short, overwriteable snapshot is the entry point for every session.
- **History is append-only**: decisions, failures, and conclusions preserve provenance.
- **Routers stay boring**: routers describe where to read, not what the current result is.
- **One fact, one source**: duplicate mutable truth is treated as a bug.
- **Completion gates activate behavior**: templates only work when memory updates are part of the definition of done.
- **Evidence boundaries matter**: do not turn preliminary results into stronger claims than the evidence supports.

## Quick Start

Use the initialization script:

```bash
python scripts/init_memory.py minimal /path/to/project
python scripts/init_memory.py research-project /path/to/project
python scripts/init_memory.py delivery-project /path/to/project
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

Then make the first commit before doing project work. The memory system depends on version history for trust.

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
templates/                 reusable project memory templates
examples/                  fully sanitized toy examples
docs/theory.md             design principles and failure modes
docs/case-studies/         anonymized case studies
docs/desensitization.md    public-release checklist
docs/portfolio-plan.md     how this project can be presented in a portfolio
docs/agent-prompts.md      starter prompts for coding agents
scripts/init_memory.py     dependency-free template initializer
scripts/validate_public_repo.py public-release validation checks
```

## When To Use This

Use ResearchMemoryKit when:

- a project spans weeks or months;
- multiple agents or sessions will touch it;
- failed experiments are useful evidence;
- decisions need rationale and revisit conditions;
- current status must be recoverable without reading the whole chat history.

Do not use it when:

- the task fits in one short session;
- a real experiment tracking platform is already required;
- the team needs permissions, dashboards, or a database-backed workflow.

## About

This project was created by [qzSOS](https://github.com/qzSOS) as a portfolio-oriented, public-safe version of a private research memory system used across multiple long-running AI-assisted projects.

The public repository intentionally uses anonymized examples and templates. It does not include private project names, unpublished results, server paths, collaborators, client information, or dataset-specific confidential details.

## Roadmap

- `rmk check`: stronger stale-state and router-truth-duplication checks;
- optional active indexes for very large append-only files;
- more sanitized examples for paper writing and benchmark packaging;
- a small GitHub Pages documentation site;
- starter prompts for common coding agents.

## License

MIT License. See [LICENSE](LICENSE).
