"""Cycle 079: calibrated resource-map Born lock.

This module audits the finite-dimensional theorem boundary:

If an operational probability assignment p_R(E|rho) is
  (i) additive under effect coarse-graining,
 (ii) normalized on I,
(iii) affine under convex preparation mixing,
and its induced state map is exactly calibrated on every pure state,
then p_R(E|rho)=Tr(rho E) for every state/effect.

The theorem is analytic.  The numerical audit below is regression evidence and
also checks standard non-identity affine candidates: depolarizing, transpose,
and unitary conjugation.  They retain effect additivity and preparation
affinity, but fail universal pure-state calibration (except the d=1 degenerate
case).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Dict, List

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64]
SEED = 79079
REPS = 5


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def random_pure(d: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=d) + 1j * rng.normal(size=d)
    z /= np.linalg.norm(z)
    return np.outer(z, z.conj())


def random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(x)
    diag = np.diag(r)
    phases = np.where(np.abs(diag) > 1e-15, diag / np.abs(diag), 1.0)
    return q @ np.diag(np.conj(phases))


def map_family(name: str, d: int, unitary: np.ndarray) -> Callable[[np.ndarray], np.ndarray]:
    if name == "identity":
        return lambda x: x
    if name == "depolarizing":
        lam = 0.73
        return lambda x: lam * x + (1.0 - lam) * np.eye(d) / d
    if name == "transpose":
        return lambda x: x.T
    if name == "unitary":
        return lambda x: unitary @ x @ unitary.conj().T
    raise ValueError(name)


def run_audit() -> Dict[str, object]:
    rng = np.random.default_rng(SEED)
    names = ["identity", "depolarizing", "transpose", "unitary"]
    calibration_failures = {name: 0 for name in names}
    max_additivity_error = 0.0
    max_mixing_error = 0.0
    max_identity_calibration_error = 0.0
    total_map_cases = 0

    per_dimension: List[Dict[str, object]] = []
    for d in DIMS:
        u = random_unitary(d, rng)
        local_failures = {name: 0 for name in names}
        for _ in range(REPS):
            rho = random_density(d, rng)
            tau = random_density(d, rng)
            t = float(rng.random())
            pure = random_pure(d, rng)
            # Small positive effects guarantee E+F <= I by ||E+F|| <= 0.4.
            e = 0.2 * random_pure(d, rng)
            f = 0.2 * random_pure(d, rng)
            for name in names:
                phi = map_family(name, d, u)
                sig = phi(rho)
                add_err = abs(np.trace(sig @ (e + f)) - (np.trace(sig @ e) + np.trace(sig @ f)))
                mix_err = np.linalg.norm(
                    phi(t * rho + (1.0 - t) * tau)
                    - (t * phi(rho) + (1.0 - t) * phi(tau)),
                    ord="fro",
                )
                cal_err = abs(np.trace(phi(pure) @ pure) - 1.0)
                max_additivity_error = max(max_additivity_error, float(add_err))
                max_mixing_error = max(max_mixing_error, float(mix_err))
                if name == "identity":
                    max_identity_calibration_error = max(max_identity_calibration_error, float(cal_err))
                if cal_err > 1e-10:
                    calibration_failures[name] += 1
                    local_failures[name] += 1
                total_map_cases += 1
        per_dimension.append({"d": d, "calibration_failures": local_failures})

    result = {
        "cycle": 79,
        "classification": [
            "PROVED",
            "FALSIFIED(nonidentity affine resource maps under universal pure-state calibration)",
            "NUMERICALLY SUPPORTED",
            "IMPORTED/KNOWN BOUNDARY",
        ],
        "breakthrough_candidate": False,
        "dimensions": DIMS,
        "repetitions_per_dimension": REPS,
        "total_map_cases": total_map_cases,
        "max_effect_additivity_error": max_additivity_error,
        "max_preparation_mixing_error": max_mixing_error,
        "max_identity_calibration_error": max_identity_calibration_error,
        "calibration_failures": calibration_failures,
        "per_dimension": per_dimension,
        "theorem_note": (
            "Effect additivity/normalization gives a density-operator representation for each fixed input state; "
            "preparation affinity gives an affine induced state map Phi_R; universal pure-state calibration "
            "forces Phi_R(P)=P on all rank-one projectors, and affine spanning then forces Phi_R=id."
        ),
    }
    return result


def main() -> None:
    result = run_audit()
    out = Path("results") / "cycle079_calibrated_resource_map_born_lock.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
