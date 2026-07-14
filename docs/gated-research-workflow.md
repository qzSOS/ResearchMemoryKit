# Gated Research Workflow

ResearchMemoryKit is not only for context recovery. Its stronger use is to make AI-assisted research auditable.

The central idea:

> Agents may execute autonomously, but progress is only trusted when a gate closes.

## The Loop

```text
Current State
  -> Decision
  -> Registered work
  -> Execution
  -> Validation
  -> Conclusion or failure
  -> Pitfall update
  -> Session log
  -> Current State replacement
```

This turns "the agent did work" into "the project advanced through a recorded gate."

## Research Gate

A research experiment is complete only when:

1. the hypothesis and promotion gate were registered before or during execution;
2. the exact code, config, input role, and output path are known;
3. metrics or validation evidence are recorded;
4. the result is classified as final, failed, deprecated, or still validating;
5. any reproducible bug is added to the pitfall catalog;
6. the Current State is replaced if the active route changed.

## Direction Gate

A project pivot is accepted only when:

1. the current route's evidence is summarized;
2. the reason for stopping or continuing is recorded;
3. alternatives are listed;
4. the revisit condition is explicit;
5. the next route appears in Current State.

This prevents drift by momentum. A project can stop weak directions without pretending that every failed branch was wasted.

## Delivery Gate

A delivery artifact is accepted only when:

1. the artifact is listed in a delivery index;
2. the evidence boundary is explicit;
3. generated outputs are classified as accepted, diagnostic, archive, or external;
4. visual or report artifacts are actually reviewed;
5. unsupported claims are written down as unsupported.

## Why This Helps Agents

Coding agents can execute many local steps. Without gates, they can also create a false sense of progress.

ResearchMemoryKit gives agents a project-level contract:

- what to read first;
- what to update;
- when to stop;
- what evidence is enough;
- what cannot be claimed yet.

The result is not full automation. It is supervised autonomy with a durable audit trail.

## Minimal Gate Template

```markdown
## Completion Gate

This task is complete only if:

- [ ] the authoritative current-state file reflects the result;
- [ ] a decision, conclusion, failure, or delivery record exists;
- [ ] commands, configs, or artifact paths needed for reproduction are recorded;
- [ ] any new pitfall is documented;
- [ ] unsupported claims are explicitly excluded.
```
