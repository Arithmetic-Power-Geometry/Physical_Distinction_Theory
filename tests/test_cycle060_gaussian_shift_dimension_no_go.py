import numpy as np

from cycle060_gaussian_shift_dimension_no_go import (
    audit,
    audit_dimension,
    log_likelihood_ratio,
    ordered_pair_stabilizer_witness,
    tv_equal_covariance_gaussians,
)


def test_tv_formula_basic_cases():
    assert tv_equal_covariance_gaussians(0.0) == 0.0
    assert 0.0 < tv_equal_covariance_gaussians(1.0) < 1.0
    assert tv_equal_covariance_gaussians(4.0) > tv_equal_covariance_gaussians(2.0)


def test_product_log_likelihood_adds_exactly():
    x1 = np.array([0.5, -1.0, 0.25])
    y1 = np.array([-0.2, 0.1, 0.4])
    z1 = np.array([0.3, -0.7, 0.9])
    x2 = np.array([0.1, 0.8])
    y2 = np.array([-0.4, 0.2])
    z2 = np.array([1.2, -0.5])
    lhs = log_likelihood_ratio(
        np.concatenate([z1, z2]),
        np.concatenate([x1, x2]),
        np.concatenate([y1, y2]),
    )
    rhs = log_likelihood_ratio(z1, x1, y1) + log_likelihood_ratio(z2, x2, y2)
    assert abs(lhs - rhs) < 1e-14


def test_nontrivial_ordered_pair_stabilizer_from_dimension_four():
    for n in range(4, 13):
        h = ordered_pair_stabilizer_witness(n)
        e1 = np.eye(n)[:, 0]
        e2 = np.eye(n)[:, 1]
        assert np.linalg.norm(h @ e1 - e1) < 1e-14
        assert np.linalg.norm(h @ e2 - e2) < 1e-14
        assert abs(np.linalg.det(h) - 1.0) < 1e-14
        assert np.linalg.norm(h - np.eye(n)) > 1e-3


def test_dimension_four_is_decisive_countermodel():
    row = audit_dimension(4, trials=40, seed=604)
    assert row["SO_n_noncommuting"]
    assert row["TPI"]
    assert not row["PCC"]
    assert row["rotation_failures"] == 0
    assert row["projection_failures"] == 0
    assert row["product_log_likelihood_failures"] == 0


def test_full_audit_has_no_numerical_failures():
    result = audit()
    assert result["total_failures"] == 0
    assert all(not row["PCC"] for row in result["higher_dimensions"])
