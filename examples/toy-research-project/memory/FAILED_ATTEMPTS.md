# Failed Attempts

## F-001: Validation Crop Leakage

| Field | Value |
|---|---|
| Date | 2026-07-14 |
| Route | Random patch split |
| What failed | Training and validation crops overlapped spatially. |
| Evidence | Identical crop hashes appeared in both manifests. |
| Preserved lesson | Split source images before extracting patches. |
| Do not repeat unless | A leakage-safe split tool is used. |
