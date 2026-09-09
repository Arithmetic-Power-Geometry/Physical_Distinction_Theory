"""Cycle 023: postselection-accounted exact-label discrimination bound.

Let labels i have priors p_i and quantum record states rho_i on a D-dimensional
Hilbert space. A postselected exact-label procedure is described by conclusive
POVM effects N_i >= 0 with sum_i N_i <= I; the remaining effect is inconclusive.
Then

    P(retain AND correct) <= min(1, D * p_max).

If s=P(retain)>0, the conditional retained-branch accuracy obeys

    P(correct | retain) <= min(1, D * p_max / s).

Thus postselection can increase conditional accuracy only by paying in retention
probability. This is standard quantum state-discrimination mathematics with
inconclusive outcomes, used here as a PDT same-input resource accounting audit.
"""
from __future__ import annotations

import numpy as np


def _validate_priors(priors) -> np.ndarray:
    p = np.asarray(priors, dtype=float)
    if p.ndim != 1 or len(p) == 0 or np.any(p < 0):
        raise ValueError("priors must be a nonempty nonnegative vector")
    if not np.isclose(float(p.sum()), 1.0, atol=1e-12):
        raise ValueError("priors must sum to one")
    return p


def postselected_joint_correct_bound(priors, dimension: int) -> float:
    p = _validate_priors(priors)
    if dimension < 1:
        raise ValueError("dimension must be positive")
    return min(1.0, dimension * float(np.max(p)))


def postselected_conditional_accuracy_bound(priors, dimension: int, retention: float) -> float:
    if retention <= 0 or retention > 1:
        raise ValueError("retention must lie in (0,1]")
    return min(1.0, postselected_joint_correct_bound(priors, dimension) / retention)


def uniform_postselection_bound(dimension: int, labels: int, retention: float) -> float:
    if labels < 1:
        raise ValueError("labels must be positive")
    return min(1.0, dimension / (labels * retention))


def random_density_matrix(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def random_povm(d: int, outcomes: int, rng: np.random.Generator) -> list[np.ndarray]:
    """Generate a normalized POVM with the last outcome usable as inconclusive."""
    if d < 1 or outcomes < 2:
        raise ValueError("require d>=1 and outcomes>=2")
    raw = []
    total = np.zeros((d, d), dtype=complex)
    for _ in range(outcomes):
        a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        b = a @ a.conj().T
        raw.append(b)
        total += b
    vals, vecs = np.linalg.eigh(total)
    inv_sqrt = (vecs * (1.0 / np.sqrt(np.maximum(vals, 1e-15)))) @ vecs.conj().T
    return [inv_sqrt @ b @ inv_sqrt for b in raw]


def evaluate_postselected_discrimination(states, conclusive_effects, inconclusive_effect, priors):
    p = _validate_priors(priors)
    if len(states) != len(p) or len(conclusive_effects) != len(p):
        raise ValueError("states, effects, and priors must have equal label count")
    d = states[0].shape[0]
    eye = np.eye(d, dtype=complex)
    joint_correct = float(sum(pi * np.trace(m @ rho).real for pi, m, rho in zip(p, conclusive_effects, states)))
    retention = float(sum(pi * np.trace((eye - inconclusive_effect) @ rho).real for pi, rho in zip(p, states)))
    conditional = joint_correct / retention if retention > 1e-15 else float("nan")
    return joint_correct, retention, conditional


def random_stress(d: int, k: int, trials: int = 300, seed: int = 26090923):
    rng = np.random.default_rng(seed + d)
    max_joint_excess = -np.inf
    max_conditional = 0.0
    min_retention = 1.0
    for _ in range(trials):
        priors = rng.dirichlet(np.ones(k))
        states = [random_density_matrix(d, rng) for _ in range(k)]
        povm = random_povm(d, k + 1, rng)
        joint, retention, conditional = evaluate_postselected_discrimination(
            states, povm[:k], povm[k], priors
        )
        bound = postselected_joint_correct_bound(priors, d)
        max_joint_excess = max(max_joint_excess, joint - bound)
        max_conditional = max(max_conditional, conditional)
        min_retention = min(min_retention, retention)
    return {
        "d": d,
        "k": k,
        "trials": trials,
        "max_joint_excess": float(max_joint_excess),
        "max_conditional_accuracy": float(max_conditional),
        "min_retention": float(min_retention),
    }


def perfect_postselection_witness(labels: int, dimension: int = 2):
    """Construct a uniform ensemble with perfect retained accuracy at low retention.

    Label 0 uses |0>; all remaining labels use |1>. The only conclusive effect is
    |0><0| assigned to label 0; everything else is inconclusive. Hence retention
    is 1/labels and conditional accuracy is exactly one.
    """
    if dimension < 2 or labels < 2:
        raise ValueError("require dimension>=2 and labels>=2")
    priors = np.full(labels, 1.0 / labels)
    states = []
    effects = []
    for i in range(labels):
        rho = np.zeros((dimension, dimension), dtype=complex)
        rho[0 if i == 0 else 1, 0 if i == 0 else 1] = 1.0
        states.append(rho)
        m = np.zeros((dimension, dimension), dtype=complex)
        if i == 0:
            m[0, 0] = 1.0
        effects.append(m)
    inconclusive = np.eye(dimension, dtype=complex)
    inconclusive[0, 0] = 0.0
    return priors, states, effects, inconclusive
