# Gate demo: catch a broken project contract

This demo creates a temporary fictional research project and introduces two
common contract failures:

1. the router no longer points to `memory/CURRENT_STATE.md`;
2. the declared experiment gate heading is missing from
   `memory/WORKFLOW.md`.

Run it from the repository root:

```bash
python scripts/demo_gate.py
```

The first check fails:

```text
Agent: "The project memory is ready."

Gate check 1
ERROR RMK020 [AGENTS.md]: Router does not reference configured target 'memory/CURRENT_STATE.md'.
ERROR RMK030 [memory/WORKFLOW.md]: Required gate heading not found: 'Experiment Completion Gate'.
FAIL: 2 error(s), 0 warning(s).
```

The script repairs the router and gate heading, then checks the same project
again:

```text
Repair
- restore the Current State route
- restore the Experiment Completion Gate heading

Gate check 2
PASS: ResearchMemoryKit contract is healthy.
PASS: 0 error(s), 0 warning(s).
```

## What this proves

`rmk check` can verify that declared project files, routes, Current State
fields, and gate headings are still present. These checks are deterministic
and suitable for CI.

## What this does not prove

P0 does not decide whether an experiment is scientifically sound, whether the
recorded evidence is sufficient, or whether a claim is true. The human and
agent workflow still has to apply the gate written in `WORKFLOW.md`.

Later checker versions may validate registry lifecycle and cross-record
consistency, but they should not be described as current behavior until they
exist.
