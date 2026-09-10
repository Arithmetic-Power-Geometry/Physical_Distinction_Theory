"""Cycle 055: exact composition of finite full-support binary distinction profiles.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Apache-2.0
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from typing import Dict, Iterable, List, Tuple

Profile = Dict[Fraction, Fraction]


def _check_prob(v: Iterable[Fraction]) -> List[Fraction]:
    x = list(v)
    if not x or any(z < 0 for z in x) or sum(x) != 1:
        raise ValueError("expected a finite probability vector")
    return x


def distinction_profile(p: Iterable[Fraction], q: Iterable[Fraction]) -> Profile:
    """Law of likelihood ratio p_i/q_i under q; assumes q has full support."""
    p, q = _check_prob(p), _check_prob(q)
    if len(p) != len(q):
        raise ValueError("dimension mismatch")
    if any(qi == 0 for qi in q):
        raise ValueError("cycle055 theorem is stated for full-support q")
    out: defaultdict[Fraction, Fraction] = defaultdict(Fraction)
    for pi, qi in zip(p, q):
        out[pi / qi] += qi
    return dict(out)


def multiplicative_convolution(a: Profile, b: Profile) -> Profile:
    """Profile product law: ratio values multiply and reference masses multiply."""
    out: defaultdict[Fraction, Fraction] = defaultdict(Fraction)
    for ra, wa in a.items():
        for rb, wb in b.items():
            out[ra * rb] += wa * wb
    return dict(out)


def tensor_prob(a: Iterable[Fraction], b: Iterable[Fraction]) -> List[Fraction]:
    return [x * y for x in a for y in b]


def total_variation(p: Iterable[Fraction], q: Iterable[Fraction]) -> Fraction:
    p, q = list(p), list(q)
    if len(p) != len(q):
        raise ValueError("dimension mismatch")
    return sum(abs(x - y) for x, y in zip(p, q)) / 2


def tv_from_profile(mu: Profile) -> Fraction:
    """TV(P,Q) = (1/2) E_Q |dP/dQ - 1|."""
    return sum(w * abs(r - 1) for r, w in mu.items()) / 2


def verify_product_law(
    p: Iterable[Fraction], q: Iterable[Fraction],
    r: Iterable[Fraction], s: Iterable[Fraction],
) -> Tuple[bool, bool]:
    p, q, r, s = map(list, (p, q, r, s))
    lhs = distinction_profile(tensor_prob(p, r), tensor_prob(q, s))
    rhs = multiplicative_convolution(distinction_profile(p, q), distinction_profile(r, s))
    profile_ok = lhs == rhs
    tv_ok = tv_from_profile(rhs) == total_variation(tensor_prob(p, r), tensor_prob(q, s))
    return profile_ok, tv_ok
