"""Cycle 077: same-input power-rule deviation and refinement no-go.

Status:
- FALSIFIED as a PDT replacement probability law for every alpha != 1 if
  operationally equivalent outcome refinements/coarse-grainings must agree.
- PROVED: within the normalized power family p_i \propto q_i**alpha, refinement
  consistency uniquely selects alpha=1 (apart from degenerate zero/one-event
  cases).

Here q_i = Tr(rho E_i) are the ordinary microscopic quantum weights for a fixed
state rho and a fixed POVM/resource window.  The candidate is intentionally
attacked rather than promoted: it gives P_PDT != P_QM on the same input, but
fails a basic operational equivalence under classical splitting of one outcome.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np


def normalized_power(weights: Iterable[float], alpha: float) -> np.ndarray:
    w = np.asarray(list(weights), dtype=float)
    if w.ndim != 1 or w.size == 0 or np.any(w < -1e-15):
        raise ValueError("weights must be a nonempty nonnegative vector")
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    w = np.clip(w, 0.0, None)
    z = float(np.sum(w ** alpha))
    if z <= 0:
        raise ValueError("at least one weight must be positive")
    return (w ** alpha) / z


def split_weight(weights: Iterable[float], index: int, t: float) -> np.ndarray:
    w = np.asarray(list(weights), dtype=float)
    if not (0.0 < t < 1.0):
        raise ValueError("t must lie strictly between 0 and 1")
    if index < 0 or index >= w.size:
        raise IndexError(index)
    q = float(w[index])
    return np.concatenate([w[:index], [t * q, (1.0 - t) * q], w[index + 1 :]])


def coarse_event_probability(weights: Iterable[float], alpha: float, index: int) -> float:
    return float(normalized_power(weights, alpha)[index])


def refined_coarse_probability(weights: Iterable[float], alpha: float, index: int, t: float) -> float:
    wr = split_weight(weights, index, t)
    pr = normalized_power(wr, alpha)
    return float(pr[index] + pr[index + 1])


def analytic_split_factor(alpha: float, t: float) -> float:
    return float(t ** alpha + (1.0 - t) ** alpha)


def exact_qubit_witness() -> dict:
    # Same microscopic input: rho=diag(3/4,1/4), Z-basis projective measurement.
    # QM weights q=(3/4,1/4).  Alpha=2 gives (9/10,1/10).
    # Split the first outcome into two classically labelled half-effects:
    # q'=(3/8,3/8,1/4). The two split probabilities sum to 9/11, not 9/10.
    q = np.array([3.0 / 4.0, 1.0 / 4.0])
    coarse = normalized_power(q, 2.0)
    refined = normalized_power(split_weight(q, 0, 0.5), 2.0)
    return {
        "dimension": 2,
        "alpha": 2.0,
        "qm_first_event": 0.75,
        "candidate_first_event_before_split": float(coarse[0]),
        "candidate_first_event_after_split_and_recoarse": float(refined[0] + refined[1]),
        "exact_before": "9/10",
        "exact_after": "9/11",
        "absolute_context_shift": float(abs(coarse[0] - (refined[0] + refined[1]))),
        "same_physical_coarse_event": True,
        "refinement_consistent": False,
    }


def stress(seed: int = 77) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    alphas = [0.5, 0.75, 1.0, 1.5, 2.0, 3.0]
    rows = []
    violations_nonunit = 0
    alpha1_failures = 0
    max_alpha1_error = 0.0
    for d in dims:
        outcomes = max(2, min(d + 1, 13))
        for _ in range(20):
            raw = rng.random(outcomes)
            q = raw / raw.sum()
            idx = int(rng.integers(0, outcomes))
            t = float(rng.uniform(0.05, 0.95))
            for alpha in alphas:
                before = coarse_event_probability(q, alpha, idx)
                after = refined_coarse_probability(q, alpha, idx, t)
                err = abs(before - after)
                if alpha == 1.0:
                    max_alpha1_error = max(max_alpha1_error, err)
                    alpha1_failures += int(err > 1e-12)
                else:
                    # With positive random weights and 0<t<1, the theorem predicts
                    # a strict shift for alpha != 1.
                    violations_nonunit += int(err > 1e-12)
                rows.append((d, alpha, err))
    expected_nonunit = len(dims) * 20 * (len(alphas) - 1)
    return {
        "dimensions": dims,
        "random_cases_per_dimension": 20,
        "alphas": alphas,
        "alpha1_failures": alpha1_failures,
        "max_alpha1_refinement_error": max_alpha1_error,
        "nonunit_alpha_strict_shifts": violations_nonunit,
        "expected_nonunit_alpha_strict_shifts": expected_nonunit,
        "all_nonunit_candidates_falsified_in_random_stress": violations_nonunit == expected_nonunit,
        "classification": ["PROVED", "FALSIFIED", "NUMERICALLY SUPPORTED", "IMPORTED/KNOWN BOUNDARY"],
    }


def write_results(path: str = "results/cycle077_power_rule_refinement_no_go.json") -> dict:
    result = {"exact_witness": exact_qubit_witness(), "stress": stress()}
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(write_results(), indent=2))
