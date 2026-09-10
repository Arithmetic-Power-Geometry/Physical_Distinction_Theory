"""Cycle 042: Tsirelson-compatible correlator-composite nonuniqueness.

This module constructs two distinct O(n)xO(n)-invariant centered binary-correlation
bodies with identical local Euclidean geometry, all product correlators, and the same
CHSH optimum 2*sqrt(2):

C_op  = {T: ||T||_op <= 1}
C_cap = {T: ||T||_op <= 1 and ||T||_* <= 2}

For n>=3 they differ because I_n belongs to C_op but not C_cap.  CHSH is still
saturated in C_cap by a rank-two partial isometry with singular values (1,1).
The construction is a correlator-sector no-go, not a claim that C_cap uniquely
extends to a full unrestricted GPT composite.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Dict, List

import numpy as np


def op_norm(T: np.ndarray) -> float:
    return float(np.linalg.svd(T, compute_uv=False)[0]) if T.size else 0.0


def nuclear_norm(T: np.ndarray) -> float:
    return float(np.linalg.svd(T, compute_uv=False).sum())


def in_c_op(T: np.ndarray, tol: float = 1e-12) -> bool:
    return op_norm(T) <= 1.0 + tol


def in_c_cap(T: np.ndarray, tol: float = 1e-12) -> bool:
    return in_c_op(T, tol) and nuclear_norm(T) <= 2.0 + tol


def product_correlator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.outer(a, b)


def canonical_chsh_coefficient(n: int) -> np.ndarray:
    if n < 2:
        raise ValueError("CHSH requires n>=2")
    e1 = np.zeros(n)
    e2 = np.zeros(n)
    e1[0] = 1.0
    e2[1] = 1.0
    y0 = (e1 + e2) / math.sqrt(2.0)
    y1 = (e1 - e2) / math.sqrt(2.0)
    return np.outer(e1, y0 + y1) + np.outer(e2, y0 - y1)


def canonical_chsh_witness(n: int) -> np.ndarray:
    """Rank-two partial isometry aligned with the CHSH coefficient."""
    C = canonical_chsh_coefficient(n)
    return C / math.sqrt(2.0)


def chsh_value(T: np.ndarray) -> float:
    C = canonical_chsh_coefficient(T.shape[0])
    return float(np.sum(C * T))


def random_orthogonal(n: int, rng: np.random.Generator) -> np.ndarray:
    Q, R = np.linalg.qr(rng.normal(size=(n, n)))
    signs = np.sign(np.diag(R))
    signs[signs == 0] = 1.0
    return Q @ np.diag(signs)


def audit_dimension(n: int, random_trials: int = 200, seed: int = 42000) -> Dict[str, float | int | bool]:
    if n < 2:
        raise ValueError("audit_dimension requires n>=2")
    I = np.eye(n)
    W = canonical_chsh_witness(n)

    rng = np.random.default_rng(seed + n)
    max_product_nuclear = 0.0
    max_rotation_op_error = 0.0
    max_rotation_nuclear_error = 0.0
    product_failures = 0

    for _ in range(random_trials):
        a = rng.normal(size=n)
        b = rng.normal(size=n)
        a /= max(1.0, np.linalg.norm(a))
        b /= max(1.0, np.linalg.norm(b))
        P = product_correlator(a, b)
        max_product_nuclear = max(max_product_nuclear, nuclear_norm(P))
        if not in_c_cap(P):
            product_failures += 1

        U = random_orthogonal(n, rng)
        V = random_orthogonal(n, rng)
        R = U @ W @ V.T
        max_rotation_op_error = max(max_rotation_op_error, abs(op_norm(R) - op_norm(W)))
        max_rotation_nuclear_error = max(max_rotation_nuclear_error, abs(nuclear_norm(R) - nuclear_norm(W)))

    return {
        "n": n,
        "identity_in_c_op": in_c_op(I),
        "identity_in_c_cap": in_c_cap(I),
        "identity_nuclear_norm": nuclear_norm(I),
        "witness_in_c_op": in_c_op(W),
        "witness_in_c_cap": in_c_cap(W),
        "witness_op_norm": op_norm(W),
        "witness_nuclear_norm": nuclear_norm(W),
        "chsh_value": chsh_value(W),
        "chsh_target": 2.0 * math.sqrt(2.0),
        "product_failures": product_failures,
        "max_product_nuclear_norm": max_product_nuclear,
        "max_rotation_op_error": max_rotation_op_error,
        "max_rotation_nuclear_error": max_rotation_nuclear_error,
        "bodies_distinct": in_c_op(I) and not in_c_cap(I),
    }


def run_audit(out_dir: str | Path = "results") -> List[Dict[str, float | int | bool]]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = [audit_dimension(n) for n in range(2, 13)]

    csv_path = out / "cycle042_tsirelson_composite_nonuniqueness.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    ledger = {
        "cycle": 42,
        "title": "Tsirelson-compatible correlator composite nonuniqueness",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN"],
        "breakthrough_candidate": False,
        "claim_falsified": "Euclidean local geometry + local tomography + local O(n) symmetry + exact CHSH Tsirelson value uniquely determine the centered correlator composite.",
        "surviving_statement": "For n>=3, C_op and C_cap are distinct invariant convex correlator bodies, both contain all product correlators and both attain CHSH=2*sqrt(2).",
        "scope_warning": "This is a centered binary-correlator-sector construction; it does not assert a unique full GPT extension for C_cap.",
        "dimensions": [2, 12],
    }
    with (out / "cycle042_theorem_status.json").open("w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2)

    return rows


if __name__ == "__main__":
    rows = run_audit()
    for row in rows:
        print(row)
