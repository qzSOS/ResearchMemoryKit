#!/usr/bin/env python3
"""Initialize a ResearchMemoryKit template in another project.

This script intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


TEMPLATE_CHOICES = ("minimal", "research-project", "delivery-project")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_tree(src: Path, dst: Path, *, force: bool, dry_run: bool) -> list[str]:
    actions: list[str] = []
    for item in sorted(src.rglob("*")):
        rel = item.relative_to(src)
        target = dst / rel
        if item.is_dir():
            if not dry_run:
                target.mkdir(parents=True, exist_ok=True)
            continue

        if target.exists() and not force:
            raise FileExistsError(
                f"{target} already exists. Re-run with --force to overwrite."
            )

        actions.append(f"{rel} -> {target}")
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
    return actions


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy a ResearchMemoryKit template into a project."
    )
    parser.add_argument(
        "template",
        choices=TEMPLATE_CHOICES,
        help="Template to copy.",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned copies without writing files.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    src = root / "templates" / args.template
    dst = Path(args.target).resolve()

    if not src.exists():
        raise SystemExit(f"Template not found: {src}")

    if not args.dry_run:
        dst.mkdir(parents=True, exist_ok=True)

    actions = copy_tree(src, dst, force=args.force, dry_run=args.dry_run)
    verb = "Would copy" if args.dry_run else "Copied"
    print(f"{verb} {len(actions)} files from template '{args.template}' to {dst}")
    for action in actions:
        print(f"  {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
