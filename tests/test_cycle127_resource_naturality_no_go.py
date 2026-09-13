import numpy as np

from cycle127_resource_naturality_no_go import (
    audit,
    degree2_covariance_residual,
    exact_residual_identity,
    hadamard_composition,
    naive_naturality_residual,
)


def test_exact_scaling_identity():
    x = np.array([1.0, -2.0, 3.0])
    y = np.array([4.0, 5.0, -6.0])
    lam = 0.5
    np.testing.assert_allclose(
        naive_naturality_residual(x, y, lam),
        exact_residual_identity(x, y, lam),
        atol=1e-14,
        rtol=1e-14,
    )


def test_nontrivial_attenuation_breaks_naive_naturality():
    x = np.array([1.0])
    y = np.array([1.0])
    for lam in (0.25, 0.5, 0.75):
        assert abs(float(naive_naturality_residual(x, y, lam)[0])) > 0.0


def test_degenerate_scalings_are_not_selective():
    x = np.array([2.0, -1.0])
    y = np.array([3.0, 4.0])
    for lam in (0.0, 1.0):
        np.testing.assert_allclose(naive_naturality_residual(x, y, lam), 0.0)


def test_degree2_resource_scaling_is_exact():
    x = np.array([1.5, -2.0, 0.25])
    y = np.array([-4.0, 1.0, 8.0])
    for lam in (0.25, 0.5, 0.75):
        np.testing.assert_allclose(degree2_covariance_residual(x, y, lam), 0.0, atol=1e-14)


def test_audit_dimension_stress_has_no_regression_failures():
    out = audit(dimensions=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 32], trials_per_pair=4)
    assert out["exact_scaling_identity_failures"] == 0
    assert out["degree2_covariance_failures"] == 0
    assert out["naive_naturality_nonzero_residual_trials"] == out["random_trials"]


def test_witness_is_nonzero_bilinear_same_sector():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 5.0, 6.0])
    b = hadamard_composition(x, y)
    np.testing.assert_allclose(b, np.array([4.0, 10.0, 18.0]))
    assert np.linalg.norm(b) > 0.0
