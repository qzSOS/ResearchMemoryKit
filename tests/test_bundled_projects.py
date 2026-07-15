from __future__ import annotations

import unittest
from pathlib import Path

from researchmemorykit.checker import check_project


REPO_ROOT = Path(__file__).resolve().parents[1]


class BundledProjectTests(unittest.TestCase):
    def test_examples_are_healthy(self) -> None:
        for relative in (
            "examples/toy-research-project",
            "examples/fictional-paper-project",
        ):
            with self.subTest(project=relative):
                report = check_project(REPO_ROOT / relative)
                self.assertEqual([], report.findings)

    def test_templates_only_require_current_state_initialization(self) -> None:
        for relative in (
            "templates/minimal",
            "templates/research-project",
            "templates/delivery-project",
        ):
            with self.subTest(template=relative):
                report = check_project(REPO_ROOT / relative)
                self.assertEqual(
                    ["RMK040", "RMK050"],
                    [item.code for item in report.findings],
                )


if __name__ == "__main__":
    unittest.main()
