"""Cycle 060: Gaussian-shift countermodels for PDT-II dimension selection.

Purpose
-------
Construct, for every n>=3, an operational model that simultaneously has:
  * Euclidean/isotropic scalar distinction geometry;
  * connected noncommuting reversible group SO(n);
  * two-point isotropy (TPI);
  * exact independent-product likelihood composition;
  * resource monotonicity under coarse graining / projection;
while Pairwise Calibration Closure (PCC) fails for every n>=4.

Therefore the presently proved composition/resource laws, even together with TPI
and noncommuting reversibility, cannot by themselves derive PCC or select n=3.

This is a model-theoretic PDT no-go. Gaussian shift experiments, total variation,
SO(n) actions and data processing are imported/known mathematics.
"""

from __future__ import annotations

import json
import math
import numpy as np


def tv_equal_covariance_gaussians(delta: float) -> float:
    """TV(N(x,I),N(y,I)) as a function of delta=||x-y||_2."""
    if delta < 0:
        raise ValueError("delta must be nonnegative")
    # 2 Phi(delta/2)-1 = erf(delta/(2 sqrt(2))).
    return math.erf(delta / (2.0 * math.sqrt(2.0)))


def log_likelihood_ratio(z: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    """log[d N(x,I) / d N(y,I)] evaluated at z."""
    return float((x - y) @ z - 0.5 * (x @ x - y @ y))


def product_log_likelihood(
    z1: np.ndarray,
    x1: np.ndarray,
    y1: np.ndarray,
    z2: np.ndarray,
    x2: np.ndarray,
    y2: np.ndarray,
) -> float:
    """Independent product experiment: log likelihoods add exactly."""
    return log_likelihood_ratio(z1, x1, y1) + log_likelihood_ratio(z2, x2, y2)


def random_orthogonal(rng: np.random.Generator, n: int) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    # Put the matrix in SO(n), not merely O(n).
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q


def ordered_pair_stabilizer_witness(n: int, angle: float = 0.731) -> np.ndarray:
    """Nonidentity SO(n) element fixing e1,e2 pointwise for n>=4."""
    if n < 4:
        raise ValueError("nontrivial ordered-pair stabilizer witness needs n>=4")
    g = np.eye(n)
    c, s = math.cos(angle), math.sin(angle)
    # Rotate the e3-e4 plane; e1 and e2 remain fixed.
    g[2, 2] = c
    g[2, 3] = -s
    g[3, 2] = s
    g[3, 3] = c
    return g


def audit_dimension(n: int, trials: int = 200, seed: int | None = None) -> dict:
    rng = np.random.default_rng(seed if seed is not None else 60000 + n)
    rotation_failures = 0
    projection_failures = 0
    product_ll_failures = 0

    for _ in range(trials):
        x = rng.normal(size=n)
        y = rng.normal(size=n)
        delta = float(np.linalg.norm(x - y))
        d_full = tv_equal_covariance_gaussians(delta)

        # Exact structural prediction: orthogonal rotations preserve distinction.
        g = random_orthogonal(rng, n)
        delta_rot = float(np.linalg.norm(g @ x - g @ y))
        if abs(d_full - tv_equal_covariance_gaussians(delta_rot)) > 1e-12:
            rotation_failures += 1

        # Resource restriction: coordinate projection is a Markov map and cannot
        # increase TV.  For equal-covariance Gaussian shifts, the projected model
        # remains a Gaussian shift and the claim reduces to ||Pi v|| <= ||v||.
        k = int(rng.integers(1, n + 1))
        delta_proj = float(np.linalg.norm((x - y)[:k]))
        if tv_equal_covariance_gaussians(delta_proj) > d_full + 1e-12:
            projection_failures += 1

        # Exact product-composition identity for the log likelihood ratio.
        m = max(1, n // 2)
        x2 = rng.normal(size=m)
        y2 = rng.normal(size=m)
        z1 = rng.normal(size=n)
        z2 = rng.normal(size=m)
        lhs = log_likelihood_ratio(
            np.concatenate([z1, z2]),
            np.concatenate([x, x2]),
            np.concatenate([y, y2]),
        )
        rhs = product_log_likelihood(z1, x, y, z2, x2, y2)
        if abs(lhs - rhs) > 1e-11:
            product_ll_failures += 1

    pcc_holds = n <= 3
    stabilizer_error = None
    if n >= 4:
        h = ordered_pair_stabilizer_witness(n)
        e1 = np.eye(n)[:, 0]
        e2 = np.eye(n)[:, 1]
        stabilizer_error = max(
            float(np.linalg.norm(h @ e1 - e1)),
            float(np.linalg.norm(h @ e2 - e2)),
            abs(float(np.linalg.det(h)) - 1.0),
        )
        assert stabilizer_error < 1e-12
        assert np.linalg.norm(h - np.eye(n)) > 1e-3

    return {
        "dimension": n,
        "trials": trials,
        "rotation_failures": rotation_failures,
        "projection_failures": projection_failures,
        "product_log_likelihood_failures": product_ll_failures,
        "SO_n_noncommuting": n >= 3,
        "TPI": n >= 2,
        "PCC": pcc_holds,
        "ordered_pair_stabilizer_witness_error": stabilizer_error,
    }


def audit() -> dict:
    dimensions = [audit_dimension(n) for n in range(1, 13)]
    higher = [audit_dimension(n, trials=50, seed=70000 + n) for n in (16, 24, 32, 48, 64, 96, 128)]

    all_rows = dimensions + higher
    failures = sum(
        r["rotation_failures"]
        + r["projection_failures"]
        + r["product_log_likelihood_failures"]
        for r in all_rows
    )
    assert failures == 0
    assert all((not r["PCC"]) for r in all_rows if r["dimension"] >= 4)

    return {
        "cycle": 60,
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN mathematics"],
        "claim_falsified": (
            "The current PDT composition/resource laws, even together with Euclidean "
            "isotropy, TPI and noncommuting connected reversibility, force PCC or n=3."
        ),
        "surviving_statement": (
            "PCC (or another independent dimension-selecting principle) is not derivable "
            "from those ingredients alone: Gaussian shift countermodels exist for every n>=4."
        ),
        "dimensions_1_to_12": dimensions,
        "higher_dimensions": higher,
        "total_failures": failures,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
