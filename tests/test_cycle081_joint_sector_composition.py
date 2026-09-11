import numpy as np
from cycle081_joint_sector_composition import energy, joint_sector, random_density


def test_exact_decomposition_random_small_dimensions():
    rng = np.random.default_rng(81)
    for n in range(1, 7):
        for _ in range(3):
            rho = random_density(n*n, rng)
            ra, rb, _, c = joint_sector(rho, n, n)
            residual = energy(rho, n*n) - energy(ra, n) - energy(rb, n) - c
            assert abs(residual) < 1e-10
            assert c >= -1e-12


def test_product_joint_sector_equals_product_energy():
    rng = np.random.default_rng(82)
    for da, db in [(1,1),(2,2),(2,3),(3,4),(4,5)]:
        ra, rb = random_density(da, rng), random_density(db, rng)
        rho = np.kron(ra, rb)
        _, _, _, c = joint_sector(rho, da, db)
        assert abs(c - energy(ra, da)*energy(rb, db)) < 1e-10


def test_maximally_mixed_has_zero_all_sectors():
    for da, db in [(1,1),(2,3),(4,5)]:
        rho = np.eye(da*db)/(da*db)
        ra, rb, _, c = joint_sector(rho, da, db)
        assert abs(energy(rho, da*db)) < 1e-12
        assert abs(energy(ra, da)) < 1e-12
        assert abs(energy(rb, db)) < 1e-12
        assert abs(c) < 1e-12


def test_bell_state_joint_sector_positive():
    psi = np.array([1,0,0,1], dtype=complex)/np.sqrt(2)
    rho = np.outer(psi, psi.conj())
    ra, rb, _, c = joint_sector(rho, 2, 2)
    assert abs(energy(ra,2)) < 1e-12
    assert abs(energy(rb,2)) < 1e-12
    assert abs(c - 3.0) < 1e-10
