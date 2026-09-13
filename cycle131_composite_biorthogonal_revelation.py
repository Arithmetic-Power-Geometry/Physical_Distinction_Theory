"""Cycle 131: composite biorthogonal revelation boundary.

Exact claims:
1. If a composite resource norm is quadratically additive on every
   biorthogonal rank-one decomposition and is calibrated on product tensors,
   then it is the Frobenius norm.
2. Local Euclidean revelation + rank-one calibration + local orthogonal
   covariance do not imply that composite revelation axiom. Schatten p norms
   provide counterexamples for p != 2.

Numerical sweeps below are regression evidence only; they are not proofs.
"""
from __future__ import annotations
import math
from typing import Iterable
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
PS = (1.0, 2.0, 4.0, math.inf)
SEED = 131011


def schatten_from_singular_values(s: Iterable[float], p: float) -> float:
    a = np.asarray(list(s), dtype=float)
    if a.size == 0:
        return 0.0
    if math.isinf(p):
        return float(np.max(np.abs(a)))
    return float(np.sum(np.abs(a) ** p) ** (1.0 / p))


def quadratic_revelation_gap(s: Iterable[float], p: float) -> float:
    a = np.asarray(list(s), dtype=float)
    n = schatten_from_singular_values(a, p)
    return float(n * n - np.dot(a, a))


def minimal_witness() -> dict:
    s = np.array([1.0, 1.0])
    return {
        "dimension": 2,
        "matrix": "I_2 = E_11 + E_22",
        "required_squared_resource": 2.0,
        "p1_gap": quadratic_revelation_gap(s, 1.0),
        "p2_gap": quadratic_revelation_gap(s, 2.0),
        "p4_gap": quadratic_revelation_gap(s, 4.0),
        "pinf_gap": quadratic_revelation_gap(s, math.inf),
    }


def run_audit(seed: int = SEED) -> dict:
    rng = np.random.default_rng(seed)
    p_evaluations = p2_failures = rank1_failures = 0
    rank_ge2_non2 = rank_ge2_non2_distinguished = 0
    max_p2_gap = max_svd_residual = 0.0
    svd_cases = 0

    for n in DIMS:
        reps = 80 if n <= 12 else 25
        for rep in range(reps):
            if rep == 0:
                s = np.zeros(n)
            elif rep == 1:
                s = np.zeros(n)
                s[0] = 1.0
            elif rep == 2 and n >= 2:
                s = np.zeros(n)
                s[:2] = 1.0
            else:
                s = rng.exponential(size=n)
                if n > 1 and rep % 7 == 0:
                    k = int(rng.integers(1, n + 1))
                    s[k:] = 0.0

            rhs = float(np.dot(s, s))
            rank = int(np.count_nonzero(s > 1e-14))
            scale = max(1.0, rhs)
            for p in PS:
                gap = quadratic_revelation_gap(s, p)
                p_evaluations += 1
                if p == 2.0:
                    max_p2_gap = max(max_p2_gap, abs(gap))
                    if abs(gap) > 1e-12 * scale:
                        p2_failures += 1
                elif rank >= 2:
                    rank_ge2_non2 += 1
                    if abs(gap) > 1e-12 * scale:
                        rank_ge2_non2_distinguished += 1
                elif abs(gap) > 1e-12 * scale:
                    rank1_failures += 1

            if n <= 12 and rep >= 3:
                u, _ = np.linalg.qr(rng.normal(size=(n, n)))
                v, _ = np.linalg.qr(rng.normal(size=(n, n)))
                a = u @ np.diag(s) @ v.T
                recovered = np.linalg.svd(a, compute_uv=False)
                residual = np.linalg.norm(np.sort(recovered) - np.sort(s))
                residual /= max(1.0, np.linalg.norm(s))
                max_svd_residual = max(max_svd_residual, float(residual))
                svd_cases += 1

    return {
        "seed": seed,
        "dimensions": DIMS,
        "p_values": ["1", "2", "4", "inf"],
        "p_evaluations": p_evaluations,
        "p2_failures": p2_failures,
        "max_abs_p2_gap": max_p2_gap,
        "rank_ge2_non2_cases": rank_ge2_non2,
        "rank_ge2_non2_distinguished": rank_ge2_non2_distinguished,
        "rank_le1_indistinguishability_failures": rank1_failures,
        "svd_reconstruction_cases": svd_cases,
        "max_relative_svd_residual": max_svd_residual,
        "minimal_witness": minimal_witness(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
