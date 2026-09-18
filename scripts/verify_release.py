from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def ok(label, detail):
    print(f"[OK] {label}: {detail}")

def value(df, stage):
    row = df.loc[df["stage"].eq(stage), "n"]
    assert len(row) == 1, stage
    return int(row.iloc[0])

def main():
    counts = pd.read_csv(ROOT / "data/geometry/sample_counts.csv")
    pca = pd.read_csv(ROOT / "data/geometry/pca_explained_variance.csv")
    models = pd.read_csv(ROOT / "data/modeling/model_performance_overall_aesthetic.csv")
    ranking = pd.read_csv(ROOT / "data/modeling/robust_model_ranking_leakfree.csv")
    pairwise = pd.read_csv(ROOT / "data/pairwise/comparison_summary_subject_level.csv")
    interaction = pd.read_csv(ROOT / "data/interaction/condition_level_summary.csv")
    qc = pd.read_csv(ROOT / "data/ratings/rating_qc_summary.csv")

    by_group = dict(zip(counts["group"], counts["n_samples"]))
    assert by_group["Ancient"] == 165
    assert by_group["Modern"] == 60
    assert by_group["Total"] == 225
    total = counts[counts["group"].eq("Total")].iloc[0]
    assert int(total["contour_points_per_sample"]) == 300
    assert int(total["width_profile_levels"]) == 240
    ok("Study geometry metadata", "225 samples = 165 ancient + 60 modern; 300 points; 240 width levels")

    p = pca.set_index("PC")["explained_variance_ratio"]
    pc1 = float(p.loc["PC1"])
    pc2 = float(p.loc["PC2"])
    assert abs(pc1 - 0.8512) < 0.002
    assert abs((pc1 + pc2) - 0.9324) < 0.002
    ok("PCA summary", f"PC1={pc1:.4%}; PC1+PC2={(pc1 + pc2):.4%}")

    expected = {"Mean", "Ridge", "SVR_RBF", "CNN1D", "LSTM_Attention", "GRU_Attention"}
    for ds in ["valid_32", "balanced_24"]:
        present = set(models.loc[models["dataset"].eq(ds), "model"])
        assert expected == present, (ds, present)
    ok("Model families", ", ".join(sorted(expected)))

    oa = models[models["dataset"].eq("balanced_24")].set_index("model")
    rho = float(oa.loc["SVR_RBF", "spearman_rho_mean"])
    assert abs(rho - 0.6616) < 0.002
    ok("Balanced overall-aesthetic RBF-SVR", f"Spearman rho={rho:.4f}")

    rr = ranking[ranking["dataset"].eq("balanced_24")].sort_values("combined_rank_score_lower_better")
    assert rr.iloc[0]["model"] == "Ridge"
    ok("Combined robust ranking", "Ridge ranks first on balanced_24")

    main_pw = pairwise[pairwise["dataset"].eq("valid_main")]
    assert set(main_pw["n_subjects"].unique()) == {30}
    rates = dict(zip(main_pw["comparison_type"], main_pw["mean_target_winrate_clear"]))
    assert rates["GEN_RULE_vs_GEN_BASELINE"] > 0.90
    assert rates["GEN_RULE_vs_REAL_LOW"] > 0.80
    assert rates["GEN_RULE_vs_REAL_HIGH"] < 0.50
    ok("2AFC", "n=30; conservative preference pattern reproduced")

    assert set(interaction["condition"]) == {"A", "B", "C"}
    assert set(interaction["n_participants"]) == {18}
    for c in ["B", "C"]:
        rate = float(interaction.loc[interaction["condition"].eq(c), "recommendation_acceptance_rate"].iloc[0])
        assert abs(rate - 0.583) < 0.001
    ok("Interactive study", "within-subject n=18; B/C acceptance rate=58.3%")

    assert value(qc, "questionnaires_collected") == 34
    assert value(qc, "hard_invalid_excluded") == 2
    assert value(qc, "valid_main") == 32
    assert value(qc, "balanced_robustness_subset") == 24
    assert value(qc, "rating_stimuli") == 48
    ok("Rating QC", "34 collected -> 32 valid -> 24 balanced; 48 stimuli")

    print("\nCompact public-release verification passed.")

if __name__ == "__main__":
    main()
