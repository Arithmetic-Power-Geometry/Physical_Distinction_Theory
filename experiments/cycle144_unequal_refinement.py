"""Cycle 144: arbitrary unequal resolved-refinement audit.

Tests the conditional law
    g(r) = sum_i g(r*sqrt(w_i)),  w_i>=0, sum_i w_i=1,
against power laws and a nonseparable deformation that survives every equal split.
"""
from __future__ import annotations

import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 144
EPS = 0.01


def power_resource(r: float, p: float) -> float:
    return float(abs(r) ** p)


def refined_power_resource(r: float, weights: np.ndarray, p: float) -> float:
    weights = np.asarray(weights, dtype=float)
    return float(sum(power_resource(r * np.sqrt(w), p) for w in weights))


def nonseparable_resource_from_q(q: np.ndarray, eps: float = EPS) -> float:
    """Zero-padding-stable, permutation-invariant deformation.

    q_i are nonnegative resolved quadratic channel weights.  The correction
    vanishes for a single active channel and for every equal-amplitude active
    split, but is positive for generic unequal active channels.
    """
    q = np.asarray(q, dtype=float)
    correction = 0.0
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            correction += q[i] * q[j] * (q[i] - q[j]) ** 2
    return float(q.sum() + eps * correction)


def run_audit() -> dict:
    rng = np.random.default_rng(SEED)
    p_values = [0.5, 1.0, 1.5, 2.0, 3.0, 4.0]
    power_failures = {str(p): 0 for p in p_values}
    equal_split_deformation_failures = 0
    unequal_deformation_detections = 0
    quadratic_partition_failures = 0
    max_quadratic_relative_residual = 0.0
    partition_cases = 0

    for n in DIMS:
        for _ in range(30):
            r = float(10 ** rng.uniform(-3, 3))
            equal_weights = np.full(n, 1.0 / n)
            q_equal = r * r * equal_weights
            equal_split_deformation_failures += int(
                abs(nonseparable_resource_from_q(q_equal) - r * r)
                > 1e-9 * max(1.0, r * r)
            )

            if n == 1:
                weights = np.array([1.0])
            else:
                weights = rng.dirichlet(np.ones(n))
            q = r * r * weights

            qsum = float(q.sum())
            rel = abs(qsum - r * r) / max(1.0, r * r)
            max_quadratic_relative_residual = max(max_quadratic_relative_residual, rel)
            quadratic_partition_failures += int(rel > 1e-12)

            if n > 1:
                unequal_deformation_detections += int(
                    abs(nonseparable_resource_from_q(q) - r * r)
                    > 1e-10 * max(1.0, r * r)
                )

            for p in p_values:
                lhs = power_resource(r, p)
                rhs = refined_power_resource(r, weights, p)
                relp = abs(lhs - rhs) / max(1.0, abs(lhs))
                power_failures[str(p)] += int(relp > 1e-10)

            partition_cases += 1

    witness_q = np.array([1.0, 3.0])
    return {
        "cycle": 144,
        "seed": SEED,
        "dimensions": DIMS,
        "partition_cases": partition_cases,
        "power_failures": power_failures,
        "equal_split_deformation_failures": equal_split_deformation_failures,
        "unequal_deformation_detections": unequal_deformation_detections,
        "quadratic_partition_failures": quadratic_partition_failures,
        "max_quadratic_relative_residual": max_quadratic_relative_residual,
        "exact_witness": {
            "q": [1, 3],
            "epsilon": EPS,
            "quadratic_total": 4.0,
            "raw_deformation_correction": 12.0,
            "deformed_total": nonseparable_resource_from_q(witness_q),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2))
