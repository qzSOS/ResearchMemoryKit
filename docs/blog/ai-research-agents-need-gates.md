# AI Research Agents Need Gates, Not Just Memory

Most discussions about AI coding agents focus on memory: how to store context, retrieve past notes, and keep useful facts available across sessions.

Memory matters. But for long-running research, memory alone is not enough.

The harder problem is making progress auditable.

An agent can run code, generate plots, write reports, and produce artifacts. That does not mean the research project has advanced. A project advances when a decision is justified, an experiment passes or fails a gate, evidence is reviewed, pitfalls are recorded, and the current state changes.

ResearchMemoryKit is built around that idea.

## A reproducible gate failure

![ResearchMemoryKit catches a broken router and missing gate, then passes after repair](../assets/rmk-gate-demo.gif)

Run the fictional demo from the repository root:

```bash
python scripts/demo_gate.py
```

The agent first claims that project memory is ready. The check then finds that
`AGENTS.md` no longer routes to Current State and the declared experiment gate
is missing from `WORKFLOW.md`. Repairing those two contract errors makes the
same project pass.

P0 checks contract drift. It does not decide whether evidence is sufficient,
the method is sound, or a claim is true. The written gate defines completion;
`rmk check` confirms that the declared gate and recovery path still exist.

## Chat History Is Not Project Memory

Chat history is linear. Research projects are not.

A real project needs to know:

- what is true now;
- why a route was chosen;
- which experiments closed;
- which routes failed;
- which bugs should not repeat;
- which artifacts are evidence;
- which claims are not supported yet.

If all of that lives in chat history, every new session becomes archaeology.

## Current State Is the Entry Point

Every long project should have a short overwriteable current-state file.

It should say:

- current phase;
- active goal;
- current best evidence;
- blockers;
- next step;
- stop condition.

This file is not history. It is the cockpit.

History belongs in append-only records:

- decisions;
- experiment conclusions;
- failed attempts;
- pitfalls;
- session logs.

## The Gate Is the Important Part

A template is only useful if agents actually maintain it.

That means memory updates must be part of the definition of done.

An experiment is not complete when code finishes. It is complete when:

- the run is registered;
- config and outputs are known;
- metrics or validation evidence are recorded;
- the conclusion or failure is written down;
- new pitfalls are recorded;
- the current state is replaced if the active route changed.

The loop looks like this:

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

This turns agent activity into auditable progress.

## Failures Are First-Class Evidence

Failed experiments are not clutter. They define the search boundary.

A good failed-attempt record says:

- what route failed;
- what evidence closed it;
- what lesson is preserved;
- when it is allowed to revisit the route.

Without this, agents repeat old failures.

## Routers Should Stay Boring

Router files should tell agents where to read. They should not contain mutable project truth.

Current truth belongs in Current State.

If a router and a current-state file both say "latest result", one of them will drift.

## Fixed Templates Are Not Enough

Projects differ. A paper project, delivery project, benchmark project, and creative pipeline need different memory layers.

The better pattern is adaptive initialization:

ask the agent to inspect the project goal, expected artifacts, workflow, privacy constraints, and collaboration pattern, then design a memory layer around those needs.

ResearchMemoryKit includes both fixed templates and an adaptive prompt for this.

## What ResearchMemoryKit Is

ResearchMemoryKit is a gated memory layer for trustworthy AI-assisted research workflows.

It is not an agent runtime, database, or experiment tracker. It is a small git-native structure for:

- current-state recovery;
- decision provenance;
- experiment gates;
- failed-attempt records;
- pitfall catalogs;
- evidence boundaries;
- reproducible engineering.

Project:

https://github.com/qzSOS/ResearchMemoryKit
