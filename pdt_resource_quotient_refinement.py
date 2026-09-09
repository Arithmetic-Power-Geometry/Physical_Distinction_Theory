"""PDT resource-quotient refinement audit.

Exact finite-dimensional consequences of nested admissible linear tests.
If the row space of A1 is contained in the row space of A2, then the
operational null space ker(A2) is contained in ker(A1), so the resolved
quotient dimension rank(A) cannot decrease under resource refinement.
"""

from __future__ import annotations

import numpy as np


def matrix_rank(a: np.ndarray, tol: float | None = None) -> int:
    a = np.asarray(a, dtype=float)
    if a.ndim != 2:
        raise ValueError("test matrix must be two-dimensional")
    if a.shape[0] == 0 or a.shape[1] == 0:
        return 0
    return int(np.linalg.matrix_rank(a, tol=tol))


def quotient_dimension(test_matrix: np.ndarray, tol: float | None = None) -> int:
    """Dimension of V/ker(A), equal to rank(A)."""
    return matrix_rank(test_matrix, tol=tol)


def nullity(test_matrix: np.ndarray, tol: float | None = None) -> int:
    a = np.asarray(test_matrix, dtype=float)
    if a.ndim != 2:
        raise ValueError("test matrix must be two-dimensional")
    return int(a.shape[1] - matrix_rank(a, tol=tol))


def is_refinement(coarse: np.ndarray, fine: np.ndarray, tol: float = 1e-10) -> bool:
    """Return True iff row(coarse) is contained in row(fine)."""
    coarse = np.asarray(coarse, dtype=float)
    fine = np.asarray(fine, dtype=float)
    if coarse.ndim != 2 or fine.ndim != 2:
        raise ValueError("test matrices must be two-dimensional")
    if coarse.shape[1] != fine.shape[1]:
        return False
    r_f = matrix_rank(fine, tol)
    if coarse.shape[0] == 0:
        return True
    stacked = np.vstack([fine, coarse])
    return matrix_rank(stacked, tol) == r_f


def refinement_audit(coarse: np.ndarray, fine: np.ndarray, tol: float = 1e-10) -> dict:
    """Audit the quotient/null-space consequences of a claimed refinement."""
    ok = is_refinement(coarse, fine, tol=tol)
    qc = quotient_dimension(coarse, tol)
    qf = quotient_dimension(fine, tol)
    nc = nullity(coarse, tol)
    nf = nullity(fine, tol)
    return {
        "is_refinement": ok,
        "coarse_quotient_dim": qc,
        "fine_quotient_dim": qf,
        "coarse_nullity": nc,
        "fine_nullity": nf,
        "quotient_monotone": (qf >= qc) if ok else None,
        "nullity_antitone": (nf <= nc) if ok else None,
        "revealed_dimensions": (qf - qc) if ok else None,
    }


def coordinate_chain(n: int) -> list[np.ndarray]:
    """Exact nested coordinate-test chain from no access to full access."""
    if n < 1:
        raise ValueError("n must be positive")
    eye = np.eye(n)
    return [eye[:k, :] for k in range(n + 1)]


def chain_revelation_dimensions(chain: list[np.ndarray], tol: float = 1e-10) -> list[int]:
    if not chain:
        raise ValueError("chain cannot be empty")
    gains: list[int] = []
    for a, b in zip(chain, chain[1:]):
        audit = refinement_audit(a, b, tol)
        if not audit["is_refinement"]:
            raise ValueError("chain contains a non-refinement step")
        gains.append(int(audit["revealed_dimensions"]))
    return gains
