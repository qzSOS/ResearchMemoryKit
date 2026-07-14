# Pitfall Catalog

## P-001: Validation Split Leakage Can Look Like Reliability

| Field | Value |
|---|---|
| Symptom | Reliability score appears predictive, but only on validation samples similar to training crops. |
| Root cause | Random patch split leaked source-image information. |
| Detection | Hash source image IDs before patch extraction and compare train/validation roles. |
| Fix | Use source-level split first, then generate patches. |
| Prevention | Make split hash audit part of the experiment completion gate. |
