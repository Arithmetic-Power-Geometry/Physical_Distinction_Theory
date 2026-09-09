"""Cycle 029: primitive-generator no-go for SPR-based dimension selection.

This module distinguishes two meanings of Single-Plane Reversibility (SPR):

1. universal SPR: every Lie-algebra element has rank <= 2;
2. primitive SPR: there exists a generating set whose primitive controls have rank <= 2.

For so(n), the coordinate-plane generators J_ij form a rank-2 basis for every n>=2.
For n>=3 they contain noncommuting pairs. Therefore primitive SPR + NCR does not
select n=3; it holds for every n>=3.
"""

from __future__ import annotations

import numpy as np


def plane_generator(n: int, i: int, j: int) -> np.ndarray:
    """Return J_ij = E_ij - E_ji in dimension n."""
    if n < 1:
        raise ValueError("n must be positive")
    if not (0 <= i < j < n):
        raise ValueError("require 0 <= i < j < n")
    a = np.zeros((n, n), dtype=float)
    a[i, j] = 1.0
    a[j, i] = -1.0
    return a


def coordinate_plane_basis(n: int) -> list[np.ndarray]:
    """Standard coordinate-plane basis of so(n)."""
    return [plane_generator(n, i, j) for i in range(n) for j in range(i + 1, n)]


def primitive_spr_holds(n: int, tol: float = 1e-10) -> bool:
    """Whether the standard primitive generating basis has rank <=2."""
    basis = coordinate_plane_basis(n)
    return all(np.linalg.matrix_rank(a, tol=tol) <= 2 for a in basis)


def ncr_holds(n: int, tol: float = 1e-10) -> bool:
    """Witness noncommuting reversibility using J_01 and J_12 when n>=3."""
    if n < 3:
        return False
    a = plane_generator(n, 0, 1)
    b = plane_generator(n, 1, 2)
    comm = a @ b - b @ a
    return np.linalg.norm(comm, ord="fro") > tol


def primitive_spr_ncr_selects(n: int) -> bool:
    """Primitive SPR + noncommuting reversibility criterion."""
    return primitive_spr_holds(n) and ncr_holds(n)


def spectator_normalized_rank(a: np.ndarray, spectator_dim: int) -> float:
    """rank(A tensor I_m)/m, the Cycle-028 factor-local repair quantity."""
    if spectator_dim < 1:
        raise ValueError("spectator_dim must be positive")
    lifted = np.kron(a, np.eye(spectator_dim))
    return float(np.linalg.matrix_rank(lifted)) / spectator_dim


def audit_dimensions(max_n: int = 12) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(1, max_n + 1):
        basis = coordinate_plane_basis(n)
        ranks = [int(np.linalg.matrix_rank(a)) for a in basis]
        rows.append(
            {
                "n": n,
                "so_dimension": n * (n - 1) // 2,
                "primitive_count": len(basis),
                "max_primitive_rank": max(ranks, default=0),
                "primitive_spr": primitive_spr_holds(n),
                "ncr": ncr_holds(n),
                "primitive_spr_plus_ncr": primitive_spr_ncr_selects(n),
                "unique_n3": primitive_spr_ncr_selects(n)
                and not any(primitive_spr_ncr_selects(m) for m in range(4, max_n + 1)),
            }
        )
    return rows


if __name__ == "__main__":
    for row in audit_dimensions(12):
        print(row)
