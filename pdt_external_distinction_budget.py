"""Cycle 024: external distinction budget for open-system distinguishability revival.

The theorem implemented here is standard trace-distance open-system mathematics,
used as a conservative PDT resource-accounting constraint. It is not claimed as
historically novel.
"""
from __future__ import annotations

import numpy as np


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    delta = (rho - sigma + (rho - sigma).conj().T) / 2
    return float(0.5 * np.sum(np.abs(np.linalg.eigvalsh(delta))))


def partial_trace_environment(rho: np.ndarray, d_s: int, d_e: int) -> np.ndarray:
    return np.trace(rho.reshape(d_s, d_e, d_s, d_e), axis1=1, axis2=3)


def partial_trace_system(rho: np.ndarray, d_s: int, d_e: int) -> np.ndarray:
    return np.trace(rho.reshape(d_s, d_e, d_s, d_e), axis1=0, axis2=2)


def correlation_distance(rho_se: np.ndarray, d_s: int, d_e: int) -> float:
    rho_s = partial_trace_environment(rho_se, d_s, d_e)
    rho_e = partial_trace_system(rho_se, d_s, d_e)
    return trace_distance(rho_se, np.kron(rho_s, rho_e))


def external_budget(rho1_se: np.ndarray, rho2_se: np.ndarray, d_s: int, d_e: int) -> float:
    """Upper bound available for any later increase in local trace distance.

    B_ext = D(rho1_E,rho2_E) + C(rho1_SE) + C(rho2_SE),
    C(rho_SE)=D(rho_SE,rho_S tensor rho_E).
    """
    e1 = partial_trace_system(rho1_se, d_s, d_e)
    e2 = partial_trace_system(rho2_se, d_s, d_e)
    return (
        trace_distance(e1, e2)
        + correlation_distance(rho1_se, d_s, d_e)
        + correlation_distance(rho2_se, d_s, d_e)
    )


def local_gain_after_unitary(
    rho1_se: np.ndarray,
    rho2_se: np.ndarray,
    unitary: np.ndarray,
    d_s: int,
    d_e: int,
) -> float:
    s1 = partial_trace_environment(rho1_se, d_s, d_e)
    s2 = partial_trace_environment(rho2_se, d_s, d_e)
    initial = trace_distance(s1, s2)
    t1 = unitary @ rho1_se @ unitary.conj().T
    t2 = unitary @ rho2_se @ unitary.conj().T
    final = trace_distance(
        partial_trace_environment(t1, d_s, d_e),
        partial_trace_environment(t2, d_s, d_e),
    )
    return final - initial


def budget_residual(
    rho1_se: np.ndarray,
    rho2_se: np.ndarray,
    unitary: np.ndarray,
    d_s: int,
    d_e: int,
) -> float:
    """Must be <= 0 up to numerical tolerance."""
    return local_gain_after_unitary(rho1_se, rho2_se, unitary, d_s, d_e) - external_budget(
        rho1_se, rho2_se, d_s, d_e
    )
