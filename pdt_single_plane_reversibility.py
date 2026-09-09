"""Cycle 027: single-plane reversibility (SPR) dimension filter.

Mathematics: so(n) is the space of real skew-symmetric n x n matrices.
SPR requires every infinitesimal reversible generator to have matrix rank <= 2,
i.e. to rotate at most one two-plane at first order.
"""
from __future__ import annotations

import numpy as np


def so_dimension(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return n * (n - 1) // 2


def maximal_skew_rank(n: int) -> int:
    """Exact maximum rank of a real n x n skew-symmetric matrix."""
    if n < 1:
        raise ValueError("n must be positive")
    return 2 * (n // 2)


def spr_holds_for_full_so(n: int) -> bool:
    """SPR iff every A in so(n) has rank(A) <= 2."""
    return maximal_skew_rank(n) <= 2


def noncommuting_reversibility(n: int) -> bool:
    """For the full connected isotropy SO(n), so(n) is non-abelian iff n >= 3."""
    if n < 1:
        raise ValueError("n must be positive")
    return n >= 3


def dimension_filter_holds(n: int) -> bool:
    return spr_holds_for_full_so(n) and noncommuting_reversibility(n)


def rank4_counterexample(n: int) -> np.ndarray:
    """Explicit SPR witness for every n >= 4: J_12 + J_34, rank 4."""
    if n < 4:
        raise ValueError("rank-4 witness requires n >= 4")
    a = np.zeros((n, n), dtype=float)
    a[0, 1], a[1, 0] = -1.0, 1.0
    a[2, 3], a[3, 2] = -1.0, 1.0
    return a


def random_skew(n: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(n, n))
    return x - x.T


def stress_dimensions(dimensions=range(1, 13), trials: int = 200, seed: int = 2701):
    """Randomly probe generator ranks; theorem status itself is exact, not numeric."""
    rng = np.random.default_rng(seed)
    rows = []
    for n in dimensions:
        observed_max = 0
        violations = 0
        for _ in range(trials):
            r = int(np.linalg.matrix_rank(random_skew(n, rng), tol=1e-10))
            observed_max = max(observed_max, r)
            if spr_holds_for_full_so(n) and r > 2:
                violations += 1
        witness_rank = int(np.linalg.matrix_rank(rank4_counterexample(n))) if n >= 4 else None
        rows.append({
            "n": n,
            "dim_so_n": so_dimension(n),
            "exact_max_skew_rank": maximal_skew_rank(n),
            "SPR_full_SO": spr_holds_for_full_so(n),
            "NCR_full_SO": noncommuting_reversibility(n),
            "SPR_plus_NCR": dimension_filter_holds(n),
            "random_observed_max_rank": observed_max,
            "rank4_witness_rank": witness_rank,
            "random_SPR_violations_when_SPR_predicted": violations,
        })
    return rows


if __name__ == "__main__":
    import json
    print(json.dumps(stress_dimensions(), indent=2))
