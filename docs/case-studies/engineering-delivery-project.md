# Case Study: Engineering Delivery Project

This anonymized case study describes an engineering delivery project with simulation outputs, client-facing reports, and evidence-boundary constraints.

No private client, device, report, model, metric, path, or deliverable is included.

## Starting Problem

The project needed to manage:

- parameterized simulation scripts;
- repeated runs and diagnostics;
- generated figures and reports;
- accepted versus rejected visuals;
- claim wording for external delivery;
- evidence boundaries.

The most important question was not "what was the latest output?" but "which output is accepted evidence, and what does it actually support?"

## Memory Design

The project used:

- a router;
- an overwriteable project state;
- an append-only experiment/work log;
- an append-only decision log;
- a pitfall catalog embedded in the router;
- mandatory checks for generated visual evidence.

## What Worked

The memory layer preserved evidence boundaries. It separated:

- accepted deliverables;
- diagnostic outputs;
- rejected outputs;
- claims supported by current evidence;
- claims that would require stronger experiments.

This prevented overclaiming under delivery pressure.

## What Degraded

The router accumulated mutable truth. A stale "latest conclusion" remained in the router while the project state had moved on.

The worktree also accumulated generated artifacts faster than they could be curated.

## Transferable Lesson

For delivery projects, the router must stay low-volatility and the accepted deliverable index should be separate from generated outputs.

Recommended addition:

> A delivery task is not complete until every output is classified as accepted evidence, diagnostic artifact, archive, or external storage.
