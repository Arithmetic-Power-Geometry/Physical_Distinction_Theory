"""Cycle 143: audit equal-amplitude split conservation versus unequal composition."""
from __future__ import annotations
import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
EPSILONS = [0.0, 0.01, 0.1, 1.0]


def variance_term(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    m = x.size
    if m <= 1:
        return 0.0
    q = x * x
    return float(np.sum(q * q) - np.sum(q) ** 2 / m)


def resource(x: np.ndarray, epsilon: float) -> float:
    x = np.asarray(x, dtype=float)
    return float(np.dot(x, x) + epsilon * variance_term(x))


def equal_split(r: float, k: int) -> np.ndarray:
    return np.full(k, r / np.sqrt(k), dtype=float)


def audit(seed: int = 143) -> dict:
    rng = np.random.default_rng(seed)
    equal_failures = 0
    unequal_differences = 0
    max_equal_residual = 0.0
    cases = 0
    for k in DIMS:
        for _ in range(40):
            r = float(10 ** rng.uniform(-6, 6))
            for eps in EPSILONS:
                got = resource(equal_split(r, k), eps)
                target = r * r
                residual = abs(got - target) / max(1.0, abs(target))
                max_equal_residual = max(max_equal_residual, residual)
                equal_failures += int(residual > 1e-10)
                cases += 1
        if k >= 2:
            x = rng.uniform(0.1, 3.0, size=k)
            baseline = resource(x, 0.0)
            for eps in EPSILONS[1:]:
                unequal_differences += int(abs(resource(x, eps) - baseline) > 1e-10)
    witness = np.array([1.0, 2.0])
    return {
        "cycle": 143,
        "dimensions": DIMS,
        "equal_split_cases": cases,
        "equal_split_failures": equal_failures,
        "max_equal_split_relative_residual": max_equal_residual,
        "unequal_random_differences": unequal_differences,
        "exact_witness": {
            "x": [1, 2],
            "R_epsilon_0": resource(witness, 0.0),
            "variance_term": variance_term(witness),
            "R_epsilon_1": resource(witness, 1.0),
        },
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
