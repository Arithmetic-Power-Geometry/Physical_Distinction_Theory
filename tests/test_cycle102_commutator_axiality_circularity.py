import cycle102_commutator_axiality_circularity as c102


def test_dimension_match_only_n3():
    rows = c102.dimension_ledger()
    assert [r["n"] for r in rows if r["dimension_match_for_vector_identification"]] == [3]


def test_commutator_conjugation_covariance():
    out = c102.conjugation_covariance_audit(trials_per_n=10, seed=7)
    assert out["violations_gt_1e-9"] == 0


def test_hat_map_is_axial():
    out = c102.axial_hat3_audit(trials=100, seed=11)
    assert out["violations_gt_1e-9"] == 0


def test_reflection_distinguishes_polar_and_axial():
    w = c102.exact_reflection_witness()
    assert w["polar_residual_norm"] > 2.0
    assert w["axial_residual_norm"] == 0.0


def test_generate_classification_and_no_breakthrough():
    out = c102.generate()
    assert out["verdict"].startswith("FALSIFIED")
    assert out["breakthrough_candidate"] is False
