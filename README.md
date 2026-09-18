# Interpretable Form Modeling and Human Evaluation

**A compact, auditable research release for shape analysis, leakage-aware prediction, interpretable guidance, and controlled human evaluation.**

This repository documents a quantitative research pipeline developed on ceramic body-form data. The application domain is design, but the methodological emphasis is broader: structured shape representation, small-sample machine learning, conservative model evaluation, interpretable computational guidance, and human evaluation of algorithmic recommendations.

> **Research logic:** shape representation → PCA morphospace → human rating → leak-free model comparison → interpretable rules → independent 2AFC validation → interactive decision support

## Research snapshot

| Component | Audited study scale |
|---|---:|
| Empirical body outlines | **225** = 165 ancient + 60 modern |
| Normalized contour representation | **300 points/sample** |
| Width-function representation | **240 levels/sample** |
| Human-rating stimuli | **48** |
| Rating quality control | **34 collected → 32 valid → 24 balanced robustness subset** |
| Predictive model families | **6** |
| Independent 2AFC validation | **30 valid participants, 48 questions** |
| Interactive within-subject study | **18 participants**; only condition-level aggregates are public |

## Key quantitative results

### 1. Shape representation

PCA on the 240-level width-function representation yielded:

- **PC1 = 85.12%** explained variance
- **PC1 + PC2 = 93.24%**
- **PC1–PC5 = 99.14%**

The public repository contains the verified explained-variance table and sample-count metadata. Full contour vectors and the full 225 × 240 width-profile matrix are intentionally not part of this lightweight public release.

### 2. Leakage-aware predictive modeling

The final comparison uses repeated outer cross-validation. Standardization, tuning, training, and neural-model early stopping are confined to the training side of each outer split.

Six model families were compared:

- Mean baseline
- Ridge regression
- RBF-SVR
- 1D-CNN
- LSTM-Attention
- GRU-Attention

For **overall aesthetic prediction**:

| Dataset | Model | MAE ↓ | Spearman ρ ↑ |
|---|---|---:|---:|
| valid_32 | Ridge | **0.327** | 0.605 |
| valid_32 | RBF-SVR | 0.353 | **0.631** |
| balanced_24 | Ridge | 0.356 | 0.609 |
| balanced_24 | RBF-SVR | **0.355** | **0.662** |

RBF-SVR achieved the highest mean rank correlation for overall-aesthetic prediction in the balanced robustness set (**ρ = 0.662**), while **Ridge ranked first in the combined robust model ranking** across the evaluated rating dimensions.

The neural models are retained as exploratory comparisons because the independent item-level sample size is 48.

### 3. Independent 2AFC validation

Thirty valid respondents completed a separate 48-question preference study.

| Comparison | Target clear-choice win rate |
|---|---:|
| Rule-constrained generation vs no-rule baseline | **92.8%** |
| Rule-constrained generation vs low-rated real outlines | **84.6%** |
| Rule-constrained generation vs high-rated real outlines | **41.3%** |
| High-rated real vs low-rated real outlines | **87.4%** |

The interpretation is deliberately conservative: rule-constrained candidates improved over weak baselines, but **did not exceed high-rated real examples**.

### 4. Interactive decision-support study

The within-subject interface study compared three conditions:

| Condition | Mean final rule distance | Mean task time | Recommendation acceptance |
|---|---:|---:|---:|
| A — free design / no guidance | 0.670 | 53.3 s | — |
| B — exploratory rule cues | 0.553 | 75.9 s | 58.3% |
| C — refinement cues + target information | 0.468 | 77.6 s | 58.3% |

The lower mean rule distance under guidance was **not statistically significant** in the 18-participant exploratory sample. Guidance increased task time, and the 58.3% acceptance rate shows that participants neither fully relied on nor uniformly ignored the recommendations.

Only condition-level aggregate results are released here. Participant-level logs and decision trajectories are withheld.

## What is public

```text
data/
  geometry/
    sample_counts.csv
    pca_explained_variance.csv
  ratings/
    rating_qc_summary.csv
  modeling/
    model_performance_overall_aesthetic.csv
    robust_model_ranking_leakfree.csv
  pairwise/
    comparison_summary_subject_level.csv
  interaction/
    condition_level_summary.csv

docs/
  DATA_DICTIONARY.md
  METHODS.md
  PRIVACY_AND_DATA_RELEASE.md
  RELEASE_AUDIT.md

scripts/
  verify_release.py
  inspect_model_results.py
  inspect_2afc_results.py
  inspect_pca_variance.py
```

This is intentionally a **compact public release**, not a dump of every intermediate research file.

## Verify the public release

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/verify_release.py
```

The verification script checks the public metadata and summary tables for:

- 225 samples = 165 ancient + 60 modern;
- 300-point contour and 240-level width-function study representations;
- PC1 ≈ 85.12% and PC1 + PC2 ≈ 93.24%;
- six final model families;
- balanced-set RBF-SVR overall-aesthetic ρ ≈ 0.662;
- Ridge ranked first in the combined robust ranking;
- 30 valid 2AFC respondents and the expected preference pattern;
- 18 participants in each within-subject interaction condition and 58.3% cue acceptance in B/C.

## Privacy and data minimization

The following are **not** public:

- participant-level behavioral logs from the 18-person interaction study;
- raw individual 2AFC response rows;
- raw questionnaire exports;
- real session identifiers or collected event histories;
- names, contact information, IP addresses, signatures, or consent records;
- private mapping keys;
- SQLite databases created during data collection;
- original source images whose redistribution rights are not established;
- synthetic/test participant data presented as if they were empirical observations.

See [docs/PRIVACY_AND_DATA_RELEASE.md](docs/PRIVACY_AND_DATA_RELEASE.md) for the release policy.

## Research scope

The project is best understood as a methodological chain rather than an attempt to claim that one predictive model can replace design judgement. The computational rules are treated as **inspectable and rejectable decision support**, and the human studies are used to test both their utility and their limits.

This framing is relevant to broader work on:

- interpretable machine learning;
- trustworthy human–AI decision support;
- small-sample model evaluation;
- human reliance on algorithmic recommendations;
- computational design and shape analysis.

## Author

**Shuofei Zan**

Research interests: computational design, machine learning, human–AI interaction, interpretable and trustworthy decision support.

## Citation and reuse

Citation metadata are provided in `CITATION.cff`.

No blanket open-source or open-data license is granted yet. The repository is shared for research inspection and application review while source-image, data-redistribution, and publication rights are being checked. Please contact the author before reuse beyond normal citation and inspection.
