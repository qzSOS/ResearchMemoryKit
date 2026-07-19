# Gated Research Workflow

ResearchMemoryKit is not only for context recovery. Its stronger use is to
make AI-assisted research auditable.

The central idea:

> Agents may execute autonomously, but progress is only trusted when a gate
> closes.

The English and Chinese versions of this document are maintained as a pair:
[中文版本](gated-research-workflow.zh-CN.md).

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

This turns "the agent did work" into "the project advanced through a recorded
gate."

## Written gates and automated checks

The gate in `WORKFLOW.md` defines what the project considers complete. Projects
that want automated structural checks can use `rmk check` to verify that the
declared gate and its supporting project structure still exist. P0 does not
inspect experimental evidence or decide whether the gate's scientific
conditions were satisfied.

Use the optional checker to catch contract drift. Use evidence review and human
judgment to close the written gate.

## Research Stages

Use one of these stages for the current research activity:

| Stage | Purpose | Evidence posture |
|---|---|---|
| `EXPLORATORY` | Find out whether a phenomenon, implementation route, or measurement is worth pursuing. | Incomplete or preliminary evidence is allowed when clearly labeled. |
| `CONFIRMATORY` | Test a pre-defined question under a frozen protocol and independent validation plan. | Results are interpreted against the registered promotion gate. |
| `PAPER` | Prepare claims and public materials that can withstand formal review. | Provenance, claim-to-evidence review, and human approval are required. |

### `EXPLORATORY`

Exploratory work may use a single sequence or limited sample, short runs,
smoke checks, preliminary metrics, incomplete data, and regenerated artifacts.
It is appropriate for checking whether an observation exists and may use a new
artifact identity.

Exploratory work must not automatically claim method validity, cross-sequence
generalization, statistical significance, clinical value, or formal
paper-level evidence. A newly generated artifact must not be presented as a
historical artifact.

### `CONFIRMATORY`

Confirmatory work requires frozen inputs, code, configuration, evaluation
protocol, and output paths. The promotion gate must be defined in advance, and
the project must identify an independent source or independent sequence.
Artifact identity and availability must both be recorded. Observations,
failures, and interpretations must remain separate.

Before treating a confirmatory result as paper evidence, check for obvious
coordinate, field-of-view, reference-support, and data-contamination
explanations. Passing an engineering test is not, by itself, a scientific
promotion.

### `PAPER`

Paper-stage work requires complete provenance; explicit data-source, access,
and license boundaries; complete experiment records; pre-defined controls and
statistical analysis; necessary multi-sequence or held-out validation;
claim-to-evidence review; and manual review of authorship, submission, and
public materials.

### Stage and claim discipline

The three stages are workflow states, not evidence grades. A stage promotion
must be recorded explicitly with its date authority, decision, evidence
references, and human owner. Tests passing cannot automatically promote
`EXPLORATORY` to `CONFIRMATORY` or `PAPER`, and an evidence grade cannot be
upgraded automatically.

Paper-level standards are not lowered by exploratory mode; they are deferred
until a formal claim is proposed. Strictness should increase with claim
strength rather than requiring every paper condition before exploration begins.

## Standard Blockers

`BLOCKED` is a state. The specific reason must be expressed with a stable
blocker code. Do not use `DATA_BLOCKED` as a catch-all for access, missing
inputs, dates, licenses, resources, or scientific failure.

Every blocker record includes:

```yaml
blocker_code: ACCESS_BLOCKED
summary: Source metadata cannot be read within the current authorization.
recoverable: true
owner: project maintainer
recovery_condition: Authorized access is granted and a read check succeeds.
safe_next_action: Validate the protocol and update the registry without reading the source.
scientific_impact: data
observed_at: 2026-01-15T09:30:00Z
evidence_reference: memory/SESSION_LOG.md#B-001
```

The fields mean: `blocker_code` is the stable enum; `summary` is the short
reason; `recoverable` says whether a defined recovery path exists; `owner`
names the role responsible for removal; `recovery_condition` is the
verifiable condition for resuming; `safe_next_action` is the action that can
be taken without extra approval; `scientific_impact` says whether the
blocker affects data, engineering, interpretation, or a paper claim;
`observed_at` records when it was observed; and `evidence_reference` points to
the supporting record.

`observed_at` is a complete ISO-8601 timestamp. `evidence_reference` may point
only to a repository-relative path, commit, Goal ID, or artifact ID. It must
not contain an absolute path, hostname, SSH alias, username, or credential.

| Code | Meaning and boundary |
|---|---|
| `ACCESS_BLOCKED` | Required source or service cannot be accessed within the current authorization. This is not a scientific failure. |
| `INPUT_MISSING` | A required input, manifest, or declared artifact is absent. This is not a method failure. |
| `LICENSE_BLOCKED` | The current license or publication boundary prevents the intended use or redistribution. It may block public redistribution without automatically prohibiting internal research. |
| `IDENTITY_DRIFT` | The observed input, code, config, or artifact identity differs from the registered identity or provenance. |
| `CONTRACT_INCOMPLETE` | A required protocol, gate, field, or acceptance rule is not defined well enough to proceed. |
| `RESOURCE_BUSY` | CPU, GPU, storage, or remote execution capacity is unavailable or occupied. |
| `DATE_NOT_DUE` | A date-dependent action is not eligible yet. Record the recovery date or condition; pause only that action. |
| `BUDGET_LIMITED` | Time, compute, storage, or financial budget is insufficient for the planned action. This is not an experiment failure. |
| `HUMAN_APPROVAL_REQUIRED` | A named human decision is required before the action or claim can proceed. |
| `SCIENTIFIC_GATE_FAILED` | The scientific question or promotion gate did not pass under the current protocol and threshold. |

These codes distinguish access and permission, inputs and artifacts, license
and publication boundaries, provenance or hash drift, incomplete protocols,
resource occupancy, date or budget limits, human approval, and scientific
failure. In particular, `ACCESS_BLOCKED` is not
`SCIENTIFIC_GATE_FAILED`; `INPUT_MISSING` is not "the method failed";
`DATE_NOT_DUE` blocks only date-related actions; and `BUDGET_LIMITED` does not
mean the experiment failed.

## Artifact Identity and Availability

Artifact identity, provenance, availability, hash verification, and load
verification are different fields. A hash does not prove that a file is
accessible. A checkpoint identity does not prove that checkpoint contents have
been loaded. Metadata-only inspection must not be recorded as load
verification. `REGISTERED` must never be interpreted downstream as
`AVAILABLE`.

Use this lifecycle:

| State | Meaning |
|---|---|
| `REGISTERED` | Artifact identity, source, or intended use is recorded; no file-existence claim is made. |
| `LOCATABLE` | A possible path, source, or retrieval location is known. |
| `ACCESSIBLE` | File metadata or content can be read within the authorized boundary. |
| `HASH_VERIFIED` | The bytes of the actual file match the registered hash. |
| `STAGED` | The file has been copied to an authorized local staging location. |
| `LOAD_VERIFIED` | The file passed the prescribed parser or loader check. |
| `EVALUATED` | The file was used under a specified evaluation protocol. |

Use these failure or blocking states when applicable:

`ACCESS_BLOCKED`, `MISSING`, `HASH_MISMATCH`, `LICENSE_BLOCKED`, and
`LOAD_FAILED`.

Their boundaries are:

| State | Meaning |
|---|---|
| `ACCESS_BLOCKED` | The artifact may be registered or locatable, but the current authorization does not permit reading it. |
| `MISSING` | The expected artifact cannot be found at the declared or locatable source. |
| `HASH_MISMATCH` | The accessible file bytes do not match the registered hash. |
| `LICENSE_BLOCKED` | The artifact cannot be used or redistributed for the intended action under the known license boundary. |
| `LOAD_FAILED` | The file is accessible but fails the prescribed parser or loader check. |

Exploratory regeneration must create a new artifact identity with
`stage: EXPLORATORY` and `provenance: newly_generated`. A new artifact must not
overwrite the hash or historical provenance of an older artifact, and artifact
availability must not be promoted into a scientific claim.

For example, a fully fictional record may say:

```text
artifact: fictional_sequence_a_estimate
REGISTERED -> ACCESS_BLOCKED
```

A later exploratory run may create:

```text
artifact: fictional_sequence_a_estimate_v2
stage: EXPLORATORY
provenance: newly_generated
```

The second record is useful for exploration, but it cannot be written back as
the first artifact's hash or historical provenance. Missing or inaccessible
artifacts cannot automatically be interpreted as method failure.

## Date Semantics

The `Date` in `memory/CURRENT_STATE.md` is the date of that project snapshot.
It is not automatically the authoritative date of a session, experiment, or
date gate. Keep system session date, project-file date, and machine clock
observations distinct.

Every date gate records:

```yaml
governing_date: 2026-01-15T00:00:00Z
date_authority: registered protocol
timezone: UTC
observed_at: 2026-01-15T09:30:00Z
eligible_after: 2026-01-16T00:00:00Z
date_conflict_policy: use the registered protocol authority and record conflicting observations
```

Host clocks, remote clocks, and NTP status are observation evidence, not
authority by themselves. When dates conflict, record the concrete dates and
times and never replace them with "today", "yesterday", or "tomorrow". Across
days or time zones, use complete ISO-8601 timestamps rather than date-only
values.

An old prompt or stale project note cannot override the current session's
authoritative date. If a date affects only one experiment, pause only that
experiment; unrelated documentation, CPU validation, and read-only audits may
continue. `DATE_NOT_DUE` must state the recovery date or a verifiable recovery
condition.

## Research Gate

A research experiment is complete only when:

1. the stage, hypothesis, and promotion gate were registered before or during
   execution;
2. the exact code, config, input role, artifact identity, availability, and
   output path are known;
3. metrics or validation evidence are recorded;
4. the result is classified as final, failed, deprecated, or still validating;
5. any blocker has a code, owner, recovery condition, safe next action, and
   evidence reference;
6. any reproducible bug is added to the pitfall catalog;
7. the Current State is replaced if the active route or evidence boundary
   changed.

## Direction Gate

A project pivot is accepted only when:

1. the current route's evidence boundary is summarized;
2. the reason for stopping or continuing is recorded;
3. alternatives are listed;
4. the revisit condition is explicit;
5. the next route appears in Current State;
6. any stage promotion or demotion is recorded explicitly.

This prevents drift by momentum. A project can stop weak directions without
pretending that every failed branch was wasted.

## Delivery Gate

A delivery artifact is accepted only when:

1. the artifact identity and availability state are listed in a delivery
   index;
2. the evidence boundary is explicit;
3. generated outputs are classified as accepted, diagnostic, archive, or
   external;
4. visual or report artifacts are actually reviewed;
5. unsupported claims are written down as unsupported;
6. final human release approval is recorded.

## Why This Helps Agents

Coding agents can execute many local steps. Without gates, they can also create
a false sense of progress.

ResearchMemoryKit gives agents a project-level contract:

- what to read first;
- which stage applies;
- what to update;
- how to name a blocker;
- which artifact state is actually known;
- when to stop or continue safely;
- what evidence is enough;
- what cannot be claimed yet.

The result is not full automation. It is supervised autonomy with a durable
audit trail and an explicit boundary for human scientific judgment.

## Minimal Gate Template

```markdown
## Completion Gate

This task is complete only if:

- [ ] the current research stage and promotion boundary are recorded;
- [ ] the authoritative current-state file reflects the result;
- [ ] a decision, conclusion, failure, or delivery record exists;
- [ ] commands, configs, artifact identities, availability states, and paths
      needed for reproduction are recorded;
- [ ] blockers include a code, recovery condition, safe next action, and
      evidence reference;
- [ ] any new pitfall is documented;
- [ ] unsupported claims are explicitly excluded;
- [ ] final human approval is recorded when the task prepares a public claim or
      release.
```
