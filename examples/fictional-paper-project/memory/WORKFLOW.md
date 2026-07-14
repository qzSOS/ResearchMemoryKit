# Workflow

## Completion Gate

An experiment is complete only if:

- [ ] registry config exists;
- [ ] registry metrics exist when metrics are available;
- [ ] the experiment has a clear `FINAL`, `FAILED`, `VALIDATING`, or `DEPRECATED` state;
- [ ] the conclusion or failure is recorded;
- [ ] any new pitfall is recorded;
- [ ] Current State is replaced if the active project state changed;
- [ ] unsupported claims are explicitly excluded.

## Direction Gate

A pivot is accepted only if:

- [ ] the old route's evidence is summarized;
- [ ] the stop reason is recorded;
- [ ] the new route has a decision entry;
- [ ] Current State names the next registered work.
