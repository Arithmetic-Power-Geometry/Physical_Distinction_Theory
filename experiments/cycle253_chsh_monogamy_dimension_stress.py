"""Cycle 253: dimension stress for CHSH-monogamy as a PDT selector.

Construct, for each local dimension n>=2, an embedded two-level maximally
entangled AB state and an uncorrelated pure C.  The standard CHSH observables
on the embedded two-level support give S_AB=2*sqrt(2), while all AC correlators
vanish because rho_A is maximally mixed on that support and A0,A1 are traceless
there. Hence S_AB^2+S_AC^2=8 in every n>=2.

This is a regression witness only; the arbitrary-dimension monogamy theorem is
prior art (Toner & Verstraete, quant-ph/0611001).
"""

import numpy as np


def embedded_observable(block: np.ndarray, n: int) -> np.ndarray:
    out = np.eye(n, dtype=complex)
    out[:2, :2] = block
    return out


def chsh_value(rho: np.ndarray, a0: np.ndarray, a1: np.ndarray,
               b0: np.ndarray, b1: np.ndarray) -> float:
    op = np.kron(a0, b0 + b1) + np.kron(a1, b0 - b1)
    return float(np.real(np.trace(rho @ op)))


def witness(n: int):
    if n < 2:
        return {"n": n, "degenerate": True}
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    z = np.array([[1, 0], [0, -1]], dtype=complex)
    a0, a1 = embedded_observable(z, n), embedded_observable(x, n)
    b0 = embedded_observable((z + x) / np.sqrt(2), n)
    b1 = embedded_observable((z - x) / np.sqrt(2), n)
    c0, c1 = embedded_observable(z, n), embedded_observable(x, n)

    psi_ab = np.zeros(n * n, dtype=complex)
    psi_ab[0] = 1 / np.sqrt(2)
    psi_ab[n + 1] = 1 / np.sqrt(2)
    rho_ab = np.outer(psi_ab, psi_ab.conj())

    rho_a = np.zeros((n, n), dtype=complex)
    rho_a[0, 0] = rho_a[1, 1] = 0.5
    rho_c = np.zeros((n, n), dtype=complex)
    rho_c[0, 0] = 1.0
    rho_ac = np.kron(rho_a, rho_c)

    s_ab = chsh_value(rho_ab, a0, a1, b0, b1)
    s_ac = chsh_value(rho_ac, a0, a1, c0, c1)
    return {"n": n, "degenerate": False, "S_AB": s_ab, "S_AC": s_ac,
            "sum_squares": s_ab * s_ab + s_ac * s_ac}


def test_dimensions_1_through_12():
    rows = [witness(n) for n in range(1, 13)]
    assert rows[0]["degenerate"]
    for row in rows[1:]:
        assert abs(row["S_AB"] - 2 * np.sqrt(2)) < 1e-12
        assert abs(row["S_AC"]) < 1e-12
        assert abs(row["sum_squares"] - 8.0) < 1e-11
    return rows


if __name__ == "__main__":
    for row in test_dimensions_1_through_12():
        print(row)
