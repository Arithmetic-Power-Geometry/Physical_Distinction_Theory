import numpy as np

from pdt_affine_mixture_lock import (
    audit_dimensions,
    born,
    mixture_deviation,
    random_density,
    random_effect,
    robust_bound_holds,
    spectral_affine_reconstruction,
)


def test_born_equals_affine_spectral_reconstruction_d1_to_d12():
    rng = np.random.default_rng(20260908)
    for d in range(1, 13):
        for _ in range(30):
            rho = random_density(d, rng)
            effect = random_effect(d, rng)
            assert abs(born(effect, rho) - spectral_affine_reconstruction(effect, rho)) < 1e-12


def test_uniform_pure_error_cannot_amplify_under_affine_mixing():
    rng = np.random.default_rng(7)
    eps = 0.01
    for d in range(1, 101):
        w = rng.random(d)
        w /= w.sum()
        deviations = rng.uniform(-eps, eps, size=d)
        assert robust_bound_holds(w, deviations, eps)
        assert abs(mixture_deviation(w, deviations)) <= eps + 1e-12


def test_dimension_audit_passes():
    rows = audit_dimensions(max_d=12, trials=20)
    assert len(rows) == 12
    assert max(row["max_born_affine_residual"] for row in rows) < 1e-12
    assert all(row["robust_bound_pass"] for row in rows)
