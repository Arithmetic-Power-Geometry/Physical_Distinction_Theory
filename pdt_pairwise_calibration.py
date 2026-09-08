"""Pairwise calibration audit for Physical Distinction Theory.

This module tests a concrete dimension-selection axiom candidate:
an ordered pair of elementary reference states should suffice to identify every
connected reversible control.  For the Euclidean ball B^n with full connected
isotropy SO(n), the pointwise stabilizer of r independent reference vectors is
SO(n-r).  Hence the minimal number of independent reference states required to
identify a generic SO(n) control is n-1.

The group-theoretic mathematics is standard.  The PDT-specific physical status
of the pairwise-calibration axiom is CONDITIONAL, not established law.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def so_dimension(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return n * (n - 1) // 2


def pointwise_stabilizer_dimension(n: int, independent_references: int) -> int:
    """Dimension of SO(n-r), r=min(n, independent_references)."""
    if n < 1:
        raise ValueError("n must be positive")
    if independent_references < 0:
        raise ValueError("independent_references must be nonnegative")
    r = min(n, independent_references)
    return so_dimension(n - r)


def minimal_reference_states(n: int) -> int:
    """Minimal independent vectors whose pointwise SO(n) stabilizer is trivial."""
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 0
    return n - 1


def pairwise_calibration_possible(n: int) -> bool:
    """Whether two reference states can form a base for the natural SO(n) action."""
    return minimal_reference_states(n) <= 2


def genuinely_noncommuting_connected_reversibility(n: int) -> bool:
    """SO(n) is nonabelian exactly for n>=3 among positive dimensions."""
    if n < 1:
        raise ValueError("n must be positive")
    return n >= 3


def pcc_dimension_filter(n: int) -> bool:
    """Pairwise Calibration Closure + noncommuting SO(n) reversibility."""
    return pairwise_calibration_possible(n) and genuinely_noncommuting_connected_reversibility(n)


def stabilizer_witness(n: int, independent_references: int, theta: float = 0.37) -> np.ndarray:
    """Return a nonidentity SO(n) element fixing the first r basis vectors when possible.

    If the orthogonal complement has dimension <2, only the identity exists in
    the connected pointwise stabilizer and the identity is returned.
    """
    if n < 1:
        raise ValueError("n must be positive")
    r = min(n, max(0, independent_references))
    Q = np.eye(n)
    if n - r >= 2:
        c, s = float(np.cos(theta)), float(np.sin(theta))
        Q[r : r + 2, r : r + 2] = np.array([[c, -s], [s, c]])
    return Q


def audit_table(max_dimension: int = 12) -> pd.DataFrame:
    rows = []
    for n in range(1, max_dimension + 1):
        stab_dim = pointwise_stabilizer_dimension(n, 2)
        rows.append(
            {
                "n": n,
                "dim_SO_n": so_dimension(n),
                "minimal_reference_states": minimal_reference_states(n),
                "two_reference_stabilizer_dimension": stab_dim,
                "pairwise_calibration_possible": pairwise_calibration_possible(n),
                "noncommuting_connected_reversibility": genuinely_noncommuting_connected_reversibility(n),
                "passes_PCC_plus_noncommuting": pcc_dimension_filter(n),
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print(audit_table(12).to_string(index=False))
