"""PDT resource-lattice dimension identities.

This module treats a finite resource window as a linear subspace E_R of
accessible effects in V*. The accessible quotient dimension equals dim E_R
when the null space is the annihilator of E_R.

The central identity is the Grassmann dimension formula

    d(R join S) + d(R meet S) = d(R) + d(S)

for join = linear span/sum and meet = subspace intersection.

This is established linear algebra; the PDT contribution is the resource-
revelation bookkeeping and its use as a consistency/kill test.
"""

from __future__ import annotations

import numpy as np


def _as_rows(a: np.ndarray, ambient_dim: int | None = None) -> np.ndarray:
    a = np.asarray(a, dtype=float)
    if a.size == 0:
        if ambient_dim is None:
            raise ValueError("ambient_dim is required for an empty effect family")
        return np.empty((0, ambient_dim), dtype=float)
    if a.ndim == 1:
        a = a.reshape(1, -1)
    if a.ndim != 2:
        raise ValueError("effect family must be a 1D or 2D array")
    return a


def effect_rank(a: np.ndarray, tol: float = 1e-10, ambient_dim: int | None = None) -> int:
    """Dimension of the linear span of accessible effects."""
    a = _as_rows(a, ambient_dim)
    if a.shape[0] == 0:
        return 0
    return int(np.linalg.matrix_rank(a, tol=tol))


def join_rank(a: np.ndarray, b: np.ndarray, tol: float = 1e-10) -> int:
    """Dimension of span(E_A + E_B)."""
    a = _as_rows(a)
    b = _as_rows(b)
    if a.shape[1] != b.shape[1]:
        raise ValueError("effect families must share the same ambient dimension")
    return effect_rank(np.vstack([a, b]), tol=tol)


def meet_rank(a: np.ndarray, b: np.ndarray, tol: float = 1e-10) -> int:
    """Dimension of E_A intersect E_B via Grassmann's formula."""
    a = _as_rows(a)
    b = _as_rows(b)
    if a.shape[1] != b.shape[1]:
        raise ValueError("effect families must share the same ambient dimension")
    return effect_rank(a, tol=tol) + effect_rank(b, tol=tol) - join_rank(a, b, tol=tol)


def modular_residual(a: np.ndarray, b: np.ndarray, tol: float = 1e-10) -> int:
    """Exact-in-rank residual of d(join)+d(meet)-d(A)-d(B)."""
    ra = effect_rank(a, tol=tol)
    rb = effect_rank(b, tol=tol)
    return join_rank(a, b, tol=tol) + meet_rank(a, b, tol=tol) - ra - rb


def unique_revelation(a: np.ndarray, b: np.ndarray, tol: float = 1e-10) -> tuple[int, int, int]:
    """Return new directions from A beyond B, from B beyond A, and shared rank."""
    ra = effect_rank(a, tol=tol)
    rb = effect_rank(b, tol=tol)
    ri = meet_rank(a, b, tol=tol)
    return ra - ri, rb - ri, ri


def coordinate_audit(n: int) -> dict[str, int]:
    """Deterministic n-dimensional witness used for n=1..12 audits."""
    if n < 1:
        raise ValueError("n must be positive")
    k = (n + 1) // 2
    eye = np.eye(n)
    a = eye[:k]
    b = eye[n - k :]
    ra = effect_rank(a)
    rb = effect_rank(b)
    rj = join_rank(a, b)
    ri = meet_rank(a, b)
    return {
        "n": n,
        "rank_A": ra,
        "rank_B": rb,
        "rank_meet": ri,
        "rank_join": rj,
        "lhs": rj + ri,
        "rhs": ra + rb,
        "residual": rj + ri - ra - rb,
    }
