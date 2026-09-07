"""Full conditional-output identifiability no-go for controlled dephasing.

Status: PROVED / NO-GO. No novelty claim is made from this module alone.

The theorem strengthens the scalar mixed-record observation: even complete
knowledge of the two conditional environment density operators need not
identify the controlled-dephasing coherence factor chi.

For eta = I_d/d and U0 = I_d, any U1 = V gives
rho0 = rho1 = I_d/d, while chi = Tr(V^dagger)/d.  Hence the same complete
conditional-output pair is compatible with different coherence factors.
"""
from __future__ import annotations

import numpy as np


def maximally_mixed(d: int) -> np.ndarray:
    if int(d) < 2:
        raise ValueError("d must be >= 2")
    return np.eye(int(d), dtype=complex) / float(d)


def diagonal_relative_unitary(phases) -> np.ndarray:
    phases = np.asarray(phases, dtype=float)
    if phases.ndim != 1 or phases.size < 2:
        raise ValueError("phases must be a one-dimensional array of length >= 2")
    return np.diag(np.exp(1j * phases)).astype(complex)


def controlled_outputs(eta: np.ndarray, u0: np.ndarray, u1: np.ndarray):
    eta = np.asarray(eta, complex)
    u0 = np.asarray(u0, complex)
    u1 = np.asarray(u1, complex)
    rho0 = u0 @ eta @ u0.conj().T
    rho1 = u1 @ eta @ u1.conj().T
    chi = complex(np.trace(u0 @ eta @ u1.conj().T))
    return rho0, rho1, chi


def full_output_pair_witness(d: int = 2) -> dict[str, float | bool]:
    """Two microscopic models with identical conditional outputs but |chi| 1 vs 0.

    Model A: V = I_d, so |chi|=1.
    Model B: V has d-th roots of unity on its diagonal, whose trace is zero,
    so |chi|=0.  In both models eta=I_d/d and rho0=rho1=I_d/d.
    """
    d = int(d)
    eta = maximally_mixed(d)
    u0 = np.eye(d, dtype=complex)
    va = np.eye(d, dtype=complex)
    phases = 2.0 * np.pi * np.arange(d) / d
    vb = diagonal_relative_unitary(phases)

    a0, a1, chia = controlled_outputs(eta, u0, va)
    b0, b1, chib = controlled_outputs(eta, u0, vb)

    pair_residual = max(
        float(np.linalg.norm(a0 - b0)),
        float(np.linalg.norm(a1 - b1)),
        float(np.linalg.norm(a0 - a1)),
        float(np.linalg.norm(b0 - b1)),
    )
    return {
        "dimension": d,
        "conditional_pair_residual": pair_residual,
        "abs_chi_model_A": float(abs(chia)),
        "abs_chi_model_B": float(abs(chib)),
        "same_complete_conditional_outputs": bool(pair_residual < 1e-12),
        "different_coherence": bool(abs(abs(chia) - abs(chib)) > 1.0 - 1e-10),
    }


def phase_family(d: int, alpha_values) -> list[dict[str, float]]:
    """Continuous family with fixed conditional outputs and varying chi.

    V(alpha)=diag(1,...,1,exp(i alpha)) gives
    chi=(d-1+exp(-i alpha))/d while rho0=rho1=I_d/d.
    """
    d = int(d)
    eta = maximally_mixed(d)
    u0 = np.eye(d, dtype=complex)
    rows = []
    for alpha in alpha_values:
        phases = np.zeros(d)
        phases[-1] = float(alpha)
        v = diagonal_relative_unitary(phases)
        rho0, rho1, chi = controlled_outputs(eta, u0, v)
        rows.append({
            "dimension": d,
            "alpha": float(alpha),
            "conditional_output_residual": float(np.linalg.norm(rho0-rho1)),
            "abs_chi": float(abs(chi)),
        })
    return rows
