from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / 'data/pairwise/comparison_summary_subject_level.csv')
keep = [c for c in ['dataset','comparison_type','n_subjects','mean_target_winrate_clear','interpretation'] if c in df.columns]
print(df[df['dataset'].eq('valid_main')][keep].to_string(index=False))
