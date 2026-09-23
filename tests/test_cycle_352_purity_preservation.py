"""Cycle 352 exact regression checks for the pure-product-preservation no-go."""

import numpy as np


def classical_vertex(n: int, i: int) -> np.ndarray:
    v = np.zeros(n, dtype=int)
    v[i] = 1
    return v


def quantum_pure_state(n: int, i: int) -> np.ndarray:
    psi = np.zeros(n, dtype=complex)
    psi[i] = 1.0
    return np.outer(psi, psi.conj())


def test_classical_pure_products_n1_n12():
    for n in range(1, 13):
        a = classical_vertex(n, 0)
        b = classical_vertex(n, n - 1)
        joint = np.kron(a, b)
        assert joint.sum() == 1
        assert np.count_nonzero(joint) == 1
        assert set(np.unique(joint)).issubset({0, 1})


def test_quantum_pure_products_n1_n12():
    for n in range(1, 13):
        rho = quantum_pure_state(n, 0)
        sigma = quantum_pure_state(n, n - 1)
        joint = np.kron(rho, sigma)
        evals = np.linalg.eigvalsh(joint)
        assert np.isclose(np.trace(joint), 1.0)
        assert np.isclose(np.trace(joint @ joint), 1.0)
        assert np.count_nonzero(evals > 1e-12) == 1


def test_n2_is_decisive_counterexample_to_n3_selection():
    # Both inequivalent model families satisfy PPP already at n=2.
    a = classical_vertex(2, 0)
    b = classical_vertex(2, 1)
    assert np.count_nonzero(np.kron(a, b)) == 1

    rho = quantum_pure_state(2, 0)
    sigma = quantum_pure_state(2, 1)
    joint = np.kron(rho, sigma)
    assert np.isclose(np.trace(joint @ joint), 1.0)
