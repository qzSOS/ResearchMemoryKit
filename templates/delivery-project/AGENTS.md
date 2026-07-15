# Delivery Project Agent Router

New session? Read in this order:

1. `PROJECT_STATE.md` - current delivery status
2. `AGENTS.md` - this router and operating rules
3. `DELIVERY_INDEX.md` - accepted deliverables and evidence boundaries
4. `WORK_LOG.md` - recent activity
5. `DECISION_LOG.md` - decision provenance

If `PROJECT_STATE.md` is stale, reconstruct current status from `WORK_LOG.md`, `DELIVERY_INDEX.md`, and git history.

## Update Rules

- Major status change: replace `PROJECT_STATE.md`.
- Deliverable accepted or rejected: update `DELIVERY_INDEX.md`.
- Important decision or wording boundary: append `DECISION_LOG.md`.
- Significant work session: append `WORK_LOG.md`.
- Generated outputs must be classified as accepted deliverable, diagnostic artifact, or external output.

## Evidence Rules

- Do not claim more than the evidence supports.
- Keep rejected outputs visible as diagnostics, but do not present them as evidence.
- Review images, videos, reports, or tables before calling them accepted deliverables.
- Keep this router free of mutable results.

## Delivery Completion Gate

A delivery task is not complete until:

- `PROJECT_STATE.md` reflects the accepted state;
- `DELIVERY_INDEX.md` classifies the artifact and evidence boundary;
- decisions or wording boundaries are appended to `DECISION_LOG.md`;
- significant validation and rejection activity is appended to `WORK_LOG.md`.
