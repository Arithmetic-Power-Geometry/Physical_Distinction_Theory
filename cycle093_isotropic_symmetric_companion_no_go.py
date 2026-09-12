"""Cycle 093: isotropic same-space symmetric companion no-go.

PDT-II target (1): test whether the symmetric companion required by Cycle 092
can live in the same elementary distinction vector space while retaining full
SO(n) isotropy.

The analytic theorem is independent of the numerical regression audit:
for n >= 2, every symmetric bilinear SO(n)-equivariant map
S: R^n x R^n -> R^n is identically zero.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

DEFAULT_DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def pi_rotation(n: int, i: int = 0, j: int = 1) -> np.ndarray:
    """Return a determinant +1 pi rotation flipping coordinate axes i and j."""
    if n < 2:
        raise ValueError("pi_rotation requires n >= 2")
    if i == j or not (0 <= i < n and 0 <= j < n):
        raise ValueError("i and j must be distinct valid coordinates")
    r = np.eye(n)
    r[i, i] = -1.0
    r[j, j] = -1.0
    return r


def random_so(n: int, rng: np.random.Generator) -> np.ndarray:
    """Generate a numerically orthogonal determinant +1 matrix."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return np.ones((1, 1))
    a = rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    s = np.sign(np.diag(r))
    s[s == 0.0] = 1.0
    q = q @ np.diag(s)
    if np.linalg.det(q) < 0.0:
        q[:, 0] *= -1.0
    return q


def fixed_axis_symmetric(x: np.ndarray, y: np.ndarray, u: np.ndarray) -> np.ndarray:
    """A tempting symmetric V-valued candidate S_u(x,y)=<x,y>u."""
    return float(np.dot(x, y)) * u


def vector_equivariance_residual(
    r: np.ndarray, x: np.ndarray, y: np.ndarray, u: np.ndarray
) -> float:
    lhs = fixed_axis_symmetric(r @ x, r @ y, u)
    rhs = r @ fixed_axis_symmetric(x, y, u)
    return float(np.linalg.norm(lhs - rhs))


def scalar_companion(x: np.ndarray, y: np.ndarray) -> float:
    """Canonical scalar-valued symmetric companion: the Euclidean inner product."""
    return float(np.dot(x, y))


def scalar_invariance_residual(r: np.ndarray, x: np.ndarray, y: np.ndarray) -> float:
    return abs(scalar_companion(r @ x, r @ y) - scalar_companion(x, y))


def exact_status(n: int) -> dict[str, Any]:
    """Encode the exact theorem status, not an inference from floating tests."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return {
            "n": 1,
            "same_space_SO_n_symmetric_companion": "NONZERO_ALLOWED",
            "reason": "SO(1) is trivial; S(x,y)=cxy is equivariant.",
        }
    return {
        "n": n,
        "same_space_SO_n_symmetric_companion": "ZERO_ONLY",
        "reason": "stabilizer + pi-rotation argument (n>=3), and -I in SO(2)",
    }


def run_audit(dims: list[int] | None = None, seed: int = 93001, trials: int = 10) -> dict[str, Any]:
    dims = DEFAULT_DIMS if dims is None else dims
    rng = np.random.default_rng(seed)
    rows: list[dict[str, Any]] = []
    max_scalar_residual = 0.0

    for n in dims:
        row = exact_status(n)
        if n == 1:
            row.update(
                {
                    "fixed_axis_candidate_residual": None,
                    "scalar_companion_max_residual": 0.0,
                    "degenerate": True,
                }
            )
            rows.append(row)
            continue

        r = pi_rotation(n)
        u = np.zeros(n)
        u[0] = 1.0
        x = u.copy()
        decisive_residual = vector_equivariance_residual(r, x, x, u)

        scalar_max = 0.0
        for _ in range(trials):
            rr = random_so(n, rng)
            xx = rng.normal(size=n)
            yy = rng.normal(size=n)
            scalar_max = max(scalar_max, scalar_invariance_residual(rr, xx, yy))
        max_scalar_residual = max(max_scalar_residual, scalar_max)

        row.update(
            {
                "fixed_axis_candidate_residual": decisive_residual,
                "scalar_companion_max_residual": scalar_max,
                "degenerate": False,
            }
        )
        rows.append(row)

    return {
        "cycle": 93,
        "target": "PDT-II target (1): PDT-native composition law",
        "theorem": (
            "For n>=2, every symmetric bilinear SO(n)-equivariant map "
            "S:R^n x R^n -> R^n is zero."
        ),
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "smallest_nondegenerate_obstruction": 2,
        "fixed_axis_countercandidate_residual_expected": 2.0,
        "max_scalar_companion_invariance_residual": max_scalar_residual,
        "dims": rows,
        "surviving_route": (
            "A rotationally invariant symmetric companion can be scalar-valued "
            "(<x,y>) or live in an enlarged algebra/codomain; it cannot be a "
            "nonzero same-space vector-valued symmetric product under full SO(n) isotropy."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=93001)
    parser.add_argument("--trials", type=int, default=10)
    args = parser.parse_args()
    result = run_audit(seed=args.seed, trials=args.trials)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output is None:
        print(text)
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
        print(args.output)


if __name__ == "__main__":
    main()
