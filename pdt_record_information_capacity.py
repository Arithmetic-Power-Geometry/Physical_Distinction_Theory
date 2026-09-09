"""Finite-dimensional record-information capacity audits for PDT.

This module deliberately implements established quantum-information bounds rather
than claiming a new PDT probability law.  It is used to kill any candidate PDT
record-revelation rule that extracts more classical branch information from a
fixed d-dimensional quantum record than the Holevo bound permits.
"""

from __future__ import annotations

import math
import numpy as np


def entropy_bits(rho: np.ndarray, tol: float = 1e-12) -> float:
    """Von Neumann entropy S(rho) in bits."""
    rho = np.asarray(rho, dtype=complex)
    rho = (rho + rho.conj().T) / 2.0
    vals = np.linalg.eigvalsh(rho)
    vals = vals[vals > tol]
    if vals.size == 0:
        return 0.0
    return float(-np.sum(vals * np.log2(vals)))


def uniform_pure_holevo(vectors: np.ndarray) -> float:
    """Holevo chi (bits) for a uniform ensemble of normalized pure states."""
    v = np.asarray(vectors, dtype=complex)
    if v.ndim != 2 or v.shape[0] < 1 or v.shape[1] < 1:
        raise ValueError("vectors must have shape (k,d) with k,d >= 1")
    norms = np.linalg.norm(v, axis=1)
    if np.any(norms <= 0):
        raise ValueError("record vectors must be nonzero")
    v = v / norms[:, None]
    rho_bar = np.einsum("ki,kj->ij", v, v.conj()) / v.shape[0]
    return entropy_bits(rho_bar)


def accessible_information_ceiling_bits(k: int, d: int) -> float:
    """Universal ceiling min(log2 k, log2 d) for k labels in dimension d."""
    if k < 1 or d < 1:
        raise ValueError("k and d must be positive")
    return min(math.log2(k), math.log2(d))


def residual_label_uncertainty_floor_bits(k: int, d: int) -> float:
    """For uniform labels, H(X|Y) >= max(0, log2(k/d)) for every measurement."""
    if k < 1 or d < 1:
        raise ValueError("k and d must be positive")
    return max(0.0, math.log2(k) - math.log2(d))


def repeated_basis_ensemble(k: int, d: int) -> np.ndarray:
    """Equal-multiplicity repeated orthonormal basis; requires d | k.

    This construction saturates the log2(d) accessible-information ceiling:
    measuring in the basis identifies the basis coordinate but cannot identify
    which duplicate label produced it.
    """
    if k < 1 or d < 1 or k % d != 0:
        raise ValueError("require positive k,d with k divisible by d")
    basis = np.eye(d, dtype=complex)
    return np.tile(basis, (k // d, 1))


def random_pure_ensemble(k: int, d: int, rng: np.random.Generator) -> np.ndarray:
    """Fixed-seed-friendly random normalized complex pure-state ensemble."""
    z = rng.normal(size=(k, d)) + 1j * rng.normal(size=(k, d))
    z /= np.linalg.norm(z, axis=1, keepdims=True)
    return z
