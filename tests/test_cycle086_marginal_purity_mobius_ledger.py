import numpy as np

from cycle086_marginal_purity_mobius_ledger import (
    direct_sector_weight,
    marginal_purity_zeta,
    mobius_sector_weights,
    random_density,
    subsets,
)


def ket_density(v):
    v = np.asarray(v, dtype=complex)
    return np.outer(v, v.conj())


def test_product_pure_two_qubits():
    rho = ket_density([1, 0, 0, 0])
    C = mobius_sector_weights(marginal_purity_zeta(rho, (2, 2)), 2)
    assert np.isclose(C[()], 1.0)
    assert np.isclose(C[(0,)], 1.0)
    assert np.isclose(C[(1,)], 1.0)
    assert np.isclose(C[(0, 1)], 1.0)


def test_bell_sector_weights():
    v = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho = ket_density(v)
    C = mobius_sector_weights(marginal_purity_zeta(rho, (2, 2)), 2)
    assert abs(C[(0,)]) < 1e-12
    assert abs(C[(1,)]) < 1e-12
    assert np.isclose(C[(0, 1)], 3.0)


def test_ghz3_sector_profile():
    v = np.zeros(8, dtype=complex)
    v[0] = v[-1] = 1 / np.sqrt(2)
    rho = ket_density(v)
    C = mobius_sector_weights(marginal_purity_zeta(rho, (2, 2, 2)), 3)
    assert all(abs(C[(i,)]) < 1e-12 for i in range(3))
    assert all(np.isclose(C[S], 1.0) for S in ((0, 1), (0, 2), (1, 2)))
    assert np.isclose(C[(0, 1, 2)], 4.0)


def test_random_direct_sector_agreement():
    rng = np.random.default_rng(86014)
    dims = (2, 3, 2)
    rho = random_density(12, rng)
    C = mobius_sector_weights(marginal_purity_zeta(rho, dims), 3)
    for S in subsets(3):
        assert abs(C[S] - direct_sector_weight(rho, dims, S)) < 1e-10


def test_degenerate_dimension_one():
    rho = np.ones((1, 1), dtype=complex)
    C = mobius_sector_weights(marginal_purity_zeta(rho, (1,)), 1)
    assert np.isclose(C[()], 1.0)
    assert abs(C[(0,)]) < 1e-12
