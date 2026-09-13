"""Cycle 129: composite resource-norm underdetermination audit.

Tests the candidate principle that product-state multiplicativity together with
independent local orthogonal covariance uniquely determines a resource norm on
V_A \otimes V_B.  Schatten p norms supply an explicit counterfamily.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
PS = (1, 2, 4, np.inf)
SEED = 129
TOL = 1e-10


def schatten_norm(matrix: np.ndarray, p: float) -> float:
    s = np.linalg.svd(matrix, compute_uv=False)
    if np.isinf(p):
        return float(np.max(s))
    return float(np.sum(s**p) ** (1.0 / p))


def run_audit() -> dict:
    rng = np.random.default_rng(SEED)
    rank_one_checks = rank_one_failures = 0
    invariance_checks = invariance_failures = 0
    max_rank_one_relative_residual = 0.0
    max_invariance_relative_residual = 0.0
    identity_separation = []

    for n in DIMS:
        trials = 10 if n <= 12 else 3
        for _ in range(trials):
            x = rng.normal(size=n)
            y = rng.normal(size=n)
            rank_one = np.outer(x, y)
            expected = float(np.linalg.norm(x) * np.linalg.norm(y))
            for p in PS:
                observed = schatten_norm(rank_one, p)
                residual = abs(observed - expected) / (1.0 + abs(expected))
                rank_one_checks += 1
                rank_one_failures += int(residual > TOL)
                max_rank_one_relative_residual = max(
                    max_rank_one_relative_residual, residual
                )

            matrix = rng.normal(size=(n, n))
            left, _ = np.linalg.qr(rng.normal(size=(n, n)))
            right, _ = np.linalg.qr(rng.normal(size=(n, n)))
            transformed = left @ matrix @ right.T
            for p in PS:
                before = schatten_norm(matrix, p)
                after = schatten_norm(transformed, p)
                residual = abs(before - after) / (1.0 + abs(before))
                invariance_checks += 1
                invariance_failures += int(residual > TOL)
                max_invariance_relative_residual = max(
                    max_invariance_relative_residual, residual
                )

        identity_values = {
            "p1": float(n),
            "p2": float(np.sqrt(n)),
            "p4": float(n ** 0.25),
            "pinf": 1.0,
        }
        identity_separation.append(
            {
                "n": n,
                "identity_schatten_norms": identity_values,
                "all_distinct_for_n_gt_1": n == 1
                or len({round(v, 14) for v in identity_values.values()}) == 4,
            }
        )

    return {
        "cycle": 129,
        "seed": SEED,
        "dimensions": DIMS,
        "p_values": [1, 2, 4, "inf"],
        "rank_one_checks": rank_one_checks,
        "rank_one_failures": rank_one_failures,
        "max_rank_one_relative_residual": max_rank_one_relative_residual,
        "local_orthogonal_invariance_checks": invariance_checks,
        "local_orthogonal_invariance_failures": invariance_failures,
        "max_invariance_relative_residual": max_invariance_relative_residual,
        "smallest_decisive_dimension": 2,
        "n2_identity_values": {
            "nuclear_p1": 2.0,
            "frobenius_p2": float(np.sqrt(2.0)),
            "schatten_p4": float(2.0 ** 0.25),
            "operator_pinf": 1.0,
        },
        "identity_separation": identity_separation,
        "classification": [
            "PROVED",
            "FALSIFIED",
            "IMPORTED/KNOWN",
            "NUMERICALLY SUPPORTED",
            "OPEN",
        ],
        "breakthrough_candidate": False,
    }


if __name__ == "__main__":
    result = run_audit()
    out = Path("results/cycle129_composite_resource_norm_underdetermination.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
