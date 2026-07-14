# Experiment Registry

The registry stores metadata only. Large outputs and checkpoints stay outside git.

## Layout

- `config/<experiment_id>.yaml`: immutable run configuration and provenance.
- `metrics/<experiment_id>.json`: measured outputs and evaluation protocol.
- `tags/<experiment_id>.json`: lifecycle status, route, dataset, and labels.

## Required Config Fields

- experiment ID and status;
- hypothesis and promotion gate;
- dataset or input role;
- code commit and third-party commits;
- environment;
- exact command and parameters;
- output and checkpoint paths;
- parent baseline or experiment.

## Required Finalization

1. Set status to `VALIDATING`.
2. Write metrics with evaluation protocol.
3. Set `FINAL`, `FAILED`, or `DEPRECATED`.
4. Update `memory/EXPERIMENT_LOG.md` or `memory/FAILED_ATTEMPTS.md`.
5. Append `memory/SESSION_LOG.md`.
6. Replace `memory/CURRENT_STATE.md` if the result changes active state.
