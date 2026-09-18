# Public Release Audit

Verified for v1.0:

- **225** contour samples: 165 Ancient + 60 Modern.
- Every released contour has **300 normalized points**.
- Width-profile representation: **225 × 240**.
- PCA outputs reproduce approximately **85.12% PC1** and **93.24% PC1+PC2** explained variance.
- Human-rating release contains **aggregate item-level statistics only**.
- Modeling tables are from the **final leak-free repeated-CV workflow**; earlier non-leak-free development outputs are excluded.
- Six model families are represented: Mean, Ridge, RBF-SVR, 1D-CNN, LSTM-Attention, GRU-Attention.
- 2AFC public tables contain **aggregate statistics only** for **30 valid respondents**.
- The web prototype release contains source/configuration but **no collected SQLite database, behavioral log, or 18-person participant-level dataset**.
- Synthetic/test participant data are not presented as empirical human-subject findings.
- Original source images are not redistributed in this release.

Run `python scripts/verify_release.py` to re-check the core numerical invariants of the public package.
