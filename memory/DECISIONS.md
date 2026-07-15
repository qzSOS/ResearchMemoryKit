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
