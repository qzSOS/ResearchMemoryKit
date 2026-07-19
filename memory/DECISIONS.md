# Decision Log

> Append-only. Record replacements or reversals as new decisions.

## D-001: Use an Explicit Manifest for `rmk check`

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | How should `rmk check` know what a project considers authoritative, append-only, routed, stale, and gated? |
| Decision | Add a small `rmk.json` contract and a dependency-free Python CLI. Do not infer the entire contract from free-form Markdown. |
| Rationale | Fixed templates and adaptive project layouts need the same checker. Explicit paths and gates are more reliable than broad text heuristics. |
| Alternatives | Hard-code each template; infer structure from filenames; build a database-backed runtime. |
| Revisit condition | Revisit if real adopters cannot express their project layout without excessive manifest duplication. |
| Source | `docs/rmk-check.md` |

## D-002: Keep P0 Focused on Contract Health

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | Which checks belong in the first release? |
| Decision | P0 checks manifest validity, path safety, required files, current-state freshness, unresolved placeholders, router reachability, and required gate headings. |
| Rationale | These checks are deterministic, useful in CI, and do not require a database, YAML dependency, or semantic model. |
| Alternatives | Add registry lifecycle, claim review, git append-only enforcement, semantic duplication detection, or retrieval indexes immediately. |
| Revisit condition | Add deeper checks only after P0 is stable and self-hosted. |
| Source | `docs/rmk-check.md` |

## D-003: Publish Self-Hosted Memory and Explicit Author Attribution

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | Which repository memory and identity information belongs in the public project? |
| Decision | Keep the root `memory/` as a sanitized self-hosting example and keep the maintainer's intentionally public identity in repository-level license, citation, and package metadata. Exclude personal identity and all private source-project details from templates, examples, case studies, and memory records. |
| Rationale | Self-hosting demonstrates that the contract is used in practice. Repository authorship supports ownership, citation, and portfolio verification, while source-project confidentiality requires a stricter content boundary. |
| Alternatives | Remove the root memory layer; anonymize all authorship metadata; publish private project-derived records after redaction. |
| Revisit condition | Revisit if the maintainer chooses a pseudonymous public identity or if a self-hosted record would expose non-public work. |
| Source | `docs/publishing-safely.md` |

## D-004: Separate Operational Privacy From Publication Safety

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | Should ResearchMemoryKit prohibit private paths and unpublished facts in every project memory layer? |
| Decision | No. Private projects should preserve operational facts needed for recovery and reproduction. Shared records should prefer repository-relative paths or named environment roots, with per-machine mappings kept locally when practical. Credentials are always excluded. Strict anonymization applies when material will be published. |
| Rationale | A blanket ban on private paths makes the system less useful in real research and confuses public-release policy with day-to-day project operation. |
| Alternatives | Ban all machine-specific details; allow every local detail in committed shared memory; maintain separate public and private products. |
| Revisit condition | Revisit if users need a first-class environment-mapping schema rather than documented conventions. |
| Source | `docs/adoption-guide.md`, `docs/publishing-safely.md` |

## D-005: Prefer Executable Fictional Examples Over Anonymous Claims

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | How should the public repository demonstrate benefits that originated in private projects? |
| Decision | Remove generic anonymized case studies that readers cannot verify. Use executable fictional examples and label the exact boundary of what the current checker proves. |
| Rationale | Concrete fail-and-pass behavior is more credible than broad claims stripped of the evidence needed to evaluate them. |
| Alternatives | Keep anonymous narratives; publish private evidence after redaction; omit examples entirely. |
| Revisit condition | Add a real case study only when its project and supporting evidence are public. |
| Source | `docs/gate-demo.md` |

## D-006: Keep Markdown as the Product Core

| Field | Value |
|---|---|
| Date | 2026-07-15 |
| Status | Active |
| Question | Should the public repository present ResearchMemoryKit primarily as the `rmk` checker? |
| Decision | No. Present the Markdown records, written gates, and operating rules as the core method. Keep templates, prompts, `rmk.json`, and `rmk check` as progressively optional adoption aids. |
| Rationale | The method remains useful without installation, while CLI-first messaging narrows the project to a validator and hides its value for context recovery, project steering, trustworthy research, and reproducible engineering. |
| Alternatives | Lead with the CLI; remove the checker; describe every component as equally required. |
| Revisit condition | Revisit if adoption data shows that a tool-first entry point is substantially clearer without obscuring the underlying method. |
| Source | `README.md`, `README.zh-CN.md`, `docs/adoption-guide.md` |

## D-007: Add Medical SLM as the First Inspectable Real-Project Case

| Field | Value |
|---|---|
| Date | 2026-07-16 |
| Status | Active; satisfies the revisit condition in D-005 |
| Question | Should ResearchMemoryKit link a real project now that its repository and supporting evidence are public? |
| Decision | Link `qzSOS/Medical-SLM` as a separate real-project case in both READMEs and the safe-publishing guide. Keep the bundled fictional examples unchanged. |
| Rationale | Medical SLM exposes a sanitized Current State, decisions, failures, pitfalls, registry, completion gates, code, and fixed-protocol evidence that readers can inspect directly. |
| Alternatives | Copy the case into this repository; replace fictional examples; make a broad unverifiable adoption claim; omit the first public adopter. |
| Revisit condition | Remove or revise the link if Medical SLM is no longer public, its evidence boundary becomes unclear, or the case is presented as scientific validation by `rmk check`. |
| Source | `https://github.com/qzSOS/Medical-SLM` |

## D-008: Add Shared Research Stage, Blocker, Artifact, and Date Semantics

| Field | Value |
|---|---|
| Date | 2026-07-19 |
| Status | Active |
| Question | How should a generic research-project memory layer describe research maturity, blocked work, artifact availability, and date authority without changing the runtime checker? |
| Decision | Add written `EXPLORATORY`, `CONFIRMATORY`, and `PAPER` stage semantics; stable blocker codes with recovery fields; separate artifact identity from availability and load verification; explicit date-authority fields; and a short Current State template for the research-project profile. Keep these semantics human-reviewed and outside the dependency-free checker. |
| Rationale | A shared vocabulary prevents access, missing-input, license, resource, date, budget, approval, provenance, and scientific failures from being collapsed into one status. It also lets exploratory work proceed with an honest evidence boundary while preserving stricter standards for later claims. |
| Alternatives | Add semantic checks to the runtime; require paper-level conditions before exploration; use `DATA_BLOCKED` as a universal reason; treat registered artifacts as available; change the manifest schema. |
| Revisit condition | Revisit after adopters have used the vocabulary in real public or sanitized projects and can identify ambiguity that written guidance cannot resolve. |
| Source | `docs/gated-research-workflow.md`, `docs/gated-research-workflow.zh-CN.md`, `templates/research-project/memory/WORKFLOW.md` |
