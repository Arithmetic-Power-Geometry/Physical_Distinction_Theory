"""Multi-branch controlled-record Gram compatibility audits for PDT.

For pure conditional environment records |e_i>, the coherence multipliers form
G_ij=<e_i|e_j>. Hence G is a correlation/Gram matrix: Hermitian, PSD, diag(G)=1.
The 3-branch principal-minor condition is

1-|g12|^2-|g23|^2-|g31|^2 + 2 Re(g12 g23 g31) >= 0.

This module is a kill test, not a new microscopic law.
"""
from __future__ import annotations

import numpy as np


def normalize_rows(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=complex)
    n = np.linalg.norm(x, axis=1, keepdims=True)
    if np.any(n == 0):
        raise ValueError("record vectors must be nonzero")
    return x / n


def gram(records: np.ndarray) -> np.ndarray:
    """Return the Hermitian Gram matrix for row-wise record vectors."""
    r = normalize_rows(records)
    return r.conj() @ r.T


def triple_minor(g12: complex, g23: complex, g31: complex) -> float:
    """Determinant of a 3x3 unit-diagonal Hermitian Gram candidate."""
    return float(
        1.0
        - abs(g12) ** 2
        - abs(g23) ** 2
        - abs(g31) ** 2
        + 2.0 * np.real(g12 * g23 * g31)
    )


def triple_compatible(g12: complex, g23: complex, g31: complex, tol: float = 1e-12) -> bool:
    """Necessary and sufficient PSD test for the 3x3 unit-diagonal candidate."""
    if max(abs(g12), abs(g23), abs(g31)) > 1.0 + tol:
        return False
    return triple_minor(g12, g23, g31) >= -tol


def equal_visibility_bound(loop_phase: float) -> float:
    """Largest equal pairwise magnitude r compatible with a given loop phase.

    Solves 1 - 3 r^2 + 2 r^3 cos(phi) >= 0 on r in [0,1].
    """
    c = float(np.cos(loop_phase))
    grid = np.linspace(0.0, 1.0, 20001)
    vals = 1.0 - 3.0 * grid**2 + 2.0 * c * grid**3
    ok = grid[vals >= -1e-12]
    return float(ok[-1]) if len(ok) else 0.0


def phase_frustrated_counterexample(r: float = 0.9) -> dict:
    """Pairwise-valid but globally impossible 3-record coherence assignment."""
    g12 = complex(r)
    g23 = complex(r)
    g31 = complex(-r)  # loop phase pi
    return {
        "r": float(r),
        "pairwise_valid": bool(r <= 1.0),
        "triple_minor": triple_minor(g12, g23, g31),
        "globally_compatible": triple_compatible(g12, g23, g31),
    }


def random_audit(max_dimension: int = 12, trials: int = 300, seed: int = 16092026) -> list[dict]:
    rng = np.random.default_rng(seed)
    rows: list[dict] = []
    for d in range(1, max_dimension + 1):
        dets = []
        for _ in range(trials):
            x = rng.normal(size=(3, d)) + 1j * rng.normal(size=(3, d))
            g = gram(x)
            dets.append(float(np.linalg.det(g).real))
        rows.append(
            {
                "dimension": d,
                "trials": trials,
                "min_det": min(dets),
                "max_det": max(dets),
                "violations_below_-1e-12": sum(v < -1e-12 for v in dets),
            }
        )
    return rows


if __name__ == "__main__":
    print(phase_frustrated_counterexample())
    for row in random_audit():
        print(row)
