from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_public_repo import iter_files, scan_sensitive


class PublicValidationTests(unittest.TestCase):
    def test_scans_repository_metadata_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            windows_path = "E:" + chr(92) + "private" + chr(92) + "models"
            email = "author" + chr(64) + "example.com"
            secret_assignment = "to" + 'ken = "not-a-real-secret"\n'
            (root / "pyproject.toml").write_text(
                f'cache_path = "{windows_path}"\n', encoding="utf-8"
            )
            (root / "CITATION.cff").write_text(f'email: "{email}"\n', encoding="utf-8")
            (root / "LICENSE").write_text(secret_assignment, encoding="utf-8")

            findings = scan_sensitive(iter_files(root), root)

        self.assertTrue(
            any("pyproject.toml" in finding for finding in findings), findings
        )
        self.assertTrue(
            any("CITATION.cff" in finding for finding in findings), findings
        )
        self.assertTrue(any("LICENSE" in finding for finding in findings), findings)


if __name__ == "__main__":
    unittest.main()
