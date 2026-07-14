# Pitfall Catalog

## P-001: Patch Splits Can Leak

| Field | Value |
|---|---|
| Symptom | Validation score improves without visible generalization. |
| Root cause | Train and validation crops came from the same source image region. |
| Detection | Hash source image IDs and crop coordinates. |
| Fix | Split source images first, then extract patches. |
| Prevention | Make split generation part of the registry config. |
