from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/modeling/model_performance_overall_aesthetic.csv")

for dataset in ["valid_32", "balanced_24"]:
    d = df[df["dataset"].eq(dataset)][["model", "mae_mean", "spearman_rho_mean"]]
    print(f"\n{dataset}")
    print(d.sort_values("mae_mean").to_string(index=False))
