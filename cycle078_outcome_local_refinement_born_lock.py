"""Cycle 078: outcome-local same-input refinement lock.

Status
------
PROVED / FALSIFIED / NUMERICALLY SUPPORTED / IMPORTED-KNOWN BOUNDARY.

Theorem (restricted but broad no-go).
Let q_i = Tr(rho E_i) be the fixed QM weights for an unchanged microscopic
state/effect/resource input. Suppose a candidate same-input law has the
outcome-local normalized-score form

    P_i = f(q_i) / sum_j f(q_j),

where f:[0,1] -> [0,infinity), f(0)=0, and f(x)>0 for x>0. If arbitrary
classical splitting of one outcome q=x+y into labelled sub-outcomes x,y,
followed by forgetting the label, must leave the coarse event probability
unchanged, then

    f(x+y)=f(x)+f(y)  for x,y>=0, x+y<=1.

Nonnegativity makes f monotone. Additivity plus monotonicity on [0,1] gives
f(x)=c*x. The normalization cancels c, hence P_i=q_i exactly.

Thus no genuinely nonlinear outcome-local reweighting can provide a defensible
same-input PDT-vs-QM probability deviation while retaining arbitrary classical
refinement invariance. Context-dependent, resource-dependent, or otherwise
non-outcome-local laws are outside this theorem and remain separate targets.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Callable, Iterable

import numpy as np

Score = Callable[[float], float]


def normalized_score(weights: Iterable[float], score: Score) -> np.ndarray:
    w = np.asarray(list(weights), dtype=float)
    if w.ndim != 1 or w.size == 0 or np.any(w < -1e-15):
        raise ValueError("weights must be a nonempty nonnegative vector")
    w = np.clip(w, 0.0, None)
    vals = np.asarray([float(score(float(x))) for x in w], dtype=float)
    if np.any(vals < -1e-15) or not np.all(np.isfinite(vals)):
        raise ValueError("score must be finite and nonnegative on supplied weights")
    vals = np.clip(vals, 0.0, None)
    z = float(vals.sum())
    if z <= 0.0:
        raise ValueError("score normalization must be positive")
    return vals / z


def split_weight(weights: Iterable[float], index: int, t: float) -> np.ndarray:
    w = np.asarray(list(weights), dtype=float)
    if not (0.0 < t < 1.0):
        raise ValueError("t must lie strictly between 0 and 1")
    if index < 0 or index >= w.size:
        raise IndexError(index)
    q = float(w[index])
    return np.concatenate([w[:index], [t * q, (1.0 - t) * q], w[index + 1 :]])


def refinement_defect(weights: Iterable[float], index: int, t: float, score: Score) -> float:
    w = np.asarray(list(weights), dtype=float)
    before = float(normalized_score(w, score)[index])
    wr = split_weight(w, index, t)
    pr = normalized_score(wr, score)
    after = float(pr[index] + pr[index + 1])
    return after - before


def additivity_defect(x: float, y: float, score: Score) -> float:
    if x < 0 or y < 0 or x + y > 1 + 1e-15:
        raise ValueError("require x,y>=0 and x+y<=1")
    return float(score(x + y) - score(x) - score(y))


def linear_score(x: float) -> float:
    return x


def square_score(x: float) -> float:
    return x * x


def sqrt_score(x: float) -> float:
    return math.sqrt(x)


def expm1_score(x: float) -> float:
    return math.expm1(x)


def quadratic_perturbation(x: float) -> float:
    return x + 0.5 * x * (1.0 - x)


def exact_qubit_witness() -> dict:
    # q=(3/4,1/4), f(q)=q^2. Splitting the first event in half is merely a
    # classical relabelling/refinement. The coarse candidate probability moves
    # from 9/10 to 9/11, reproducing Cycle 077 as one member of the general no-go.
    q = np.array([3.0 / 4.0, 1.0 / 4.0])
    before = float(normalized_score(q, square_score)[0])
    qr = split_weight(q, 0, 0.5)
    pr = normalized_score(qr, square_score)
    after = float(pr[0] + pr[1])
    return {
        "dimension": 2,
        "score": "f(q)=q^2",
        "qm_coarse_weight": "3/4",
        "candidate_before": before,
        "candidate_after_recoarse": after,
        "exact_before": "9/10",
        "exact_after": "9/11",
        "refinement_defect": after - before,
        "f_additivity_witness": "f(3/8)+f(3/8) != f(3/4)",
    }


def stress(seed: int = 78) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    scores: dict[str, Score] = {
        "linear": linear_score,
        "square": square_score,
        "sqrt": sqrt_score,
        "expm1": expm1_score,
        "quadratic_perturbation": quadratic_perturbation,
    }
    strict_shifts = {name: 0 for name in scores if name != "linear"}
    max_linear_error = 0.0
    linear_failures = 0
    random_cases = 0
    for d in dims:
        # d=1 is retained as an edge case: generalized/classically split
        # outcomes still form a probability simplex even though the Hilbert
        # state space itself is degenerate.
        outcomes = max(2, min(d + 1, 13))
        for _ in range(20):
            raw = rng.random(outcomes) + 1e-12
            q = raw / raw.sum()
            idx = int(rng.integers(0, outcomes))
            t = float(rng.uniform(0.05, 0.95))
            random_cases += 1
            for name, score in scores.items():
                err = abs(refinement_defect(q, idx, t, score))
                if name == "linear":
                    max_linear_error = max(max_linear_error, err)
                    linear_failures += int(err > 1e-12)
                else:
                    strict_shifts[name] += int(err > 1e-12)
    return {
        "dimensions": dims,
        "random_cases": random_cases,
        "scores": list(scores),
        "linear_failures": linear_failures,
        "max_linear_refinement_error": max_linear_error,
        "nonlinear_strict_shifts": strict_shifts,
        "all_sampled_nonlinear_scores_shifted_in_every_random_case": all(
            v == random_cases for v in strict_shifts.values()
        ),
        "scope_warning": "The random family audit is regression evidence only; the theorem is analytic and applies to any score satisfying its hypotheses.",
        "classification": [
            "PROVED",
            "FALSIFIED",
            "NUMERICALLY SUPPORTED",
            "IMPORTED/KNOWN BOUNDARY",
        ],
        "breakthrough_candidate": False,
    }


def write_results(path: str = "results/cycle078_outcome_local_refinement_born_lock.json") -> dict:
    result = {
        "theorem": {
            "hypotheses": [
                "same microscopic q_i=Tr(rho E_i)",
                "outcome-local normalized score P_i=f(q_i)/sum_j f(q_j)",
                "f(0)=0 and f(x)>0 for x>0",
                "arbitrary classical split/recoarse invariance",
            ],
            "conclusion": "f(x)=c*x and therefore P_i=q_i",
            "status": "PROVED",
            "novelty": "IMPORTED/KNOWN mathematical boundary; not claimed novel",
        },
        "exact_witness": exact_qubit_witness(),
        "stress": stress(),
        "surviving_loopholes": [
            "context-dependent laws",
            "resource-dependent laws not reducible to q_i alone",
            "nonlocal/composite operational laws",
            "modified state/effect dynamics (not same microscopic input)",
        ],
    }
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(write_results(), indent=2))
