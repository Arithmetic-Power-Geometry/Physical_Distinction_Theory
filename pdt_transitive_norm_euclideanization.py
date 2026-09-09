"""Cycle 017: transitive reversible norm spheres force Euclidean geometry.

The theorem is mathematical prior art / finite-dimensional rotation-problem folklore.
This module supplies exact l_p witnesses and deterministic audits used by PDT.
"""
from __future__ import annotations

import math


def equal_coordinate_euclidean_radius(n: int, p: float) -> float:
    """Euclidean norm of the equal-coordinate point on the l_p unit sphere."""
    if n < 2 or p <= 0:
        raise ValueError("require n>=2 and p>0")
    return n ** (0.5 - 1.0 / p)


def axis_euclidean_radius() -> float:
    return 1.0


def lp_anisotropy_witness(n: int, p: float) -> float:
    """Absolute Euclidean-radius gap between two l_p-unit vectors."""
    return abs(equal_coordinate_euclidean_radius(n, p) - 1.0)


def euclidean_only_among_lp(n: int, p: float, tol: float = 1e-12) -> bool:
    """True exactly when the two-point witness is compatible with transitivity."""
    return lp_anisotropy_witness(n, p) <= tol


def audit(max_dimension: int = 12, ps=(1.0, 1.5, 2.0, 3.0, 4.0, 10.0)):
    rows = []
    for n in range(2, max_dimension + 1):
        for p in ps:
            rows.append(
                {
                    "n": n,
                    "p": p,
                    "axis_euclidean_radius": 1.0,
                    "equal_coordinate_euclidean_radius": equal_coordinate_euclidean_radius(n, p),
                    "radius_gap": lp_anisotropy_witness(n, p),
                    "passes_two_point_transitivity_witness": euclidean_only_among_lp(n, p),
                }
            )
    return rows


if __name__ == "__main__":
    for row in audit():
        print(row)
