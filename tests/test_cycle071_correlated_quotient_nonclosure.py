import numpy as np

from cycle071_correlated_quotient_nonclosure import DIMS, run_audit, witness


def test_dimension_one_is_recorded_as_degenerate():
    row = witness(1)
    assert row["classification"] == "DEGENERATE"


def test_identical_local_marginals_but_distinct_joint_statistics_2_through_12():
    for d in range(2, 13):
        row = witness(d)
        assert row["min_eigenvalue_rho_plus"] >= -1e-15
        assert row["min_eigenvalue_rho_minus"] >= -1e-15
        assert row["max_local_marginal_difference"] < 1e-15
        assert row["joint_product_observable_separation"] > 0.0
        assert row["separation_residual"] < 1e-14


def test_higher_dimension_stress_family():
    for d in [16, 24, 32, 48, 64, 96, 128]:
        row = witness(d)
        assert row["max_local_marginal_difference"] < 1e-15
        assert row["joint_product_observable_separation"] > 0.0
        assert row["separation_residual"] < 1e-14


def test_audit_classification_and_scope():
    result = run_audit()
    assert result["dimensions"] == DIMS
    assert result["nondegenerate_cases"] == len(DIMS) - 1
    assert result["breakthrough_candidate"] is False
    assert "FALSIFIED" in result["status"]
    assert result["max_local_marginal_difference"] < 1e-15
    assert result["max_separation_residual"] < 1e-14
