"""Dependency-free validation for ResearchMemoryKit project contracts."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Iterable


SUPPORTED_SCHEMA_VERSION = 1
DEFAULT_MANIFEST = "rmk.json"
PLACEHOLDER_PATTERNS = (
    re.compile(r"YYYY-MM-DD"),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bFILL:", re.IGNORECASE),
)
DATE_FIELD_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?Date(?:\*\*)?\s*:\s*(\d{4}-\d{2}-\d{2})\s*$",
    re.MULTILINE,
)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")


@dataclass(frozen=True)
class Finding:
    """One stable checker finding."""

    code: str
    severity: str
    message: str
    path: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CheckReport:
    """Validation result for one project root."""

    root: Path
    manifest_path: Path
    findings: list[Finding]

    @property
    def error_count(self) -> int:
        return sum(item.severity == "error" for item in self.findings)

    @property
    def warning_count(self) -> int:
        return sum(item.severity == "warning" for item in self.findings)

    def passed(self, *, strict: bool = False) -> bool:
        if self.error_count:
            return False
        return not strict or self.warning_count == 0

    def to_dict(self, *, strict: bool = False) -> dict[str, Any]:
        return {
            "root": str(self.root),
            "manifest": str(self.manifest_path),
            "strict": strict,
            "passed": self.passed(strict=strict),
            "counts": {
                "errors": self.error_count,
                "warnings": self.warning_count,
            },
            "findings": [item.to_dict() for item in self.findings],
        }


@dataclass(frozen=True)
class CurrentStateConfig:
    path: str
    stale_after_days: int


@dataclass(frozen=True)
class GateConfig:
    file: str
    heading: str


@dataclass(frozen=True)
class Manifest:
    schema_version: int
    profile: str
    router: str
    current_state: CurrentStateConfig
    required_files: tuple[str, ...]
    append_only_files: tuple[str, ...]
    router_targets: tuple[str, ...]
    gates: tuple[GateConfig, ...]


def _finding(
    code: str,
    severity: str,
    message: str,
    path: str | None = None,
) -> Finding:
    return Finding(code=code, severity=severity, message=message, path=path)


def _string_list(
    data: dict[str, Any],
    key: str,
    findings: list[Finding],
    manifest_label: str,
) -> tuple[str, ...]:
    value = data.get(key)
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        findings.append(
            _finding(
                "RMK002",
                "error",
                f"Manifest field '{key}' must be a list of non-empty strings.",
                manifest_label,
            )
        )
        return ()
    return tuple(item.strip() for item in value)


def _parse_manifest(
    data: Any,
    findings: list[Finding],
    manifest_label: str,
) -> Manifest | None:
    if not isinstance(data, dict):
        findings.append(
            _finding(
                "RMK002",
                "error",
                "Manifest root must be a JSON object.",
                manifest_label,
            )
        )
        return None

    schema_version = data.get("schema_version")
    if (
        not isinstance(schema_version, int)
        or isinstance(schema_version, bool)
        or schema_version != SUPPORTED_SCHEMA_VERSION
    ):
        findings.append(
            _finding(
                "RMK002",
                "error",
                f"Unsupported schema_version: {schema_version!r}. Expected 1.",
                manifest_label,
            )
        )

    profile = data.get("profile")
    if not isinstance(profile, str) or not profile.strip():
        findings.append(
            _finding(
                "RMK002",
                "error",
                "Manifest field 'profile' must be a non-empty string.",
                manifest_label,
            )
        )
        profile = ""

    router = data.get("router")
    if not isinstance(router, str) or not router.strip():
        findings.append(
            _finding(
                "RMK002",
                "error",
                "Manifest field 'router' must be a non-empty string.",
                manifest_label,
            )
        )
        router = ""

    current_state_data = data.get("current_state")
    current_state: CurrentStateConfig | None = None
    if not isinstance(current_state_data, dict):
        findings.append(
            _finding(
                "RMK002",
                "error",
                "Manifest field 'current_state' must be an object.",
                manifest_label,
            )
        )
    else:
        state_path = current_state_data.get("path")
        stale_after_days = current_state_data.get("stale_after_days")
        if not isinstance(state_path, str) or not state_path.strip():
            findings.append(
                _finding(
                    "RMK002",
                    "error",
                    "current_state.path must be a non-empty string.",
                    manifest_label,
                )
            )
        elif (
            not isinstance(stale_after_days, int)
            or isinstance(stale_after_days, bool)
            or stale_after_days < 0
        ):
            findings.append(
                _finding(
                    "RMK002",
                    "error",
                    "current_state.stale_after_days must be a non-negative integer.",
                    manifest_label,
                )
            )
        else:
            current_state = CurrentStateConfig(
                path=state_path.strip(),
                stale_after_days=stale_after_days,
            )

    required_files = _string_list(data, "required_files", findings, manifest_label)
    append_only_files = _string_list(
        data, "append_only_files", findings, manifest_label
    )
    router_targets = _string_list(data, "router_targets", findings, manifest_label)
    for key, values in (
        ("required_files", required_files),
        ("router_targets", router_targets),
    ):
        if not values:
            findings.append(
                _finding(
                    "RMK002",
                    "error",
                    f"Manifest field '{key}' must not be empty.",
                    manifest_label,
                )
            )

    gates_data = data.get("gates")
    gates: list[GateConfig] = []
    if not isinstance(gates_data, list):
        findings.append(
            _finding(
                "RMK002",
                "error",
                "Manifest field 'gates' must be a list.",
                manifest_label,
            )
        )
    else:
        for index, item in enumerate(gates_data):
            if not isinstance(item, dict):
                findings.append(
                    _finding(
                        "RMK002",
                        "error",
                        f"gates[{index}] must be an object.",
                        manifest_label,
                    )
                )
                continue
            gate_file = item.get("file")
            heading = item.get("heading")
            if (
                not isinstance(gate_file, str)
                or not gate_file.strip()
                or not isinstance(heading, str)
                or not heading.strip()
            ):
                findings.append(
                    _finding(
                        "RMK002",
                        "error",
                        f"gates[{index}] requires non-empty 'file' and 'heading' strings.",
                        manifest_label,
                    )
                )
                continue
            gates.append(GateConfig(file=gate_file.strip(), heading=heading.strip()))
        if not gates:
            findings.append(
                _finding(
                    "RMK002",
                    "error",
                    "Manifest field 'gates' must contain at least one gate.",
                    manifest_label,
                )
            )

    if any(item.code == "RMK002" for item in findings):
        return None
    assert current_state is not None
    return Manifest(
        schema_version=schema_version,
        profile=profile.strip(),
        router=router.strip(),
        current_state=current_state,
        required_files=required_files,
        append_only_files=append_only_files,
        router_targets=router_targets,
        gates=tuple(gates),
    )


def _safe_project_path(root: Path, value: str) -> Path | None:
    candidate = Path(value)
    if candidate.is_absolute() or not value.strip():
        return None
    resolved = (root / candidate).resolve()
    try:
        resolved.relative_to(root)
    except ValueError:
        return None
    return resolved


def _configured_paths(manifest: Manifest) -> Iterable[tuple[str, str]]:
    yield "router", manifest.router
    yield "current_state.path", manifest.current_state.path
    for index, value in enumerate(manifest.required_files):
        yield f"required_files[{index}]", value
    for index, value in enumerate(manifest.append_only_files):
        yield f"append_only_files[{index}]", value
    for index, value in enumerate(manifest.router_targets):
        yield f"router_targets[{index}]", value
    for index, gate in enumerate(manifest.gates):
        yield f"gates[{index}].file", gate.file


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _outside_markdown_fences(text: str) -> str:
    visible_lines: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""
            continue
        if not in_fence:
            visible_lines.append(line)
    return "\n".join(visible_lines)


def _markdown_headings(text: str) -> set[str]:
    headings: set[str] = set()
    for line in _outside_markdown_fences(text).splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.add(match.group(1).strip())
    return headings


def _relative_label(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def check_project(
    root: str | Path = ".",
    *,
    manifest_path: str | Path | None = None,
    today: date | None = None,
) -> CheckReport:
    """Check one project and return stable findings."""

    root_path = Path(root).resolve()
    if manifest_path is None:
        manifest_file = root_path / DEFAULT_MANIFEST
    else:
        candidate = Path(manifest_path)
        manifest_file = (
            candidate.resolve()
            if candidate.is_absolute()
            else (root_path / candidate).resolve()
        )

    findings: list[Finding] = []
    manifest_label = _relative_label(manifest_file, root_path)
    try:
        manifest_file.relative_to(root_path)
    except ValueError:
        findings.append(
            _finding(
                "RMK003",
                "error",
                "Manifest path must resolve inside the checked project root.",
                str(manifest_file),
            )
        )
        return CheckReport(root_path, manifest_file, findings)

    if not manifest_file.is_file():
        findings.append(
            _finding(
                "RMK001",
                "error",
                f"Manifest not found: {manifest_label}",
                manifest_label,
            )
        )
        return CheckReport(root_path, manifest_file, findings)

    try:
        manifest_data = json.loads(_read_text(manifest_file))
    except (OSError, json.JSONDecodeError) as exc:
        findings.append(
            _finding(
                "RMK001",
                "error",
                f"Manifest could not be parsed as JSON: {exc}",
                manifest_label,
            )
        )
        return CheckReport(root_path, manifest_file, findings)

    manifest = _parse_manifest(manifest_data, findings, manifest_label)
    if manifest is None:
        return CheckReport(root_path, manifest_file, findings)

    resolved_paths: dict[str, Path] = {}
    invalid_values: set[str] = set()
    for field, value in _configured_paths(manifest):
        resolved = _safe_project_path(root_path, value)
        if resolved is None:
            invalid_values.add(value)
            findings.append(
                _finding(
                    "RMK003",
                    "error",
                    f"Configured path in {field} must stay inside the project root.",
                    value,
                )
            )
        else:
            resolved_paths[value] = resolved

    required_values = {
        manifest.router,
        manifest.current_state.path,
        *manifest.required_files,
        *manifest.append_only_files,
        *manifest.router_targets,
        *(gate.file for gate in manifest.gates),
    }
    for value in sorted(required_values):
        if value in invalid_values:
            continue
        path = resolved_paths[value]
        if not path.is_file():
            findings.append(
                _finding(
                    "RMK010",
                    "error",
                    "Required contract file does not exist.",
                    value,
                )
            )

    router_path = resolved_paths.get(manifest.router)
    if router_path is not None and router_path.is_file():
        router_text = _read_text(router_path)
        for target in manifest.router_targets:
            if target in invalid_values:
                continue
            target_variants = {target, target.replace("/", "\\")}
            if not any(variant in router_text for variant in target_variants):
                findings.append(
                    _finding(
                        "RMK020",
                        "error",
                        f"Router does not reference configured target '{target}'.",
                        manifest.router,
                    )
                )

    for gate in manifest.gates:
        if gate.file in invalid_values:
            continue
        gate_path = resolved_paths[gate.file]
        if not gate_path.is_file():
            continue
        headings = _markdown_headings(_read_text(gate_path))
        if gate.heading not in headings:
            findings.append(
                _finding(
                    "RMK030",
                    "error",
                    f"Required gate heading not found: '{gate.heading}'.",
                    gate.file,
                )
            )

    state_path = resolved_paths.get(manifest.current_state.path)
    if state_path is not None and state_path.is_file():
        state_text = _read_text(state_path)
        visible_state_text = _outside_markdown_fences(state_text)
        date_match = DATE_FIELD_RE.search(visible_state_text)
        state_date: date | None = None
        if date_match is None:
            findings.append(
                _finding(
                    "RMK040",
                    "error",
                    "Current State must contain a Date field in YYYY-MM-DD format.",
                    manifest.current_state.path,
                )
            )
        else:
            try:
                state_date = date.fromisoformat(date_match.group(1))
            except ValueError:
                findings.append(
                    _finding(
                        "RMK040",
                        "error",
                        "Current State Date is not a valid calendar date.",
                        manifest.current_state.path,
                    )
                )

        if state_date is not None:
            check_date = today or date.today()
            age_days = (check_date - state_date).days
            if age_days < 0:
                findings.append(
                    _finding(
                        "RMK042",
                        "warning",
                        f"Current State date is {-age_days} day(s) in the future.",
                        manifest.current_state.path,
                    )
                )
            elif age_days > manifest.current_state.stale_after_days:
                findings.append(
                    _finding(
                        "RMK041",
                        "warning",
                        (
                            f"Current State is {age_days} day(s) old; "
                            f"threshold is {manifest.current_state.stale_after_days}."
                        ),
                        manifest.current_state.path,
                    )
                )

        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(visible_state_text):
                findings.append(
                    _finding(
                        "RMK050",
                        "warning",
                        f"Current State contains unresolved placeholder '{pattern.pattern}'.",
                        manifest.current_state.path,
                    )
                )

    return CheckReport(root_path, manifest_file, findings)
