"""Cycle 038: nonlinear/predictive resource revelation can exhibit pure synergy.

This module provides exact finite XOR/parity witnesses showing that mutual-information
revelation is not modular or submodular on resource subsets, even though linear effect
rank is modular. The mathematics is standard information theory; PDT uses it as a kill
test against overextending the Cycle 037 linear-rank law.
"""
from __future__ import annotations

from itertools import product
from math import log2
from typing import Iterable, Sequence


def entropy(values: Sequence[int]) -> float:
    if not values:
        raise ValueError("values must be nonempty")
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
    n = len(values)
    return -sum((c / n) * log2(c / n) for c in counts.values())


def mutual_information(x: Sequence[object], y: Sequence[object]) -> float:
    if len(x) != len(y) or not x:
        raise ValueError("x and y must have the same positive length")
    hx = entropy(list(x))
    hy = entropy(list(y))
    pairs = list(zip(x, y))
    hxy = entropy(pairs)
    return hx + hy - hxy


def parity_table(m: int) -> list[tuple[tuple[int, ...], int]]:
    if m < 1:
        raise ValueError("m must be >= 1")
    rows = []
    for bits in product((0, 1), repeat=m):
        rows.append((bits, sum(bits) % 2))
    return rows


def subset_revelation(m: int, subset: Iterable[int]) -> float:
    """I(Y; X_subset) in bits for uniform m-bit parity target Y."""
    idx = tuple(sorted(set(subset)))
    if any(i < 0 or i >= m for i in idx):
        raise ValueError("subset index out of range")
    rows = parity_table(m)
    target = [y for _, y in rows]
    if not idx:
        observation = [0] * len(rows)
    else:
        observation = [tuple(bits[i] for i in idx) for bits, _ in rows]
    return mutual_information(observation, target)


def two_resource_submodular_residual() -> float:
    """f(R)+f(S)-f(R union S)-f(R intersection S) for XOR."""
    f_r = subset_revelation(2, [0])
    f_s = subset_revelation(2, [1])
    f_join = subset_revelation(2, [0, 1])
    f_meet = subset_revelation(2, [])
    return f_r + f_s - f_join - f_meet


def parity_audit(max_m: int = 12) -> list[dict[str, float | int]]:
    if max_m < 1:
        raise ValueError("max_m must be >= 1")
    out = []
    for m in range(1, max_m + 1):
        full = subset_revelation(m, range(m))
        max_strict = 0.0
        if m > 1:
            # For parity, every strict subset has exactly zero information. It is
            # sufficient to audit all leave-one-out subsets plus the empty set;
            # unit tests exhaust all subsets through m=8.
            vals = [subset_revelation(m, [j for j in range(m) if j != i]) for i in range(m)]
            vals.append(subset_revelation(m, []))
            max_strict = max(vals)
        out.append({"m": m, "full_information_bits": full, "max_audited_strict_subset_bits": max_strict})
    return out
