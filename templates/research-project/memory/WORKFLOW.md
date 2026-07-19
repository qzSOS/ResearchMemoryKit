# Workflow

## Editing

- Make narrow, reversible changes.
- Run the smallest meaningful validation.
- Record commands and outcomes when they affect future work.

## Research Stage Semantics

Mark each active research task as one of:

- `EXPLORATORY`: investigate whether an observation, route, or measurement is
  worth pursuing. Single sequences, limited samples, smoke runs, preliminary
  metrics, incomplete data, and regenerated artifacts are allowed when clearly
  labeled. Do not claim method validity, cross-sequence generalization,
  statistical significance, clinical value, or paper-level evidence.
- `CONFIRMATORY`: test a pre-defined question with frozen inputs, code,
  configuration, evaluation protocol, and output paths. Register the promotion
  gate, an independent source or sequence, artifact identity and availability,
  observations, failures, and interpretations. Before paper use, check
  coordinate, FoV, reference-support, and contamination explanations.
- `PAPER`: prepare claims or public materials with complete provenance, data
  access and license boundaries, complete records, pre-defined controls and
  statistics, necessary multi-sequence or held-out validation, claim-to-evidence
  review, and manual author, submission, and release review.

These are workflow states, not evidence grades. Stage promotion must be
recorded explicitly. Passing a test cannot automatically promote
`EXPLORATORY` to `CONFIRMATORY` or `PAPER`, and exploratory mode does not lower
paper-level standards. Strictness increases with claim strength.

## Blocker Record

`BLOCKED` is a state, not a reason. Use one stable code and record all fields:

```yaml
blocker_code: ACCESS_BLOCKED
summary: Short reason.
recoverable: true
owner: Role responsible for removal.
recovery_condition: Verifiable condition for resuming.
safe_next_action: Action that needs no extra approval.
scientific_impact: data | engineering | interpretation | paper_claim
observed_at: 2026-01-15T09:30:00Z
evidence_reference: repository-relative/path.md#record
```

Allowed codes:

| Code | Boundary |
|---|---|
| `ACCESS_BLOCKED` | Access or permission failure; not scientific failure. |
| `INPUT_MISSING` | Missing input or declared artifact; not method failure. |
| `LICENSE_BLOCKED` | Use or redistribution is outside the current license boundary. Internal research is not automatically prohibited. |
| `IDENTITY_DRIFT` | Observed identity or provenance differs from the registered one. |
| `CONTRACT_INCOMPLETE` | Protocol, gate, field, or acceptance rule is incomplete. |
| `RESOURCE_BUSY` | CPU, GPU, storage, or remote capacity is occupied or unavailable. |
| `DATE_NOT_DUE` | A date-dependent action is not eligible; record its recovery date or condition. |
| `BUDGET_LIMITED` | Time, compute, storage, or financial budget is insufficient; not experiment failure. |
| `HUMAN_APPROVAL_REQUIRED` | A named human decision is required. |
| `SCIENTIFIC_GATE_FAILED` | The scientific question or promotion gate failed under the current protocol. |

Do not use `DATA_BLOCKED` as a catch-all. `evidence_reference` may contain only
a relative path, commit, Goal ID, or artifact ID. `observed_at` must be a full
ISO-8601 timestamp.

## Artifact Lifecycle

Keep artifact identity, provenance, availability, hash verification, and load
verification as separate fields:

| State | Meaning |
|---|---|
| `REGISTERED` | Identity or intended use is recorded; file existence is unknown. |
| `LOCATABLE` | A possible path, source, or retrieval location is known. |
| `ACCESSIBLE` | Metadata or content is readable within authorization. |
| `HASH_VERIFIED` | Actual bytes match the registered hash. |
| `STAGED` | File is in an authorized local staging location. |
| `LOAD_VERIFIED` | The prescribed parser or loader succeeded. |
| `EVALUATED` | Used under a specified evaluation protocol. |

Failure or blocking states are `ACCESS_BLOCKED`, `MISSING`, `HASH_MISMATCH`,
`LICENSE_BLOCKED`, and `LOAD_FAILED`. `REGISTERED` is not `AVAILABLE`; a hash or
checkpoint identity is not proof of access or loading; metadata-only checks are
not load verification. Exploratory regeneration creates a new artifact identity
with `stage: EXPLORATORY` and `provenance: newly_generated`, never a rewrite of
historical hash or provenance. Missing artifacts are not automatically method
failures.

The failure states mean:

- `ACCESS_BLOCKED`: registered or locatable, but not readable within current
  authorization;
- `MISSING`: not found at the declared or locatable source;
- `HASH_MISMATCH`: actual bytes do not match the registered hash;
- `LICENSE_BLOCKED`: intended use or redistribution is outside the known
  license boundary;
- `LOAD_FAILED`: accessible, but rejected by the prescribed parser or loader.

## Date Semantics

The `Date` in `CURRENT_STATE.md` is a project snapshot date, not automatically
the session's authoritative date. A date gate records:

```yaml
governing_date: 2026-01-15T00:00:00Z
date_authority: registered protocol
timezone: UTC
observed_at: 2026-01-15T09:30:00Z
eligible_after: 2026-01-16T00:00:00Z
date_conflict_policy: record concrete conflicts and follow the named authority
```

Separate session dates, project-file dates, and machine-clock observations.
Use complete ISO-8601 timestamps across days or time zones. Do not use
"today", "yesterday", or "tomorrow" in a date conflict. Host, remote, and NTP
clocks are evidence, not authority by themselves. An old prompt cannot
override the current authority. A date gate pauses only its affected action;
unrelated documentation, CPU validation, and read-only audits may continue.

## Experiment Completion Gate

An experiment is not complete until:

1. research stage, hypothesis, and promotion gate are recorded;
2. registry status, metrics, artifact identity, availability, and provenance are
   updated;
3. conclusion or failure is recorded;
4. blockers include a code, recovery condition, safe next action, and evidence
   reference;
5. new reproducible bugs are added to `PITFALLS.md`;
6. significant activity is appended to `SESSION_LOG.md`;
7. `CURRENT_STATE.md` is replaced when the active state or evidence boundary
   changes.

## Evidence Boundary

- Separate observed results from interpretation.
- Record negative results as first-class evidence.
- Do not upgrade a preliminary run into a strong claim without validation or
  explicit human stage promotion.
- Keep generated outputs out of git unless they are small, curated, and needed for review.
