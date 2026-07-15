from __future__ import annotations

import io
import unittest

from scripts.demo_gate import run_demo


class GateDemoTests(unittest.TestCase):
    def test_demo_fails_then_passes(self) -> None:
        output = io.StringIO()

        exit_code = run_demo(output)
        transcript = output.getvalue()

        self.assertEqual(exit_code, 0)
        self.assertIn("ERROR RMK020", transcript)
        self.assertIn("ERROR RMK030", transcript)
        self.assertIn("FAIL: 2 error(s), 0 warning(s).", transcript)
        self.assertIn("PASS: 0 error(s), 0 warning(s).", transcript)


if __name__ == "__main__":
    unittest.main()
