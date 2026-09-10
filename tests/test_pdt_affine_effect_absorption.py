import numpy as np

from pdt_affine_effect_absorption import (
    audit,
    effect_bounds,
    mixture_residual,
    nonlinear_mixture_residual,
    random_density,
    random_effect,
)


def test_affine_effect_law_dimensions_1_to_12():
    rows = audit(max_d=12, samples=20, seed=44)
    assert len(rows) == 12
    assert max(r["max_affine_residual"] for r in rows) < 1e-10


def test_effect_spectrum_bounds():
    rng = np.random.default_rng(7)
    for d in range(1, 13):
        for _ in range(10):
            assert effect_bounds(random_effect(d, rng))


def test_nonlinear_purity_correction_breaks_affinity():
    rng = np.random.default_rng(99)
    witnessed = False
    for d in range(2, 13):
        e = random_effect(d, rng)
        for _ in range(30):
            rho = random_density(d, rng)
            sigma = random_density(d, rng)
            residual = nonlinear_mixture_residual(e, rho, sigma, 0.37, 0.1)
            witnessed |= residual > 1e-8
    assert witnessed


def test_affinity_exact_up_to_roundoff_for_arbitrary_t():
    rng = np.random.default_rng(123)
    d = 12
    e = random_effect(d, rng)
    rho = random_density(d, rng)
    sigma = random_density(d, rng)
    for t in [0.0, 0.01, 0.2, 0.5, 0.9, 1.0]:
        assert mixture_residual(e, rho, sigma, t) < 1e-10
