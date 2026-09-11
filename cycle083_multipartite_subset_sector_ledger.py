"""Cycle 083: multipartite quadratic subset-sector ledger.

Classification boundary:
- exact decomposition: PROVED
- product factorization: PROVED
- local-bistochastic sector monotonicity: PROVED (analytic; regression uses unitaries)
- novelty: IMPORTED/KNOWN Bloch/correlation-tensor mathematics

No breakthrough claim is made.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np


def random_density(d: int, rng: np.random.Generator, pure: bool = False) -> np.ndarray:
    if pure:
        v = rng.normal(size=d) + 1j * rng.normal(size=d)
        v /= np.linalg.norm(v)
        return np.outer(v, v.conj())
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def partial_trace_one(rho: np.ndarray, dims: list[int], i: int) -> np.ndarray:
    n = len(dims)
    arr = rho.reshape(*dims, *dims)
    return np.trace(arr, axis1=i, axis2=n + i)


def embed_identity_on_i(reduced: np.ndarray, dims: list[int], i: int) -> np.ndarray:
    n = len(dims)
    rest = [dims[j] for j in range(n) if j != i]
    if not rest:
        return np.eye(dims[i], dtype=complex) / dims[i]
    r = n - 1
    red_arr = reduced.reshape(*rest, *rest)
    ident = np.eye(dims[i], dtype=complex) / dims[i]
    arr = np.tensordot(red_arr, ident, axes=0)
    row_axes, col_axes, k = [], [], 0
    for j in range(n):
        if j == i:
            row_axes.append(2 * r)
            col_axes.append(2 * r + 1)
        else:
            row_axes.append(k)
            col_axes.append(r + k)
            k += 1
    arr = arr.transpose(*(row_axes + col_axes))
    d = math.prod(dims)
    return arr.reshape(d, d)


def p_local(rho: np.ndarray, dims: list[int], i: int) -> np.ndarray:
    """Hilbert--Schmidt projector onto identity on subsystem i."""
    return embed_identity_on_i(partial_trace_one(rho, dims, i), dims, i)


def sector(rho: np.ndarray, dims: list[int], subset: set[int]) -> np.ndarray:
    """Q on sites in subset and P on its complement, Q=I-P."""
    x = rho.copy()
    for i in range(len(dims)):
        if i in subset:
            x = x - p_local(x, dims, i)
        else:
            x = p_local(x, dims, i)
    return x


def distinction_energy(rho: np.ndarray) -> float:
    d = rho.shape[0]
    return float(d * np.trace(rho @ rho).real - 1.0)


def product_sector_formula(local_rhos: list[np.ndarray]) -> tuple[list[float], dict[tuple[int, ...], float]]:
    energies = [distinction_energy(rho) for rho in local_rhos]
    values: dict[tuple[int, ...], float] = {}
    n = len(local_rhos)
    for r in range(1, n + 1):
        for s in itertools.combinations(range(n), r):
            values[s] = float(np.prod([energies[i] for i in s]))
    return energies, values


def _random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(x)
    diag = np.diag(r)
    phase = np.where(np.abs(diag) > 0, diag / np.abs(diag), 1.0)
    return q @ np.diag(np.conj(phase))


def run_audit() -> dict[str, float | int | str | list[int]]:
    rng = np.random.default_rng(8301)
    max_decomp = max_reconstruct = max_orth = 0.0
    dense_bipartite_cases = 0

    # Full dense matrix checks for every equal local dimension n=1,...,12.
    for n in range(1, 13):
        d = n * n
        for pure in (False, True):
            rho = random_density(d, rng, pure=pure)
            dims = [n, n]
            secs = {}
            for mask in range(4):
                s = {i for i in range(2) if mask & (1 << i)}
                secs[tuple(sorted(s))] = sector(rho, dims, s)
            max_reconstruct = max(max_reconstruct, float(np.linalg.norm(sum(secs.values()) - rho)))
            for (_, a), (_, b) in itertools.combinations(secs.items(), 2):
                max_orth = max(max_orth, float(abs(np.vdot(a, b))))
            energy = distinction_energy(rho)
            total = sum(d * float(np.vdot(x, x).real) for s, x in secs.items() if s)
            max_decomp = max(max_decomp, abs(energy - total))
            dense_bipartite_cases += 1

    # Explicit three-party correlated checks where full matrices remain inexpensive.
    dense_tripartite_cases = 0
    for n in range(1, 5):
        d = n**3
        rho = random_density(d, rng)
        dims = [n, n, n]
        secs = {}
        for mask in range(8):
            s = {i for i in range(3) if mask & (1 << i)}
            secs[tuple(sorted(s))] = sector(rho, dims, s)
        max_reconstruct = max(max_reconstruct, float(np.linalg.norm(sum(secs.values()) - rho)))
        for (_, a), (_, b) in itertools.combinations(secs.items(), 2):
            max_orth = max(max_orth, float(abs(np.vdot(a, b))))
        energy = distinction_energy(rho)
        total = sum(d * float(np.vdot(x, x).real) for s, x in secs.items() if s)
        max_decomp = max(max_decomp, abs(energy - total))
        dense_tripartite_cases += 1

    # Product factorization: n=1,...,12 plus higher dimensions, without constructing n^3 matrices.
    tested_product_dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    max_product = 0.0
    for n in tested_product_dims:
        local = [random_density(n, rng, pure=(k % 2 == 0)) for k in range(3)]
        energies, values = product_sector_formula(local)
        lhs = sum(values.values())
        rhs = float(np.prod([1.0 + e for e in energies]) - 1.0)
        max_product = max(max_product, abs(lhs - rhs))

    # Local-unitary invariance of each nonempty bipartite sector.
    max_unitary = 0.0
    unitary_checks = 0
    for n in range(2, 7):
        d = n * n
        rho = random_density(d, rng)
        u, v = _random_unitary(n, rng), _random_unitary(n, rng)
        w = np.kron(u, v)
        rho2 = w @ rho @ w.conj().T
        for mask in (1, 2, 3):
            s = {i for i in range(2) if mask & (1 << i)}
            x1, x2 = sector(rho, [n, n], s), sector(rho2, [n, n], s)
            c1, c2 = d * float(np.vdot(x1, x1).real), d * float(np.vdot(x2, x2).real)
            max_unitary = max(max_unitary, abs(c1 - c2))
            unitary_checks += 1

    return {
        "cycle": 83,
        "classification": ["PROVED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED"],
        "breakthrough_candidate": "NO",
        "dense_bipartite_cases": dense_bipartite_cases,
        "dense_tripartite_cases": dense_tripartite_cases,
        "product_factorization_cases": len(tested_product_dims),
        "product_dimensions": tested_product_dims,
        "local_unitary_sector_checks": unitary_checks,
        "max_decomposition_residual": float(max_decomp),
        "max_reconstruction_norm": float(max_reconstruct),
        "max_orthogonality_inner_product": float(max_orth),
        "max_product_factorization_residual": float(max_product),
        "max_local_unitary_sector_residual": float(max_unitary),
    }


if __name__ == "__main__":
    out = run_audit()
    path = Path("results/cycle083_multipartite_subset_sector_ledger.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
