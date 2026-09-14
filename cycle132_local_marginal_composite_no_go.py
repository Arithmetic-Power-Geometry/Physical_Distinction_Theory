"""Cycle 132: local-marginal revelation does not determine composite resource geometry.

Exact witness family:
    A_n = I_n
    B_n = J_n / sqrt(n)
Both matrices have every row and every column of Euclidean norm one, but they
have different singular spectra for n>1. Therefore local row/column quadratic
revelation profiles do not determine a unitarily invariant composite resource.
"""
from __future__ import annotations

import json
import math
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
PS = (1, 2, 4, np.inf)


def schatten(a: np.ndarray, p: float) -> float:
    s = np.linalg.svd(a, compute_uv=False)
    if np.isinf(p):
        return float(np.max(s))
    return float(np.sum(s ** p) ** (1.0 / p))


def witness(n: int) -> tuple[np.ndarray, np.ndarray]:
    return np.eye(n), np.ones((n, n)) / math.sqrt(n)


def run_audit() -> dict:
    rows = []
    local_failures = 0
    max_local_gap = 0.0
    for n in DIMS:
        a, b = witness(n)
        row_gap = float(np.max(np.abs(np.linalg.norm(a, axis=1) - np.linalg.norm(b, axis=1))))
        col_gap = float(np.max(np.abs(np.linalg.norm(a, axis=0) - np.linalg.norm(b, axis=0))))
        local_gap = max(row_gap, col_gap)
        max_local_gap = max(max_local_gap, local_gap)
        if local_gap > 1e-10:
            local_failures += 1
        values = {}
        for p in PS:
            key = "inf" if np.isinf(p) else str(int(p))
            na, nb = schatten(a, p), schatten(b, p)
            values[key] = {"A": na, "B": nb, "gap_B_minus_A": nb - na}
        rows.append({"n": n, "max_local_row_col_l2_gap": local_gap, "schatten": values})

    nontrivial = [r for r in rows if r["n"] > 1]
    return {
        "cycle": 132,
        "claim": "Local row/column Euclidean revelation profiles do not determine composite unitarily invariant resource geometry.",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "dimensions": DIMS,
        "witness_family": {
            "A_n": "I_n",
            "B_n": "J_n/sqrt(n)",
            "local_profile": "every row and every column has Euclidean norm 1",
            "singular_values_A": "(1,...,1)",
            "singular_values_B": "(sqrt(n),0,...,0)",
        },
        "checks": {
            "total_dimension_p_cases": len(DIMS) * len(PS),
            "local_profile_failures": local_failures,
            "max_local_profile_abs_gap": max_local_gap,
            "p1_distinguishes_for_all_n_gt_1": all(abs(r["schatten"]["1"]["gap_B_minus_A"]) > 1e-10 for r in nontrivial),
            "p2_distinguishes_for_any_n_gt_1": any(abs(r["schatten"]["2"]["gap_B_minus_A"]) > 1e-10 for r in nontrivial),
            "p4_distinguishes_for_all_n_gt_1": all(abs(r["schatten"]["4"]["gap_B_minus_A"]) > 1e-10 for r in nontrivial),
            "pinf_distinguishes_for_all_n_gt_1": all(abs(r["schatten"]["inf"]["gap_B_minus_A"]) > 1e-10 for r in nontrivial),
        },
        "records": rows,
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
