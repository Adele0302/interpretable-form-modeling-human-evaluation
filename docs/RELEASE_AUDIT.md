# Public Release Audit

## Source-package audit

Before preparing the compact public release, the underlying research package was checked for the following invariants:

- 225 empirical contour samples: **165 Ancient + 60 Modern**;
- each normalized contour represented by **300 points**;
- width-function representation: **225 × 240**;
- PCA results consistent with **85.12% PC1** and **93.24% PC1+PC2**;
- human-rating workflow: **34 collected → 32 valid → 24 balanced robustness subset**;
- final leakage-aware model comparison includes six families: Mean, Ridge, RBF-SVR, 1D-CNN, LSTM-Attention, GRU-Attention;
- RBF-SVR reaches approximately **ρ = 0.662** for balanced-set overall-aesthetic prediction;
- Ridge ranks first in the combined robust model ranking;
- independent 2AFC analysis contains **30 valid respondents**;
- interactive study reported as a separate **18-participant within-subject** experiment.

## Public-package policy

The GitHub release intentionally exposes compact metadata and aggregate outputs rather than the complete source package.

Excluded from the public repository are:

- original source images;
- full contour and width matrices;
- raw questionnaires;
- raw individual 2AFC rows;
- 18-person participant-level interaction data;
- session databases, logs, private mappings, and identifiers;
- synthetic/test participant records that could be mistaken for empirical results.

Run `python scripts/verify_release.py` to check the numerical consistency of the files that are actually public.
