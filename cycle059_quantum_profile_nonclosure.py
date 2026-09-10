"""Cycle 059: noncommutative obstruction to a scalar/spectral PDT composition profile.

Constructs a 4D family with identical reference-weighted spectral measure of
L = sigma^{-1/2} rho sigma^{-1/2} but different trace distance D(rho,sigma).
Embeds the witness into dimensions 4..12 and scans a phase family.
"""

import json
import math
import numpy as np

LAM = np.array([1.8, 1.2, 0.7, 0.3], dtype=float)
SIGMA4 = np.diag([0.50, 0.25, 0.15, 0.10])


def hadamard_family(theta: float) -> np.ndarray:
    z = np.exp(1j * theta)
    return 0.5 * np.array(
        [
            [1, 1, 1, 1],
            [1, z, -1, -z],
            [1, -1, 1, -1],
            [1, -z, -1, z],
        ],
        dtype=complex,
    )


def state_from(theta: float) -> np.ndarray:
    u = hadamard_family(theta)
    root = np.diag(np.sqrt(np.diag(SIGMA4)))
    l_op = u @ np.diag(LAM) @ u.conj().T
    return root @ l_op @ root


def trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    return 0.5 * float(np.abs(np.linalg.eigvalsh(a - b)).sum())


def spectral_weights(theta: float) -> np.ndarray:
    u = hadamard_family(theta)
    return np.real(np.diag(u.conj().T @ SIGMA4 @ u))


def embed(theta: float, d: int, tail_mass: float = 0.2):
    if d == 4:
        return state_from(theta), SIGMA4.copy()
    if d < 4:
        raise ValueError("Witness requires d>=4")
    rho = np.zeros((d, d), dtype=complex)
    sigma = np.zeros((d, d), dtype=complex)
    rho[:4, :4] = (1 - tail_mass) * state_from(theta)
    sigma[:4, :4] = (1 - tail_mass) * SIGMA4
    tail = tail_mass / (d - 4)
    rho[4:, 4:] = np.diag(np.full(d - 4, tail))
    sigma[4:, 4:] = np.diag(np.full(d - 4, tail))
    return rho, sigma


def audit():
    phases = np.linspace(0.0, math.pi, 129)
    rows = []
    failures = 0
    for d in range(4, 13):
        vals = []
        for theta in phases:
            rho, sigma = embed(theta, d)
            if abs(np.trace(rho).real - 1.0) > 1e-12:
                failures += 1
            if np.min(np.linalg.eigvalsh(rho)) < -1e-12:
                failures += 1
            vals.append(trace_distance(rho, sigma))
        rows.append(
            {
                "dimension": d,
                "min_trace_distance": min(vals),
                "max_trace_distance": max(vals),
                "spread": max(vals) - min(vals),
            }
        )
    weights0 = spectral_weights(0.0)
    weightspi = spectral_weights(math.pi)
    result = {
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN boundary"],
        "claim_falsified": "The reference-weighted spectrum of the sandwich likelihood operator alone determines operational trace distinction.",
        "lambda_atoms": LAM.tolist(),
        "weights_theta_0": weights0.tolist(),
        "weights_theta_pi": weightspi.tolist(),
        "trace_distance_theta_0": trace_distance(state_from(0.0), SIGMA4),
        "trace_distance_theta_pi": trace_distance(state_from(math.pi), SIGMA4),
        "dimensions": rows,
        "failures": failures,
    }
    assert np.max(np.abs(weights0 - weightspi)) < 1e-12
    assert result["trace_distance_theta_0"] - result["trace_distance_theta_pi"] > 0.02
    assert all(r["spread"] > 0.015 for r in rows)
    assert failures == 0
    return result


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
