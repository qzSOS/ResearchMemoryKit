# Current State

> Fictional example. Overwrite this block after major state changes.

- **Date**: 2026-07-14
- **Phase**: Baseline comparison.
- **Active goal**: Validate whether patch-wise denoising improves the toy restoration baseline.
- **Current best**: `EXP-001` baseline is the only validated run.
- **Active experiment**: `EXP-002` is planned, not started.
- **Key decision**: `D-001` defines the toy scope and stop condition.
- **Known risk**: Patch overlap can inflate apparent quality if validation crops overlap training crops.
- **Next step**: Register `EXP-002` and run it on the held-out toy split.
- **Stop condition**: If `EXP-002` improves only on overlapping crops, close the route as leakage.
