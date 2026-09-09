"""Cycle 021: dimension-limited exact branch-identification bound.

For k equiprobable record states rho_i supported on a d-dimensional Hilbert
space and any k-outcome POVM {M_i},

    P_success = (1/k) sum_i Tr(M_i rho_i) <= min(1, d/k).

The proof is immediate from 0 <= rho_i <= I and sum_i M_i = I.  Hence
P_error >= max(0, 1-d/k).  The bound is sharp when k is a multiple of d by
repeating each vector of an orthonormal basis equally often.

This is standard minimum-error quantum-state-discrimination mathematics.  PDT
uses it only as an operational finite-record resource bound; no historical
novelty is claimed.
"""

from __future__ import annotations

import numpy as np


def success_upper_bound(d: int, k: int) -> float:
    if d < 1 or k < 1:
        raise ValueError("d and k must be positive")
    return min(1.0, d / k)


def error_lower_bound(d: int, k: int) -> float:
    return 1.0 - success_upper_bound(d, k)


def random_density_matrix(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def random_povm(d: int, k: int, rng: np.random.Generator) -> list[np.ndarray]:
    effects = []
    total = np.zeros((d, d), dtype=complex)
    for _ in range(k):
        a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        b = a @ a.conj().T
        effects.append(b)
        total += b
    vals, vecs = np.linalg.eigh(total)
    inv_sqrt = (vecs * (1.0 / np.sqrt(np.maximum(vals, 1e-15)))) @ vecs.conj().T
    return [inv_sqrt @ b @ inv_sqrt for b in effects]


def discrimination_success(states: list[np.ndarray], povm: list[np.ndarray]) -> float:
    if len(states) != len(povm) or not states:
        raise ValueError("states and POVM must have the same nonzero length")
    k = len(states)
    return float(sum(np.trace(m @ rho).real for m, rho in zip(povm, states)) / k)


def saturation_ensemble(d: int, q: int) -> tuple[list[np.ndarray], list[np.ndarray]]:
    """Return k=q*d states and a POVM attaining P_success=d/k=1/q.

    Each basis state is repeated q times.  For each repeated label the effect
    is |j><j|/q, so the k effects sum to identity and every correct-label
    probability equals 1/q.
    """
    if d < 1 or q < 1:
        raise ValueError("d and q must be positive")
    states: list[np.ndarray] = []
    povm: list[np.ndarray] = []
    for j in range(d):
        proj = np.zeros((d, d), dtype=complex)
        proj[j, j] = 1.0
        for _ in range(q):
            states.append(proj.copy())
            povm.append(proj / q)
    return states, povm


def random_stress(d: int, k: int, trials: int = 300, seed: int = 260909) -> dict[str, float]:
    rng = np.random.default_rng(seed + 1009 * d + k)
    best = 0.0
    for _ in range(trials):
        states = [random_density_matrix(d, rng) for _ in range(k)]
        povm = random_povm(d, k, rng)
        best = max(best, discrimination_success(states, povm))
    bound = success_upper_bound(d, k)
    return {
        "dimension": float(d),
        "labels": float(k),
        "trials": float(trials),
        "success_upper_bound": bound,
        "error_lower_bound": error_lower_bound(d, k),
        "largest_random_success": best,
        "max_violation": best - bound,
    }
