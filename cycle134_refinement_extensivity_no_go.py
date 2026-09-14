"""Cycle 134: exact-refinement-conservation does not imply resolved-channel additivity.

The counterfamily is R_alpha(A) = ||A||_F^(2 alpha) = (sum_ij a_ij^2)^alpha,
alpha > 0.  It is nonnegative, calibrated on every matrix unit, invariant under
SO(n)xSO(n), and exactly conserved by every orthogonal refinement/re-basing.
For alpha != 1 it is not additive over resolved orthogonal product channels.

This module generates deterministic regression evidence; the no-go argument is
algebraic and does not depend on the numerical sweep.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
ALPHAS = [0.5, 1.0, 2.0, 3.0]
SEED = 134
TRIALS_PER_DIM = 20
TOL = 1e-10


def resource(a: np.ndarray, alpha: float) -> float:
    return float(np.sum(a * a) ** alpha)


def random_so(n: int, rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1.0
    return q


@dataclass
class Audit:
    dimensions: list[int]
    alphas: list[float]
    covariance_cases: int
    covariance_failures: int
    max_relative_covariance_residual: float
    exact_nonadditive_witnesses: int
    smallest_witness_dimension: int
    smallest_witness: dict


def run_audit() -> Audit:
    rng = np.random.default_rng(SEED)
    covariance_cases = 0
    covariance_failures = 0
    max_rel = 0.0

    for n in DIMS:
        for _ in range(TRIALS_PER_DIM):
            a = rng.normal(size=(n, n))
            u = random_so(n, rng)
            v = random_so(n, rng)
            b = u @ a @ v.T
            for alpha in ALPHAS:
                r0 = resource(a, alpha)
                r1 = resource(b, alpha)
                rel = abs(r1 - r0) / max(1.0, abs(r0))
                max_rel = max(max_rel, rel)
                covariance_cases += 1
                covariance_failures += int(rel > TOL)

    # Exact symbolic values for A=E_11+E_22.  Each component has resource 1.
    exact_nonadditive_witnesses = 0
    witness = {}
    for alpha in (0.5, 2.0, 3.0):
        whole = 2.0 ** alpha
        parts = 2.0
        if whole != parts:
            exact_nonadditive_witnesses += 1
        witness[str(alpha)] = {
            "R(E11+E22)": whole,
            "R(E11)+R(E22)": parts,
            "gap": whole - parts,
        }

    return Audit(
        dimensions=DIMS,
        alphas=ALPHAS,
        covariance_cases=covariance_cases,
        covariance_failures=covariance_failures,
        max_relative_covariance_residual=max_rel,
        exact_nonadditive_witnesses=exact_nonadditive_witnesses,
        smallest_witness_dimension=2,
        smallest_witness=witness,
    )


def main() -> None:
    result = run_audit()
    print(json.dumps(asdict(result), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
