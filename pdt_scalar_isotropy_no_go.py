"""Counterexamples showing scalar metric isotropy does not imply two-point isotropy.

For the natural real action of SU(m) on C^m ~= R^(2m), all group elements
preserve the Euclidean norm and hence every scalar Euclidean distance.  The
action is sphere-transitive.  Nevertheless, for m>=2 it is not two-point
isotropic with respect to the real Euclidean angle.

Fix x=e1.  Every element of Stab(x) also preserves the complex inner product
<x, .>.  Choose
    y=e2,
    z=i*a*e1 + sqrt(1-a^2)*e2,  0<a<1.
Then ||y||=||z||=1 and Re<x,y>=Re<x,z>=0, so y,z have the same real angle
(and same Euclidean distance) from x.  But <x,y>=0 whereas <x,z>=i*a, so no
g in Stab(x) can send y to z.

This kills the derivation route
    scalar distinction isotropy + sphere transitivity => TPI.
It is a mathematical no-go, not a novelty claim.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Iterable

import numpy as np


def witness(m: int, a: float = 0.6) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if m < 2:
        raise ValueError("m must be >= 2")
    if not (0.0 < a < 1.0):
        raise ValueError("a must lie in (0,1)")
    x = np.zeros(m, dtype=complex)
    y = np.zeros(m, dtype=complex)
    z = np.zeros(m, dtype=complex)
    x[0] = 1.0
    y[1] = 1.0
    z[0] = 1j * a
    z[1] = math.sqrt(1.0 - a * a)
    return x, y, z


def real_inner(u: np.ndarray, v: np.ndarray) -> float:
    return float(np.real(np.vdot(u, v)))


def complex_inner(u: np.ndarray, v: np.ndarray) -> complex:
    return complex(np.vdot(u, v))


def euclidean_distance(u: np.ndarray, v: np.ndarray) -> float:
    return float(np.linalg.norm(u - v))


def verify_witness(m: int, a: float = 0.6, atol: float = 1e-12) -> dict[str, object]:
    x, y, z = witness(m, a)
    same_norm = abs(np.linalg.norm(y) - 1.0) <= atol and abs(np.linalg.norm(z) - 1.0) <= atol
    same_real_angle = abs(real_inner(x, y) - real_inner(x, z)) <= atol
    same_scalar_distance = abs(euclidean_distance(x, y) - euclidean_distance(x, z)) <= atol
    complex_invariant_separates = abs(complex_inner(x, y) - complex_inner(x, z)) > atol
    tpi_fails = same_norm and same_real_angle and same_scalar_distance and complex_invariant_separates
    return {
        "m": m,
        "real_dimension": 2 * m,
        "same_norm": bool(same_norm),
        "same_real_angle": bool(same_real_angle),
        "same_scalar_distance": bool(same_scalar_distance),
        "complex_inner_y_abs": abs(complex_inner(x, y)),
        "complex_inner_z_abs": abs(complex_inner(x, z)),
        "tpi_fails": bool(tpi_fails),
        "classification": "FALSIFIED_ROUTE" if tpi_fails else "CHECK_FAILED",
    }


def audit(ms: Iterable[int] = range(2, 7), a: float = 0.6) -> list[dict[str, object]]:
    return [verify_witness(m, a) for m in ms]


def write_csv(path: str | Path, ms: Iterable[int] = range(2, 7), a: float = 0.6) -> None:
    rows = audit(ms, a)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    out = Path("results/scalar_isotropy_tpi_no_go.csv")
    write_csv(out, range(2, 7))
    for row in audit(range(2, 7)):
        print(row)
    print(f"wrote {out}")
