"""Operational resolution-dimension tools for the PDT breakthrough laboratory.

The mathematics is standard metric entropy / Minkowski-dimension theory.  PDT uses
it only as an operational corollary: resolution-dependent distinguishable-codebook
growth can identify an already existing finite metric dimension, but it does not
select n=3 from first principles.
"""
from __future__ import annotations

import math
import pandas as pd


def euclidean_capacity_bounds(n: int, epsilon: float) -> tuple[float, float]:
    """Conservative log2 packing/covering bounds for the Euclidean unit ball.

    For 0 < epsilon <= 1 we use the standard volumetric bounds
        (1/epsilon)^n <= M(epsilon) <= (1 + 2/epsilon)^n,
    where M is a maximal epsilon-separated codebook up to the usual packing /
    covering convention.  The constants do not affect the epsilon->0 slope.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if not 0.0 < epsilon <= 1.0:
        raise ValueError("epsilon must lie in (0,1]")
    lower = n * math.log2(1.0 / epsilon)
    upper = n * math.log2(1.0 + 2.0 / epsilon)
    return float(lower), float(upper)


def operational_dimension_interval(n: int, epsilon: float) -> tuple[float, float]:
    """Finite-resolution interval for K(eps)/log2(1/eps)."""
    if epsilon >= 1.0:
        raise ValueError("epsilon must be < 1 for a dimension ratio")
    lo, hi = euclidean_capacity_bounds(n, epsilon)
    scale = math.log2(1.0 / epsilon)
    return float(lo / scale), float(hi / scale)


def dimension_audit(ns=(2, 3, 4, 5), epsilons=(0.25, 0.1, 0.03, 0.01, 0.003)) -> pd.DataFrame:
    rows = []
    for n in ns:
        for eps in epsilons:
            lo, hi = euclidean_capacity_bounds(int(n), float(eps))
            dlo, dhi = operational_dimension_interval(int(n), float(eps))
            rows.append({
                "n": int(n),
                "epsilon": float(eps),
                "lower_capacity_bits": lo,
                "upper_capacity_bits": hi,
                "dimension_ratio_lower": dlo,
                "dimension_ratio_upper": dhi,
            })
    return pd.DataFrame(rows)
