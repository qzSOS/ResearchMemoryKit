# `rmk check` Design

`rmk check` turns ResearchMemoryKit from a readable convention into a
machine-verifiable project contract.

## Goals

- validate a memory layer without a server or database;
- support fixed templates and agent-designed custom layouts;
- distinguish broken contracts from maintainability warnings;
- produce stable text and JSON output for humans and CI;
- remain dependency-free at runtime.

## Non-Goals

P0 does not:

- retrieve memories or build a knowledge graph;
- replace an experiment tracker;
- execute project tasks or choose research direction;
- infer a complete project contract from arbitrary prose;
- semantically judge whether a scientific claim is true;
- enforce append-only history across git revisions.

## Manifest

Each project that enables automated structural checks contains `rmk.json`.

```json
{
  "schema_version": 1,
  "profile": "research-project",
  "router": "AGENTS.md",
  "current_state": {
    "path": "memory/CURRENT_STATE.md",
    "stale_after_days": 7
  },
  "required_files": [
    "AGENTS.md",
    "memory/CURRENT_STATE.md",
    "memory/README.md",
    "memory/WORKFLOW.md"
  ],
  "append_only_files": [
    "memory/DECISIONS.md",
    "memory/FAILED_ATTEMPTS.md",
    "memory/PITFALLS.md",
    "memory/SESSION_LOG.md"
  ],
  "router_targets": [
    "memory/CURRENT_STATE.md",
    "memory/README.md",
    "memory/WORKFLOW.md"
  ],
  "gates": [
    {
      "file": "memory/WORKFLOW.md",
      "heading": "Experiment Completion Gate"
    }
  ]
}
```

All paths are repository-relative and must resolve inside the checked root.
Unknown top-level fields are allowed for forward-compatible project metadata.
`required_files`, `router_targets`, and `gates` must be non-empty.

## P0 Checks

| Code | Severity | Check |
|---|---|---|
| `RMK001` | error | `rmk.json` exists and parses as JSON |
| `RMK002` | error | manifest fields have supported types and values |
| `RMK003` | error | configured paths are relative and remain inside the project root |
| `RMK010` | error | required and append-only files exist |
| `RMK020` | error | the router references each configured router target |
| `RMK030` | error | each configured gate heading exists outside fenced examples |
| `RMK040` | error | Current State contains a valid `YYYY-MM-DD` Date field |
| `RMK041` | warning | Current State is older than `stale_after_days` |
| `RMK042` | warning | Current State has a future date |
| `RMK050` | warning | Current State still contains template placeholders |

P0 recognizes `YYYY-MM-DD`, `TODO`, `TBD`, and `FILL:` as unresolved
placeholder markers. Placeholder checks are intentionally limited to Current
State to reduce false positives in reusable logs and examples.

## CLI

```text
rmk check [ROOT] [--manifest PATH] [--strict] [--format text|json]
python -m researchmemorykit check [ROOT] ...
```

- default root: current directory;
- default manifest: `rmk.json` under the checked root;
- normal mode exits non-zero only when errors exist;
- `--strict` also fails on warnings;
- malformed command usage exits with code `2`;
- JSON output contains findings, counts, root, manifest path, and pass/fail.

## Future Checks

Later phases may add:

- registry lifecycle and cross-record experiment IDs;
- evidence-boundary and human-review status;
- orphaned memory files;
- git-aware append-only deletion detection;
- decision and Current State reference integrity;
- conservative router truth-duplication heuristics.

These checks should extend the explicit contract rather than turn the checker
into a general agent runtime.
