"""Cycle 068: finite trace-word operator-completeness boundary.

For a Hermitian pair (rho, sigma), mixed trace words
    M_w(rho,sigma)=Tr[w(rho,sigma)]
compose exactly under independent tensor products. Classical invariant theory
(Procesi/Razmyslov/Specht-type results) additionally gives finite degree bounds
at fixed matrix size, so this is an IMPORTED/KNOWN completeness boundary, not
a PDT-native breakthrough.

This script stress-tests only the exact tensor-factorization law. The finite
completeness statement is theorem-level prior art and is not inferred from the
numerics below.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np


def density_matrix(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    x = a @ a.conj().T
    return x / np.trace(x)


def trace_word(rho: np.ndarray, sigma: np.ndarray, word: str) -> complex:
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
    lhs = trace_word(np.kron(rho_a, rho_b), np.kron(sigma_a, sigma_b), word)
    rhs = trace_word(rho_a, sigma_a, word) * trace_word(rho_b, sigma_b, word)
    return float(abs(lhs - rhs))


def random_word(length: int, rng: np.random.Generator) -> str:
    return "".join(rng.choice(np.array(list("rs")), size=length).tolist())


def run_audit(seed: int = 6801) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    lengths = [1, 2, 3, 4, 5, 6, 8, 10, 12]
    failures = 0
    cases = 0
    max_error = 0.0
    per_dimension = []

    for d_a in dims:
        d_b = 1 if d_a == 1 else 2
        trials = 10 if d_a <= 12 else 4
        local_failures = 0
        local_max = 0.0
        for _ in range(trials):
            rho_a, sigma_a = density_matrix(d_a, rng), density_matrix(d_a, rng)
            rho_b, sigma_b = density_matrix(d_b, rng), density_matrix(d_b, rng)
            for length in lengths:
                word = random_word(length, rng)
                err = tensor_factorization_error(rho_a, sigma_a, rho_b, sigma_b, word)
                cases += 1
                max_error = max(max_error, err)
                local_max = max(local_max, err)
                if err > 1e-9:
                    failures += 1
                    local_failures += 1
        per_dimension.append(
            {
                "d_a": d_a,
                "d_b": d_b,
                "trials": trials,
                "failures": local_failures,
                "max_error": local_max,
            }
        )

    return {
        "cycle": 68,
        "classification": ["PROVED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED"],
        "breakthrough_candidate": False,
        "claim": (
            "At fixed matrix dimension, full simultaneous-unitary information can be "
            "captured by finitely many trace-word invariants from established invariant "
            "theory; each trace word composes multiplicatively under independent tensors."
        ),
        "tensor_factorization_cases": cases,
        "tensor_factorization_failures": failures,
        "max_abs_error": max_error,
        "dimensions": dims,
        "word_lengths_sampled": lengths,
        "prior_art_boundary": (
            "Procesi/Razmyslov trace-invariant generation and Specht-type simultaneous "
            "unitary equivalence results. No PDT novelty claim is made for completeness."
        ),
        "interpretation": (
            "Cycle 067's infinite trace-word boundary can be sharpened to a finite, "
            "dimension-dependent operator-complete boundary. The PDT-native target must "
            "therefore derive a physically selected proper subfamily/resource truncation "
            "with a new operational consequence, rather than rediscover finite matrix invariants."
        ),
        "per_dimension": per_dimension,
    }


if __name__ == "__main__":
    result = run_audit()
    out = Path("results/cycle068_finite_trace_word_boundary.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
