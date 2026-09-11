"""Cycle 076: dimension-3 underdetermination audit.

Status: PROVED no-go at the level of the stated axiom family; NUMERICALLY SUPPORTED
by regression tests. This module does not claim novelty.

Claim tested: the currently surviving PDT-II structures (finite-dimensional density
states, Hilbert-Schmidt quadratic distinction/revelation, and exact independent-product
composition) do not by themselves entail Hilbert-space dimension d=3. For every
integer d>=1 there is a standard finite-dimensional model satisfying the same formal
identities. Therefore a non-circular n=3 derivation requires at least one additional
physical postulate whose content is genuinely dimension-selective.
"""
from __future__ import annotations

import numpy as np


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    d = int(d)
    if d < 1:
        raise ValueError("d must be >= 1")
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = x @ x.conj().T
    return rho / np.trace(rho)


def distinction_energy(rho: np.ndarray) -> float:
    """Dimension-normalized quadratic distinction E_d=d Tr(rho^2)-1."""
    rho = np.asarray(rho, dtype=complex)
    d = rho.shape[0]
    if rho.shape != (d, d):
        raise ValueError("rho must be square")
    return float(np.real(d * np.trace(rho @ rho) - 1.0))


def product_composition_residual(rho: np.ndarray, sigma: np.ndarray) -> float:
    """Residual of 1+E_AB=(1+E_A)(1+E_B)."""
    lhs = 1.0 + distinction_energy(np.kron(rho, sigma))
    rhs = (1.0 + distinction_energy(rho)) * (1.0 + distinction_energy(sigma))
    return float(abs(lhs - rhs))


def orthogonal_revelation_residual(x: np.ndarray, cut: int) -> float:
    """Pythagorean revelation residual for a coordinate resource refinement."""
    x = np.asarray(x, dtype=float).reshape(-1)
    cut = int(cut)
    if not 0 <= cut <= x.size:
        raise ValueError("cut outside vector")
    old = x[:cut]
    new = x[cut:]
    return float(abs(np.dot(x, x) - np.dot(old, old) - np.dot(new, new)))


def pure_state_energy(d: int) -> float:
    """Exact value E_d=d-1 for any pure state; exposes dimension dependence without selecting d."""
    d = int(d)
    if d < 1:
        raise ValueError("d must be >= 1")
    rho = np.zeros((d, d), dtype=complex)
    rho[0, 0] = 1.0
    return distinction_energy(rho)


def stress_audit(seed: int = 76076) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    rows = []
    max_product = 0.0
    max_revelation = 0.0
    cases = 0
    for d in dims:
        reps = 20 if d <= 12 else 5
        for _ in range(reps):
            rho = random_density(d, rng)
            # Keep the partner small so high-dimension regression remains cheap.
            e = 1 + int(rng.integers(1, 5))
            sigma = random_density(e, rng)
            pr = product_composition_residual(rho, sigma)
            x = rng.normal(size=max(1, d * d - 1))
            cut = int(rng.integers(0, x.size + 1))
            rr = orthogonal_revelation_residual(x, cut)
            max_product = max(max_product, pr)
            max_revelation = max(max_revelation, rr)
            cases += 1
        rows.append({
            "dimension": d,
            "pure_state_energy": pure_state_energy(d),
            "expected_pure_state_energy": float(d - 1),
        })
    return {
        "classification": ["PROVED", "NUMERICALLY SUPPORTED", "FALSIFIED: current axioms entail n=3"],
        "dimensions": dims,
        "cases": cases,
        "max_product_composition_residual": max_product,
        "max_quadratic_revelation_residual": max_revelation,
        "rows": rows,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(stress_audit(), indent=2))
