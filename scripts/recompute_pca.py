from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / 'data/geometry/width_profiles_225x240.csv')
cols = [f'w{i}' for i in range(240)]
X = df[cols].to_numpy(float)
pca = PCA().fit(X)
for i, x in enumerate(pca.explained_variance_ratio_[:10], start=1):
    print(f'PC{i}: {x*100:.4f}%')
print('PC1+PC2:', pca.explained_variance_ratio_[:2].sum()*100)
