"""Numerical audit for the unchanged-record spectral coherence annulus theorem."""
from __future__ import annotations
import numpy as np


def annulus_lower_radius(probabilities) -> float:
    p = np.asarray(probabilities, dtype=float)
    if p.ndim != 1 or len(p) == 0 or np.any(p < 0) or not np.isclose(p.sum(), 1.0):
        raise ValueError("probabilities must be a normalized nonnegative vector")
    return float(max(0.0, 2.0 * p.max() - 1.0))


def coherence(probabilities, phases) -> complex:
    p = np.asarray(probabilities, dtype=float)
    th = np.asarray(phases, dtype=float)
    if p.shape != th.shape:
        raise ValueError("probabilities and phases must have same shape")
    return complex(np.sum(p * np.exp(1j * th)))


def unchanged_record_residual(probabilities, phases) -> float:
    p = np.asarray(probabilities, dtype=float)
    th = np.asarray(phases, dtype=float)
    eta = np.diag(p).astype(complex)
    U = np.diag(np.exp(-1j * th))
    out = U @ eta @ U.conj().T
    return float(np.linalg.norm(out - eta))


def monte_carlo_audit(probabilities, samples=50000, seed=260908):
    p = np.asarray(probabilities, dtype=float)
    rng = np.random.default_rng(seed)
    phases = rng.uniform(0.0, 2*np.pi, size=(samples, len(p)))
    z = np.sum(p[None, :] * np.exp(1j * phases), axis=1)
    mod = np.abs(z)
    theory_min = annulus_lower_radius(p)
    return {
        "p_max": float(p.max()),
        "theory_min": theory_min,
        "sample_min": float(mod.min()),
        "sample_max": float(mod.max()),
        "lower_bound_violation": float(max(0.0, theory_min - mod.min())),
    }


if __name__ == "__main__":
    cases = [
        [0.5, 0.5],
        [0.7, 0.3],
        [0.4, 0.35, 0.25],
        [0.9, 0.05, 0.05],
        [1.0],
    ]
    for p in cases:
        print(p, monte_carlo_audit(p))
