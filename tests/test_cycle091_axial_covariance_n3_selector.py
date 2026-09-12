import numpy as np

from cycle091_axial_covariance_n3_selector import (
    AUDIT_DIMS,
    analytic_dimension_audit,
    random_axial_covariance_audit,
    reflection_witness,
)


def test_reflection_kills_polar_but_not_axial_covariance():
    w = reflection_witness()
    assert w["det_R"] == -1.0
    assert np.isclose(w["polar_residual"], 2.0)
    assert np.isclose(w["axial_residual"], 0.0)


def test_axial_selector_keeps_only_dimension_three_in_audit_range():
    rows = analytic_dimension_audit(AUDIT_DIMS)
    survivors = [r["n"] for r in rows if r["nonzero_axial_equivariant_alternating_map"]]
    assert survivors == [3]


def test_random_o3_axial_covariance_regression():
    result = random_axial_covariance_audit(trials=250, seed=91091)
    assert result["proper_trials"] > 0
    assert result["improper_trials"] > 0
    assert result["max_axial_covariance_residual"] < 1e-12
