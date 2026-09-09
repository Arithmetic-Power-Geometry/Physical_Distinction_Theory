"""Cycle 022: prior-weighted composite record identification bound.

For an ensemble {p_i, rho_i} supported on a Hilbert space of total dimension D
and any POVM {M_i} used to guess the exact classical label,

    P_success = sum_i p_i Tr(M_i rho_i) <= min(1, D * p_max).

For a tensor-product record with subsystem dimensions d_1,...,d_m,
D = prod_j d_j. Equivalently,

    H_min(X|measurement) >= max(0, H_min(X) - log2 D),

where H_min(X)=-log2 p_max and the left side denotes -log2 of the optimal
guessing probability after measuring the record.

This is standard minimum-error quantum-state-discrimination / one-shot
information mathematics. PDT uses it as a finite-resource composition audit;
no historical novelty is claimed.
"""
from __future__ import annotations

import math
import numpy as np


def _validate_priors(priors) -> np.ndarray:
    p = np.asarray(priors, dtype=float)
    if p.ndim != 1 or len(p) == 0 or np.any(p < 0):
        raise ValueError("priors must be a nonempty nonnegative vector")
    s = float(p.sum())
    if not np.isfinite(s) or not np.isclose(s, 1.0, atol=1e-12):
        raise ValueError("priors must sum to one")
    return p


def total_dimension(dimensions) -> int:
    dims = tuple(int(d) for d in dimensions)
    if not dims or any(d < 1 for d in dims):
        raise ValueError("dimensions must be positive")
    return math.prod(dims)


def success_upper_bound(priors, dimensions=(1,)) -> float:
    p = _validate_priors(priors)
    D = total_dimension(dimensions)
    return min(1.0, D * float(np.max(p)))


def error_lower_bound(priors, dimensions=(1,)) -> float:
    return 1.0 - success_upper_bound(priors, dimensions)


def source_min_entropy(priors) -> float:
    p = _validate_priors(priors)
    return -math.log2(float(np.max(p)))


def postmeasurement_min_entropy_floor(priors, dimensions=(1,)) -> float:
    D = total_dimension(dimensions)
    return max(0.0, source_min_entropy(priors) - math.log2(D))


def uniform_copy_bound(d: int, copies: int, labels: int) -> float:
    if d < 1 or copies < 1 or labels < 1:
        raise ValueError("d, copies, labels must be positive")
    return min(1.0, (d ** copies) / labels)


def minimum_copies_dimension_necessary(d: int, labels: int) -> int:
    """Necessary copy count for perfect uniform-label identification.

    This is only a dimension-capacity necessity, not a sufficiency statement
    for arbitrary record states.
    """
    if d < 1 or labels < 1:
        raise ValueError("d and labels must be positive")
    if labels == 1:
        return 0
    if d == 1:
        return math.inf
    return math.ceil(math.log(labels, d) - 1e-14)


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


def discrimination_success(states, povm, priors) -> float:
    p = _validate_priors(priors)
    if len(states) != len(povm) or len(states) != len(p):
        raise ValueError("states, POVM, and priors must have equal length")
    return float(sum(pi * np.trace(m @ rho).real for pi, m, rho in zip(p, povm, states)))


def saturation_ensemble(D: int, k: int, p_max: float):
    """Construct a family attaining D*p_max when 1/k <= p_max <= 1/D.

    The first D labels use orthogonal basis states and prior p_max. The
    remaining prior mass is distributed evenly over the other labels, whose
    POVM effects are zero. This proves sharpness throughout the nontrivial
    D*p_max <= 1 regime whenever k>D.
    """
    if D < 1 or k <= D:
        raise ValueError("require k>D>=1")
    if p_max < 1.0 / k - 1e-12 or p_max > 1.0 / D + 1e-12:
        raise ValueError("require 1/k <= p_max <= 1/D")
    residual = 1.0 - D * p_max
    tail = residual / (k - D)
    if tail > p_max + 1e-12:
        raise ValueError("infeasible p_max")
    priors = np.array([p_max] * D + [tail] * (k - D), dtype=float)
    states = []
    povm = []
    for i in range(k):
        rho = np.zeros((D, D), dtype=complex)
        rho[i if i < D else 0, i if i < D else 0] = 1.0
        states.append(rho)
        if i < D:
            m = np.zeros((D, D), dtype=complex)
            m[i, i] = 1.0
        else:
            m = np.zeros((D, D), dtype=complex)
        povm.append(m)
    return priors, states, povm


def random_stress(d: int, k: int, trials: int = 300, seed: int = 26090922):
    rng = np.random.default_rng(seed + 1009 * d + k)
    maximum_violation = -float("inf")
    largest_success = 0.0
    for _ in range(trials):
        priors = rng.dirichlet(rng.uniform(0.2, 3.0, size=k))
        states = [random_density_matrix(d, rng) for _ in range(k)]
        povm = random_povm(d, k, rng)
        got = discrimination_success(states, povm, priors)
        bound = success_upper_bound(priors, (d,))
        maximum_violation = max(maximum_violation, got - bound)
        largest_success = max(largest_success, got)
    return {
        "dimension": d,
        "labels": k,
        "trials": trials,
        "largest_random_success": largest_success,
        "maximum_violation": maximum_violation,
    }
