"""Cycle 086: exact marginal-purity <-> subset-sector ledger.

For an N-partite density operator rho with local dimensions d_i, define
F(T)=D_T Tr(rho_T^2), F(empty)=1.  If C_S denotes the labelled
Hilbert--Schmidt subset-sector weight (C_empty=1), then

    F(T) = sum_{S subseteq T} C_S,
    C(S) = sum_{T subseteq S} (-1)^(|S|-|T|) F(T).

The second identity is Boolean-lattice Mobius inversion.  The result is an
exact algebraic accounting law; numerical routines below are regression
checks only.
"""
from __future__ import annotations

from itertools import combinations
from math import prod
import numpy as np


def subsets(n: int):
    items = range(n)
    for r in range(n + 1):
        yield from combinations(items, r)


def partial_trace(rho: np.ndarray, dims, keep):
    dims = tuple(int(d) for d in dims)
    keep = tuple(sorted(keep))
    if not keep:
        return np.array([[np.trace(rho)]], dtype=complex)
    arr = rho.reshape(dims + dims)
    trace_out = [i for i in range(len(dims)) if i not in keep]
    cur_dims = list(dims)
    for i in sorted(trace_out, reverse=True):
        arr = np.trace(arr, axis1=i, axis2=i + len(cur_dims))
        cur_dims.pop(i)
    dkeep = prod(dims[i] for i in keep)
    return arr.reshape(dkeep, dkeep)


def marginal_purity_zeta(rho: np.ndarray, dims):
    n = len(dims)
    out = {(): 1.0}
    for T in subsets(n):
        if not T:
            continue
        rT = partial_trace(rho, dims, T)
        DT = prod(dims[i] for i in T)
        out[T] = float(DT * np.real(np.trace(rT @ rT)))
    return out


def mobius_sector_weights(F, n: int):
    C = {}
    for S in subsets(n):
        total = 0.0
        Sset = set(S)
        for T in subsets(n):
            if set(T).issubset(Sset):
                total += ((-1) ** (len(S) - len(T))) * F[T]
        C[S] = float(total)
    return C


def apply_local_projector(x: np.ndarray, dims, site: int, traceless: bool):
    """Apply Q_i=I-P_i or P_i, where P_i replaces site i by I_i/d_i."""
    n = len(dims)
    keep = tuple(j for j in range(n) if j != site)
    red = partial_trace(x, dims, keep)
    # Reinsert the maximally mixed factor at its original tensor position.
    d = dims[site]
    if n == 1:
        px = np.eye(d, dtype=complex) * np.trace(x) / d
    else:
        rest_dims = [dims[j] for j in keep]
        rt = red.reshape(tuple(rest_dims) * 2)
        ident = np.eye(d, dtype=complex) / d
        # Build by explicit basis insertion; dimensions here are intentionally small.
        D = prod(dims)
        px = np.zeros((D, D), dtype=complex)
        for a in np.ndindex(*dims):
            for b in np.ndindex(*dims):
                if a[site] != b[site]:
                    continue
                ar = tuple(a[j] for j in keep)
                br = tuple(b[j] for j in keep)
                px[np.ravel_multi_index(a, dims), np.ravel_multi_index(b, dims)] = (
                    rt[ar + br] / d
                )
    return x - px if traceless else px


def direct_sector_weight(rho: np.ndarray, dims, S):
    x = rho.copy()
    S = set(S)
    for i in range(len(dims)):
        x = apply_local_projector(x, dims, i, i in S)
    D = prod(dims)
    return float(D * np.real(np.vdot(x, x)))


def random_density(D: int, rng: np.random.Generator, pure=False):
    if pure:
        v = rng.normal(size=D) + 1j * rng.normal(size=D)
        v /= np.linalg.norm(v)
        return np.outer(v, v.conj())
    a = rng.normal(size=(D, D)) + 1j * rng.normal(size=(D, D))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def run_audit(seed: int = 86013):
    rng = np.random.default_rng(seed)
    configs = [(1,), (2,), (3,), (4,), (2, 2), (2, 3), (3, 3),
               (2, 2, 2), (2, 3, 2), (3, 2, 2), (2, 2, 2, 2)]
    max_res = 0.0
    checks = 0
    states = 0
    min_c = float("inf")
    for dims in configs:
        for pure in (False, True):
            for _ in range(3):
                rho = random_density(prod(dims), rng, pure=pure)
                F = marginal_purity_zeta(rho, dims)
                C = mobius_sector_weights(F, len(dims))
                states += 1
                for S in subsets(len(dims)):
                    direct = direct_sector_weight(rho, dims, S)
                    max_res = max(max_res, abs(C[S] - direct))
                    min_c = min(min_c, direct)
                    checks += 1
    return {
        "seed": seed,
        "dense_states": states,
        "dense_sector_checks": checks,
        "max_dense_abs_residual": max_res,
        "min_direct_sector_weight": min_c,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
