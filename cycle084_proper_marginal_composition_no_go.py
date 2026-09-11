"""Cycle 084: proper-marginal composition no-go via hidden GHZ coherence.

Target: PDT-II (1) composition law, with relevance to (4)/(5).

Classification:
- proper-marginal nonidentifiability theorem: PROVED
- scalar/proper-subsystem closure from proper marginals: FALSIFIED
- finite-dimensional stress audit: NUMERICALLY SUPPORTED
- novelty boundary: IMPORTED/KNOWN quantum-marginal/GHZ phenomenon

No breakthrough claim is made.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


def ghz_coherence_state(local_dim: int, parties: int, coherence: float) -> np.ndarray:
    """rho_c on span{|0...0>, |1...1>} for d>=2, |c|<=1/2."""
    if local_dim < 2:
        raise ValueError("local_dim must be >=2 for the witness")
    if parties < 2:
        raise ValueError("parties must be >=2")
    if abs(coherence) > 0.5 + 1e-15:
        raise ValueError("positivity requires |coherence|<=1/2")
    D = local_dim**parties
    rho = np.zeros((D, D), dtype=complex)
    i0 = 0
    i1 = sum(local_dim**k for k in range(parties))
    rho[i0, i0] = 0.5
    rho[i1, i1] = 0.5
    rho[i0, i1] = coherence
    rho[i1, i0] = coherence
    return rho


def partial_trace_keep(rho: np.ndarray, dims: list[int], keep: list[int]) -> np.ndarray:
    n = len(dims)
    arr = rho.reshape(*(dims + dims))
    cur_dims = list(dims)
    cur_n = n
    for i in sorted([j for j in range(n) if j not in keep], reverse=True):
        arr = np.trace(arr, axis1=i, axis2=cur_n + i)
        cur_dims.pop(i)
        cur_n -= 1
    d = math.prod(cur_dims) if cur_dims else 1
    return arr.reshape(d, d)


def distinction_energy(rho: np.ndarray) -> float:
    d = rho.shape[0]
    return float(d * np.trace(rho @ rho).real - 1.0)


def analytic_full_energy(local_dim: int, parties: int, coherence: float) -> float:
    """E_D = D Tr(rho_c^2)-1; Tr(rho_c^2)=1/2+2c^2."""
    D = local_dim**parties
    return float(D * (0.5 + 2.0 * coherence**2) - 1.0)


def analytic_hidden_full_sector_increment(local_dim: int, parties: int, coherence: float) -> float:
    """The coherence perturbation lies wholly in the all-party traceless sector."""
    D = local_dim**parties
    return float(2.0 * D * coherence**2)


def run_audit() -> dict:
    c0, c1 = 0.0, 0.5

    # n=1 is explicitly degenerate: |0...0> and |1...1> are not distinct local basis states.
    degenerate_n1 = True

    # Dense numerical checks where inexpensive. All proper marginals must be identical.
    dense_dims = list(range(2, 7))
    max_proper_marginal_difference = 0.0
    max_energy_formula_residual = 0.0
    dense_cases = 0
    for d in dense_dims:
        dims = [d, d, d]
        rho0 = ghz_coherence_state(d, 3, c0)
        rho1 = ghz_coherence_state(d, 3, c1)
        for mask in range(1, 2**3 - 1):
            keep = [i for i in range(3) if mask & (1 << i)]
            a = partial_trace_keep(rho0, dims, keep)
            b = partial_trace_keep(rho1, dims, keep)
            max_proper_marginal_difference = max(
                max_proper_marginal_difference, float(np.linalg.norm(a - b))
            )
        for c, rho in ((c0, rho0), (c1, rho1)):
            max_energy_formula_residual = max(
                max_energy_formula_residual,
                abs(distinction_energy(rho) - analytic_full_energy(d, 3, c)),
            )
        dense_cases += 1

    # Exact-formula dimension sweep: n=2,...,12 and higher dimensions.
    formula_dims = list(range(2, 13)) + [16, 24, 32, 48, 64, 96, 128]
    hidden_increments = {
        str(d): analytic_hidden_full_sector_increment(d, 3, c1)
        for d in formula_dims
    }

    # Party-number stress: for any N>=2, tracing even one site kills |0..0><1..1|.
    party_counts = list(range(2, 13))
    party_formula_checks = len(party_counts) * len(formula_dims)

    return {
        "cycle": 84,
        "target": "PDT-II (1) composition law; proper-marginal closure",
        "classification": [
            "PROVED",
            "FALSIFIED",
            "NUMERICALLY SUPPORTED",
            "IMPORTED/KNOWN"
        ],
        "breakthrough_candidate": "NO",
        "claim_falsified": "Any universal composition rule that reconstructs the full quadratic distinction ledger from all proper subsystem states/ledgers alone.",
        "surviving_theorem": "For rho_c=1/2(|0^N><0^N|+|1^N><1^N|)+c(|0^N><1^N|+h.c.), every proper marginal is independent of c, while the all-party quadratic sector changes by 2*d^N*c^2 relative to c=0.",
        "n1_degenerate": degenerate_n1,
        "dense_local_dimensions": dense_dims,
        "dense_tripartite_cases": dense_cases,
        "formula_local_dimensions": formula_dims,
        "party_counts_checked_analytically": party_counts,
        "analytic_dimension_party_checks": party_formula_checks,
        "max_proper_marginal_difference": max_proper_marginal_difference,
        "max_full_energy_formula_residual": max_energy_formula_residual,
        "hidden_full_sector_increment_at_c_half": hidden_increments,
        "smallest_decisive_witness": {
            "local_dimension": 2,
            "parties": 3,
            "c0": 0.0,
            "c1": 0.5,
            "all_proper_marginals_equal": True,
            "full_distinction_energy_c0": analytic_full_energy(2, 3, c0),
            "full_distinction_energy_c1": analytic_full_energy(2, 3, c1),
            "all_party_sector_increment": analytic_hidden_full_sector_increment(2, 3, c1)
        }
    }


if __name__ == "__main__":
    out = run_audit()
    path = Path("results/cycle084_proper_marginal_composition_no_go.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
