# Methods Overview

## 1. Geometry and continuous width representation

The study uses 225 empirical ceramic body outlines: 165 historical Yaozhou-kiln examples and 60 modern examples.

Each body outline was normalized and resampled to 300 contour points. A 240-level vertical width function was then computed to represent continuous changes along vessel height while supporting direct comparison across samples.

The public repository contains audited study-scale metadata and PCA summaries rather than the full contour and width matrices.

## 2. Empirical morphospace

PCA was applied to the 225 × 240 width-profile matrix.

The verified explained variance is:

- PC1: 85.12%
- PC1 + PC2: 93.24%
- PC1–PC5: 99.14%

## 3. Human rating and quality control

Forty-eight empirical stimuli were evaluated. Thirty-four questionnaires were collected.

Quality control produced:

- 32 valid questionnaires for the main analysis;
- a balanced 24-rater subset for robustness checks.

The public release contains only aggregate QC counts, not raw questionnaire rows.

## 4. Leakage-aware predictive model comparison

Six model families were evaluated:

1. mean baseline;
2. Ridge regression;
3. RBF-SVR;
4. 1D-CNN;
5. LSTM-Attention;
6. GRU-Attention.

The final comparison used repeated outer cross-validation. Standardization and hyperparameter selection were performed within the training side of each outer split. Neural-model epoch selection used an inner validation split from the outer-training fold; the outer-test fold was not used for early stopping.

For overall-aesthetic prediction, RBF-SVR reached the highest mean Spearman rank correlation in the balanced robustness set (approximately 0.662), while Ridge ranked first in the combined robust ranking across the evaluated rating dimensions.

The neural models are treated as exploratory because the independent item-level sample size is 48.

## 5. Interpretable rule construction

The study does not treat a single predictive model as sufficient evidence for design rules. Candidate relationships were screened through converging evidence, including rank correlations, high-versus-low rating contrasts, linear coefficient direction, resampling stability, and nonlinear-model support.

The final rules are therefore interpreted as transparent decision-support constraints rather than globally optimal design laws.

## 6. Independent 2AFC validation

A separate two-alternative forced-choice study tested rule-constrained generated candidates against:

- a no-rule generated baseline;
- low-rated real outlines;
- high-rated real outlines.

Thirty respondents were valid for the main analysis. The validation shows strong preference over the no-rule baseline and low-rated real forms, but not over high-rated real forms.

This boundary is central to the interpretation: computational guidance supports design exploration but does not replace high-quality human design examples.

## 7. Interactive decision-support study

A separate exploratory within-subject study involved 18 participants and three interface conditions:

- **A:** free design / no computational guidance;
- **B:** rule cues during exploration;
- **C:** refinement-stage cues with target information.

The system was designed to support rejectable guidance and logged interaction measures during the study. The public repository releases only condition-level aggregate outcomes.

Mean final rule distances were 0.670, 0.553, and 0.468 for A, B, and C, respectively. These differences were not statistically significant in the exploratory sample. Guidance increased mean task time, and B/C each had a 58.3% recommendation-acceptance rate.

Participant-level event logs, session identifiers, and individual decision trajectories are not public.
