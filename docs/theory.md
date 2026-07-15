# Theory

This document summarizes the public design theory behind ResearchMemoryKit.

## Goals

1. **Recoverability**: a new session can recover enough context to continue.
2. **Provenance**: decisions, results, and failures have traceable origins.
3. **Decision credibility**: stored information is reliable enough to act on.
4. **Direction discipline**: project pivots, stops, and promotions happen through explicit gates rather than momentum.
5. **Reproducible engineering**: commands, metadata, outputs, and claims stay connected.
6. **Human bandwidth conservation**: the system reduces, rather than increases, maintenance burden.

## Axioms

### A1: Knowledge Value Is Retrospective

The value of a note is often unknown when it is created. A debug observation may later become the key result, and a small environment issue may later explain an entire failure branch.

Design implication: avoid forcing all knowledge into final categories at creation time.

### A2: Research Workflow Entropy Is Normal

Long projects create failed paths, old outputs, temporary scripts, and half-retired conventions. This is not a moral failure; it is exploration.

Design implication: optimize for graceful degradation, not perfect cleanliness.

### A3: Context Requires Stratification

Human attention and model context are finite. A single monolithic memory file eventually becomes unreadable.

Design implication: use a router-plus-leaf structure: short entry points, detailed records on demand.

### A4: Append-Only Preserves Credibility

Silent overwrites destroy trust. If a result was wrong, keep the old record and append the correction.

Design implication: decisions, failures, and conclusions should be append-only.

### A5: Scarce Resources Compress Ideal Workflow

GPU windows, deadlines, remote access, and client delivery pressure push people toward the shortest path.

Design implication: make the degraded path the default path. A rule that only works in calm conditions will be bypassed.

### A6: Human Direction Remains Central

Agents can execute structured work, compare files, run validations, and keep records. Choosing what matters still requires human judgment.

Design implication: memory should support human decisions, not pretend to replace them.

## Failure Modes

### FM-1: Knowledge Drift

Long-term files gradually diverge from the real project state.

Mitigation: Current State plus completion gates.

### FM-2: Silent Overwrite

Old information is replaced without a visible correction trail.

Mitigation: append-only records for decisions, failures, and conclusions.

### FM-3: Memory Sedimentation

Temporary notes stay in the staging area forever, making recovery harder.

Mitigation: short overwriteable snapshots and periodic migration into stable records.

### FM-4: Truth Duplication

The same mutable fact appears in several files. When it changes, only some copies are updated.

Mitigation: one authoritative source per mutable fact; routers link instead of restating.

### FM-5: Output Graveyard

Generated outputs accumulate and become too valuable to delete but too disorganized to use.

Mitigation: classify outputs as accepted evidence, diagnostics, archive, or external storage.

### FM-6: Orphaned Decisions

Decisions are recorded without rationale or revisit conditions.

Mitigation: every decision entry includes the question, rationale, alternatives, and revisit condition.

### FM-7: Draft-Record Confusion

Experiment logs serve two jobs: preserving conclusions and presenting results clearly. Treating the whole file as strictly append-only can produce duplicate-truth clutter.

Mitigation: conclusions are append-only; presentation can be reorganized if conclusions are preserved.

## Design Principles

### P1: Current-State Files Are Overwriteable; History Files Are Append-Only

Use overwriteable files for the present and append-only files for history.

### P2: Day-0 Templates Need Completion Gates

Putting the files in a repository is not enough. The agent adopts the pattern when memory updates are part of the definition of done.

### P3: Routers Should Not Contain Mutable Project Truth

Routers should contain recovery order, file maps, stable rules, and links. Current results belong in Current State.

### P4: Failed Attempts Are First-Class Evidence

Failed routes reduce future search space. They are not embarrassing leftovers.

### P5: Provenance Beats Completeness

A minimal result with commit, config, dataset/input role, and status is more valuable than a perfect record that never gets written.

### P6: Add Indexes When Append-Only Logs Become Slow

Append-only files can grow large. When retrieval becomes slow, add an active index or summary rather than deleting history.

### P7: Memory Should Gate Progress, Not Only Describe It

The memory layer should define what counts as a completed experiment, accepted claim, valid pivot, or deliverable. This lets agents move autonomously while still producing auditable progress.

### P8: Trust Comes From Closed Loops

An agent can run many commands without advancing research. Progress becomes trustworthy when each loop closes: decision, execution, validation, conclusion or failure, pitfall update, and Current State replacement.

### P9: Explicit Contracts Make Gates Verifiable

Human-readable rules define intent, but reliable automation needs a small
machine-readable contract for authoritative files, routing, freshness, and
gates.

Design implication: keep the contract explicit and inspectable, and keep the
checker narrower than a general workflow engine.

The written gate and the automated check have different jobs. The written
gate defines what evidence and records a project requires before work is
accepted. P0 verifies that the declared files, routes, state fields, and gate
headings still exist; it does not decide whether the evidence satisfies the
gate.

## What This Is Not

- not a replacement for ML experiment trackers;
- not a vector database;
- not a full agent operating system;
- not a project management tool;
- not a guarantee that agents will maintain memory without explicit gates.
