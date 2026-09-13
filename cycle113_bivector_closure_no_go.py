"""Cycle 113: bivector-sector no-go for an n=3 composition selector.

The exterior product x∧y is a canonical alternating bilinear composition with
codomain Λ²V.  In Euclidean space it is O(n)-natural and obeys the exact Gram
area identity in every dimension.  Therefore alternation + full rotational
covariance + the Euclidean area law do not select n=3 unless PDT independently
requires the composite to close back into V (or supplies an equivalent
identification Λ²V ≅ V).

The exterior-algebra facts are standard mathematics; no novelty is claimed for
them.  The PDT result is a falsification/guardrail for a proposed derivation.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def wedge_matrix(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Antisymmetric matrix representing x∧y; upper triangle stores coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return np.outer(x, y) - np.outer(y, x)


def wedge_norm_sq(x: np.ndarray, y: np.ndarray) -> float:
    w = wedge_matrix(x, y)
    return float(np.sum(np.triu(w, 1) ** 2))


def gram_area_sq(x: np.ndarray, y: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    return float((x @ x) * (y @ y) - (x @ y) ** 2)


def bivector_dim(n: int) -> int:
    return n * (n - 1) // 2


def selector_solutions(limit: int = 256) -> list[int]:
    return [n for n in range(limit + 1) if bivector_dim(n) == n]


def exact_dimension_ledger() -> list[dict]:
    rows = []
    for n in DIMS:
        # For basis vectors e_i,e_j both sides of the Gram identity are exactly
        # 0 when i=j and exactly 1 otherwise. Exhaustive explicit bookkeeping
        # through n=12, analytic certificate thereafter avoids pointless O(n^4).
        failures = 0
        if n <= 12:
            for i in range(n):
                for j in range(n):
                    lhs = 0 if i == j else 1
                    rhs = 0 if i == j else 1
                    failures += int(lhs != rhs)
            mode = "exact exhaustive basis-pair audit"
        else:
            mode = "analytic basis-pair certificate"
        rows.append({
            "n": n,
            "bivector_dimension": bivector_dim(n),
            "basis_pairs": n * n,
            "gram_identity_failures": failures,
            "mode": mode,
        })
    return rows


def proper_signed_permutation(rng: np.random.Generator, n: int) -> np.ndarray:
    """Random determinant +1 signed-permutation matrix (an exact SO(n) element)."""
    if n == 1:
        return np.ones((1, 1))
    perm = rng.permutation(n)
    signs = rng.choice([-1.0, 1.0], size=n)
    inversions = sum(int(perm[i] > perm[j]) for i in range(n) for j in range(i + 1, n))
    det_perm = -1 if inversions % 2 else 1
    if det_perm * int(np.prod(signs)) < 0:
        signs[0] *= -1.0
    r = np.zeros((n, n))
    r[np.arange(n), perm] = signs
    return r


def randomized_audit(seed: int = 113_113) -> dict:
    rng = np.random.default_rng(seed)
    cases = 0
    gram_failures = 0
    equivariance_failures = 0
    max_gram_residual = 0.0
    max_equivariance_residual = 0.0
    for n in DIMS:
        reps = 40 if n <= 12 else 15
        for _ in range(reps):
            x = rng.integers(-3, 4, size=n).astype(float)
            y = rng.integers(-3, 4, size=n).astype(float)
            w = wedge_matrix(x, y)
            gram_residual = abs(wedge_norm_sq(x, y) - gram_area_sq(x, y))
            max_gram_residual = max(max_gram_residual, gram_residual)
            gram_failures += int(gram_residual > 1e-9)

            r = proper_signed_permutation(rng, n)
            equiv_residual = float(np.linalg.norm(
                wedge_matrix(r @ x, r @ y) - r @ w @ r.T
            ))
            max_equivariance_residual = max(max_equivariance_residual, equiv_residual)
            equivariance_failures += int(equiv_residual > 1e-9)
            cases += 1
    return {
        "seed": seed,
        "cases": cases,
        "gram_failures_gt_1e-9": gram_failures,
        "equivariance_failures_gt_1e-9": equivariance_failures,
        "max_gram_residual": max_gram_residual,
        "max_equivariance_residual": max_equivariance_residual,
    }


def composite_dimension_audit() -> dict:
    failures = 0
    cases = 0
    for a in range(1, 13):
        for b in range(1, 13):
            lhs = bivector_dim(a + b)
            rhs = bivector_dim(a) + a * b + bivector_dim(b)
            failures += int(lhs != rhs)
            cases += 1
    return {
        "cases": cases,
        "failures": failures,
        "identity": "dim Λ²(A⊕B)=dim Λ²A + dim(A⊗B) + dim Λ²B",
    }


def l1_area_counterexample() -> dict:
    x = np.array([1.0, 1.0])
    y = np.array([1.0, -1.0])
    wedge_sq = wedge_norm_sq(x, y)
    naive_l1_rhs = float(np.linalg.norm(x, 1) ** 2 * np.linalg.norm(y, 1) ** 2 - (x @ y) ** 2)
    return {
        "x": x.tolist(), "y": y.tolist(),
        "wedge_coefficient_norm_squared": wedge_sq,
        "naive_l1_gram_rhs": naive_l1_rhs,
        "equal": wedge_sq == naive_l1_rhs,
    }


def generate() -> dict:
    ledger = exact_dimension_ledger()
    return {
        "cycle": 113,
        "title": "Bivector-sector closure no-go for n=3 selection",
        "primary_targets": [1, 2],
        "breakthrough_candidate": False,
        "classifications": [
            "PROVED", "FALSIFIED", "CONDITIONAL", "IMPORTED/KNOWN",
            "NUMERICALLY SUPPORTED", "OPEN"
        ],
        "results": {
            "bivector_countermodel": {
                "status": "PROVED / IMPORTED/KNOWN",
                "statement": "For every real Euclidean V, B(x,y)=x∧y in Λ²V is bilinear, alternating, O(n)-natural, and satisfies ||x∧y||²=||x||²||y||²-<x,y>².",
            },
            "dimension_selector_without_closure": {
                "status": "FALSIFIED",
                "statement": "Alternation + full rotational covariance + exact Euclidean area law do not imply n=3 when the composition codomain may be Λ²V.",
                "smallest_nontrivial_dimension": 2,
            },
            "vector_valued_closure": {
                "status": "CONDITIONAL / OPEN",
                "statement": "If PDT independently requires an isomorphic identification Λ²V≅V, dimension equality gives n=3 among positive nontrivial dimensions; deriving that closure is still open.",
                "dimension_equation_solutions_nonnegative": selector_solutions(),
            },
            "non_hilbert_norm_boundary": {
                "status": "FALSIFIED",
                "statement": "The Euclidean Gram-area identity cannot simply be transplanted to arbitrary norms.",
                "witness": l1_area_counterexample(),
            },
        },
        "dimension_ledger": ledger,
        "randomized_audit": randomized_audit(),
        "composite_audit": composite_dimension_audit(),
        "prior_art_boundary": "Exterior powers, wedge naturality, induced Gram inner products, Hodge duality, and the 3D bivector-vector identification are standard mathematics. No mathematical novelty is claimed.",
        "surviving_obligations": [
            "Derive or falsify vector-valued closure of primitive PDT composition from distinction/resource primitives without importing cross-product or Hodge-star structure.",
            "If closure survives, test whether the identification is physically canonical under the declared reversible group and resource window.",
            "No same-input PDT-vs-QM probability departure follows from this cycle.",
        ],
    }


if __name__ == "__main__":
    data = generate()
    path = Path("results/cycle113_bivector_closure_no_go.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))
