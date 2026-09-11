"""Cycle 074: exact quadratic revelation conservation under orthogonal refinement.

This audit is regression evidence for a proof-level Hilbert-space identity.  It also
records the elementary l_p counterexample showing that squared norm additivity over
orthogonal coordinate blocks singles out p=2 within the l_p family.
"""
from __future__ import annotations

import json
import numpy as np


def run_audit(seed: int = 74011) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    failures = 0
    cases = 0
    max_err = 0.0
    rows = []

    for n in dims:
        reps = 100 if n <= 12 else 40
        for _ in range(reps):
            x = rng.normal(size=n)
            perm = rng.permutation(n)
            previous = 0.0
            total_increment = 0.0
            for k in range(1, n + 1):
                current = float(np.dot(x[perm[:k]], x[perm[:k]]))
                increment = current - previous
                if increment < -1e-12:
                    failures += 1
                total_increment += increment
                previous = current
            target = float(np.dot(x, x))
            err = abs(total_increment - target)
            max_err = max(max_err, err)
            if err > 1e-10:
                failures += 1
            cases += 1
        rows.append({"n": n, "repetitions": reps})

    lp = {}
    for p in [1.0, 1.5, 2.0, 3.0, 4.0, 8.0]:
        whole = 2.0 ** (2.0 / p)  # ||(1,1)||_p^2
        block_sum = 2.0           # ||(1,0)||_p^2 + ||(0,1)||_p^2
        lp[str(p)] = {
            "whole_squared_norm": whole,
            "sum_block_squared_norms": block_sum,
            "gap": whole - block_sum,
        }
    lp["inf"] = {
        "whole_squared_norm": 1.0,
        "sum_block_squared_norms": 2.0,
        "gap": -1.0,
    }

    return {
        "classification": [
            "PROVED",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
            "FALSIFIED(nonquadratic universal extension)",
        ],
        "cases": cases,
        "failures": failures,
        "max_abs_telescoping_error": max_err,
        "dimensions": dims,
        "dimension_rows": rows,
        "lp_witness": lp,
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
