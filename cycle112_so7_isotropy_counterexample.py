"""Cycle 112: explicit SO(7) counterexample for octonionic cross-product isotropy.

Purpose
-------
Cycle 089 already established the imported/conditional selector that a nonzero
SO(n)-equivariant alternating bilinear map R^n x R^n -> R^n is possible only
for n=3.  This cycle does NOT repeat that result as a novelty claim.  Instead it
records the smallest explicit proper-rotation witness showing why the familiar
7D octonionic cross product cannot rescue full SO(7) covariance.

With the standard imaginary-octonion convention e1 x e2 = e3, let R swap
(e1,e2) and also swap (e4,e5).  Two transpositions give det(R)=+1, so R is a
proper orthogonal transformation.  But

    (R e1) x (R e2) = e2 x e1 = -e3,
    R(e1 x e2) = R e3 = +e3,

hence the covariance residual has norm 2.

Prior-art boundary
------------------
The 7D cross product and its G2 stabilizer are standard octonion mathematics.
This file is a PDT counterexample/catalog artifact, not a mathematical novelty
claim.  It sharpens the PDT obligation: any non-circular n=3 route using full
proper-rotation covariance must derive that physical symmetry premise from PDT;
one cannot appeal merely to the existence of a normed 7D cross product.
"""
from __future__ import annotations

import json
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def cross7_basis(i: int, j: int) -> np.ndarray:
    """Standard imaginary-octonion cross product on basis indices 0..6."""
    if i == j:
        return np.zeros(7)
    triples = [
        (0, 1, 2), (0, 3, 4), (0, 6, 5),
        (1, 3, 5), (1, 4, 6), (2, 3, 6), (2, 5, 4),
    ]
    out = np.zeros(7)
    for a, b, c in triples:
        cyclic = {(a, b): c, (b, c): a, (c, a): b}
        anti = {(b, a): c, (c, b): a, (a, c): b}
        if (i, j) in cyclic:
            out[cyclic[(i, j)]] = 1.0
            return out
        if (i, j) in anti:
            out[anti[(i, j)]] = -1.0
            return out
    raise RuntimeError((i, j))


def explicit_so7_witness() -> dict:
    """Return a determinant +1 rotation that violates 7D cross covariance."""
    R = np.eye(7)
    R[[0, 1]] = R[[1, 0]]
    R[[3, 4]] = R[[4, 3]]

    lhs = cross7_basis(1, 0)       # cross(R e1, R e2)
    rhs = R @ cross7_basis(0, 1)   # R cross(e1,e2)
    return {
        "det_R": float(round(np.linalg.det(R))),
        "orthogonality_residual": float(np.linalg.norm(R.T @ R - np.eye(7))),
        "lhs_cross_Re1_Re2": lhs.tolist(),
        "rhs_R_cross_e1_e2": rhs.tolist(),
        "covariance_residual": float(np.linalg.norm(lhs - rhs)),
        "is_SO7": bool(np.allclose(R.T @ R, np.eye(7)) and np.linalg.det(R) > 0),
    }


def dimension_stress_ledger() -> list[dict]:
    """Ledger linking this witness to the already-known Cycle-089 selector.

    This is deliberately a theorem-status ledger, not a new proof routine.  The
    full SO(n)-equivariant vector-valued alternating selector was already
    audited in Cycle 089; Cycle 112 adds the explicit n=7 obstruction.
    """
    rows = []
    for n in DIMS:
        rows.append({
            "n": n,
            "full_SO_n_vector_cross_product_candidate": n == 3,
            "status": "SURVIVES_IMPORTED_SELECTOR" if n == 3 else "EXCLUDED_BY_IMPORTED_SELECTOR",
        })
    return rows


def generate() -> dict:
    witness = explicit_so7_witness()
    return {
        "cycle": 112,
        "targets": [1, 2],
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "OPEN"],
        "breakthrough_candidate": False,
        "decisive_counterexample": {
            "status": "FALSIFIED",
            "claim": "The standard 7D octonionic cross product is equivariant under the full SO(7) group.",
            "witness": witness,
        },
        "dimension_stress_ledger": dimension_stress_ledger(),
        "prior_art_boundary": (
            "The imaginary-octonion cross product and the fact that its linear symmetry group is G2, "
            "a proper subgroup of SO(7), are imported/known mathematics. No novelty is claimed."
        ),
        "pdt_consequence": (
            "The n=7 normed-cross-product branch cannot satisfy full SO(7) covariance. "
            "Thus full proper-rotation covariance would eliminate n=7, but PDT still has to derive "
            "full SO(n) covariance and vector-valued alternating closure non-circularly."
        ),
        "next_obligation": (
            "Derive or falsify the full-SO(n) covariance premise from PDT operational/reversible "
            "distinction primitives without assuming a cross product, Hodge duality, or generator-state dimension equality."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(generate(), indent=2, sort_keys=True))
