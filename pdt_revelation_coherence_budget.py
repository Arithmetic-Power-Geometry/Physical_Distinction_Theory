"""PDT controlled-record revelation/coherence budget.

For a density operator eta and relative unitary V, define
  rho0 = eta,
  rho1 = V eta V^dagger,
  D = 1/2 ||rho0-rho1||_1,
  chi = Tr(eta V).
Then D^2 + |chi|^2 <= 1.

The proof factors through root fidelity f:
|chi| <= f(eta,rho1) and D^2 + f^2 <= 1.
This is established quantum-information mathematics (Englert/Fuchs-van de Graaf
landscape), recorded here as a PDT operational audit rather than a novelty claim.
"""
from __future__ import annotations

import numpy as np


def _hermitize(a: np.ndarray) -> np.ndarray:
    return 0.5 * (a + a.conj().T)


def sqrt_psd(a: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eigh(_hermitize(a))
    w = np.clip(w.real, 0.0, None)
    return (v * np.sqrt(w)) @ v.conj().T


def trace_norm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False).sum())


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    return 0.5 * trace_norm(rho - sigma)


def root_fidelity_unitary_orbit(eta: np.ndarray, v: np.ndarray) -> float:
    s = sqrt_psd(eta)
    return trace_norm(s @ v @ s)


def coherence_factor(eta: np.ndarray, v: np.ndarray) -> complex:
    return complex(np.trace(eta @ v))


def budget_terms(eta: np.ndarray, v: np.ndarray) -> dict[str, float]:
    rho1 = v @ eta @ v.conj().T
    d = trace_distance(eta, rho1)
    f = root_fidelity_unitary_orbit(eta, v)
    c = abs(coherence_factor(eta, v))
    return {
        "trace_distance": d,
        "root_fidelity": f,
        "abs_chi": c,
        "chi_le_f_margin": f - c,
        "fvdg_margin": 1.0 - (d * d + f * f),
        "revelation_coherence_margin": 1.0 - (d * d + c * c),
    }


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    if d < 1:
        raise ValueError("d must be positive")
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = x @ x.conj().T
    return rho / np.trace(rho)


def random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    if d < 1:
        raise ValueError("d must be positive")
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    phase = np.where(np.abs(diag) > 0.0, diag / np.abs(diag), 1.0)
    return q @ np.diag(np.conj(phase))


def audit_dimensions(max_d: int = 12, trials: int = 200, seed: int = 20260909) -> list[dict[str, float]]:
    rng = np.random.default_rng(seed)
    out: list[dict[str, float]] = []
    for d in range(1, max_d + 1):
        max_lhs = 0.0
        min_margin = float("inf")
        for _ in range(trials):
            eta = random_density(d, rng)
            v = random_unitary(d, rng)
            terms = budget_terms(eta, v)
            lhs = terms["trace_distance"] ** 2 + terms["abs_chi"] ** 2
            max_lhs = max(max_lhs, lhs)
            min_margin = min(min_margin, terms["revelation_coherence_margin"])
        out.append({"dimension": float(d), "max_lhs": max_lhs, "min_margin": min_margin})
    return out


if __name__ == "__main__":
    for row in audit_dimensions():
        print(row)
