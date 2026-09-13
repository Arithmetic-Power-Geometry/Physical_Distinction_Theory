"""Cycle 125: Hurwitz norm-composition no-go for a PDT n=3 route.

This module does not prove Hurwitz's theorem. It records the theorem's
consequence for PDT and provides deterministic regression checks on the
standard real composition algebras R, C, H, O.

Hypothesis under test:
    There exists a finite-dimensional real unital bilinear product * on V
    with a positive-definite Euclidean norm satisfying
        ||x*y|| = ||x|| ||y||  for all x,y.

Known Hurwitz theorem consequence:
    dim(V) is in {1,2,4,8}.
Therefore this hypothesis cannot be a non-circular route to dim(V)=3;
it actually excludes n=3.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import numpy as np

ALLOWED_HURWITZ_DIMS = (1, 2, 4, 8)
AUDIT_DIMS = tuple(range(1, 13)) + (16, 24, 32, 48, 64, 96, 128)


def cd_conj(x: np.ndarray) -> np.ndarray:
    """Cayley-Dickson conjugation in dimensions 1,2,4,8."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or len(x) == 0:
        raise ValueError("x must be a nonempty one-dimensional vector")
    if len(x) == 1:
        return x.copy()
    return np.concatenate(([x[0]], -x[1:]))


def cd_mul(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Standard Cayley-Dickson multiplication through octonions."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y):
        raise ValueError("x and y must be same-length one-dimensional vectors")
    n = len(x)
    if n not in ALLOWED_HURWITZ_DIMS:
        raise ValueError("implemented only for dimensions 1,2,4,8")
    if n == 1:
        return x * y
    h = n // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    left = cd_mul(a, c) - cd_mul(cd_conj(d), b)
    right = cd_mul(d, a) + cd_mul(b, cd_conj(c))
    return np.concatenate((left, right))


def norm2(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    return float(np.dot(x, x))


def unit(n: int) -> np.ndarray:
    e = np.zeros(n, dtype=float)
    e[0] = 1.0
    return e


def basis_audit(n: int) -> Dict[str, float | int]:
    """Exact-integer basis audit of unit and squared-norm multiplicativity."""
    eye = np.eye(n, dtype=float)
    unit_failures = 0
    norm_failures = 0
    checks = 0
    one = unit(n)
    for i in range(n):
        if not np.array_equal(cd_mul(one, eye[i]), eye[i]):
            unit_failures += 1
        if not np.array_equal(cd_mul(eye[i], one), eye[i]):
            unit_failures += 1
        for j in range(n):
            z = cd_mul(eye[i], eye[j])
            checks += 1
            if norm2(z) != 1.0:
                norm_failures += 1
    return {
        "dimension": n,
        "basis_product_checks": checks,
        "unit_failures": unit_failures,
        "basis_norm_failures": norm_failures,
    }


def random_norm_audit(n: int, trials: int = 500, seed: int = 0) -> Dict[str, float | int]:
    rng = np.random.default_rng(seed)
    failures = 0
    max_relative_error = 0.0
    for _ in range(trials):
        x = rng.normal(size=n)
        y = rng.normal(size=n)
        lhs = norm2(cd_mul(x, y))
        rhs = norm2(x) * norm2(y)
        scale = max(1.0, abs(rhs))
        rel = abs(lhs - rhs) / scale
        max_relative_error = max(max_relative_error, rel)
        if rel > 1e-12:
            failures += 1
    return {
        "dimension": n,
        "trials": trials,
        "failures_at_1e-12": failures,
        "max_relative_error": max_relative_error,
    }


def theorem_dimension_audit() -> List[Dict[str, object]]:
    """Record the exact Hurwitz dimension filter over requested audit dimensions."""
    return [
        {
            "dimension": n,
            "compatible_with_positive_definite_unital_bilinear_norm_composition": n in ALLOWED_HURWITZ_DIMS,
            "n3_selected": False,
        }
        for n in AUDIT_DIMS
    ]


def run_audit() -> Dict[str, object]:
    constructions = []
    for n in ALLOWED_HURWITZ_DIMS:
        constructions.append(
            {
                "basis": basis_audit(n),
                "random": random_norm_audit(n, trials=500, seed=125000 + n),
            }
        )
    return {
        "cycle": 125,
        "candidate": "unital bilinear positive-definite norm-multiplicative same-sector composition",
        "status": ["FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "known_theorem": "Hurwitz composition-algebra theorem",
        "theorem_consequence": "finite-dimensional real positive-definite unital composition algebras have dimensions 1,2,4,8; n=3 is excluded",
        "allowed_dimensions": list(ALLOWED_HURWITZ_DIMS),
        "dimension_audit": theorem_dimension_audit(),
        "explicit_construction_audits": constructions,
        "smallest_counterdirection": {
            "dimension": 1,
            "algebra": "R",
            "reason": "all candidate axioms already hold, so they do not select n=3",
        },
        "pdt_boundary": "Do not add exact norm multiplicativity plus a unit as an n=3 selector. The surviving SO(n)-equivariant bilinear route must remain non-unital/area-like unless a different PDT-native principle is derived.",
        "breakthrough_candidate": False,
    }


def main() -> None:
    result = run_audit()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
