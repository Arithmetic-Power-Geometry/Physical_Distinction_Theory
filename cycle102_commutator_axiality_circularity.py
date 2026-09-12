"""Cycle 102: sequential-commutator axiality circularity audit.

Tests a tempting PDT-II n=3 route: derive the parity-odd/axial closure of Cycle 091
from sequential composition via commutators.  The commutator of orthogonal generators
is naturally an element of so(n) ~= Lambda^2 V and transforms by conjugation, with
no determinant twist.  Only in n=3 can Lambda^2 V be identified equivariantly with
V tensor det.  Therefore using the commutator to justify an axial vector output
already invokes the dimension-specific Hodge identification and is not a
non-circular n=3 derivation.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def commutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def skew(x: np.ndarray) -> np.ndarray:
    return x - x.T


def hat3(v: np.ndarray) -> np.ndarray:
    x, y, z = np.asarray(v, dtype=float)
    return np.array([[0.0, -z, y], [z, 0.0, -x], [-y, x, 0.0]])


def random_orthogonal(rng: np.random.Generator, n: int, improper: bool) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    if improper:
        q[:, 0] *= -1
    return q


def dimension_ledger() -> list[dict]:
    rows = []
    for n in DIMS:
        biv = n * (n - 1) // 2
        rows.append({
            "n": n,
            "dim_vector": n,
            "dim_bivector_so_n": biv,
            "dimension_match_for_vector_identification": biv == n and n > 0,
        })
    return rows


def conjugation_covariance_audit(trials_per_n: int = 80, seed: int = 102_007) -> dict:
    rng = np.random.default_rng(seed)
    max_residual = 0.0
    violations = 0
    proper = improper = 0
    for n in range(2, 13):
        for t in range(trials_per_n):
            a = skew(rng.normal(size=(n, n)))
            b = skew(rng.normal(size=(n, n)))
            is_improper = bool(t % 2)
            r = random_orthogonal(rng, n, is_improper)
            lhs = commutator(r @ a @ r.T, r @ b @ r.T)
            rhs = r @ commutator(a, b) @ r.T
            residual = float(np.linalg.norm(lhs - rhs))
            max_residual = max(max_residual, residual)
            violations += int(residual > 1e-9)
            improper += int(is_improper)
            proper += int(not is_improper)
    return {
        "seed": seed,
        "dimensions": list(range(2, 13)),
        "trials_per_dimension": trials_per_n,
        "proper_trials": proper,
        "improper_trials": improper,
        "max_conjugation_covariance_residual": max_residual,
        "violations_gt_1e-9": violations,
    }


def axial_hat3_audit(trials: int = 1000, seed: int = 102_003) -> dict:
    rng = np.random.default_rng(seed)
    max_residual = 0.0
    improper = proper = 0
    for t in range(trials):
        v = rng.normal(size=3)
        is_improper = bool(t % 2)
        r = random_orthogonal(rng, 3, is_improper)
        lhs = r @ hat3(v) @ r.T
        rhs = hat3(np.linalg.det(r) * (r @ v))
        residual = float(np.linalg.norm(lhs - rhs))
        max_residual = max(max_residual, residual)
        improper += int(is_improper)
        proper += int(not is_improper)
    return {
        "seed": seed,
        "trials": trials,
        "proper_trials": proper,
        "improper_trials": improper,
        "max_hat_axial_identity_residual": max_residual,
        "violations_gt_1e-9": int(max_residual > 1e-9),
    }


def exact_reflection_witness() -> dict:
    r = np.diag([-1.0, 1.0, 1.0])
    v = np.array([1.0, 0.0, 0.0])
    lhs = r @ hat3(v) @ r.T
    polar_rhs = hat3(r @ v)
    axial_rhs = hat3(np.linalg.det(r) * (r @ v))
    return {
        "R": r.astype(int).tolist(),
        "v": v.astype(int).tolist(),
        "det_R": int(round(np.linalg.det(r))),
        "polar_residual_norm": float(np.linalg.norm(lhs - polar_rhs)),
        "axial_residual_norm": float(np.linalg.norm(lhs - axial_rhs)),
    }


def generate() -> dict:
    ledger = dimension_ledger()
    survivors = [r["n"] for r in ledger if r["dimension_match_for_vector_identification"]]
    return {
        "cycle": 102,
        "target": "PDT-II targets (1)/(2): can sequential commutators non-circularly derive the axial n=3 closure?",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "candidate_claim": "Sequential composition/commutators force the determinant-twisted axial-vector closure required by the Cycle-091 n=3 selector without assuming n=3.",
        "verdict": "FALSIFIED as a non-circular derivation route.",
        "theorem": {
            "statement": "For V=R^n with the standard O(n) action, skew generators and their commutators transform in so(n) ~= Lambda^2 V by A -> R A R^T. A same-dimension vector/pseudovector identification Lambda^2 V ~= V tensor det requires n(n-1)/2=n, hence positive n=3 only.",
            "proof_core": "The commutator covariance follows by direct matrix multiplication. Dimension equality gives n(n-1)/2=n, i.e. n(n-3)=0. In n=3 the hat/Hodge identification obeys R hat(v) R^T = hat(det(R) R v), producing axial parity. For n != 3 there is no dimension-preserving identification of the full bivector generator sector with V.",
            "logical_boundary": "Thus commutator structure supplies a bivector sector in every n; converting it to the axial vector assumed in Cycle 091 is exactly the dimension-specific step. Using that conversion to derive n=3 would be circular."
        },
        "dimension_ledger": ledger,
        "positive_dimension_matches": survivors,
        "conjugation_covariance": conjugation_covariance_audit(),
        "n3_hat_axial_identity": axial_hat3_audit(),
        "reflection_witness": exact_reflection_witness(),
        "prior_art_boundary": "so(n) as skew matrices/exterior bivectors, conjugation under O(n), the 3D hat-map/cross-product pseudovector identity, and Hodge duality are standard mathematics. No novelty is claimed for them.",
        "surviving_pdt_obligation": "If PDT is to derive n=3 non-circularly, it must derive an operational reason that the physically closed primitive generator sector has vector dimension n rather than the generic bivector dimension n(n-1)/2, or derive an equivalent resource/composition constraint without invoking the 3D Hodge identification."
    }


if __name__ == "__main__":
    data = generate()
    p = Path("results/cycle102_commutator_axiality_circularity.json")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
