"""Cycle 127: resource-naturality no-go for nonzero bilinear PDT composition.

If a bilinear composition B is required to commute with the same uniform
resource attenuation T_lambda = lambda I on each input and the output,
then for any lambda not in {0,1} the only solution is B=0:

    B(lambda x, lambda y) = lambda^2 B(x,y)
    T_lambda B(x,y)       = lambda B(x,y)

Exact naturality therefore implies lambda(lambda-1)B(x,y)=0.

The correct homogeneous scaling for a nonzero degree-2 law is instead
T_{lambda^2} B(x,y) = B(T_lambda x, T_lambda y).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import numpy as np


def hadamard_composition(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Simple nonzero same-sector bilinear witness in every dimension."""
    return np.asarray(x, dtype=float) * np.asarray(y, dtype=float)


def naive_naturality_residual(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """B(T_lam x,T_lam y)-T_lam B(x,y)."""
    b = hadamard_composition(x, y)
    return hadamard_composition(lam * x, lam * y) - lam * b


def exact_residual_identity(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """Closed form: lambda(lambda-1)B(x,y)."""
    return lam * (lam - 1.0) * hadamard_composition(x, y)


def degree2_covariance_residual(x: np.ndarray, y: np.ndarray, lam: float) -> np.ndarray:
    """B(T_lam x,T_lam y)-T_{lam^2}B(x,y), which vanishes identically."""
    b = hadamard_composition(x, y)
    return hadamard_composition(lam * x, lam * y) - (lam * lam) * b


def audit(
    dimensions: Iterable[int] = tuple(list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]),
    lambdas: Iterable[float] = (0.25, 0.5, 0.75),
    trials_per_pair: int = 20,
    seed: int = 127,
) -> dict:
    rng = np.random.default_rng(seed)
    trials = 0
    naive_nonzero = 0
    identity_failures = 0
    corrected_failures = 0
    max_identity_error = 0.0
    max_corrected_error = 0.0

    dims = [int(n) for n in dimensions]
    lams = [float(v) for v in lambdas]

    for n in dims:
        for lam in lams:
            for _ in range(trials_per_pair):
                x = rng.normal(size=n)
                y = rng.normal(size=n)
                residual = naive_naturality_residual(x, y, lam)
                predicted = exact_residual_identity(x, y, lam)
                err = float(np.linalg.norm(residual - predicted))
                max_identity_error = max(max_identity_error, err)
                if err > 1e-11 * (1.0 + float(np.linalg.norm(predicted))):
                    identity_failures += 1
                if float(np.linalg.norm(residual)) > 1e-10:
                    naive_nonzero += 1

                corrected = degree2_covariance_residual(x, y, lam)
                corr_err = float(np.linalg.norm(corrected))
                max_corrected_error = max(max_corrected_error, corr_err)
                if corr_err > 1e-11 * (1.0 + float(np.linalg.norm(hadamard_composition(x, y)))):
                    corrected_failures += 1
                trials += 1

    return {
        "cycle": 127,
        "status": ["PROVED", "FALSIFIED", "NUMERICALLY SUPPORTED", "OPEN"],
        "theorem": (
            "For bilinear B and T_lambda=lambda I with lambda not in {0,1}, "
            "B(T_lambda x,T_lambda y)=T_lambda B(x,y) for all x,y iff B=0."
        ),
        "dimensions": dims,
        "lambdas": lams,
        "trials_per_dimension_lambda": trials_per_pair,
        "random_trials": trials,
        "naive_naturality_nonzero_residual_trials": naive_nonzero,
        "exact_scaling_identity_failures": identity_failures,
        "degree2_covariance_failures": corrected_failures,
        "max_exact_identity_error": max_identity_error,
        "max_degree2_covariance_error": max_corrected_error,
        "breakthrough_candidate": False,
    }


if __name__ == "__main__":
    out = audit()
    print(json.dumps(out, indent=2, sort_keys=True))
    path = Path("results/cycle127_resource_naturality_no_go.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
