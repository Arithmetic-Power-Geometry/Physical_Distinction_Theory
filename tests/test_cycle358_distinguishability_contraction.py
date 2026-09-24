import numpy as np


def trace_distance(rho, sigma):
    vals = np.linalg.eigvalsh(rho - sigma)
    return 0.5 * np.sum(np.abs(vals))


def basis_state(d, j):
    v = np.zeros((d, 1), dtype=complex)
    v[j, 0] = 1.0
    return v @ v.conj().T


def replacement_channel(rho, tau):
    return tau * np.trace(rho)


def test_unitary_saturation_n2_to_n12():
    for d in range(2, 13):
        rho = basis_state(d, 0)
        sigma = basis_state(d, 1)
        # Cyclic shift is unitary.
        U = np.roll(np.eye(d, dtype=complex), 1, axis=0)
        before = trace_distance(rho, sigma)
        after = trace_distance(U @ rho @ U.conj().T, U @ sigma @ U.conj().T)
        assert np.isclose(before, 1.0)
        assert np.isclose(after, before)


def test_replacement_erasure_n2_to_n12():
    for d in range(2, 13):
        rho = basis_state(d, 0)
        sigma = basis_state(d, 1)
        tau = np.eye(d, dtype=complex) / d
        before = trace_distance(rho, sigma)
        after = trace_distance(replacement_channel(rho, tau), replacement_channel(sigma, tau))
        assert np.isclose(before, 1.0)
        assert np.isclose(after, 0.0)
        assert after <= before


def test_fixed_ancilla_stability():
    for d in range(2, 13):
        rho = basis_state(d, 0)
        sigma = basis_state(d, 1)
        tau = np.diag([0.7, 0.3]).astype(complex)
        lhs = trace_distance(np.kron(rho, tau), np.kron(sigma, tau))
        rhs = trace_distance(rho, sigma)
        assert np.isclose(lhs, rhs)
