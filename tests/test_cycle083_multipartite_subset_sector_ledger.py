import itertools

import numpy as np

from cycle083_multipartite_subset_sector_ledger import (
    distinction_energy,
    random_density,
    run_audit,
    sector,
)


def test_three_party_sector_decomposition_and_orthogonality():
    rng = np.random.default_rng(83)
    dims = [2, 2, 2]
    d = 8
    rho = random_density(d, rng)
    sectors = {}
    for mask in range(8):
        s = {i for i in range(3) if mask & (1 << i)}
        sectors[tuple(sorted(s))] = sector(rho, dims, s)
    assert np.linalg.norm(sum(sectors.values()) - rho) < 1e-12
    total = sum(d * np.vdot(x, x).real for s, x in sectors.items() if s)
    assert abs(distinction_energy(rho) - total) < 1e-12
    for (_, a), (_, b) in itertools.combinations(sectors.items(), 2):
        assert abs(np.vdot(a, b)) < 1e-12


def test_degenerate_dimension_one_has_zero_nonempty_energy():
    rho = np.ones((1, 1), dtype=complex)
    assert distinction_energy(rho) == 0.0
    assert np.linalg.norm(sector(rho, [1], {0})) == 0.0


def test_frozen_audit_thresholds():
    out = run_audit()
    assert out["dense_bipartite_cases"] == 24
    assert out["dense_tripartite_cases"] == 4
    assert out["product_factorization_cases"] == 19
    assert out["max_decomposition_residual"] < 1e-11
    assert out["max_product_factorization_residual"] < 1e-11
    assert out["max_local_unitary_sector_residual"] < 1e-11
