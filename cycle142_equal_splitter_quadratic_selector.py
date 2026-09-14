"""PDT cycle 142: equal-splitter conservation audit.

Conditional theorem target:
If a continuous radial rank-one resource g(r) is conserved by resolved equal-amplitude
2-way and 3-way orthogonal splitters, then g(r)=c r^2 (r>=0).
Calibration g(1)=1 gives g(r)=r^2.

The script also supplies a decisive counterexample showing that the binary splitter
alone is insufficient.
"""
from __future__ import annotations

import json
import math
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 142
TOL = 1e-10
EPS = 0.05


def g_quadratic(r: float) -> float:
    return r * r


def g_binary_only_counterexample(r: float, eps: float = EPS) -> float:
    """Positive continuous nonlinear g with exact binary equal-split conservation.

    g(r)=r^2[1+eps sin(4 pi log_2 r)] for r>0, g(0)=0.
    Since log_2(r/sqrt(2))=log_2 r-1/2, the sine is unchanged, hence
    g(r)=2 g(r/sqrt(2)).  It generically fails the 3-way identity.
    """
    if r == 0.0:
        return 0.0
    return r * r * (1.0 + eps * math.sin(4.0 * math.pi * math.log2(r)))


def relerr(a: float, b: float) -> float:
    return abs(a - b) / max(1.0, abs(a), abs(b))


def audit() -> dict:
    rng = np.random.default_rng(SEED)
    out = {
        "cycle": 142,
        "dimensions": DIMS,
        "seed": SEED,
        "tolerance": TOL,
        "theorem": (
            "For continuous g:[0,infinity)->[0,infinity), if g(r)=2g(r/sqrt(2)) "
            "and g(r)=3g(r/sqrt(3)) for every r>=0, then g(r)=c r^2. "
            "With g(1)=1, g(r)=r^2."
        ),
        "classification": {
            "proved": True,
            "conditional": True,
            "imported_known": "Dense-period/continuity argument is standard analysis.",
            "numerically_supported": True,
            "falsified": "Binary equal-splitter conservation alone fixes the quadratic law.",
            "open": "Derive 2-way and 3-way resolved equal-split conservation from PDT-native primitives.",
            "breakthrough_candidate": False,
        },
    }

    cases = 0
    stats = {}
    for name, g in [
        ("quadratic", g_quadratic),
        ("binary_only_counterexample", g_binary_only_counterexample),
    ]:
        binary_fail = 0
        ternary_fail = 0
        max_binary = 0.0
        max_ternary = 0.0
        for n in DIMS:
            reps = 40 if n <= 32 else 15
            for _ in range(reps):
                # n labels the ambient composite dimension.  The radial identity itself
                # is dimension-independent; a wide logarithmic resource range is tested.
                r = 10.0 ** rng.uniform(-6.0, 6.0)
                eb = relerr(g(r), 2.0 * g(r / math.sqrt(2.0)))
                et = relerr(g(r), 3.0 * g(r / math.sqrt(3.0)))
                binary_fail += int(eb > TOL)
                ternary_fail += int(et > TOL)
                max_binary = max(max_binary, eb)
                max_ternary = max(max_ternary, et)
                cases += 1
        stats[name] = {
            "binary_failures": binary_fail,
            "ternary_failures": ternary_fail,
            "max_binary_relative_residual": max_binary,
            "max_ternary_relative_residual": max_ternary,
        }

    # Explicit fixed witness for the nonlinear counterfamily.
    r = 1.23456789
    out["fixed_counterexample"] = {
        "r": r,
        "g_r": g_binary_only_counterexample(r),
        "binary_rhs": 2.0 * g_binary_only_counterexample(r / math.sqrt(2.0)),
        "ternary_rhs": 3.0 * g_binary_only_counterexample(r / math.sqrt(3.0)),
        "binary_relative_residual": relerr(
            g_binary_only_counterexample(r),
            2.0 * g_binary_only_counterexample(r / math.sqrt(2.0)),
        ),
        "ternary_relative_residual": relerr(
            g_binary_only_counterexample(r),
            3.0 * g_binary_only_counterexample(r / math.sqrt(3.0)),
        ),
    }
    out["total_function_dimension_cases"] = cases
    out["stats"] = stats
    return out


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
