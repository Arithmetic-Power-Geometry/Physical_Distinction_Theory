import numpy as np

from cycle082_joint_sector_local_channel_boundary import (
    joint_sector_energy,
    local_depolarizing_pair,
    random_density,
    reset_witness,
)


def test_smallest_reset_counterexample_is_qubit():
    assert reset_witness(1) == (0.0, 0.0)
    assert reset_witness(2) == (0.0, 1.0)


def test_reset_growth_formula_through_dimension_12():
    for n in range(1, 13):
        before, after = reset_witness(n)
        assert before == 0.0
        assert after == float((n - 1) ** 2)


def test_local_depolarizing_scaling_and_monotonicity():
    rng = np.random.default_rng(8202026)
    for n in range(1, 7):
        rho = random_density(n * n, rng)
        la, lb = 0.37, 0.71
        c0 = joint_sector_energy(rho, n, n)
        out = local_depolarizing_pair(rho, n, la, lb)
        c1 = joint_sector_energy(out, n, n)
        assert np.isclose(c1, (la * lb) ** 2 * c0, atol=1e-12, rtol=1e-12)
        assert c1 <= c0 + 1e-12
