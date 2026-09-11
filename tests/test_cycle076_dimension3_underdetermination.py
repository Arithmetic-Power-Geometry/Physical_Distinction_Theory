import numpy as np

from cycle076_dimension3_underdetermination import (
    distinction_energy,
    orthogonal_revelation_residual,
    product_composition_residual,
    pure_state_energy,
    random_density,
    stress_audit,
)


def test_pure_state_energy_all_dimensions_1_to_12():
    for d in range(1, 13):
        assert abs(pure_state_energy(d) - (d - 1)) < 1e-12


def test_product_composition_multiple_dimensions():
    rng = np.random.default_rng(12345)
    for d in range(1, 13):
        rho = random_density(d, rng)
        sigma = random_density(2, rng)
        assert product_composition_residual(rho, sigma) < 1e-10


def test_quadratic_revelation_multiple_dimensions():
    rng = np.random.default_rng(54321)
    for d in range(1, 13):
        x = rng.normal(size=max(1, d * d - 1))
        for cut in (0, x.size // 2, x.size):
            assert orthogonal_revelation_residual(x, cut) < 1e-10


def test_stress_audit_includes_required_dimensions_and_no_selection_of_three():
    out = stress_audit(seed=76076)
    assert out["dimensions"][:12] == list(range(1, 13))
    assert 16 in out["dimensions"] and 64 in out["dimensions"]
    assert out["max_product_composition_residual"] < 1e-9
    assert out["max_quadratic_revelation_residual"] < 1e-9
    # The same identities hold in dimensions distinct from three.
    assert pure_state_energy(2) == 1.0
    assert pure_state_energy(3) == 2.0
    assert pure_state_energy(4) == 3.0
