"""Cycle 025: exact local/inaccessible distinction balance.

Trace distance is used as the operational distinction measure. The mathematics is
standard open-system information-flow accounting and is not claimed as novel PDT.
"""
from __future__ import annotations
import numpy as np


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    delta = (rho - sigma + (rho - sigma).conj().T) / 2
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(delta))))


def partial_trace_environment(rho: np.ndarray, d_s: int, d_e: int) -> np.ndarray:
    return np.trace(rho.reshape(d_s, d_e, d_s, d_e), axis1=1, axis2=3)


def local_distinction(rho1: np.ndarray, rho2: np.ndarray, d_s: int, d_e: int) -> float:
    return trace_distance(partial_trace_environment(rho1, d_s, d_e), partial_trace_environment(rho2, d_s, d_e))


def total_distinction(rho1: np.ndarray, rho2: np.ndarray) -> float:
    return trace_distance(rho1, rho2)


def inaccessible_reserve(rho1: np.ndarray, rho2: np.ndarray, d_s: int, d_e: int) -> float:
    """R_S = D_SE - D_S >= 0 by partial-trace contractivity."""
    return total_distinction(rho1, rho2) - local_distinction(rho1, rho2, d_s, d_e)


def balance_terms(rho1_s, rho2_s, rho1_t, rho2_t, d_s: int, d_e: int):
    ds0 = local_distinction(rho1_s, rho2_s, d_s, d_e)
    ds1 = local_distinction(rho1_t, rho2_t, d_s, d_e)
    rt0 = inaccessible_reserve(rho1_s, rho2_s, d_s, d_e)
    rt1 = inaccessible_reserve(rho1_t, rho2_t, d_s, d_e)
    loss = total_distinction(rho1_s, rho2_s) - total_distinction(rho1_t, rho2_t)
    gain = ds1 - ds0
    residual = gain - ((rt0 - rt1) - loss)
    return {"gain": gain, "reserve_initial": rt0, "reserve_final": rt1, "global_loss": loss, "balance_residual": residual}


def apply_unitary(rho: np.ndarray, u: np.ndarray) -> np.ndarray:
    return u @ rho @ u.conj().T


def depolarize(rho: np.ndarray, lam: float) -> np.ndarray:
    if not 0 <= lam <= 1:
        raise ValueError("lam must be in [0,1]")
    d = rho.shape[0]
    return (1 - lam) * rho + lam * np.eye(d) / d
