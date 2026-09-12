"""Cycle 099: separating records diagnose composition defects; they do not enforce associativity.

This cycle attacks a tempting bridge left by Cycles 095--098: perhaps a
tomographically complete / separating record family could eliminate the n=7
octonionic alternative and thereby help select n=3.  It cannot.

General observation-enforcement separation theorem:
Let delta:X->W be any composition-defect map and L:W->Y be injective. Then
L(delta(x))=0 iff delta(x)=0. Injectivity makes defects certifiable when their
record is observed, but places no equation on delta that forces it to vanish.

The octonions provide the relevant exact counterexample. Their associators span
the full seven-dimensional imaginary sector. The seven imaginary coordinate
records are injective on that sector and detect every nonzero basis associator,
yet the algebra remains alternative, norm-composing, and nonassociative.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from cycle095_octonion_alternative_boundary import DIMS, associator
from cycle097_associator_record_separation import associator_matrix


def full_imaginary_records(v: np.ndarray) -> np.ndarray:
    """Seven-coordinate separating record map on the octonion defect sector."""
    v = np.asarray(v, dtype=float)
    if v.shape != (8,):
        raise ValueError("octonion vector must have shape (8,)")
    return v[1:].copy()


def exact_octonion_audit() -> dict:
    a = associator_matrix()
    norms = np.linalg.norm(a, axis=1)
    nonzero = norms > 0.0
    records = a[:, 1:]
    record_norms = np.linalg.norm(records, axis=1)
    missed = np.logical_and(nonzero, record_norms == 0.0)

    e = np.eye(8)
    witness = associator(e[1], e[2], e[4])
    witness_record = full_imaginary_records(witness)

    return {
        "basis_triples": 8 ** 3,
        "nonzero_basis_associators": int(np.count_nonzero(nonzero)),
        "associator_span_rank": int(np.linalg.matrix_rank(a)),
        "full_record_rank_on_defect_sector": int(np.linalg.matrix_rank(records)),
        "missed_nonzero_basis_associators": int(np.count_nonzero(missed)),
        "scalar_components_all_zero_exactly": bool(np.all(a[:, 0] == 0.0)),
        "witness_indices": [1, 2, 4],
        "witness_associator": witness.tolist(),
        "witness_record": witness_record.tolist(),
        "witness_record_norm": float(np.linalg.norm(witness_record)),
        "associative_despite_separating_records": False,
    }


def generic_rank_stress() -> list[dict]:
    """Dimension audit of the logical separation fact for n=1..12 and higher."""
    rows = []
    for n in DIMS:
        # Identity records are maximally separating on an n-dimensional defect space.
        L = np.eye(n)
        defect = np.arange(1, n + 1, dtype=float)
        rows.append({
            "defect_dimension": n,
            "record_rank": int(np.linalg.matrix_rank(L)),
            "separating": bool(np.linalg.matrix_rank(L) == n),
            "nonzero_defect_exists": bool(np.linalg.norm(defect) > 0.0),
            "nonzero_record_exists": bool(np.linalg.norm(L @ defect) > 0.0),
            "logical_consequence": "detection_not_enforcement",
        })
    return rows


def random_octonion_record_audit(trials: int = 3000, seed: int = 9907) -> dict:
    rng = np.random.default_rng(seed)
    max_scalar_component = 0.0
    max_record_vs_full_norm_gap = 0.0
    max_associator_norm = 0.0
    min_detected_record_norm = float("inf")
    detected_nonzero = 0

    for _ in range(trials):
        xyz = []
        for _ in range(3):
            x = rng.normal(size=8)
            x /= np.linalg.norm(x)
            xyz.append(x)
        a = associator(*xyz)
        full_norm = float(np.linalg.norm(a))
        record_norm = float(np.linalg.norm(full_imaginary_records(a)))
        max_scalar_component = max(max_scalar_component, abs(float(a[0])))
        max_record_vs_full_norm_gap = max(
            max_record_vs_full_norm_gap, abs(record_norm - full_norm)
        )
        max_associator_norm = max(max_associator_norm, full_norm)
        if full_norm > 1e-10:
            detected_nonzero += 1
            min_detected_record_norm = min(min_detected_record_norm, record_norm)

    return {
        "trials": trials,
        "detected_nonzero_associators_gt_1e-10": detected_nonzero,
        "max_scalar_component_abs": max_scalar_component,
        "max_record_vs_full_norm_gap": max_record_vs_full_norm_gap,
        "max_associator_norm": max_associator_norm,
        "min_detected_record_norm": min_detected_record_norm,
    }


def generate() -> dict:
    return {
        "cycle": 99,
        "target": (
            "PDT-II targets (1)/(2)/(4): test whether complete/separating "
            "operational records can enforce associativity and remove n=7"
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
            "proved_theorem": (
                "For any defect map delta:X->W and injective linear record map "
                "L:W->Y, L(delta(x))=0 iff delta(x)=0. Separating records "
                "therefore provide faithful diagnosis/certification, not a law "
                "forcing delta to vanish."
            ),
            "falsified_candidate": (
                "Unital bilinear positive-norm-composing alternative composition "
                "plus a tomographically complete/separating operational record "
                "family selects n=3 or enforces associativity."
            ),
            "counterexample": (
                "O=R+R^7 with its seven imaginary-coordinate records. The record "
                "map is injective on the full associator span, while nonzero "
                "associators remain; hence n=7 survives complete defect visibility."
            ),
            "consequence": (
                "PDT cannot obtain associative composition or n=3 merely by "
                "deriving informationally complete records. It needs a separate "
                "dynamical/compositional principle that suppresses, quotients, or "
                "operationally forbids nonzero defects."
            ),
        },
        "octonion_exact_audit": exact_octonion_audit(),
        "dimension_stress": generic_rank_stress(),
        "random_octonion_record_audit": random_octonion_record_audit(),
        "prior_art_boundary": (
            "The logical injectivity statement is elementary linear algebra. "
            "Octonion alternativity, norm composition and nonassociativity are "
            "classical. This cycle claims no historical novelty for those facts; "
            "its role is to falsify a specific PDT derivation route."
        ),
        "open": (
            "Derive or falsify a PDT-native law that constrains the defect itself "
            "rather than only observing it: e.g. an operational path-independence, "
            "coherent composition, or resource-cost principle strong enough to "
            "exclude the octonionic sector without assuming associativity by fiat."
        ),
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle099_record_completeness_not_associativity.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
