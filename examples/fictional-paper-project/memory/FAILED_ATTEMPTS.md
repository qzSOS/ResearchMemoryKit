# Failed Attempts

## F-001: Random Patch Split Invalidated the First Reliability Signal

| Field | Value |
|---|---|
| Date | 2026-07-14 |
| Route | Random patch-level train/validation split |
| What failed | The split allowed patches from the same source image to appear in both train and validation sets. |
| Evidence | Synthetic manifest audit found duplicate source IDs across roles. |
| Preserved lesson | Split by source image before patch extraction. |
| Do not repeat unless | A source-level split manifest is generated and hash-checked. |
