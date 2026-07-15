#!/usr/bin/env python3
"""Demonstrate one failing and one passing ResearchMemoryKit contract."""

from __future__ import annotations

import sys
import tempfile
from datetime import date
from pathlib import Path
from typing import TextIO

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from researchmemorykit.checker import CheckReport, check_project  # noqa: E402
from scripts.init_memory import copy_tree, repo_root  # noqa: E402


CURRENT_STATE_TARGET = "memory/CURRENT_STATE.md"
GATE_HEADING = "Experiment Completion Gate"


def _render_report(report: CheckReport) -> list[str]:
    lines: list[str] = []
    for finding in report.findings:
        location = f" [{finding.path}]" if finding.path else ""
        lines.append(
            f"{finding.severity.upper()} {finding.code}{location}: {finding.message}"
        )
    if not report.findings:
        lines.append("PASS: ResearchMemoryKit contract is healthy.")
    status = "PASS" if report.passed(strict=True) else "FAIL"
    lines.append(
        f"{status}: {report.error_count} error(s), {report.warning_count} warning(s)."
    )
    return lines


def _write_current_state(project: Path) -> None:
    content = f"""# Current State

- **Date**: {date.today().isoformat()}
- **Phase**: Demo initialization.
- **Active goal**: Verify the project memory contract.
- **Current best**: The fictional project files have been created.
- **Active experiment**: None.
- **Key decision**: Use the research-project template.
- **Known risk**: The router or gate contract may drift.
- **Next step**: Run `rmk check`.
- **Stop condition**: Stop if the declared contract is broken.
"""
    (project / CURRENT_STATE_TARGET).write_text(content, encoding="utf-8")


def _break_contract(project: Path) -> tuple[str, str]:
    router_path = project / "AGENTS.md"
    workflow_path = project / "memory" / "WORKFLOW.md"
    router = router_path.read_text(encoding="utf-8")
    workflow = workflow_path.read_text(encoding="utf-8")
    router_path.write_text(
        router.replace(CURRENT_STATE_TARGET, "memory/STATE.md"),
        encoding="utf-8",
    )
    workflow_path.write_text(
        workflow.replace(f"## {GATE_HEADING}", "## Experiment Notes"),
        encoding="utf-8",
    )
    return router, workflow


def run_demo(stream: TextIO = sys.stdout) -> int:
    with tempfile.TemporaryDirectory(prefix="rmk-gate-demo-") as temp_dir:
        project = Path(temp_dir) / "fictional-project"
        template = repo_root() / "templates" / "research-project"
        copy_tree(template, project, force=False, dry_run=False)
        _write_current_state(project)
        router, workflow = _break_contract(project)

        print("$ python scripts/demo_gate.py", file=stream)
        print("", file=stream)
        print('Agent: "The project memory is ready."', file=stream)
        print("", file=stream)
        print("Gate check 1", file=stream)
        broken_report = check_project(project)
        for line in _render_report(broken_report):
            print(line, file=stream)

        print("", file=stream)
        print("Repair", file=stream)
        print("- restore the Current State route", file=stream)
        print("- restore the Experiment Completion Gate heading", file=stream)
        (project / "AGENTS.md").write_text(router, encoding="utf-8")
        (project / "memory" / "WORKFLOW.md").write_text(workflow, encoding="utf-8")

        print("", file=stream)
        print("Gate check 2", file=stream)
        repaired_report = check_project(project)
        for line in _render_report(repaired_report):
            print(line, file=stream)

    broken_codes = {finding.code for finding in broken_report.findings}
    expected_codes = {"RMK020", "RMK030"}
    return int(
        broken_codes != expected_codes or not repaired_report.passed(strict=True)
    )


if __name__ == "__main__":
    raise SystemExit(run_demo())
