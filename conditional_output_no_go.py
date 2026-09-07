"""Full conditional-output identifiability no-go for controlled dephasing.

Status: PROVED / NO-GO. No novelty claim is made from this module alone.

Even complete knowledge of the two conditional environment density operators
need not identify the controlled-dephasing coherence factor chi.  For a
maximally mixed qubit environment the same output pair is compatible with
every chi in the closed complex unit disk.
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
    d = int(d)
    eta = maximally_mixed(d)
    u0 = np.eye(d, dtype=complex)
    va = np.eye(d, dtype=complex)
    phases = 2.0 * np.pi * np.arange(d) / d
    vb = diagonal_relative_unitary(phases)
    a0, a1, chia = controlled_outputs(eta, u0, va)
    b0, b1, chib = controlled_outputs(eta, u0, vb)
    pair_residual = max(float(np.linalg.norm(a0-b0)), float(np.linalg.norm(a1-b1)),
                        float(np.linalg.norm(a0-a1)), float(np.linalg.norm(b0-b1)))
    return {"dimension": d, "conditional_pair_residual": pair_residual,
            "abs_chi_model_A": float(abs(chia)), "abs_chi_model_B": float(abs(chib)),
            "same_complete_conditional_outputs": bool(pair_residual < 1e-12),
            "different_coherence": bool(abs(abs(chia)-abs(chib)) > 1.0-1e-10)}


def qubit_unitary_for_target_chi(z: complex) -> np.ndarray:
    """Construct V such that eta=I/2, U0=I gives chi=Tr(V^dagger)/2=z."""
    z = complex(z)
    r = abs(z)
    if r > 1.0 + 1e-12:
        raise ValueError("target chi must lie in the closed unit disk")
    r = min(r, 1.0)
    phi = float(np.angle(z)) if r > 0 else 0.0
    theta = float(np.arccos(r))
    # V^dagger eigenphases are phi +/- theta, hence V has their negatives.
    return diagonal_relative_unitary([-(phi + theta), -(phi - theta)])


def full_disk_witness(z: complex) -> dict[str, float | bool]:
    """Exact d=2 witness: fixed rho0=rho1=I/2, arbitrary target |z|<=1."""
    z = complex(z)
    eta = maximally_mixed(2)
    u0 = np.eye(2, dtype=complex)
    v = qubit_unitary_for_target_chi(z)
    rho0, rho1, chi = controlled_outputs(eta, u0, v)
    return {
        "target_real": float(z.real), "target_imag": float(z.imag),
        "chi_real": float(chi.real), "chi_imag": float(chi.imag),
        "target_residual": float(abs(chi-z)),
        "conditional_output_residual": float(np.linalg.norm(rho0-rho1)),
        "target_reached": bool(abs(chi-z) < 1e-12),
        "outputs_identical": bool(np.linalg.norm(rho0-rho1) < 1e-12),
    }


def phase_family(d: int, alpha_values) -> list[dict[str, float]]:
    d = int(d)
    eta = maximally_mixed(d)
    u0 = np.eye(d, dtype=complex)
    rows = []
    for alpha in alpha_values:
        phases = np.zeros(d); phases[-1] = float(alpha)
        v = diagonal_relative_unitary(phases)
        rho0, rho1, chi = controlled_outputs(eta, u0, v)
        rows.append({"dimension": d, "alpha": float(alpha),
                     "conditional_output_residual": float(np.linalg.norm(rho0-rho1)),
                     "abs_chi": float(abs(chi))})
    return rows
