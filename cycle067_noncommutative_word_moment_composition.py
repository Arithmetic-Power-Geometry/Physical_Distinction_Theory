"""Cycle 067: noncommutative mixed-word moment composition audit.

Purpose
-------
Test an operator-level replacement for scalar/spectral PDT composition
summaries. For a pair (rho, sigma), define for every word w over {r,s}

    M_w(rho,sigma) = Tr[w(rho,sigma)].

For independent tensor products, M_w is exactly multiplicative.  For
Hermitian tuples, the complete trace-word family is a known simultaneous-
unitary invariant (Specht/trace-invariant theory), so this is an imported
completeness boundary rather than a PDT-native breakthrough.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np


def density_matrix(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    x = a @ a.conj().T
    return x / np.trace(x)


def mixed_moment(rho: np.ndarray, sigma: np.ndarray, word: str) -> complex:
    if rho.shape != sigma.shape or rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError("rho and sigma must be same-size square matrices")
    x = np.eye(rho.shape[0], dtype=complex)
    for letter in word:
        if letter == "r":
            x = x @ rho
        elif letter == "s":
            x = x @ sigma
        else:
            raise ValueError("word alphabet is {'r','s'}")
    return complex(np.trace(x))


def tensor_factorization_error(
    rho_a: np.ndarray,
    sigma_a: np.ndarray,
    rho_b: np.ndarray,
    sigma_b: np.ndarray,
    word: str,
) -> float:
    lhs = mixed_moment(np.kron(rho_a, rho_b), np.kron(sigma_a, sigma_b), word)
    rhs = mixed_moment(rho_a, sigma_a, word) * mixed_moment(rho_b, sigma_b, word)
    return float(abs(lhs - rhs))


def cycle066_witness(theta: float) -> tuple[np.ndarray, np.ndarray]:
    r = np.array([11 / 20, 1 / 4, 3 / 20, 1 / 20], dtype=float)
    s = np.array([1 / 2, 1 / 4, 3 / 20, 1 / 10], dtype=float)
    z = np.exp(1j * theta)
    h = 0.5 * np.array(
        [
            [1, 1, 1, 1],
            [1, z, -1, -z],
            [1, -1, 1, -1],
            [1, -z, -1, z],
        ],
        dtype=complex,
    )
    return h @ np.diag(r) @ h.conj().T, np.diag(s)


def shortest_separating_word(max_len: int = 8, tol: float = 1e-12):
    rho0, sigma0 = cycle066_witness(0.0)
    rhopi, sigmapi = cycle066_witness(np.pi)
    for length in range(1, max_len + 1):
        for letters in itertools.product("rs", repeat=length):
            word = "".join(letters)
            a = mixed_moment(rho0, sigma0, word)
            b = mixed_moment(rhopi, sigmapi, word)
            if abs(a - b) > tol:
                return word, a, b
    return None


def run_audit(seed: int = 6701) -> dict:
    rng = np.random.default_rng(seed)
    words = ["r", "s", "rs", "rrs", "rsrs", "rrssr", "rsrssr"]
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64]
    failures = 0
    cases = 0
    max_error = 0.0
    per_dimension = []

    for d_a in dims:
        # Keep the second factor small so the exact tensor identity is tested
        # without needlessly large Kronecker matrices.
        d_b = 1 if d_a == 1 else 2
        trials = 20 if d_a <= 12 else 8
        local_failures = 0
        local_max = 0.0
        for _ in range(trials):
            rho_a, sigma_a = density_matrix(d_a, rng), density_matrix(d_a, rng)
            rho_b, sigma_b = density_matrix(d_b, rng), density_matrix(d_b, rng)
            for word in words:
                err = tensor_factorization_error(rho_a, sigma_a, rho_b, sigma_b, word)
                cases += 1
                max_error = max(max_error, err)
                local_max = max(local_max, err)
                if err > 1e-10:
                    failures += 1
                    local_failures += 1
        per_dimension.append(
            {"d_a": d_a, "d_b": d_b, "trials": trials, "failures": local_failures, "max_error": local_max}
        )

    sep = shortest_separating_word()
    if sep is None:
        separator = None
    else:
        word, a, b = sep
        separator = {
            "word": word,
            "theta_0_real": float(a.real),
            "theta_pi_real": float(b.real),
            "absolute_gap": float(abs(a - b)),
        }

    return {
        "cycle": 67,
        "classification": ["PROVED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED"],
        "breakthrough_candidate": False,
        "tensor_factorization_cases": cases,
        "tensor_factorization_failures": failures,
        "max_abs_error": max_error,
        "dimensions": dims,
        "separator_of_cycle066_counterfamily": separator,
        "interpretation": (
            "Complete noncommutative trace-word data retains relative operator information "
            "lost by spectra/Petz summaries and composes multiplicatively under independent tensors, "
            "but completeness belongs to established simultaneous-unitary invariant theory."
        ),
        "per_dimension": per_dimension,
    }


if __name__ == "__main__":
    result = run_audit()
    out = Path("results/cycle067_noncommutative_word_moments.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
