"""Cycle 095: alternativity/norm-composition boundary audit.

Tests whether weakening associative grouping to alternative composition can still
select the 3-dimensional distinction-vector sector.

The explicit counterexample is the octonion algebra O = R ⊕ R^7.  It is:
- unital and bilinear,
- norm-composing: ||xy||^2 = ||x||^2 ||y||^2,
- alternative,
- nonassociative.

Therefore "unit + positive norm composition + alternativity" does not select
dim(V)=3: dim(V)=7 survives exactly.  This is classical Hurwitz/octonion
mathematics and is recorded as an imported/known boundary, not PDT novelty.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
HURWITZ_IMAGINARY_DIMS = {0, 1, 3, 7}


def conjugate(x: np.ndarray) -> np.ndarray:
    """Cayley-Dickson conjugation for lengths 1,2,4,8."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or x.size not in (1, 2, 4, 8):
        raise ValueError("length must be one of 1,2,4,8")
    if x.size == 1:
        return x.copy()
    h = x.size // 2
    return np.concatenate((conjugate(x[:h]), -x[h:]))


def cd_mul(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Cayley-Dickson product through octonions.

    Convention:
      (a,b)(c,d) = (ac - conjugate(d)b, da + b conjugate(c)).
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1 or x.shape != y.shape:
        raise ValueError("equal one-dimensional shapes required")
    if x.size not in (1, 2, 4, 8):
        raise ValueError("length must be one of 1,2,4,8")
    if x.size == 1:
        return x * y
    h = x.size // 2
    a, b = x[:h], x[h:]
    c, d = y[:h], y[h:]
    first = cd_mul(a, c) - cd_mul(conjugate(d), b)
    second = cd_mul(d, a) + cd_mul(b, conjugate(c))
    return np.concatenate((first, second))


def associator(x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
    return cd_mul(cd_mul(x, y), z) - cd_mul(x, cd_mul(y, z))


def basis_nonassociativity_witness() -> dict:
    """Exact integer-coordinate octonion witness: [e1,e2,e4] = 2 e7."""
    e = np.eye(8)
    a = associator(e[1], e[2], e[4])
    expected = np.zeros(8)
    expected[7] = 2.0
    return {
        "indices": [1, 2, 4],
        "associator": a.tolist(),
        "expected": expected.tolist(),
        "exact_integer_match": bool(np.array_equal(a, expected)),
        "norm": float(np.linalg.norm(a)),
    }


def basis_alternativity_audit() -> dict:
    """Exact basis check of left/right/flexible alternativity in O."""
    e = np.eye(8)
    max_left = max_right = max_flexible = 0.0
    violations = []
    for i in range(8):
        for j in range(8):
            left = associator(e[i], e[i], e[j])
            right = associator(e[j], e[i], e[i])
            flex = associator(e[i], e[j], e[i])
            vals = (float(np.linalg.norm(left)),
                    float(np.linalg.norm(right)),
                    float(np.linalg.norm(flex)))
            max_left = max(max_left, vals[0])
            max_right = max(max_right, vals[1])
            max_flexible = max(max_flexible, vals[2])
            if any(v != 0.0 for v in vals):
                violations.append({"i": i, "j": j, "residuals": vals})
    return {
        "basis_pairs": 64,
        "max_left_residual": max_left,
        "max_right_residual": max_right,
        "max_flexible_residual": max_flexible,
        "violations": violations,
    }


def random_octonion_audit(trials: int = 3000, seed: int = 9507) -> dict:
    rng = np.random.default_rng(seed)
    max_norm_residual = 0.0
    max_left_alt = 0.0
    max_right_alt = 0.0
    max_flexible = 0.0
    max_generic_assoc = 0.0
    nonassoc_count = 0

    for _ in range(trials):
        x = rng.normal(size=8)
        y = rng.normal(size=8)
        z = rng.normal(size=8)
        x /= np.linalg.norm(x)
        y /= np.linalg.norm(y)
        z /= np.linalg.norm(z)

        xy = cd_mul(x, y)
        norm_res = abs(float(np.dot(xy, xy) - np.dot(x, x) * np.dot(y, y)))
        max_norm_residual = max(max_norm_residual, norm_res)

        la = float(np.linalg.norm(associator(x, x, y)))
        ra = float(np.linalg.norm(associator(y, x, x)))
        fl = float(np.linalg.norm(associator(x, y, x)))
        ga = float(np.linalg.norm(associator(x, y, z)))
        max_left_alt = max(max_left_alt, la)
        max_right_alt = max(max_right_alt, ra)
        max_flexible = max(max_flexible, fl)
        max_generic_assoc = max(max_generic_assoc, ga)
        if ga > 1e-10:
            nonassoc_count += 1

    return {
        "trials": trials,
        "max_norm_multiplicativity_residual": max_norm_residual,
        "max_left_alternativity_residual": max_left_alt,
        "max_right_alternativity_residual": max_right_alt,
        "max_flexible_residual": max_flexible,
        "max_generic_associator_norm": max_generic_assoc,
        "generic_nonassociative_cases_gt_1e-10": nonassoc_count,
    }


def dimension_ledger() -> list[dict]:
    rows = []
    for n in DIMS:
        rows.append({
            "distinction_vector_dimension_n": n,
            "full_algebra_dimension_n_plus_1": n + 1,
            "hurwitz_normed_division_dimension_allowed":
                n in HURWITZ_IMAGINARY_DIMS,
            "note": (
                "classical allowed case"
                if n in HURWITZ_IMAGINARY_DIMS
                else "excluded under positive-definite real normed-division-algebra hypotheses"
            ),
        })
    return rows


def generate() -> dict:
    witness = basis_nonassociativity_witness()
    basis_alt = basis_alternativity_audit()
    random_audit = random_octonion_audit()
    return {
        "cycle": 95,
        "target": "PDT-II targets (1)/(2): test alternative rather than associative scalar/unit composition",
        "classification": [
            "PROVED",
            "FALSIFIED",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
            "OPEN",
        ],
        "breakthrough_candidate": False,
        "exact_result": {
            "falsified_candidate": (
                "Unital bilinear positive-norm-composing alternative composition "
                "selects distinction-vector dimension n=3."
            ),
            "counterexample": (
                "Octonions O=R⊕R^7 satisfy unital bilinearity, positive Euclidean "
                "norm composition, and alternativity, but are nonassociative."
            ),
            "smallest_relevant_surviving_higher_dimension": 7,
            "basis_nonassociativity_witness": witness,
            "basis_alternativity_audit": basis_alt,
            "consequence": (
                "If PDT weakens associative grouping to alternativity while allowing "
                "the octonionic/G2 reversible boundary, n=7 survives. Associativity "
                "or an independently derived stronger symmetry/operational principle "
                "is therefore doing indispensable selection work in the Cycle-094 n=3 route."
            ),
        },
        "dimension_ledger": dimension_ledger(),
        "random_octonion_regression": random_audit,
        "prior_art_boundary": (
            "Hurwitz/classical normed-division-algebra theory permits real algebra "
            "dimensions 1,2,4,8 (imaginary/vector dimensions 0,1,3,7). The octonions "
            "are the 8-dimensional alternative nonassociative case; their automorphism "
            "group is G2. These facts are imported/known, not PDT novelty."
        ),
        "open": (
            "Derive from PDT primitives whether operational composition must be fully "
            "associative, merely alternative, or resource-indexed/nonassociative; then "
            "test the surviving law against composites, restricted resources and "
            "same-input experimental predictions."
        ),
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle095_octonion_alternative_boundary.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
