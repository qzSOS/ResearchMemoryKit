#!/usr/bin/env python3
"""Install the optional GitHub Actions workflow locally.

GitHub requires the `workflow` token scope to push files under
`.github/workflows/`. If a token lacks that scope, keep the workflow template
under `docs/github-actions/` and run this script after refreshing auth.
"""

from __future__ import annotations

import shutil
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    src = root / "docs" / "github-actions" / "validate.yml"
    dst = root / ".github" / "workflows" / "validate.yml"

    if not src.exists():
        raise SystemExit(f"Missing workflow template: {src}")

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Installed {dst.relative_to(root)}")
    print("Before pushing, make sure your GitHub token has the workflow scope:")
    print("  gh auth refresh -s workflow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
