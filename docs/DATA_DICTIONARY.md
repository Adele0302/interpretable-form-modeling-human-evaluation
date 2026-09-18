# Data Dictionary

This repository is a compact public release. It contains audited study metadata and aggregate result tables, not raw participant records or the complete contour/width matrices.

## data/geometry/sample_counts.csv

- `group`: Ancient, Modern, or Total.
- `n_samples`: number of empirical body-outline samples.
- `contour_points_per_sample`: contour-vector resolution used in the study (300).
- `width_profile_levels`: vertical width-function resolution used in the study (240).

## data/geometry/pca_explained_variance.csv

- `PC`: principal-component label.
- `explained_variance_ratio`: component-wise explained-variance ratio.
- `explained_variance_percent`: same value in percent.
- `cumulative_explained_variance_ratio`: cumulative ratio.
- `cumulative_explained_variance_percent`: cumulative percentage.

The full 225 × 240 width-profile matrix is not included in this lightweight release.

## data/ratings/rating_qc_summary.csv

Aggregate study counts only:

- questionnaires collected;
- hard-invalid questionnaires excluded;
- valid main dataset size;
- balanced robustness subset size;
- number of rating stimuli.

No rater-level rows are included.

## data/modeling/model_performance_overall_aesthetic.csv

Final leak-free repeated-CV summary for overall-aesthetic prediction.

Key fields:

- `dataset`: valid_32 or balanced_24;
- `model`: model family;
- `n_folds`: outer-fold evaluations;
- `mae_mean`, `mae_sd`;
- `rmse_mean`;
- `spearman_rho_mean`, `spearman_rho_sd`.

## data/modeling/robust_model_ranking_leakfree.csv

Combined robust ranking across evaluated rating dimensions.

Lower rank scores are better.

## data/pairwise/comparison_summary_subject_level.csv

Aggregate subject-level 2AFC statistics only.

Important fields include:

- `comparison_type`;
- `target_preference_group`;
- `n_subjects`;
- `mean_target_winrate_clear`;
- bootstrap confidence bounds;
- statistical-test p-values;
- conservative interpretation label.

Raw individual trial rows are not public.

## data/interaction/condition_level_summary.csv

Condition-level summary from the 18-participant within-subject interface study.

- `condition`: A, B, or C;
- `description`;
- `n_participants`;
- `mean_final_rule_distance`;
- `mean_task_time_seconds`;
- `mean_satisfaction`;
- `mean_control`;
- `recommendation_acceptance_rate`.

No participant-level interaction logs or trajectories are included.
