from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import date, timedelta
from io import StringIO
from pathlib import Path

from researchmemorykit.checker import check_project
from researchmemorykit.cli import main


class ProjectFixture:
    def __init__(self, root: Path, *, state_date: date | None = None) -> None:
        self.root = root
        self.state_date = state_date or date.today()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def create_valid(self) -> None:
        manifest = {
            "schema_version": 1,
            "profile": "test",
            "router": "AGENTS.md",
            "current_state": {
                "path": "memory/CURRENT_STATE.md",
                "stale_after_days": 7,
            },
            "required_files": [
                "AGENTS.md",
                "memory/CURRENT_STATE.md",
                "memory/WORKFLOW.md",
            ],
            "append_only_files": ["memory/SESSION_LOG.md"],
            "router_targets": [
                "memory/CURRENT_STATE.md",
                "memory/WORKFLOW.md",
            ],
            "gates": [
                {
                    "file": "memory/WORKFLOW.md",
                    "heading": "Completion Gate",
                }
            ],
        }
        self.write("rmk.json", json.dumps(manifest, indent=2))
        self.write(
            "AGENTS.md",
            "Read `memory/CURRENT_STATE.md` and `memory/WORKFLOW.md`.\n",
        )
        self.write(
            "memory/CURRENT_STATE.md",
            f"# Current State\n\n- **Date**: {self.state_date.isoformat()}\n",
        )
        self.write(
            "memory/WORKFLOW.md",
            "# Workflow\n\n## Completion Gate\n\n- [x] state updated\n",
        )
        self.write("memory/SESSION_LOG.md", "# Session Log\n")


class CheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.fixture = ProjectFixture(self.root)
        self.fixture.create_valid()

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def codes(self) -> list[str]:
        return [item.code for item in check_project(self.root).findings]

    def test_valid_project_passes(self) -> None:
        report = check_project(self.root)
        self.assertTrue(report.passed())
        self.assertEqual([], report.findings)

    def test_missing_manifest_is_rmk001(self) -> None:
        (self.root / "rmk.json").unlink()
        self.assertEqual(["RMK001"], self.codes())

    def test_invalid_manifest_shape_is_rmk002(self) -> None:
        self.fixture.write("rmk.json", "[]")
        self.assertEqual(["RMK002"], self.codes())

    def test_boolean_schema_version_is_rmk002(self) -> None:
        manifest = json.loads((self.root / "rmk.json").read_text(encoding="utf-8"))
        manifest["schema_version"] = True
        self.fixture.write("rmk.json", json.dumps(manifest))
        self.assertEqual(["RMK002"], self.codes())

    def test_unsafe_contract_path_is_rmk003(self) -> None:
        manifest = json.loads((self.root / "rmk.json").read_text(encoding="utf-8"))
        manifest["required_files"].append("../outside.md")
        self.fixture.write("rmk.json", json.dumps(manifest))
        self.assertIn("RMK003", self.codes())

    def test_missing_contract_file_is_rmk010(self) -> None:
        (self.root / "memory" / "SESSION_LOG.md").unlink()
        self.assertEqual(["RMK010"], self.codes())

    def test_unrouted_target_is_rmk020(self) -> None:
        self.fixture.write("AGENTS.md", "Read `memory/CURRENT_STATE.md`.\n")
        self.assertEqual(["RMK020"], self.codes())

    def test_missing_router_target_is_rmk010(self) -> None:
        (self.root / "memory" / "WORKFLOW.md").unlink()
        report = check_project(self.root)
        self.assertIn("RMK010", [item.code for item in report.findings])

    def test_gate_heading_inside_fence_does_not_count(self) -> None:
        self.fixture.write(
            "memory/WORKFLOW.md",
            "# Workflow\n\n```markdown\n## Completion Gate\n```\n",
        )
        self.assertEqual(["RMK030"], self.codes())

    def test_invalid_current_state_date_is_rmk040(self) -> None:
        self.fixture.write(
            "memory/CURRENT_STATE.md",
            "# Current State\n\n- **Date**: 2026-02-31\n",
        )
        self.assertEqual(["RMK040"], self.codes())

    def test_stale_current_state_is_warning(self) -> None:
        old_date = date.today() - timedelta(days=8)
        self.fixture.write(
            "memory/CURRENT_STATE.md",
            f"# Current State\n\n- **Date**: {old_date.isoformat()}\n",
        )
        report = check_project(self.root)
        self.assertEqual(["RMK041"], [item.code for item in report.findings])
        self.assertTrue(report.passed())
        self.assertFalse(report.passed(strict=True))

    def test_future_current_state_is_warning(self) -> None:
        future_date = date.today() + timedelta(days=1)
        self.fixture.write(
            "memory/CURRENT_STATE.md",
            f"# Current State\n\n- **Date**: {future_date.isoformat()}\n",
        )
        self.assertEqual(["RMK042"], self.codes())

    def test_placeholder_is_warning(self) -> None:
        self.fixture.write(
            "memory/CURRENT_STATE.md",
            f"# Current State\n\n- **Date**: {date.today().isoformat()}\n- TODO\n",
        )
        self.assertEqual(["RMK050"], self.codes())

    def test_json_cli_output_and_strict_exit(self) -> None:
        self.fixture.write(
            "memory/CURRENT_STATE.md",
            f"# Current State\n\n- **Date**: {date.today().isoformat()}\n- TBD\n",
        )
        stdout = StringIO()
        with redirect_stdout(stdout):
            exit_code = main(
                ["check", str(self.root), "--strict", "--format", "json"]
            )
        payload = json.loads(stdout.getvalue())
        self.assertEqual(1, exit_code)
        self.assertFalse(payload["passed"])
        self.assertEqual(1, payload["counts"]["warnings"])

    def test_custom_manifest_name_is_reported(self) -> None:
        (self.root / "rmk.json").rename(self.root / "custom.json")
        manifest = json.loads(
            (self.root / "custom.json").read_text(encoding="utf-8")
        )
        manifest["required_files"] = "not-a-list"
        self.fixture.write("custom.json", json.dumps(manifest))
        report = check_project(self.root, manifest_path="custom.json")
        self.assertEqual("custom.json", report.findings[0].path)


if __name__ == "__main__":
    unittest.main()
