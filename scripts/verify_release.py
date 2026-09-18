from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def ok(label, detail):
    print(f"[OK] {label}: {detail}")

def main():
    contours = pd.read_csv(ROOT / "data/geometry/contours_225_300pt_long.csv")
    width = pd.read_csv(ROOT / "data/geometry/width_profiles_225x240.csv")
    pca = pd.read_csv(ROOT / "data/geometry/pca_explained_variance.csv")
    valid = pd.read_csv(ROOT / "data/modeling/model_performance_valid32_leakfree.csv")
    balanced = pd.read_csv(ROOT / "data/modeling/model_performance_balanced24_leakfree.csv")
    ranking = pd.read_csv(ROOT / "data/modeling/robust_model_ranking_leakfree.csv")
    pairwise = pd.read_csv(ROOT / "data/pairwise/comparison_summary_subject_level.csv")

    counts = contours.groupby("sample_id").size()
    assert counts.size == 225, counts.size
    assert counts.min() == 300 and counts.max() == 300, (counts.min(), counts.max())
    ok("Contour data", "225 samples × 300 points")

    wcols = [c for c in width.columns if c.lower().startswith("w") and c[1:].isdigit()]
    assert width["sample_id"].nunique() == 225
    assert len(wcols) == 240, len(wcols)
    ok("Width profiles", "225 samples × 240 levels")

    ev_col = next(c for c in pca.columns if "explained" in c.lower() and "cumulative" not in c.lower())
    pc_col = next(c for c in pca.columns if c.lower() in {"pc", "component", "principal_component"})
    p = pca.set_index(pc_col)[ev_col]
    pc1 = float(p.loc["PC1"])
    pc2 = float(p.loc["PC2"])
    assert abs(pc1 - 0.8512) < 0.002
    assert abs((pc1 + pc2) - 0.9324) < 0.002
    ok("PCA", f"PC1={pc1:.4%}; PC1+PC2={(pc1+pc2):.4%}")

    expected_models = {"Mean", "Ridge", "SVR_RBF", "CNN1D", "LSTM_Attention", "GRU_Attention"}
    assert expected_models.issubset(set(valid["model"]))
    assert expected_models.issubset(set(balanced["model"]))
    ok("Model families", ", ".join(sorted(expected_models)))

    oa = balanced[balanced["dimension"].eq("overall_aesthetic")].set_index("model")
    svr_rho = float(oa.loc["SVR_RBF", "spearman_rho_mean"])
    assert abs(svr_rho - 0.6616) < 0.002
    ok("Balanced overall-aesthetic RBF-SVR", f"Spearman rho={svr_rho:.4f}")

    rr = ranking[ranking["dataset"].eq("balanced_24")].sort_values("combined_rank_score_lower_better")
    assert rr.iloc[0]["model"] == "Ridge"
    ok("Combined robust ranking", "Ridge ranks first on balanced_24")

    main_pw = pairwise[pairwise["dataset"].eq("valid_main")]
    assert set(main_pw["n_subjects"].unique()) == {30}
    rates = dict(zip(main_pw["comparison_type"], main_pw["mean_target_winrate_clear"]))
    assert rates["GEN_RULE_vs_GEN_BASELINE"] > 0.90
    assert rates["GEN_RULE_vs_REAL_LOW"] > 0.80
    assert rates["GEN_RULE_vs_REAL_HIGH"] < 0.50
    ok("2AFC", "n=30; expected preference pattern reproduced")

    print("\nPublic-release verification passed.")

if __name__ == "__main__":
    main()
