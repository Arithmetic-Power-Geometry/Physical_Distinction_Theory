"""Alternative reversible-group kill tests for Pairwise Calibration Closure.

The natural SU(m) action on C^m, viewed as a real action on R^(2m), is a
connected compact nonabelian subgroup of SO(2m).  Fixing r complex-linearly
independent reference vectors leaves pointwise stabilizer SU(m-r).  Thus the
minimal number of references needed to identify an SU(m) control is m-1.

Consequently PCC (two references suffice) plus noncommutativity does NOT by
itself select real dimension three: SU(2) on R^4 and SU(3) on R^6 are explicit
higher-dimensional counterexamples.  The full-isotropy SO(n) assumption in the
PCC dimension theorem is therefore essential.
"""
from __future__ import annotations

import pandas as pd


def su_dimension(m: int) -> int:
    if m < 1:
        raise ValueError("m must be positive")
    return m * m - 1


def su_minimal_reference_states(m: int) -> int:
    if m < 1:
        raise ValueError("m must be positive")
    if m == 1:
        return 0
    return m - 1


def su_pairwise_calibration_possible(m: int) -> bool:
    return su_minimal_reference_states(m) <= 2


def su_noncommuting(m: int) -> bool:
    return m >= 2


def su_pcc_counterexample(m: int) -> bool:
    """Higher-than-3 real dimension satisfying PCC + noncommuting reversibility."""
    real_dimension = 2 * m
    return real_dimension > 3 and su_pairwise_calibration_possible(m) and su_noncommuting(m)


def audit_table(max_m: int = 8) -> pd.DataFrame:
    rows = []
    for m in range(1, max_m + 1):
        rows.append(
            {
                "m": m,
                "real_state_dimension_n": 2 * m,
                "group": f"SU({m})",
                "dim_group": su_dimension(m),
                "minimal_reference_states": su_minimal_reference_states(m),
                "pairwise_calibration_possible": su_pairwise_calibration_possible(m),
                "noncommuting": su_noncommuting(m),
                "higher_dim_PCC_counterexample": su_pcc_counterexample(m),
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print(audit_table().to_string(index=False))
