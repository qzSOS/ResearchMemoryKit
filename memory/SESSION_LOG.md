# Session Log

> Append-only. Record significant work and gate closures.

## 2026-07-15: `rmk check` Research and Design Started

- Compared project-skill routing, spec-driven development, agent harness, and project-memory repositories.
- Identified the missing machine-readable contract as the main blocker to reliable checking.
- Started self-hosting ResearchMemoryKit with explicit design, implementation, adoption, and release gates.

## 2026-07-15: Gate 1 Closed

- Added the public `rmk check` design and explicit `rmk.json` contract.
- Added the repository's self-hosted router, Current State, decisions, workflow, and session log.
- Passed public validation, JSON parsing, Markdown link checks, sensitive-pattern scanning, and whitespace diff checks.

## 2026-07-15: Gate 2 Closed

- Added the dependency-free `researchmemorykit` package and `rmk` console command.
- Implemented stable P0 findings for manifest, path, file, routing, gate, date, staleness, and placeholder checks.
- Added 15 standard-library unit tests covering valid contracts, failures, warnings, strict mode, JSON output, and custom manifests.
- Verified editable installation, `rmk --version`, `rmk check . --strict`, bytecode compilation, and public-release validation.

## 2026-07-15: Gate 3 Closed

- Added `rmk.json` contracts to all bundled templates and sanitized examples.
- Added explicit completion gates to the minimal and delivery templates.
- Added bundled-project regression tests; the suite now contains 17 tests.
- Updated bilingual README, adoption prompts, comparison, portfolio, theory, CI, and citation metadata for `0.2.0`.
- Verified initialized templates copy the manifest and fail only on the intentionally uninitialized Current State date.

## 2026-07-15: Release Audit Hardening

- Corrected the supported Python range from 3.9 to 3.10+ to match the type syntax used by the package.
- Rejected empty required-file, router-target, and gate contracts.
- Prevented fenced Markdown examples from satisfying Current State date checks.
- Added regression tests, synchronized contribution guidance, formatted all Python sources, and verified the built wheel metadata and installed console entry point.

## 2026-07-15: Gate 4 Closed and `v0.2.0` Released

- Pushed the four gated implementation commits to `main`.
- Verified the complete GitHub Actions workflow on Python 3.11.
- Published tag and GitHub Release `v0.2.0`.
- Closed the P0 goal with 19 passing tests, zero strict self-check findings, no sensitive scan matches, and a clean wheel installation.

## 2026-07-15: Public Boundary Audit

- Re-audited the GitHub-visible tree, release metadata, project memory, author metadata, portfolio material, and publishable essays.
- Kept the root `memory/` as an explicit sanitized self-hosting example and documented its public boundary.
- Removed the internal portfolio planning document from the public documentation tree while keeping the reusable gated-research essays.
- Defined public maintainer attribution as distinct from private source-project information.
- Expanded public validation to scan citation, package, and license metadata.

## 2026-07-15: Public Boundary Gate Closed

- Passed 20 standard-library tests, Ruff checks, bytecode compilation, strict self-checks, and validation of 94 public files.
- Built and installed the wheel in an isolated environment and verified the installed `rmk` entry point.
- Confirmed no private project names, local workspace paths, or unpublished project identifiers in the current public tree.
- Pushed commit `ca6cfeb` and verified GitHub Actions run `29403328767` completed successfully.
- Returned the active route to adoption observation rather than expanding P1 without a concrete failure mode.

## 2026-07-15: GitHub Actions Runtime Maintenance

- The final remote audit found Node.js 20 deprecation warnings on otherwise successful official actions.
- Upgraded `actions/checkout` from v4 to v6 and `actions/setup-python` from v5 to v6.
- Synchronized the public workflow template and CI documentation with the live workflow.

## 2026-07-15: CI Maintenance Gate Closed

- Pushed commit `cd031ec` and verified GitHub Actions run `29403696496` completed successfully.
- Confirmed the upgraded run used `actions/checkout@v6` and `actions/setup-python@v6`.
- Confirmed the check run produced zero annotations and no Node.js 20 deprecation warning.
- Returned the active route to adoption observation.

## 2026-07-15: Reader-Facing Audit and Gate Demo

- Separated private project operation, shared environment conventions, and public-release anonymization.
- Replaced the blanket private-path prohibition with repository-relative contract paths, optional exact operational paths, local machine mappings, and a permanent credentials ban.
- Removed three generic anonymous case studies and replaced them with an executable fictional contract demo.
- Added a 1200 x 675, seven-frame GIF generated from the real demo transcript.
- Distinguished written scientific gates from P0 checks for files, routes, state fields, and gate headings.
- Removed a repository-specific Actions installer and replaced the copied workflow with a minimal adopter workflow.
- Passed 21 tests, Ruff, compilation, strict self-check, validation of 94 public files, current-source wheel installation, and release-tag installation.

## 2026-07-15: Gate 5 Closed

- Pushed reader-facing audit commit `4321eed` and verified GitHub Actions run `29406693604`.
- Verified the GIF, revised README, minimal adopter workflow, and replacement documents on the remote `main` tree.
- Added the executable demo and P0 boundary to both gate essays in commit `46a048a`.
- Verified GitHub Actions run `29406912310` after the article update.
- Closed Gate 5 and routed the next phase to Zhihu publication before PyPI distribution.

## 2026-07-15: Markdown-First Positioning Pass

- Reframed the bilingual README around a small Git-native set of Markdown records, written gates, and operating rules.
- Moved the zero-install adoption path ahead of the optional checker demo.
- Changed `rmk.json` and `rmk check` from mandatory project identity to optional structural guardrails for projects that need CI or drift detection.
- Synchronized the adoption guide, agent prompts, checker reference, comparison, gated workflow, theory, and package description with the same boundary.
- Passed 21 tests, Ruff, bytecode compilation, strict self-check, public validation of 94 files, UTF-8 validation of 62 Markdown files, and whitespace checks.

## 2026-07-16: First Real Public Case Linked

- Published `qzSOS/Medical-SLM` as a separate, sanitized project repository
  with code, tests, registered experiments, negative results, fixed-protocol
  metrics, and its own ResearchMemoryKit layer.
- Added the case to both READMEs and `docs/publishing-safely.md` after the D-005
  revisit condition became true.
- Kept bundled examples fictional and executable; did not copy Medical SLM
  project records into this repository.
- Stated explicitly that `rmk check` validates structure and routing rather
  than medical correctness, evidence sufficiency, or scientific claim truth.
