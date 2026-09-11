"""Cycle 071: correlated-composite nonclosure of local resource quotients.

The previous product-state law q_AB(rho_A tensor rho_B)=q_A(rho_A) tensor q_B(rho_B)
is exact, but no map of the two local quotient states alone can reconstruct arbitrary
correlated composites.  This file supplies an explicit dimension-uniform witness family.
"""

from __future__ import annotations

import json
from math import sqrt
from pathlib import Path

import numpy as np


DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def traceless_unit_hs_diagonal(d: int) -> np.ndarray:
    """Return a traceless Hermitian diagonal observable with Hilbert-Schmidt norm 1."""
    if d < 2:
        raise ValueError("d must be >= 2")
    a = np.zeros(d, dtype=float)
    a[0] = 1.0 / sqrt(2.0)
    a[1] = -1.0 / sqrt(2.0)
    return a


def witness(d: int) -> dict:
    """Construct rho_+/- = I/d^2 +/- epsilon A tensor B using diagonal storage.

    Both states have exactly the same full local marginals, hence the same local
    resource quotients for *every* local observable space.  A tensor B separates
    their joint product-observable statistics.
    """
    if d == 1:
        return {
            "dimension": 1,
            "classification": "DEGENERATE",
            "reason": "No nonzero traceless local observable exists in dimension 1.",
        }

    a = traceless_unit_hs_diagonal(d)
    b = traceless_unit_hs_diagonal(d)
    total_dim = d * d
    eps = 1.0 / total_dim
    corr = np.outer(a, b)

    rho_plus = np.full((d, d), 1.0 / total_dim) + eps * corr
    rho_minus = np.full((d, d), 1.0 / total_dim) - eps * corr

    a_plus = rho_plus.sum(axis=1)
    a_minus = rho_minus.sum(axis=1)
    b_plus = rho_plus.sum(axis=0)
    b_minus = rho_minus.sum(axis=0)

    local_error = max(
        float(np.max(np.abs(a_plus - a_minus))),
        float(np.max(np.abs(b_plus - b_minus))),
    )
    plus_expectation = float(np.sum(rho_plus * corr))
    minus_expectation = float(np.sum(rho_minus * corr))
    separation = abs(plus_expectation - minus_expectation)
    expected = 2.0 / total_dim

    return {
        "dimension": d,
        "classification": "FALSIFIED_LOCAL_ONLY_COMPOSITION",
        "epsilon": eps,
        "min_eigenvalue_rho_plus": float(np.min(rho_plus)),
        "min_eigenvalue_rho_minus": float(np.min(rho_minus)),
        "max_local_marginal_difference": local_error,
        "joint_product_observable_separation": separation,
        "expected_separation": expected,
        "separation_residual": abs(separation - expected),
    }


def run_audit() -> dict:
    rows = [witness(d) for d in DIMS]
    nondegenerate = [r for r in rows if r["dimension"] >= 2]
    result = {
        "cycle": 71,
        "target": "PDT-II (1) native composition law",
        "status": "PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED",
        "claim_falsified": (
            "The two local resource quotient states alone determine the resource state "
            "of every correlated bipartite composite."
        ),
        "theorem": (
            "Whenever both local accessible spaces contain a nonzero traceless Hermitian "
            "observable, there exist two valid bipartite states with identical full local "
            "marginals but different accessible product-observable statistics."
        ),
        "surviving_replacement": (
            "q_AB = q_A tensor q_B + Gamma_R, where Gamma_R is a correlation sector; "
            "Gamma_R=0 on product states but cannot be inferred from q_A and q_B in general."
        ),
        "breakthrough_candidate": False,
        "dimensions": DIMS,
        "nondegenerate_cases": len(nondegenerate),
        "max_local_marginal_difference": max(r["max_local_marginal_difference"] for r in nondegenerate),
        "max_separation_residual": max(r["separation_residual"] for r in nondegenerate),
        "min_joint_separation": min(r["joint_product_observable_separation"] for r in nondegenerate),
        "rows": rows,
    }
    return result


if __name__ == "__main__":
    result = run_audit()
    out = Path("results/cycle071_correlated_quotient_nonclosure.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))
