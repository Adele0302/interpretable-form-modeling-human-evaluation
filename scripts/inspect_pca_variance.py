from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/geometry/pca_explained_variance.csv")
print(df[["PC", "explained_variance_percent", "cumulative_explained_variance_percent"]].to_string(index=False))
