"""Cycle 091: determinant-twisted O(n) covariance and the n=3 selector.

This module does NOT claim a PDT breakthrough.  It audits the precise boundary
left by Cycle 090: a 3D cross product is not a polar vector under reflections;
it is an axial vector (pseudovector).

Exact hypothesis tested
-----------------------
Let V=R^n be Euclidean and let B: V x V -> V_ax be bilinear and alternating,
where the output transforms in the determinant-twisted standard
representation

    B(Rx,Ry) = det(R) R B(x,y),    R in O(n).

Then a non-zero O(n)-equivariant B exists iff n=3.  At n=3 it is the usual
cross product regarded as AXIAL, not polar.  For n>3 an orientation-preserving
pi rotation in a plane containing one tensor index and one unused index kills
every coefficient.  n=1 is alternating-trivial; n=2 has no O(2)-equivariant
map Lambda^2 V -> V tensor det.

The mathematical representation fact is standard/imported.  PDT still has to
derive why its primitive closure should carry axial parity.
"""

from __future__ import annotations

import json
from typing import Dict, List

import numpy as np


AUDIT_DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def reflection_witness() -> Dict[str, float]:
    """Exact 3D witness: polar covariance fails, axial covariance succeeds."""
    R = np.diag([-1.0, 1.0, 1.0])
    x = np.array([0.0, 1.0, 0.0])
    y = np.array([0.0, 0.0, 1.0])
    lhs = np.cross(R @ x, R @ y)
    polar_rhs = R @ np.cross(x, y)
    axial_rhs = np.linalg.det(R) * (R @ np.cross(x, y))
    return {
        "det_R": float(np.linalg.det(R)),
        "polar_residual": float(np.linalg.norm(lhs - polar_rhs)),
        "axial_residual": float(np.linalg.norm(lhs - axial_rhs)),
    }


def random_orthogonal(rng: np.random.Generator, determinant: int) -> np.ndarray:
    """Return a random numerical orthogonal 3x3 matrix with requested sign."""
    A = rng.normal(size=(3, 3))
    Q, _ = np.linalg.qr(A)
    sign = 1 if np.linalg.det(Q) > 0 else -1
    if sign != determinant:
        Q[:, 0] *= -1.0
    return Q


def random_axial_covariance_audit(trials: int = 1000, seed: int = 91091) -> Dict[str, float]:
    """Regression check of cross(Rx,Ry)=det(R)R cross(x,y) in 3D."""
    rng = np.random.default_rng(seed)
    max_residual = 0.0
    proper = 0
    improper = 0
    for _ in range(trials):
        requested = 1 if rng.random() < 0.5 else -1
        R = random_orthogonal(rng, requested)
        x = rng.normal(size=3)
        y = rng.normal(size=3)
        lhs = np.cross(R @ x, R @ y)
        rhs = np.linalg.det(R) * (R @ np.cross(x, y))
        max_residual = max(max_residual, float(np.linalg.norm(lhs - rhs)))
        if np.linalg.det(R) > 0:
            proper += 1
        else:
            improper += 1
    return {
        "trials": trials,
        "proper_trials": proper,
        "improper_trials": improper,
        "max_axial_covariance_residual": max_residual,
    }


def analytic_dimension_audit(dimensions: List[int] = AUDIT_DIMS) -> List[Dict[str, object]]:
    """Encode the exact analytic classification used in this cycle.

    This is a ledger, not a numerical discovery routine.  For n>3 the proof
    uses an SO(n) pi-rotation on an occupied + unused coordinate pair, so the
    determinant twist is +1 and cannot rescue a nonzero alternating 3-form.
    """
    rows: List[Dict[str, object]] = []
    for n in dimensions:
        if n == 1:
            reason = "alternation is identically zero"
            exists = False
        elif n == 2:
            reason = "Lambda^2(V)=det has no map to V tensor det without an O(2)-fixed vector"
            exists = False
        elif n == 3:
            reason = "Hodge/cross-product axial map Lambda^2(V) -> V tensor det exists"
            exists = True
        else:
            reason = "unused-index determinant+1 pi rotation kills every 3-form coefficient"
            exists = False
        rows.append({"n": n, "nonzero_axial_equivariant_alternating_map": exists, "reason": reason})
    return rows


def build_result() -> Dict[str, object]:
    witness = reflection_witness()
    regression = random_axial_covariance_audit()
    dimensions = analytic_dimension_audit()
    surviving = [row["n"] for row in dimensions if row["nonzero_axial_equivariant_alternating_map"]]
    return {
        "cycle": 91,
        "target": "PDT-II target (2): non-circular elementary n=3 derivation",
        "classification": ["CONDITIONAL", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "theorem": "Hom_O(n)(Lambda^2 V, V tensor det) is nonzero iff n=3 for nontrivial finite Euclidean V",
        "reflection_witness": witness,
        "regression": regression,
        "dimension_audit": dimensions,
        "surviving_dimensions": surviving,
        "breakthrough_candidate": False,
        "open_pdt_obligation": "derive axial/parity-odd transformation character of primitive distinction closure from PDT primitives",
    }


if __name__ == "__main__":
    print(json.dumps(build_result(), indent=2, sort_keys=True))
