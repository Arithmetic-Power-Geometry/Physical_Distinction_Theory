"""Cycle 098: compatible refinement with defect creation.

Let U be a coarse defect space embedded in a refined defect space V, with
q = dim(V/U). Let A:U->Y be coarse records and B:V->Z refined records.
Compatibility means coarse records factor through refined records on U:
A = P B|_U for some linear P. Hence ker(B|_U) is contained in ker(A).

Writing
  r = rank(A), r_i = rank(B|_U), r_f = rank(B),
  h = dim(U)-r, h_i = dim(U)-r_i, h_f = dim(V)-r_f,
  g = r_i-r, v = r_f-r_i,
gives exact balances
  r_f-r = g+v,
  h_f-h = q-g-v,
with g>=0 and 0<=v<=q.

Therefore revealed rank cannot decrease under compatible refinement even when
new defect directions are admitted, and hidden dimension can increase by at
most q. These are linear-algebra consequences, not claimed as PDT novelty.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = [1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,48,64,96,128]


def _rank(a: np.ndarray) -> int:
    a = np.asarray(a, dtype=float)
    return 0 if a.size == 0 else int(np.linalg.matrix_rank(a))


def refinement_ledger(coarse_records: np.ndarray,
                      refined_records: np.ndarray,
                      coarse_dim: int) -> dict:
    """Coordinate model U=R^coarse_dim embedded as first coordinates of V.

    The caller is responsible for checking/constructing record compatibility.
    The returned identities themselves are purely rank-nullity statements.
    """
    A = np.asarray(coarse_records, dtype=float)
    B = np.asarray(refined_records, dtype=float)
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("record arrays must be matrices")
    if A.shape[1] != coarse_dim:
        raise ValueError("coarse_records has wrong domain dimension")
    if B.shape[1] < coarse_dim:
        raise ValueError("refined domain cannot be smaller than coarse domain")
    q = B.shape[1] - coarse_dim
    r = _rank(A)
    r_i = _rank(B[:, :coarse_dim])
    r_f = _rank(B)
    h = coarse_dim - r
    h_i = coarse_dim - r_i
    h_f = coarse_dim + q - r_f
    g = r_i - r
    v = r_f - r_i
    return {
        "coarse_dim": coarse_dim,
        "new_defect_dim": q,
        "coarse_revealed": r,
        "inherited_revealed": r_i,
        "refined_revealed": r_f,
        "coarse_hidden": h,
        "inherited_hidden": h_i,
        "refined_hidden": h_f,
        "inherited_revelation_gain": g,
        "new_sector_visible_gain": v,
        "revealed_delta": r_f - r,
        "hidden_delta": h_f - h,
        "exact_revealed_balance": (r_f - r) == g + v,
        "exact_hidden_balance": (h_f - h) == q - g - v,
        "compatible_consequences_hold": (
            g >= 0 and 0 <= v <= q and r_f >= r and h_f <= h + q
        ),
    }


def canonical_compatible_case(n: int, q: int) -> dict:
    """Construct a refinement that retains all coarse record rows exactly."""
    if n < 1 or q < 0:
        raise ValueError("n>=1 and q>=0 required")
    r = max(1, n // 2)
    A = np.zeros((r, n))
    A[np.arange(r), np.arange(r)] = 1.0

    # First r rows restrict exactly to A. Added rows may reveal inherited
    # hidden directions and directions in the new quotient V/U.
    extra = min(q + 1, (n - r) + q)
    B = np.zeros((r + extra, n + q))
    B[:r, :n] = A
    row = r
    if r < n and row < B.shape[0]:
        B[row, r] = 1.0
        row += 1
    j = 0
    while row < B.shape[0] and j < q:
        B[row, n + j] = 1.0
        row += 1
        j += 1

    out = refinement_ledger(A, B, n)
    out["coarse_rows_retained_exactly"] = bool(np.array_equal(B[:r, :n], A))
    return out


def randomized_compatible_stress(seed: int = 9801, trials: int = 400) -> dict:
    """Numerical stress with compatible records and variable defect growth."""
    rng = np.random.default_rng(seed)
    failures = []
    max_n = 0
    for t in range(trials):
        n = int(rng.integers(1, 65))
        q = int(rng.integers(0, 9))
        m = int(rng.integers(1, min(n, 8) + 1))
        A = rng.integers(-2, 3, size=(m, n)).astype(float)

        # Compatibility is stronger than required here: all coarse rows are
        # literally retained in the refined map on U.
        top_new = rng.integers(-2, 3, size=(m, q)).astype(float)
        extra_rows = int(rng.integers(0, 9))
        bottom = rng.integers(-2, 3, size=(extra_rows, n + q)).astype(float)
        B = np.block([[A, top_new], [bottom]]) if extra_rows else np.hstack([A, top_new])
        led = refinement_ledger(A, B, n)
        if not led["compatible_consequences_hold"]:
            failures.append({"trial": t, **led})
        max_n = max(max_n, n)
    return {
        "seed": seed,
        "trials": trials,
        "max_dimension_tested": max_n,
        "failures": failures,
        "all_pass": not failures,
    }


def incompatible_record_counterexample() -> dict:
    """Smallest witness that compatibility is essential for rank monotonicity."""
    A = np.array([[1.0]])
    B = np.array([[0.0]])
    return {
        "coarse_dim": 1,
        "coarse_record": A.tolist(),
        "refined_record": B.tolist(),
        "coarse_revealed": _rank(A),
        "refined_revealed": _rank(B),
        "revealed_rank_decreases": bool(_rank(B) < _rank(A)),
        "interpretation": (
            "If refinement is allowed to discard/degrade an old record, "
            "revealed rank can fall even without defect-space growth."
        ),
    }


def dimension_stress() -> list[dict]:
    rows = []
    for n in DIMS:
        qs = sorted(set([0, 1, 2, min(4, n)]))
        for q in qs:
            rows.append(canonical_compatible_case(n, q))
    return rows


def generate() -> dict:
    rows = dimension_stress()
    random = randomized_compatible_stress()
    all_exact = all(
        row["coarse_rows_retained_exactly"]
        and row["exact_revealed_balance"]
        and row["exact_hidden_balance"]
        and row["compatible_consequences_hold"]
        for row in rows
    )
    return {
        "cycle": 98,
        "target": "PDT-II (1)/(4): compatible refinement when defect spaces grow",
        "classification": [
            "PROVED", "CONDITIONAL", "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED", "FALSIFIED", "OPEN"
        ],
        "breakthrough_candidate": False,
        "theorem": {
            "hypotheses": (
                "U embeds in V; q=dim(V/U). Coarse A:U->Y and refined "
                "B:V->Z are record-compatible: A=P(B|U) for some P."
            ),
            "exact_balances": [
                "Delta revealed = inherited revelation gain + new-sector visible gain",
                "Delta hidden = q - inherited revelation gain - new-sector visible gain",
            ],
            "consequences": [
                "refined revealed rank >= coarse revealed rank",
                "refined hidden dimension <= coarse hidden dimension + q",
                "when q=0 this reduces to Cycle 097 fixed-space monotonicity",
            ],
        },
        "falsified_unqualified_claim": (
            "Revealed rank is nondecreasing under arbitrary things called "
            "resource refinements. False without record compatibility."
        ),
        "smallest_counterexample": incompatible_record_counterexample(),
        "dimension_stress_cases": len(rows),
        "dimension_stress_all_pass": all_exact,
        "dimension_stress": rows,
        "randomized_stress": random,
        "prior_art_boundary": (
            "The proof is rank-nullity/exact-sequence linear algebra. Nested "
            "vector spaces and compatible maps are standard filtration/"
            "persistence structures. No mathematical novelty is claimed."
        ),
        "open": (
            "PDT must derive, rather than assume, why physical resource "
            "refinement induces an embedding of defect spaces and a compatible "
            "record map. Only then may this accounting become PDT-native."
        ),
    }


if __name__ == "__main__":
    data = generate()
    p = Path("results/cycle098_compatible_refinement_defect_creation.json")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
