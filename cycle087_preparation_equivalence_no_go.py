"""Cycle 087: preparation-equivalence boundary for PDT pre-measurement dynamics.

The analytic theorem is elementary: if a deterministic state update Phi is operationally
well-defined on mixed preparations, then for every ensemble rho=sum_i p_i rho_i,
Phi(rho)=sum_i p_i Phi(rho_i). Hence Phi is affine on density operators.
If, in addition, Phi is trace preserving and completely positive, it is an ordinary
quantum channel. A genuinely nonlinear PDT state update must therefore abandon
preparation equivalence / ensemble independence (or another standard assumption).

This script only supplies regression witnesses for the nonlinear candidate
N(rho)=rho^2/Tr(rho^2); it is not the proof.
"""

from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 8701
TRIALS = 20


def nonlinear_square_on_diagonal(p: np.ndarray) -> np.ndarray:
    q = p * p
    return q / q.sum()


def run() -> dict:
    rng = np.random.default_rng(SEED)
    rows = []
    total_nontrivial_failures = 0
    for d in DIMS:
        if d == 1:
            rows.append({"d": 1, "max_preparation_gap": 0.0, "failures": 0})
            continue
        max_gap = 0.0
        failures = 0
        for _ in range(TRIALS):
            p = rng.dirichlet(np.ones(d))
            direct = nonlinear_square_on_diagonal(p)
            # Spectral ensemble consists of pure basis states. N fixes each pure state,
            # so ensemble-wise application followed by forgetting the label returns p.
            ensemble = p
            gap = float(np.max(np.abs(direct - ensemble)))
            max_gap = max(max_gap, gap)
            if gap > 1e-12:
                failures += 1
        total_nontrivial_failures += failures
        rows.append({"d": d, "max_preparation_gap": max_gap, "failures": failures})

    result = {
        "cycle": 87,
        "seed": SEED,
        "trials_per_nontrivial_dimension": TRIALS,
        "dimensions": DIMS,
        "candidate": "N(rho)=rho^2/Tr(rho^2)",
        "nontrivial_cases": (len(DIMS) - 1) * TRIALS,
        "preparation_equivalence_failures": total_nontrivial_failures,
        "rows": rows,
    }
    return result


if __name__ == "__main__":
    out = run()
    path = Path("results/cycle087_preparation_equivalence_no_go.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
