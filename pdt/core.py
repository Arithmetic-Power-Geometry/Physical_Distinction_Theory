"""Core computational utilities for Physical Distinction Theory (PDT).

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

The module separates exact mathematical identities from model-specific numerical
illustrations. Nothing here is presented as experimental evidence for quantum gravity.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import log2, sqrt
import itertools
import numpy as np
from numpy.linalg import eigvalsh, svd

TOL = 1e-12


def _as_density(rho: np.ndarray) -> np.ndarray:
    rho = np.asarray(rho, dtype=complex)
    if rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError("density matrix must be square")
    rho = (rho + rho.conj().T) / 2
    tr = np.trace(rho)
    if abs(tr) <= TOL:
        raise ValueError("density matrix has zero trace")
    rho = rho / tr
    vals = eigvalsh(rho)
    if vals.min() < -1e-10:
        raise ValueError("matrix is not positive semidefinite")
    return rho


def von_neumann_entropy(rho: np.ndarray, base: float = 2.0) -> float:
    vals = np.clip(eigvalsh(_as_density(rho)).real, 0, 1)
    vals = vals[vals > 1e-15]
    return float(-np.sum(vals * np.log(vals) / np.log(base)))


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    d = _as_density(rho) - _as_density(sigma)
    return float(0.5 * np.sum(svd(d, compute_uv=False)))


def helstrom_error_binary(rho: np.ndarray, sigma: np.ndarray) -> float:
    return float(0.5 * (1.0 - trace_distance(rho, sigma)))


def depolarize(rho: np.ndarray, p: float) -> np.ndarray:
    rho = _as_density(rho)
    if not 0 <= p <= 1:
        raise ValueError("p must be in [0,1]")
    d = rho.shape[0]
    return (1 - p) * rho + p * np.eye(d) / d


def pure_state(theta: float, phi: float = 0.0) -> np.ndarray:
    v = np.array([np.cos(theta / 2), np.exp(1j * phi) * np.sin(theta / 2)], complex)
    return np.outer(v, v.conj())


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def equatorial_codebook(n: int) -> list[np.ndarray]:
    return [pure_state(np.pi / 2, 2 * np.pi * k / n) for k in range(n)]


def resource_bounded_code_capacity(states, epsilon=0.1, budget=None):
    """Exact maximum log2 codebook size for a finite candidate set.

    Compatibility is defined pairwise through equal-prior binary Helstrom error.
    This is a finite proxy for the manuscript's resource-bounded distinction capacity,
    not a universal multi-hypothesis channel capacity theorem.
    """
    states = list(states)
    if budget is not None:
        if callable(budget):
            states = [s for i, s in enumerate(states) if budget(i, s)]
        else:
            states = [s for s, m in zip(states, budget) if bool(m)]
    n = len(states)
    if n == 0:
        return 0.0, []
    compat = np.eye(n, dtype=bool)
    for i in range(n):
        for j in range(i + 1, n):
            ok = helstrom_error_binary(states[i], states[j]) <= epsilon + 1e-12
            compat[i, j] = compat[j, i] = ok

    best: list[int] = []

    def expand(clique: list[int], candidates: list[int]):
        nonlocal best
        if len(clique) + len(candidates) <= len(best):
            return
        while candidates:
            v = candidates.pop()
            new_candidates = [u for u in candidates if compat[v, u] and all(compat[u, w] for w in clique)]
            new_clique = clique + [v]
            if len(new_clique) > len(best):
                best = new_clique
            expand(new_clique, new_candidates)
            if len(clique) + len(candidates) <= len(best):
                return

    expand([], list(range(n)))
    return float(log2(max(1, len(best)))), best


def chsh_from_correlators(E00: float, E01: float, E10: float, E11: float) -> float:
    return float(abs(E00 + E01 + E10 - E11))


def classical_chsh_bound() -> float:
    best = 0.0
    for a0, a1, b0, b1 in itertools.product([-1, 1], repeat=4):
        best = max(best, chsh_from_correlators(a0*b0, a0*b1, a1*b0, a1*b1))
    return best


def pr_box_chsh() -> float:
    return chsh_from_correlators(1.0, 1.0, 1.0, -1.0)


def chsh_value(a0, a1, b0, b1) -> float:
    def unit(x):
        x = np.asarray(x, float); n = np.linalg.norm(x)
        if n <= TOL: raise ValueError("zero vector")
        return x / n
    a0, a1, b0, b1 = map(unit, (a0, a1, b0, b1))
    return float(abs(-a0 @ b0 - a0 @ b1 - a1 @ b0 + a1 @ b1))


def vectorized_chsh_search(samples: int = 1_000_000, seed: int = 11):
    rng = np.random.default_rng(seed)
    ang = rng.uniform(0, 2*np.pi, size=(samples, 4))
    E00 = -np.cos(ang[:, 0] - ang[:, 2]); E01 = -np.cos(ang[:, 0] - ang[:, 3])
    E10 = -np.cos(ang[:, 1] - ang[:, 2]); E11 = -np.cos(ang[:, 1] - ang[:, 3])
    S = np.abs(E00 + E01 + E10 - E11); i = int(np.argmax(S))
    return float(S[i]), ang[i].copy()


def p_norm(x, p: float) -> float:
    x = np.asarray(x, float)
    if p == np.inf: return float(np.max(np.abs(x)))
    return float(np.sum(np.abs(x) ** p) ** (1.0 / p))


def parallelogram_defect(x, y, p: float = 2.0) -> float:
    lhs = p_norm(np.asarray(x)+np.asarray(y), p)**2 + p_norm(np.asarray(x)-np.asarray(y), p)**2
    rhs = 2*p_norm(x, p)**2 + 2*p_norm(y, p)**2
    return float(abs(lhs-rhs))


def max_parallelogram_defect(p: float, dimension: int = 4, samples: int = 10000, seed: int = 17) -> float:
    rng = np.random.default_rng(seed); X = rng.normal(size=(samples, dimension)); Y = rng.normal(size=(samples, dimension))
    return float(max(parallelogram_defect(x, y, p) for x, y in zip(X, Y)))


def tsirelson_bound_from_parallelogram(norm_b0=1.0, norm_b1=1.0) -> float:
    q = 2*norm_b0**2 + 2*norm_b1**2
    return float(np.sqrt(2*q))


def refinement_residual(q: float, m: int, r: float = 0.731) -> float:
    lhs = abs(r)**q; rhs = m * abs(r/np.sqrt(m))**q
    return float(lhs-rhs)


def refinement_objective(q: float, m_values=(2,3,4,5,7,11), r_values=(0.23,0.51,0.79)) -> float:
    return float(sum(refinement_residual(q, m, r)**2 for m in m_values for r in r_values))


def born_exponent_grid(qmin=0.5, qmax=4.5, points=801):
    qs = np.linspace(qmin, qmax, points); obj = np.array([refinement_objective(q) for q in qs]); i = int(np.argmin(obj))
    return qs, obj, float(qs[i]), float(obj[i])


def canonical_complex_structure(n_pairs: int = 2) -> np.ndarray:
    J2 = np.array([[0.0, -1.0], [1.0, 0.0]])
    return np.kron(np.eye(n_pairs), J2)


def complex_structure_residual(J: np.ndarray) -> tuple[float, float]:
    J = np.asarray(J, float); n = J.shape[0]
    return float(np.linalg.norm(J @ J + np.eye(n), ord='fro')), float(np.linalg.norm(J.T @ J - np.eye(n), ord='fro'))


def homogeneous_capacity(cell_count, kappa: float = 0.75):
    return kappa * np.asarray(cell_count, dtype=float)


def screen_capacity(area_planck_units, bits_per_planck_area=1/(4*np.log(2))):
    return bits_per_planck_area * np.asarray(area_planck_units, dtype=float)


def planck_area_scaling(localization_scale_planck_units):
    L = np.asarray(localization_scale_planck_units, dtype=float)
    if np.any(L <= 0): raise ValueError("L must be positive")
    return 1.0 / (L**2)


@dataclass(frozen=True)
class FoilModel:
    name: str
    finite: bool
    no_signalling: bool
    composable: bool
    reversible_symmetries: bool
    resource_monotone_possible: bool
    chsh_max: float
    born_forced: bool


def foil_models():
    return [
        FoilModel("Classical local simplex", True, True, True, True, True, 2.0, False),
        FoilModel("Hilbertian quantum realization", True, True, True, True, True, 2*sqrt(2), True),
        FoilModel("PR-box no-signalling foil", True, True, True, True, True, 4.0, False),
    ]
