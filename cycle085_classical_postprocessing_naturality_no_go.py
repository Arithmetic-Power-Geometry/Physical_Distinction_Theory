"""Cycle 085: classical post-processing naturality no-go.

A candidate same-input probability deformation is a family F_n: Delta_n -> Delta_n.
If it commutes with every classical stochastic post-processing map T,
    F_m(T q) = T F_n(q),
then F_n is the identity for every n.  The proof is exact: every q in
Delta_n is the image of the unique point of Delta_1 under a stochastic map.

The numerical code below is regression/counterexample-search support only.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

import numpy as np


DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 85085


def identity_map(q: np.ndarray) -> np.ndarray:
    return np.asarray(q, dtype=float)


def power_map(q: np.ndarray, alpha: float) -> np.ndarray:
    q = np.asarray(q, dtype=float)
    z = np.power(q, alpha)
    return z / z.sum()


def exp_map(q: np.ndarray, beta: float = 1.0) -> np.ndarray:
    q = np.asarray(q, dtype=float)
    z = np.expm1(beta * q)
    return z / z.sum()


def random_distribution(n: int, rng: np.random.Generator) -> np.ndarray:
    q = rng.random(n)
    return q / q.sum()


def random_stochastic(m: int, n: int, rng: np.random.Generator) -> np.ndarray:
    """Column-stochastic T mapping Delta_n to Delta_m."""
    T = rng.random((m, n))
    T /= T.sum(axis=0, keepdims=True)
    return T


def naturality_residual(
    q: np.ndarray,
    T: np.ndarray,
    F: Callable[[np.ndarray], np.ndarray],
) -> float:
    return float(np.max(np.abs(F(T @ q) - T @ F(q))))


def square_split_witness() -> dict:
    """Small explicit violation for F(q)=q^2/sum(q^2)."""
    q = np.array([0.75, 0.25])
    # Split the first outcome into two equiprobable classical labels.
    T = np.array([[0.5, 0.0], [0.5, 0.0], [0.0, 1.0]])
    lhs = power_map(T @ q, 2.0)
    rhs = T @ power_map(q, 2.0)
    return {
        "q": q.tolist(),
        "Tq": (T @ q).tolist(),
        "F3_Tq": lhs.tolist(),
        "T_F2_q": rhs.tolist(),
        "max_residual": float(np.max(np.abs(lhs - rhs))),
    }


def direct_singleton_identity(q: np.ndarray) -> float:
    """Numerically instantiate the exact proof F_n(q)=T_q F_1(1)=q."""
    Tq = np.asarray(q, dtype=float).reshape((-1, 1))
    singleton = np.array([1.0])
    return float(np.max(np.abs(Tq @ singleton - q)))


def run_audit(samples_per_dimension: int = 20) -> dict:
    rng = np.random.default_rng(SEED)
    nonlinear = {
        "power2": lambda x: power_map(x, 2.0),
        "sqrt": lambda x: power_map(x, 0.5),
        "exp": exp_map,
    }
    failures = {name: 0 for name in nonlinear}
    tested_nontrivial = 0
    total = 0
    max_identity_residual = 0.0
    max_singleton_proof_residual = 0.0

    for n in DIMS:
        for _ in range(samples_per_dimension):
            q = random_distribution(n, rng)
            max_singleton_proof_residual = max(
                max_singleton_proof_residual, direct_singleton_identity(q)
            )
            m = int(rng.integers(1, min(20, n + 5) + 1))
            T = random_stochastic(m, n, rng)
            max_identity_residual = max(
                max_identity_residual, naturality_residual(q, T, identity_map)
            )
            if m > 1:
                tested_nontrivial += 1
            for name, F in nonlinear.items():
                if naturality_residual(q, T, F) > 1e-10:
                    failures[name] += 1
            total += 1

    return {
        "cycle": 85,
        "classification": {
            "theorem": "PROVED",
            "postprocessing_deformation_class": "FALSIFIED",
            "regression": "NUMERICALLY SUPPORTED",
            "prior_art_boundary": "IMPORTED/KNOWN",
            "breakthrough_candidate": False,
        },
        "hypotheses": [
            "F_n maps every finite probability simplex Delta_n to itself",
            "F_m(Tq)=T F_n(q) for every column-stochastic classical channel T",
            "Delta_1 contains its unique normalized point (1)",
            "microscopic quantum input and physical measurement are unchanged; F is only an output-distribution deformation",
        ],
        "exact_conclusion": "F_n(q)=q for every finite n and every q in Delta_n",
        "dimensions": DIMS,
        "samples_per_dimension": samples_per_dimension,
        "total_random_cases": total,
        "nontrivial_output_cases": tested_nontrivial,
        "max_identity_naturality_residual": max_identity_residual,
        "max_singleton_proof_residual": max_singleton_proof_residual,
        "nonlinear_naturality_failures": failures,
        "small_square_split_witness": square_split_witness(),
    }


def main() -> None:
    result = run_audit()
    out = Path("results/cycle085_classical_postprocessing_naturality_no_go.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
