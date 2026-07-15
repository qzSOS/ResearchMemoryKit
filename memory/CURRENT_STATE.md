# Current State

> Overwriteable project snapshot. Replace this content when the active phase changes.

- **Date**: 2026-07-15
- **Phase**: `rmk check` P0 released.
- **Active goal**: Observe real adoption feedback before expanding contract depth.
- **Current best**: `v0.2.0` provides a dependency-free CLI, explicit manifests, 19 tests, self-hosting, template contracts, and passing Python 3.11 CI.
- **Active work**: Monitor issues and usage signals for registry lifecycle, append-only, and evidence-review checks.
- **Key decision**: `D-001` defines an explicit JSON manifest and zero-runtime-dependency CLI.
- **Known risk**: Adding deeper checks before real projects reveal which failures are frequent enough to justify them.
- **Next step**: Design P1 around registry lifecycle and cross-record consistency while preserving the small explicit contract.
- **Stop condition**: Do not add semantic search, a database, or automatic research-direction decisions.
