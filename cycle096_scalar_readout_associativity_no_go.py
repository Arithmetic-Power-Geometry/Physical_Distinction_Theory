"""Cycle 096: scalar-readout associativity no-go.

Tests a natural weakening of full operational associativity: require grouping
independence only after projecting the scalar/unit readout.

The octonions provide an exact counterexample. Their associator is purely
imaginary, so Re((xy)z) = Re(x(yz)) for all x,y,z, even though the full
associator is generically nonzero. Therefore scalar-readout associativity,
even combined with unital bilinearity, positive norm composition and
alternativity, does not exclude the n=7 distinction-vector sector.

This is classical octonion/composition-algebra mathematics and is classified
as an imported/known boundary, not PDT novelty.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

from cycle095_octonion_alternative_boundary import DIMS, HURWITZ_IMAGINARY_DIMS, associator


def exact_basis_audit() -> dict:
    e = np.eye(8)
    max_scalar_associator = 0.0
    max_full_associator = 0.0
    nonzero_full = 0
    first_witness = None
    for i in range(8):
        for j in range(8):
            for k in range(8):
                a = associator(e[i], e[j], e[k])
                scalar = abs(float(a[0]))
                full = float(np.linalg.norm(a))
                max_scalar_associator = max(max_scalar_associator, scalar)
                max_full_associator = max(max_full_associator, full)
                if full != 0.0:
                    nonzero_full += 1
                    if first_witness is None:
                        first_witness = {"indices": [i, j, k], "associator": a.tolist(), "norm": full, "scalar_part": float(a[0])}
    return {"basis_triples": 8 ** 3, "max_abs_scalar_associator": max_scalar_associator, "max_full_associator_norm": max_full_associator, "nonzero_full_associator_basis_triples": nonzero_full, "first_nonassociative_scalar_invisible_witness": first_witness}


def random_audit(trials: int = 5000, seed: int = 9607) -> dict:
    rng = np.random.default_rng(seed)
    max_scalar = 0.0
    max_full = 0.0
    nonzero_full = 0
    for _ in range(trials):
        x = rng.normal(size=8); y = rng.normal(size=8); z = rng.normal(size=8)
        x /= np.linalg.norm(x); y /= np.linalg.norm(y); z /= np.linalg.norm(z)
        a = associator(x, y, z)
        max_scalar = max(max_scalar, abs(float(a[0])))
        full = float(np.linalg.norm(a))
        max_full = max(max_full, full)
        if full > 1e-10:
            nonzero_full += 1
    return {"trials": trials, "seed": seed, "max_abs_scalar_associator": max_scalar, "max_full_associator_norm": max_full, "nonzero_full_associator_cases_gt_1e-10": nonzero_full}


def dimension_ledger() -> list[dict]:
    return [{"distinction_vector_dimension_n": n, "full_algebra_dimension_n_plus_1": n + 1, "hurwitz_positive_normed_division_case": n in HURWITZ_IMAGINARY_DIMS, "scalar_readout_associativity_excludes_n": False if n == 7 else None} for n in DIMS]


def generate() -> dict:
    return {
        "cycle": 96,
        "target": "PDT-II targets (1)/(2): scalar/unit-readout grouping consistency versus full associativity",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "exact_result": {
            "falsified_candidate": "Unital bilinear positive-norm-composing alternative composition plus associativity of the scalar/unit readout is sufficient to exclude n=7 and select n=3.",
            "counterexample": "Octonions O=R⊕R^7 have purely imaginary associators: Re((xy)z)=Re(x(yz)) for all x,y,z, while generic full associators are nonzero.",
            "consequence": "A PDT composition axiom checked only after a scalar probability/capacity/unit projection cannot detect octonionic nonassociativity. Excluding n=7 requires full operational grouping coherence or a separating family of records/effects that can reveal the non-scalar associator sector."
        },
        "exact_basis_audit": exact_basis_audit(),
        "random_regression": random_audit(),
        "dimension_ledger": dimension_ledger(),
        "prior_art_boundary": "The octonion associator is alternating/purely imaginary and octonions are the 8-dimensional alternative normed division algebra. These are classical imported facts.",
        "open": "Derive from PDT primitives whether available records/effects separate the full composition sector. If only scalar readouts are operationally accessible, n=7 remains hidden from this test."
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle096_scalar_readout_associativity_no_go.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
