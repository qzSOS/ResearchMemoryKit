#!/usr/bin/env python3
"""Validate the public repository before release.

Checks:
- JSON files parse.
- Markdown relative links resolve.
- Obvious private paths, emails, and secret-like assignments are absent.

The scanner is intentionally conservative and dependency-free.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "venv",
}
SKIP_DIR_SUFFIXES = (".egg-info",)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

SENSITIVE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("windows-drive-path", re.compile(r"\b[A-Za-z]:\\")),
    ("unix-private-path", re.compile(r"(?<!`)\/(?:home|data|Users)\/[A-Za-z0-9_.-]+")),
    ("email-address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
    (
        "secret-assignment",
        re.compile(
            r"\b(?:api[_-]?key|token|password|secret|hf_token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{8,}",
            re.I,
        ),
    ),
]


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(
            part in SKIP_DIRS or part.endswith(SKIP_DIR_SUFFIXES)
            for part in path.parts
        ):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def validate_json(files: list[Path], root: Path) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".json":
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - report parse failure
            errors.append(f"JSON parse failed: {path.relative_to(root)}: {exc}")
    return errors


def validate_markdown_links(files: list[Path], root: Path) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for _label, target in MARKDOWN_LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(
                    f"Missing Markdown link: {path.relative_to(root)} -> {target}"
                )
    return errors


def scan_sensitive(files: list[Path], root: Path) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in {".md", ".txt", ".json", ".yaml", ".yml", ".py"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for name, pattern in SENSITIVE_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"Sensitive pattern {name}: {path.relative_to(root)}:{line}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ResearchMemoryKit public repo.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root. Defaults to current directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    files = iter_files(root)

    errors: list[str] = []
    errors.extend(validate_json(files, root))
    errors.extend(validate_markdown_links(files, root))
    errors.extend(scan_sensitive(files, root))

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed: {len(files)} files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
