# Data Dictionary

## geometry/contours_225_300pt_long.csv
- `sample_id`: anonymized research sample identifier (e.g., Ancient_001).
- `group`: Ancient or Modern.
- `point_index`: 0-299.
- `x_norm`, `y_norm`: normalized contour coordinates.

## geometry/width_profiles_225x240.csv
- `sample_id`, `group`.
- `w0` ... `w239`: normalized width-function samples along vessel height.

## geometry/pca_scores_pc1_pc10.csv
- sample metadata and PC1-PC10 scores from width-profile PCA.

## ratings/item_ratings_48_aggregate_valid32.csv
Aggregate item-level statistics only; no rater-level rows are included.

## modeling/
Released tables contain final leak-free cross-validation summaries and robust ranking outputs.

## pairwise/
Only aggregate comparison/question-level statistics are released. Raw subject-response rows are excluded.
