"""Cycle 018: finite-record-dimension coherence floor via the first Welch bound.

For k unit pure record vectors in C^d with Gram matrix G,

    avg_{i!=j} |G_ij|^2 >= max(0, (k-d)/(d(k-1))).

Equivalently, if R_ij := 1-|G_ij|^2 is used as a pairwise revelation score,
its ordered-pair average obeys

    avg R_ij <= 1 - max(0, (k-d)/(d(k-1))).

This module treats the inequality as imported/known frame-theory mathematics and
uses it only as a PDT operational resource constraint.
"""
from __future__ import annotations

import numpy as np


def welch_average_floor(k: int, d: int) -> float:
    if k < 1 or d < 1:
        raise ValueError("k and d must be positive")
    if k <= d:
        return 0.0
    return (k - d) / (d * (k - 1))


def revelation_average_ceiling(k: int, d: int) -> float:
    return 1.0 - welch_average_floor(k, d)


def gram_matrix(records: np.ndarray) -> np.ndarray:
    """Return Gram matrix for columns containing record vectors."""
    x = np.asarray(records, dtype=np.complex128)
    if x.ndim != 2:
        raise ValueError("records must be a 2D array with record vectors as columns")
    norms = np.linalg.norm(x, axis=0)
    if np.any(norms == 0):
        raise ValueError("record vectors must be nonzero")
    x = x / norms
    return x.conj().T @ x


def average_squared_overlap(records: np.ndarray) -> float:
    g = gram_matrix(records)
    k = g.shape[0]
    if k <= 1:
        return 0.0
    off = np.abs(g) ** 2
    return float((off.sum() - k) / (k * (k - 1)))


def maximum_squared_overlap(records: np.ndarray) -> float:
    g = gram_matrix(records)
    k = g.shape[0]
    if k <= 1:
        return 0.0
    mask = ~np.eye(k, dtype=bool)
    return float(np.max(np.abs(g[mask]) ** 2))


def audit_random_records(d: int, k: int, trials: int = 500, seed: int = 260909) -> dict:
    if d < 1 or k < 1 or trials < 1:
        raise ValueError("d, k, and trials must be positive")
    rng = np.random.default_rng(seed + 1009 * d + 9176 * k)
    floor = welch_average_floor(k, d)
    min_avg_margin = float("inf")
    min_max_margin = float("inf")
    for _ in range(trials):
        x = rng.normal(size=(d, k)) + 1j * rng.normal(size=(d, k))
        x /= np.linalg.norm(x, axis=0, keepdims=True)
        avg = average_squared_overlap(x)
        mx = maximum_squared_overlap(x)
        min_avg_margin = min(min_avg_margin, avg - floor)
        min_max_margin = min(min_max_margin, mx - floor)
    return {
        "d": d,
        "k": k,
        "trials": trials,
        "welch_average_floor": floor,
        "revelation_average_ceiling": revelation_average_ceiling(k, d),
        "min_average_margin": min_avg_margin,
        "min_maximum_margin": min_max_margin,
    }


def orthonormal_records(d: int) -> np.ndarray:
    return np.eye(d, dtype=np.complex128)


def repeated_records(k: int) -> np.ndarray:
    return np.ones((1, k), dtype=np.complex128)
