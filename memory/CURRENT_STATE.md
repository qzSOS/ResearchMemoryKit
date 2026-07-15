# Current State

> Overwriteable project snapshot. Replace this content when the active phase changes.

- **Date**: 2026-07-15
- **Phase**: `rmk check` P0 adoption.
- **Active goal**: Turn ResearchMemoryKit into a machine-verifiable, self-hosted gated memory protocol.
- **Current best**: The dependency-free `rmk check` CLI passes 15 unit tests and validates this repository with zero findings.
- **Active work**: Add manifests to bundled templates and examples, then expose the real command in docs and CI.
- **Key decision**: `D-001` defines an explicit JSON manifest and zero-runtime-dependency CLI.
- **Known risk**: Over-expanding into a general agent runtime, specification framework, or memory database.
- **Next step**: Make every generated project contract-aware and verify the repository self-hosts the checker in CI.
- **Stop condition**: Do not prepare a release until templates, examples, docs, and CI all use the implemented command.
