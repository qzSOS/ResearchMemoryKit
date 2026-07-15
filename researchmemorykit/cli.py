"""Command-line interface for ResearchMemoryKit."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from . import __version__
from .checker import CheckReport, check_project


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rmk",
        description="Validate ResearchMemoryKit project contracts.",
    )
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser(
        "check",
        help="Check one project memory contract.",
    )
    check_parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Project root. Defaults to the current directory.",
    )
    check_parser.add_argument(
        "--manifest",
        default=None,
        help="Manifest path relative to the project root. Defaults to rmk.json.",
    )
    check_parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as a failed check.",
    )
    check_parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    return parser


def _render_text(report: CheckReport, *, strict: bool) -> str:
    lines: list[str] = []
    for finding in report.findings:
        location = f" [{finding.path}]" if finding.path else ""
        lines.append(
            f"{finding.severity.upper()} {finding.code}{location}: {finding.message}"
        )

    if not report.findings:
        lines.append("PASS: ResearchMemoryKit contract is healthy.")

    status = "PASS" if report.passed(strict=strict) else "FAIL"
    lines.append(
        (f"{status}: {report.error_count} error(s), {report.warning_count} warning(s).")
    )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command != "check":
        parser.error(f"Unsupported command: {args.command}")

    report = check_project(args.root, manifest_path=args.manifest)
    if args.format == "json":
        print(
            json.dumps(
                report.to_dict(strict=args.strict),
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(_render_text(report, strict=args.strict))
    return 0 if report.passed(strict=args.strict) else 1
