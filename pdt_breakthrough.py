"""Exploratory PDT breakthrough-lab utilities.

Every function in this module carries a conservative scientific interpretation.
The metric-entropy result implemented here is known mathematics; PDT uses it as
an operational audit, not as a novelty claim or an n=3 derivation.
"""
from __future__ import annotations

import math
import pandas as pd


def euclidean_distinction_capacity_bounds(n: int, epsilon: float) -> dict[str, float]:
    """Bounds log2 M_epsilon for the Euclidean unit ball B_2^n.

    M_epsilon is the maximum cardinality of an epsilon-separated codebook.
    A maximal epsilon-separated set is an epsilon-cover, giving M >= eps^-n.
    Disjoint epsilon/2 balls around packing points fit in the expanded ball
    (1+epsilon/2)B, giving M <= (1+2/epsilon)^n.

    These are standard covering/packing-volume bounds (metric entropy).
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    epsilon = float(epsilon)
    if not 0.0 < epsilon < 1.0:
        raise ValueError("epsilon must lie in (0,1)")
    lower_M = epsilon ** (-n)
    upper_M = (1.0 + 2.0 / epsilon) ** n
    return {
        "n": float(n),
        "epsilon": epsilon,
        "lower_capacity_bits": math.log2(lower_M),
        "upper_capacity_bits": math.log2(upper_M),
    }


def operational_dimension_slope_bounds(n: int, epsilon: float) -> dict[str, float]:
    """Return bounds on K(epsilon)/log2(1/epsilon).

    Both bounds converge to n as epsilon -> 0. Hence, under the explicit
    Euclidean-resolution/codebook assumptions, the capacity scaling identifies
    dimension operationally. It does not select which n Nature must use.
    """
    b = euclidean_distinction_capacity_bounds(n, epsilon)
    denom = math.log2(1.0 / float(epsilon))
    return {
        **b,
        "slope_lower": b["lower_capacity_bits"] / denom,
        "slope_upper": b["upper_capacity_bits"] / denom,
        "target_dimension": float(n),
    }


def dimension_identifiability_audit(
    dimensions=(2, 3, 4, 5),
    epsilons=(0.25, 0.1, 0.03, 0.01, 0.003),
) -> pd.DataFrame:
    rows = []
    for n in dimensions:
        for eps in epsilons:
            rows.append(operational_dimension_slope_bounds(int(n), float(eps)))
    return pd.DataFrame(rows)


def dimension_theorem_status() -> dict[str, str]:
    return {
        "claim": "Fine-resolution distinction-capacity scaling identifies Euclidean dimension",
        "status": "CONDITIONAL / KNOWN-MATH OPERATIONALIZATION",
        "assumptions": "Euclidean unit ball; epsilon-separated admissible codebooks; epsilon -> 0",
        "novelty_boundary": "Uses standard metric-entropy/packing-covering asymptotics; not new mathematics",
        "consequence": "n is operationally estimable from scaling, but n=3 is not selected",
    }
