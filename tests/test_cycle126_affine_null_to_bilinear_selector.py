import numpy as np

from pdt_cycle126_affine_null_to_bilinear_selector import (
    affine_null_regression,
    biaffine_eval,
    bilinear_eval,
    exact_sign_survivor_count,
    so3_cross_covariance_audit,
)


def test_exact_sign_filter_n1_to_n12():
    expected = {1: 1, 2: 0, 3: 6, **{n: 0 for n in range(4, 13)}}
    assert {n: exact_sign_survivor_count(n) for n in range(1, 13)} == expected


def test_null_absorbing_biaffine_form_is_bilinear_regression():
    rows = affine_null_regression(seed=126, max_dim=12)
    assert len(rows) == 12
    assert all(r["left_null_residual"] == 0.0 for r in rows)
    assert all(r["right_null_residual"] == 0.0 for r in rows)
    assert all(r["bilinear_residual"] == 0.0 for r in rows)


def test_nonzero_affine_term_breaks_null_absorption():
    B = np.zeros((2, 2, 2))
    L = np.eye(2)
    M = np.zeros((2, 2))
    c = np.zeros(2)
    x = np.array([1.0, 0.0])
    z = np.zeros(2)
    assert np.linalg.norm(biaffine_eval(x, z, B, L, M, c)) == 1.0


def test_bilinear_zero_axes():
    rng = np.random.default_rng(126)
    for n in range(1, 13):
        B = rng.normal(size=(n, n, n))
        x = rng.normal(size=n)
        z = np.zeros(n)
        assert np.allclose(bilinear_eval(x, z, B), 0.0)
        assert np.allclose(bilinear_eval(z, x, B), 0.0)


def test_so3_cross_product_covariance():
    audit = so3_cross_covariance_audit(seed=126, trials=2000, tol=1e-10)
    assert audit["violations"] == 0
    assert audit["max_residual"] < 1e-10
