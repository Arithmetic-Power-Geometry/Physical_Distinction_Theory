"""Cycle 097: operational record separation and revelation-rank law.

For a fixed finite-dimensional composition-defect subspace W, scalar operational
records define a linear map L_R: W -> R^m. Full defect detection is equivalent
to injectivity of L_R on W. Rank-nullity yields an exact resource-indexed
revelation law when refinement enlarges the record family while W stays fixed.

The octonion associator sector gives an exact stress test: its basis
associators span all seven imaginary directions. Thus the scalar/unit record
has rank zero on this sector, and fewer than seven independent scalar linear
records cannot detect every octonionic associator.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from cycle095_octonion_alternative_boundary import DIMS, associator


def associator_matrix() -> np.ndarray:
    """Rows are the 512 ordered octonion basis associators."""
    e = np.eye(8)
    return np.asarray(
        [associator(e[i], e[j], e[k])
         for i in range(8) for j in range(8) for k in range(8)],
        dtype=float,
    )


def octonion_exact_audit() -> dict:
    a = associator_matrix()
    nonzero = np.linalg.norm(a, axis=1) > 0.0
    rank = int(np.linalg.matrix_rank(a))
    scalar_rank = int(np.linalg.matrix_rank(a[:, :1]))
    witnesses = {}
    e = np.eye(8)
    for r in range(1, 8):
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    v = associator(e[i], e[j], e[k])
                    if np.array_equal(np.abs(v), 2.0 * e[r]):
                        witnesses[str(r)] = {
                            "indices": [i, j, k],
                            "associator": v.tolist(),
                        }
                        break
                if str(r) in witnesses:
                    break
            if str(r) in witnesses:
                break
    return {
        "basis_triples": 8 ** 3,
        "nonzero_basis_associators": int(np.count_nonzero(nonzero)),
        "associator_span_rank": rank,
        "scalar_record_rank_on_associator_span": scalar_rank,
        "minimum_independent_scalar_records_for_full_detection": rank,
        "basis_direction_witnesses": witnesses,
    }


def revelation_counts(record_matrix: np.ndarray, defect_basis: np.ndarray) -> dict:
    """Exact finite-dimensional rank/nullity accounting up to floating rank."""
    record_matrix = np.asarray(record_matrix, dtype=float)
    defect_basis = np.asarray(defect_basis, dtype=float)
    if record_matrix.ndim != 2 or defect_basis.ndim != 2:
        raise ValueError("record_matrix and defect_basis must be matrices")
    if record_matrix.shape[1] != defect_basis.shape[1]:
        raise ValueError("ambient dimensions must agree")
    wdim = int(np.linalg.matrix_rank(defect_basis))
    restricted = record_matrix @ defect_basis.T
    revealed = 0 if restricted.size == 0 else int(np.linalg.matrix_rank(restricted))
    hidden = wdim - revealed
    return {
        "defect_dimension": wdim,
        "revealed_rank": revealed,
        "hidden_dimension": hidden,
        "rank_nullity_sum": revealed + hidden,
        "separating": bool(hidden == 0),
    }


def canonical_dimension_stress() -> list[dict]:
    rows = []
    for n in DIMS:
        defect_basis = np.eye(n)
        records = np.eye(n)[: max(n - 1, 0)]
        row = revelation_counts(records, defect_basis)
        row["records"] = max(n - 1, 0)
        rows.append(row)
    return rows


def octonion_refinement_curve() -> list[dict]:
    """Add imaginary coordinate records one by one."""
    defect_basis = np.eye(8)[1:]
    rows = []
    for m in range(0, 8):
        records = np.eye(8)[1 : 1 + m]
        row = revelation_counts(records, defect_basis)
        row["imaginary_records"] = m
        rows.append(row)
    return rows


def expanding_defect_space_counterexample() -> dict:
    """Shows why fixed/nested W is needed for monotone hidden dimension."""
    coarse_w = np.array([[1.0, 0.0]])
    refined_w = np.eye(2)
    coarse_records = np.array([[1.0, 0.0]])
    refined_records = np.array([[1.0, 0.0]])
    coarse = revelation_counts(coarse_records, coarse_w)
    refined = revelation_counts(refined_records, refined_w)
    return {
        "coarse": coarse,
        "refined": refined,
        "hidden_dimension_increases": bool(
            refined["hidden_dimension"] > coarse["hidden_dimension"]
        ),
    }


def generate() -> dict:
    return {
        "cycle": 97,
        "target": (
            "PDT-II targets (1)/(4): separating operational records for "
            "composition defects and resource-refinement revelation law"
        ),
        "classification": [
            "PROVED",
            "FALSIFIED",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
            "OPEN",
        ],
        "breakthrough_candidate": False,
        "exact_result": {
            "separation_theorem": (
                "For fixed finite-dimensional defect subspace W and scalar "
                "linear record map L_R:W->R^m, every nonzero defect is detected "
                "iff L_R|_W is injective, equivalently rank(L_R|_W)=dim(W). "
                "Therefore m>=dim(W) is necessary."
            ),
            "falsified_candidate": (
                "A scalar readout or any subcomplete family of fewer than "
                "dim(W) scalar linear records can universally certify absence "
                "of composition defects on W."
            ),
            "rank_nullity_revelation_law": (
                "rev_R+hid_R=dim(W), with rev_R=rank(L_R|_W) and "
                "hid_R=dim(W intersect ker L_R). If refinement only adds "
                "records while W stays fixed, rev is nondecreasing, hid is "
                "nonincreasing, and Delta rev=-Delta hid."
            ),
            "boundary": (
                "If the admissible defect space W itself expands under resource "
                "refinement, hidden-defect monotonicity can fail without an "
                "additional compatibility axiom."
            ),
        },
        "octonion_exact_audit": octonion_exact_audit(),
        "octonion_refinement_curve": octonion_refinement_curve(),
        "dimension_stress": canonical_dimension_stress(),
        "expanding_defect_space_counterexample": expanding_defect_space_counterexample(),
        "prior_art_boundary": (
            "Injectivity/rank-nullity is standard finite-dimensional linear "
            "algebra and operationally parallels informational completeness "
            "and tomography. Octonion nonassociativity is classical. No PDT "
            "novelty is claimed for these mathematical ingredients."
        ),
        "open": (
            "Derive from PDT primitives which record family is physically "
            "available at resource R, whether the defect space is fixed/nested "
            "under refinement, and whether record rank produces a same-input "
            "prediction distinct from quantum mechanics."
        ),
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle097_associator_record_separation.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
