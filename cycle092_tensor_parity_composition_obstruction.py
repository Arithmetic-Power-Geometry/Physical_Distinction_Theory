"""Cycle 092: tensor-parity obstruction for antisymmetric-only composition.

This cycle attacks PDT-II target (1), the native composition law.

Exact theorem
-------------
Let A_i: V_i x V_i -> V_i be bilinear maps with definite exchange parity

    A_i(y,x) = eps_i A_i(x,y),   eps_i in {+1,-1}.

For the factorized composite bilinear map on pure tensors

    C(x1⊗...⊗xN, y1⊗...⊗yN)
      = A_1(x1,y1) ⊗ ... ⊗ A_N(xN,yN),

bilinear extension gives exchange parity prod_i eps_i.  Hence a tensor product
of two antisymmetric local closures is SYMMETRIC, not antisymmetric.  More
generally, a factorized N-partite term is antisymmetric iff it contains an odd
number of antisymmetric local factors.

Consequences for PDT
--------------------
A primitive alternating closure B cannot compose bipartitely by the naive rule
B_AB = B_A ⊗ B_B.  Any linear combination made only of such two-local
antisymmetric⊗antisymmetric factors remains symmetric.  Its antisymmetrization
vanishes identically.  To obtain a nonzero factorized alternating composite
term, one needs an odd exchange parity: e.g. an antisymmetric local product B
paired with an independently supplied symmetric product S.

This is a structural no-go for an *antisymmetric-only factorized* PDT
composition proposal, not a no-go for all possible composition laws.  The
mathematics is standard tensor/exchange-parity algebra; Lie-Jordan operator
composition is prior art showing exactly this symmetric/antisymmetric pairing.
"""

from __future__ import annotations

import json
from typing import Dict, Iterable, List, Sequence, Tuple

import numpy as np

AUDIT_DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]

Vector = np.ndarray
PureTerm = Tuple[Vector, Vector]


def alternating_map(x: Vector, y: Vector) -> Vector:
    """Cheap nonzero alternating map for every dimension n>=2.

    It is deliberately not assumed to satisfy a norm, Jacobi, or covariance
    axiom; Cycle 092 concerns exchange parity only.
    """
    if x.shape != y.shape:
        raise ValueError("shape mismatch")
    out = np.zeros_like(x, dtype=float)
    if x.size >= 2:
        out[0] = x[0] * y[1] - x[1] * y[0]
    return out


def symmetric_map(x: Vector, y: Vector) -> Vector:
    """A simple nonzero symmetric companion: <x,y> e_0."""
    if x.shape != y.shape:
        raise ValueError("shape mismatch")
    out = np.zeros_like(x, dtype=float)
    if x.size:
        out[0] = float(np.dot(x, y))
    return out


def factorized_bilinear(
    z_terms: Sequence[PureTerm],
    w_terms: Sequence[PureTerm],
    left_map,
    right_map,
) -> np.ndarray:
    """Evaluate the bilinear extension of left_map ⊗ right_map.

    Each argument is represented as a finite sum of pure tensors (x,u).
    The returned n x n matrix represents the composite vector in V⊗V.
    This avoids materializing an n^2-dimensional vector for high n.
    """
    if not z_terms or not w_terms:
        raise ValueError("arguments must contain at least one pure term")
    n = z_terms[0][0].size
    out = np.zeros((n, n), dtype=float)
    for x, u in z_terms:
        for y, v in w_terms:
            out += np.outer(left_map(x, y), right_map(u, v))
    return out


def repaired_composite(z_terms: Sequence[PureTerm], w_terms: Sequence[PureTerm]) -> np.ndarray:
    """One parity-correct example: B⊗S + S⊗B."""
    return (
        factorized_bilinear(z_terms, w_terms, alternating_map, symmetric_map)
        + factorized_bilinear(z_terms, w_terms, symmetric_map, alternating_map)
    )


def exact_parity(epsilons: Iterable[int]) -> int:
    parity = 1
    for eps in epsilons:
        if eps not in (-1, 1):
            raise ValueError("exchange parity must be +/-1")
        parity *= eps
    return parity


def explicit_dimension_witness(n: int) -> Dict[str, object]:
    """Return decisive witnesses in dimension n.

    For n>=2 set z=e0⊗e0 + e1⊗e1.  With B(e0,e1)=e0,

        (B⊗B)(z,z) = 2 e0⊗e0 != 0,

    so B⊗B is not alternating.  The same example works in every n>=2.
    A B⊗S+S⊗B composite is checked to be nonzero and alternating.
    """
    if n < 1:
        raise ValueError("dimension must be positive")
    e0 = np.zeros(n)
    e0[0] = 1.0
    if n == 1:
        return {
            "n": 1,
            "degenerate": True,
            "bb_diagonal_witness_norm": 0.0,
            "bb_swap_sum_norm": 0.0,
            "parity_repair_swap_sum_norm": 0.0,
            "parity_repair_nonzero_norm": 0.0,
        }

    e1 = np.zeros(n)
    e1[1] = 1.0

    z = [(e0, e0), (e1, e1)]
    bb_zz = factorized_bilinear(z, z, alternating_map, alternating_map)

    a = [(e0, e0)]
    b = [(e1, e1)]
    bb_ab = factorized_bilinear(a, b, alternating_map, alternating_map)
    bb_ba = factorized_bilinear(b, a, alternating_map, alternating_map)

    # For the repaired term choose the second subsystem equal in both inputs,
    # so S contributes while B on that subsystem vanishes.
    a_repair = [(e0, e0)]
    b_repair = [(e1, e0)]
    r_ab = repaired_composite(a_repair, b_repair)
    r_ba = repaired_composite(b_repair, a_repair)

    return {
        "n": n,
        "degenerate": False,
        "bb_diagonal_witness_norm": float(np.linalg.norm(bb_zz)),
        "bb_swap_sum_norm": float(np.linalg.norm(bb_ab + bb_ba)),
        "parity_repair_swap_sum_norm": float(np.linalg.norm(r_ab + r_ba)),
        "parity_repair_nonzero_norm": float(np.linalg.norm(r_ab)),
    }


def multipartite_parity_table(max_parties: int = 12) -> List[Dict[str, int | str]]:
    """All-local alternating factor B^{⊗N}: odd N alternating, even N symmetric."""
    rows: List[Dict[str, int | str]] = []
    for parties in range(1, max_parties + 1):
        eps = exact_parity([-1] * parties)
        rows.append(
            {
                "parties": parties,
                "exchange_parity": eps,
                "type": "alternating" if eps == -1 else "symmetric",
            }
        )
    return rows


def build_result() -> Dict[str, object]:
    dimensions = [explicit_dimension_witness(n) for n in AUDIT_DIMS]
    nondegenerate_failures = [
        row["n"] for row in dimensions
        if not row["degenerate"] and row["bb_diagonal_witness_norm"] > 1e-12
    ]
    repaired = [
        row["n"] for row in dimensions
        if not row["degenerate"]
        and row["parity_repair_swap_sum_norm"] <= 1e-12
        and row["parity_repair_nonzero_norm"] > 1e-12
    ]
    return {
        "cycle": 92,
        "target": "PDT-II target (1): PDT-native composition law",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "theorem": "A factorized tensor product of bilinear maps has exchange parity equal to the product of the local exchange parities.",
        "falsified_candidate": "nonzero bipartite alternating composite closure B_AB = B_A tensor B_B built only from alternating local closures",
        "smallest_nondegenerate_witness_dimension": 2,
        "dimension_audit": dimensions,
        "bb_failure_dimensions": nondegenerate_failures,
        "parity_repair_dimensions": repaired,
        "multipartite_all_B_parity": multipartite_parity_table(),
        "breakthrough_candidate": False,
        "open_pdt_obligation": "derive an independently motivated symmetric companion or a genuinely non-factorized composition rule; antisymmetric closure alone is insufficient for binary tensor composition",
    }


if __name__ == "__main__":
    print(json.dumps(build_result(), indent=2, sort_keys=True))
