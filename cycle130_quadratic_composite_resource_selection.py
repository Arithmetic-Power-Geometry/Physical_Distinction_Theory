"""Cycle 130: quadratic composite-resource selection.

Exact theorem audited here:
On M_n(R), a norm N that (i) satisfies the parallelogram law,
(ii) is invariant under independent left/right orthogonal actions, and
(iii) is normalized on simple tensors N(x y^T)=||x||_2 ||y||_2,
is uniquely the Frobenius norm.

The proof is elementary: the parallelogram law gives an inner product by
Jordan-von Neumann. Row/column sign flips force distinct matrix units E_ij
to be orthogonal; row/column permutations force equal squared lengths; and
simple-tensor normalization fixes ||E_ij||=1. Hence the induced inner product
is the Frobenius inner product.

Numerics are regression evidence only; the theorem is exact.
"""
from __future__ import annotations

import json
import math
import numpy as np


def schatten_norm(a: np.ndarray, p: float) -> float:
    s = np.linalg.svd(a, compute_uv=False)
    if math.isinf(p):
        return float(np.max(s))
    return float(np.linalg.norm(s, ord=p))


def parallelogram_gap(a: np.ndarray, b: np.ndarray, p: float) -> float:
    lhs = schatten_norm(a + b, p) ** 2 + schatten_norm(a - b, p) ** 2
    rhs = 2.0 * schatten_norm(a, p) ** 2 + 2.0 * schatten_norm(b, p) ** 2
    return float(lhs - rhs)


def run_audit(seed: int = 130) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    ps = [1.0, 2.0, 4.0, math.inf]

    witness = {}
    for p in ps:
        a = np.zeros((2, 2)); a[0, 0] = 1.0
        b = np.zeros((2, 2)); b[1, 1] = 1.0
        witness[str(p)] = parallelogram_gap(a, b, p)

    frob_failures = 0
    covariance_failures = 0
    max_frob_gap = 0.0
    max_cov_err = 0.0
    cases = 0

    for n in dims:
        reps = 60 if n <= 12 else 20
        for _ in range(reps):
            a = rng.normal(size=(n, n))
            b = rng.normal(size=(n, n))
            gap = abs(parallelogram_gap(a, b, 2.0))
            scale = max(1.0, np.linalg.norm(a, 'fro')**2 + np.linalg.norm(b, 'fro')**2)
            rel_gap = gap / scale
            max_frob_gap = max(max_frob_gap, rel_gap)
            if rel_gap > 1e-10:
                frob_failures += 1

            # local orthogonal covariance of the selected norm
            q1, _ = np.linalg.qr(rng.normal(size=(n, n)))
            q2, _ = np.linalg.qr(rng.normal(size=(n, n)))
            left = np.linalg.norm(q1 @ a @ q2.T, 'fro')
            right = np.linalg.norm(a, 'fro')
            err = abs(left - right) / max(1.0, right)
            max_cov_err = max(max_cov_err, err)
            if err > 1e-10:
                covariance_failures += 1
            cases += 1

    return {
        "cycle": 130,
        "classification": [
            "PROVED",
            "CONDITIONAL",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
            "FALSIFIED(non-Hilbert Schatten alternatives under parallelogram law)",
            "OPEN(PDT-native derivation of the composite parallelogram law)",
        ],
        "breakthrough_candidate": False,
        "dimensions": dims,
        "random_cases": cases,
        "frobenius_parallelogram_failures": frob_failures,
        "frobenius_covariance_failures": covariance_failures,
        "max_relative_parallelogram_gap": max_frob_gap,
        "max_relative_covariance_error": max_cov_err,
        "n2_exact_witness_gaps": witness,
        "theorem": "parallelogram + O(n)xO(n) covariance + simple-tensor normalization uniquely selects Frobenius norm on M_n(R)",
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
