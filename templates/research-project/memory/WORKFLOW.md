# Workflow

## Editing

- Make narrow, reversible changes.
- Run the smallest meaningful validation.
- Record commands and outcomes when they affect future work.

## Experiment Completion Gate

An experiment is not complete until:

1. registry status and metrics are updated;
2. conclusion or failure is recorded;
3. new reproducible bugs are added to `PITFALLS.md`;
4. significant activity is appended to `SESSION_LOG.md`;
5. `CURRENT_STATE.md` is replaced when the active state changes.

## Evidence Boundary

- Separate observed results from interpretation.
- Record negative results as first-class evidence.
- Do not upgrade a preliminary run into a strong claim without validation.
- Keep generated outputs out of git unless they are small, curated, and needed for review.
