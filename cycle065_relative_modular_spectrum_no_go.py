"""Cycle 065: relative-modular-spectrum nonclosure kill test.

Claim tested: the spectrum of the finite-dimensional relative modular
superoperator Delta_{rho|sigma}=L_rho R_{sigma^{-1}} is a complete
operational distinction object.

Result: FALSIFIED. Its eigenvalues depend only on the separate spectra of
rho and sigma, while trace distance also depends on their relative basis.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np


def trace_distance(rho: np.ndarray, sigma: np.ndarray) -> float:
    return 0.5 * float(np.sum(np.abs(np.linalg.eigvalsh(rho - sigma))))


def modular_spectrum(rho: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    r = np.linalg.eigvalsh(rho)
    s = np.linalg.eigvalsh(sigma)
    if np.min(s) <= 0:
        raise ValueError("sigma must be faithful")
    return np.sort(np.array([x / y for x in r for y in s], dtype=float))


def random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    phase = np.where(np.abs(d) > 0, d / np.abs(d), 1.0)
    return q @ np.diag(np.conj(phase))


def exact_qubit_witness() -> dict:
    sigma = np.diag([0.8, 0.2])
    rho_commuting = np.diag([0.7, 0.3])
    rho_swapped = np.diag([0.3, 0.7])
    m0 = modular_spectrum(rho_commuting, sigma)
    m1 = modular_spectrum(rho_swapped, sigma)
    d0 = trace_distance(rho_commuting, sigma)
    d1 = trace_distance(rho_swapped, sigma)
    assert np.allclose(m0, m1, atol=1e-14)
    assert abs(d0 - 0.1) < 1e-14
    assert abs(d1 - 0.5) < 1e-14
    return {
        "dimension": 2,
        "sigma": [0.8, 0.2],
        "rho_spectrum": [0.7, 0.3],
        "relative_modular_spectrum": m0.tolist(),
        "trace_distance_commuting": d0,
        "trace_distance_swapped": d1,
        "separation": d1 - d0,
    }


def stress(seed: int = 65011) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    records = []
    failures = 0
    for n in dims:
        if n == 1:
            records.append({"n": 1, "trials": 1, "degenerate": True, "spectrum_failures": 0})
            continue
        s = np.arange(n, 0, -1, dtype=float); s /= s.sum()
        r = np.arange(1, n + 1, dtype=float); r /= r.sum()
        sigma = np.diag(s)
        target = modular_spectrum(np.diag(r), sigma)
        trials = 100 if n <= 12 else 25
        vals = []
        local_fail = 0
        for _ in range(trials):
            u = random_unitary(n, rng)
            rho = u @ np.diag(r) @ u.conj().T
            if not np.allclose(modular_spectrum(rho, sigma), target, atol=5e-12, rtol=5e-12):
                local_fail += 1
            vals.append(trace_distance(rho, sigma))
        failures += local_fail
        records.append({
            "n": n, "trials": trials, "degenerate": False,
            "spectrum_failures": local_fail,
            "trace_distance_min": float(min(vals)),
            "trace_distance_max": float(max(vals)),
            "trace_distance_spread": float(max(vals) - min(vals)),
        })
    return {"seed": seed, "classification": "FALSIFIED", "spectrum_failures": failures,
            "witness": exact_qubit_witness(), "records": records}


if __name__ == "__main__":
    out = stress()
    path = Path("results/cycle065_relative_modular_spectrum_no_go.json")
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
