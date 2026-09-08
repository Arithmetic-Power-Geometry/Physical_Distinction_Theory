"""Affine-mixture lock tests for PDT same-input prediction candidates.

If a candidate prediction is affine under classical preparation mixing and agrees
with the Born rule on every pure state, it is locked to the Born rule on every
mixed state.  The numerical routines below audit the identity and its robust
uniform-error version; they do not establish novelty.
"""
from __future__ import annotations

import numpy as np


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    e = a @ a.conj().T
    lam = float(np.linalg.eigvalsh(e).max())
    return e / lam if lam > 0 else e


def born(effect: np.ndarray, rho: np.ndarray) -> float:
    return float(np.real(np.trace(effect @ rho)))


def spectral_affine_reconstruction(effect: np.ndarray, rho: np.ndarray) -> float:
    """Reconstruct the mixed-state prediction from its pure spectral components."""
    vals, vecs = np.linalg.eigh(rho)
    return float(sum(
        float(vals[i]) * float(np.real(vecs[:, i].conj().T @ effect @ vecs[:, i]))
        for i in range(len(vals))
    ))


def mixture_deviation(weights: np.ndarray, pure_deviations: np.ndarray) -> float:
    """Deviation inherited by an affine mixture from pure-component deviations."""
    weights = np.asarray(weights, dtype=float)
    pure_deviations = np.asarray(pure_deviations, dtype=float)
    if weights.shape != pure_deviations.shape:
        raise ValueError("weights and deviations must have the same shape")
    if np.any(weights < -1e-15) or not np.isclose(weights.sum(), 1.0):
        raise ValueError("weights must be a probability vector")
    return float(np.dot(weights, pure_deviations))


def robust_bound_holds(weights: np.ndarray, pure_deviations: np.ndarray, eps: float, tol: float = 1e-12) -> bool:
    """Uniform |delta_pure|<=eps implies |delta_mixed|<=eps under affinity."""
    if np.max(np.abs(pure_deviations)) > eps + tol:
        raise ValueError("pure deviation bound violated by supplied data")
    return abs(mixture_deviation(weights, pure_deviations)) <= eps + tol


def audit_dimensions(max_d: int = 12, trials: int = 100, seed: int = 20260908, eps: float = 1e-2):
    rng = np.random.default_rng(seed)
    rows = []
    for d in range(1, max_d + 1):
        max_identity_residual = 0.0
        max_mixed_deviation = 0.0
        for _ in range(trials):
            rho = random_density(d, rng)
            effect = random_effect(d, rng)
            residual = abs(born(effect, rho) - spectral_affine_reconstruction(effect, rho))
            max_identity_residual = max(max_identity_residual, residual)
            vals = np.linalg.eigvalsh(rho)
            deltas = rng.uniform(-eps, eps, size=d)
            mixed = mixture_deviation(vals, deltas)
            max_mixed_deviation = max(max_mixed_deviation, abs(mixed))
            assert robust_bound_holds(vals, deltas, eps)
        rows.append({
            "dimension": d,
            "trials": trials,
            "max_born_affine_residual": max_identity_residual,
            "epsilon": eps,
            "max_observed_mixed_deviation": max_mixed_deviation,
            "robust_bound_pass": max_mixed_deviation <= eps + 1e-12,
        })
    return rows
