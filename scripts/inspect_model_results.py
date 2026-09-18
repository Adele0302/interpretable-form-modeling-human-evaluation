from pathlib import Path
import pandas as pd
root = Path(__file__).resolve().parents[1]
for name in ['valid32','balanced24']:
    p = root / f'data/modeling/model_performance_{name}_leakfree.csv'
    df = pd.read_csv(p)
    a = df[df['dimension'].eq('overall_aesthetic')][['model','mae_mean','spearman_rho_mean']]
    print('\n', name)
    print(a.sort_values('mae_mean').to_string(index=False))
