"""Cycle 094: scalar/unit augmentation associativity audit.

Tests the minimal isotropic unital ansatz on A = R ⊕ V:
    (a,x) * (b,y) = (ab + alpha <x,y>,
                     a y + b x + beta cross(x,y))
where the cross term is available only in V=R^3 under the SO(3) route.

Exact facts audited:
1) With beta=0 and alpha != 0, associativity fails for every dim(V)>=2.
2) In dim(V)=3, associativity holds iff alpha = -beta^2.
The second condition is the quaternion coefficient relation up to rescaling.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def cross3(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.cross(x, y)


def mul(a, b, alpha=1.0, beta=0.0):
    """Product on R ⊕ R^n. beta must be zero unless n=3."""
    sa, x = a
    sb, y = b
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.shape != y.shape:
        raise ValueError("dimension mismatch")
    n = x.size
    if beta != 0.0 and n != 3:
        raise ValueError("SO(n)-equivariant alternating vector term is only supplied for n=3")
    v = sa * y + sb * x
    if n == 3 and beta != 0.0:
        v = v + beta * cross3(x, y)
    return float(sa * sb + alpha * np.dot(x, y)), v


def assoc(a, b, c, alpha=1.0, beta=0.0):
    left = mul(mul(a, b, alpha, beta), c, alpha, beta)
    right = mul(a, mul(b, c, alpha, beta), alpha, beta)
    return left[0] - right[0], left[1] - right[1]


def witness_residual(n: int, alpha: float = 1.0) -> float:
    if n < 2:
        return 0.0
    e0 = np.zeros(n); e0[0] = 1.0
    e1 = np.zeros(n); e1[1] = 1.0
    ds, dv = assoc((0.0, e0), (0.0, e0), (0.0, e1), alpha=alpha, beta=0.0)
    return float(np.sqrt(ds * ds + np.dot(dv, dv)))


def random_assoc_max(alpha: float, beta: float, trials: int = 1000, seed: int = 9403) -> float:
    rng = np.random.default_rng(seed)
    m = 0.0
    for _ in range(trials):
        elems = []
        for _ in range(3):
            elems.append((float(rng.normal()), rng.normal(size=3)))
        ds, dv = assoc(*elems, alpha=alpha, beta=beta)
        m = max(m, float(np.sqrt(ds * ds + np.dot(dv, dv))))
    return m


def coefficient_scan():
    pairs = [
        (-1.0, 1.0),
        (-4.0, 2.0),
        (-0.25, 0.5),
        (0.0, 0.0),
        (1.0, 0.0),
        (-1.0, 0.5),
        (-1.0, 1.25),
    ]
    return [
        {
            "alpha": a,
            "beta": b,
            "condition_abs": abs(a + b * b),
            "random_assoc_max": random_assoc_max(a, b),
            "expected_associative": abs(a + b * b) < 1e-14,
        }
        for a, b in pairs
    ]


def generate():
    dimension_rows = []
    for n in DIMS:
        dimension_rows.append({
            "n": n,
            "metric_only_witness_residual_alpha_1": witness_residual(n, 1.0),
            "status": "ASSOCIATIVE_1D_EXCEPTION" if n == 1 else "NONASSOCIATIVE_FOR_NONZERO_ALPHA",
        })

    out = {
        "cycle": 94,
        "target": "PDT-II target (1): minimal scalar/unit augmentation",
        "classification": [
            "PROVED",
            "FALSIFIED",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
            "OPEN",
        ],
        "breakthrough_candidate": False,
        "exact_results": {
            "metric_only": (
                "For A=R⊕V with (a,x)*(b,y)=(ab+alpha<x,y>, ay+bx), "
                "dim(V)>=2 and alpha!=0 imply nonassociativity."
            ),
            "three_dimensional_repair": (
                "For A=R⊕R^3 with vector term beta x×y, associativity holds "
                "iff alpha=-beta^2. For beta!=0 this is quaternion multiplication "
                "up to a scaling/sign convention."
            ),
            "smallest_decisive_dimension": 2,
            "smallest_witness": "x=y=e1, z=e2 gives associator vector alpha*e2",
        },
        "dimension_audit": dimension_rows,
        "coefficient_scan_n3": coefficient_scan(),
        "interpretation": (
            "The scalar/unit enlargement surviving Cycle 093 is insufficient by itself "
            "if associative grouping is required. A nonzero metric scalar coupling needs "
            "an antisymmetric vector term; under the current full SO(n) route that term is "
            "available only at n=3, where associativity fixes alpha=-beta^2. This is a "
            "conditional known quaternion boundary, not PDT novelty."
        ),
    }
    return out


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle094_scalar_unit_associativity.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
