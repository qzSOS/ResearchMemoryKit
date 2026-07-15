# Current State

> Overwriteable project snapshot. Replace this content when the active phase changes.

- **Date**: 2026-07-15
- **Phase**: Post-release CI maintenance.
- **Active goal**: Remove GitHub Actions Node.js 20 deprecation warnings found during the public-boundary audit.
- **Current best**: The dependency-free CLI, explicit contracts, 20 tests, self-hosted gates, and metadata-aware public validation pass on the sanitized public tree.
- **Active work**: Upgrade the official checkout and Python setup actions, synchronize the reusable CI template, and verify the remote workflow.
- **Key decision**: `D-003` keeps sanitized self-hosting memory and explicit repository-level author attribution while excluding private source-project details.
- **Known risk**: A successful workflow can still accumulate platform deprecation warnings that later become failures.
- **Next step**: Close the CI maintenance gate, then return to adoption observation.
- **Stop condition**: Do not add semantic search, a database, or automatic research-direction decisions.
