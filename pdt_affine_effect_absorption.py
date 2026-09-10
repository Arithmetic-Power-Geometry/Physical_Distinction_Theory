"""Cycle 044: affine probability laws on density matrices are effective effects.

For each fixed resource context R, an affine probability functional f_R on the
convex set of d-dimensional density matrices has the form
    f_R(rho) = Tr(E_R rho)
for a Hermitian E_R. If 0 <= f_R(rho) <= 1 for every state, then 0 <= E_R <= I.
Hence a resource-dependent affine probability law is operationally an
R-dependent effective measurement effect, not a new probability rule.
"""

from __future__ import annotations

import numpy as np


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    u, _ = np.linalg.qr(rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)))
    vals = rng.uniform(0.0, 1.0, size=d)
    return u @ np.diag(vals) @ u.conj().T


def born_probability(rho: np.ndarray, effect: np.ndarray) -> float:
    return float(np.real(np.trace(effect @ rho)))


def mixture_residual(effect: np.ndarray, rho: np.ndarray, sigma: np.ndarray, t: float) -> float:
    lhs = born_probability(t * rho + (1.0 - t) * sigma, effect)
    rhs = t * born_probability(rho, effect) + (1.0 - t) * born_probability(sigma, effect)
    return abs(lhs - rhs)


def purity_corrected_probability(rho: np.ndarray, effect: np.ndarray, lam: float) -> float:
    """Illustrative nonlinear candidate; deliberately not asserted physical."""
    base = born_probability(rho, effect)
    purity = float(np.real(np.trace(rho @ rho)))
    d = rho.shape[0]
    return base + lam * (purity - 1.0 / d)


def nonlinear_mixture_residual(effect: np.ndarray, rho: np.ndarray, sigma: np.ndarray, t: float, lam: float) -> float:
    mix = t * rho + (1.0 - t) * sigma
    lhs = purity_corrected_probability(mix, effect, lam)
    rhs = t * purity_corrected_probability(rho, effect, lam) + (1.0 - t) * purity_corrected_probability(sigma, effect, lam)
    return abs(lhs - rhs)


def effect_bounds(effect: np.ndarray, tol: float = 1e-10) -> bool:
    vals = np.linalg.eigvalsh((effect + effect.conj().T) / 2)
    return bool(vals.min() >= -tol and vals.max() <= 1.0 + tol)


def audit(max_d: int = 12, samples: int = 40, seed: int = 4401) -> list[dict]:
    rng = np.random.default_rng(seed)
    rows = []
    for d in range(1, max_d + 1):
        worst_affine = 0.0
        max_nonlinear = 0.0
        for _ in range(samples):
            e = random_effect(d, rng)
            rho = random_density(d, rng)
            sigma = random_density(d, rng)
            t = float(rng.uniform())
            worst_affine = max(worst_affine, mixture_residual(e, rho, sigma, t))
            if d >= 2:
                max_nonlinear = max(max_nonlinear, nonlinear_mixture_residual(e, rho, sigma, t, 0.1))
            assert effect_bounds(e)
            p = born_probability(rho, e)
            assert -1e-10 <= p <= 1.0 + 1e-10
        rows.append({"dimension": d, "max_affine_residual": worst_affine, "max_nonlinear_residual": max_nonlinear})
    return rows


if __name__ == "__main__":
    for row in audit():
        print(row)
