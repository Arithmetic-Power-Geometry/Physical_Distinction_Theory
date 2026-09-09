import numpy as np

from pdt_external_distinction_budget import (
    budget_residual,
    external_budget,
    local_gain_after_unitary,
)


def random_density(rng, d):
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    x = a @ a.conj().T
    return x / np.trace(x)


def random_unitary(rng, d):
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(a)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    return q @ np.diag(phases.conj())


def test_product_same_environment_has_zero_external_budget():
    s1 = np.diag([1.0, 0.0])
    s2 = np.diag([0.0, 1.0])
    e = np.diag([0.7, 0.3])
    r1, r2 = np.kron(s1, e), np.kron(s2, e)
    assert external_budget(r1, r2, 2, 2) < 1e-12


def test_no_gain_when_external_budget_zero():
    s1 = np.diag([1.0, 0.0])
    s2 = np.diag([0.0, 1.0])
    e = np.diag([0.7, 0.3])
    r1, r2 = np.kron(s1, e), np.kron(s2, e)
    u = np.eye(4)
    assert local_gain_after_unitary(r1, r2, u, 2, 2) <= 1e-12


def test_random_bound_dimensions_1_to_12():
    rng = np.random.default_rng(24024)
    for d_s in range(1, 13):
        d_e = 2
        d = d_s * d_e
        for _ in range(20):
            r1, r2 = random_density(rng, d), random_density(rng, d)
            u = random_unitary(rng, d)
            assert budget_residual(r1, r2, u, d_s, d_e) <= 1e-10


def test_random_higher_dimension_stress():
    rng = np.random.default_rng(240240)
    for d_s in (16, 24, 32):
        d_e = 2
        d = d_s * d_e
        r1, r2 = random_density(rng, d), random_density(rng, d)
        u = random_unitary(rng, d)
        assert budget_residual(r1, r2, u, d_s, d_e) <= 1e-10
