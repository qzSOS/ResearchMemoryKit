# Case Study: Research Paper Project

This anonymized case study describes a long-running research-paper project with many experiments, negative results, and publication-boundary decisions.

No private project names, datasets, metrics, server paths, or unpublished claims are included.

## Starting Problem

The project had to coordinate:

- algorithm exploration;
- baseline reproduction;
- controlled experiments;
- failed branches;
- environment setup;
- paper evidence;
- reviewer-facing claims.

Early memory patterns were not enough because experiment results, decisions, pitfalls, and current status all grew at different speeds.

## Memory Design

The project used:

- `memory/CURRENT_STATE.md` as the session entry point;
- `memory/DECISIONS.md` for direction choices and stop conditions;
- `memory/EXPERIMENT_LOG.md` for completed experiment conclusions;
- `memory/FAILED_ATTEMPTS.md` for closed routes;
- `memory/PITFALLS.md` for reproducible bugs and diagnostics;
- `memory/SESSION_LOG.md` for session handoff;
- `registry/` for experiment metadata;
- `memory/WORKFLOW.md` for the Memory Completion Gate.

## What Worked

The strongest pattern was the completion gate:

> An experiment is not complete until registry status, conclusion/failure, pitfalls, session activity, and Current State are updated.

This made memory maintenance part of execution rather than after-the-fact documentation.

## What Had To Be Watched

Append-only files became large. The router still made recovery possible, but the project began to need active indexes and summaries for decisions, pitfalls, and session history.

## Transferable Lesson

Day-0 templates work best when paired with completion gates. Without gates, agents treat memory files as optional documentation. With gates, the memory layer becomes part of the project workflow.
