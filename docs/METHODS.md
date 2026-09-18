# Methods Overview

## Geometry
Each of 225 ceramic body outlines was normalized and resampled to 300 contour points. A 240-level vertical width function was then computed to represent continuous variation along vessel height.

## Morphospace
PCA was applied to the 225 x 240 width-profile matrix. The first component explained 85.12% of variance and the first two components explained 93.24%.

## Human rating and predictive modeling
Forty-eight empirical stimuli were rated on multiple dimensions. Quality control produced a main valid dataset and a balanced robustness subset. Predictive comparisons used repeated outer cross-validation. For neural models, epoch selection used an inner validation split within each outer-training fold; outer-test folds were not used for early stopping.

Six model families were compared: mean baseline, Ridge, RBF-SVR, 1D-CNN, LSTM-Attention, and GRU-Attention. Neural models are interpreted as exploratory because the independent item-level sample size is 48.

## Independent preference validation
A separate 48-question 2AFC study compared rule-constrained candidates with a no-rule generated baseline, low-rated real outlines, and high-rated real outlines. Thirty responses were valid for the main analysis.

## Interactive evaluation
A three-condition web system was developed to examine how rule guidance changes design behavior. The public repository includes the interface source but omits participant-level logs and the 18-person behavioral dataset.
