"""Mixed-record identifiability no-go for PDT controlled dephasing.

Scientific status: PROVED / NO-GO, but not claimed as new quantum mathematics.
It sharpens the PDT identifiability boundary: trace distinguishability of the
conditional environment states alone does not determine the system coherence
factor for mixed environmental records.
"""
from __future__ import annotations

import numpy as np


def maximally_mixed_qubit_environment() -> np.ndarray:
    return 0.5 * np.eye(2, dtype=complex)


def z_relative_unitary(theta: float) -> np.ndarray:
    """Return exp(-i theta sigma_z / 2)."""
    theta = float(theta)
    return np.diag([np.exp(-0.5j * theta), np.exp(0.5j * theta)]).astype(complex)


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    d = np.asarray(rho, complex) - np.asarray(sigma, complex)
    return float(0.5 * np.sum(np.linalg.svd(d, compute_uv=False)))


def controlled_record_quantities(theta: float) -> dict[str, float]:
    """Construct a family with fixed D_E=0 but variable |chi|.

    Set eta=I/2, U0=I and U1=exp(-i theta sigma_z/2). Then
    rho_E^(0)=rho_E^(1)=I/2 for every theta, so D_E=0, while
    chi=Tr(U0 eta U1^dagger)=cos(theta/2), up to complex conjugation.
    """
    eta = maximally_mixed_qubit_environment()
    u0 = np.eye(2, dtype=complex)
    u1 = z_relative_unitary(theta)
    rho0 = u0 @ eta @ u0.conj().T
    rho1 = u1 @ eta @ u1.conj().T
    chi = np.trace(u0 @ eta @ u1.conj().T)
    return {
        "theta": float(theta),
        "D_E": trace_distance(rho0, rho1),
        "abs_chi": float(abs(chi)),
        "analytic_abs_chi": float(abs(np.cos(float(theta) / 2.0))),
    }


def scalar_record_nonidentifiability_witness() -> dict[str, float | bool]:
    """Return an explicit same-D, different-coherence witness."""
    a = controlled_record_quantities(0.0)
    b = controlled_record_quantities(np.pi)
    return {
        "D_case_a": a["D_E"],
        "D_case_b": b["D_E"],
        "abs_chi_case_a": a["abs_chi"],
        "abs_chi_case_b": b["abs_chi"],
        "same_D": bool(abs(a["D_E"] - b["D_E"]) < 1e-12),
        "different_abs_chi": bool(abs(a["abs_chi"] - b["abs_chi"]) > 1e-6),
    }
