"""Cycle 051: exact total-variation composition bounds for independent records.

For probability pairs (p,q) and (r,s), with d1=TV(p,q), d2=TV(r,s),

    max(d1,d2) <= TV(p⊗r, q⊗s) <= d1+d2-d1*d2.

The upper bound iterates to k independent factors:
    TV(⊗P_i, ⊗Q_i) <= 1 - Π_i(1-TV(P_i,Q_i)).

This is established probability/coupling mathematics. PDT use: it is a rigorous
composition constraint for operational distinction, not a unique state-space tensor rule.
"""
from fractions import Fraction
from functools import reduce
from operator import mul


def _as_fraction(x):
    return x if isinstance(x, Fraction) else Fraction(x)


def normalize(weights):
    w = [_as_fraction(x) for x in weights]
    if any(x < 0 for x in w):
        raise ValueError("probability weights must be nonnegative")
    total = sum(w, Fraction(0))
    if total == 0:
        raise ValueError("at least one weight must be positive")
    return [x / total for x in w]


def total_variation(p, q):
    if len(p) != len(q):
        raise ValueError("distributions must have equal length")
    return sum((abs(_as_fraction(a)-_as_fraction(b)) for a,b in zip(p,q)), Fraction(0))/2


def tensor(p, q):
    return [_as_fraction(a)*_as_fraction(b) for a in p for b in q]


def product_tv(p, q, r, s):
    return total_variation(tensor(p,r), tensor(q,s))


def lower_bound(d1, d2):
    return max(_as_fraction(d1), _as_fraction(d2))


def upper_bound(d1, d2):
    d1, d2 = _as_fraction(d1), _as_fraction(d2)
    return d1 + d2 - d1*d2


def k_factor_upper(distances):
    one = Fraction(1)
    complement = reduce(mul, (one-_as_fraction(d) for d in distances), one)
    return one-complement


def upper_saturating_witness(d1, d2):
    """Binary pairs attaining d1+d2-d1*d2 exactly."""
    d1, d2 = _as_fraction(d1), _as_fraction(d2)
    if not (0 <= d1 <= 1 and 0 <= d2 <= 1):
        raise ValueError("distances must lie in [0,1]")
    p = [Fraction(1), Fraction(0)]
    q = [1-d1, d1]
    r = [Fraction(1), Fraction(0)]
    s = [1-d2, d2]
    return p,q,r,s


def falsify_naive_rules():
    """Small exact counterexamples to additive and multiplicative scalar rules."""
    p=[Fraction(1),Fraction(0)]
    q=[Fraction(1,2),Fraction(1,2)]
    r=[Fraction(1),Fraction(0)]
    s=[Fraction(3,4),Fraction(1,4)]
    d1,d2=total_variation(p,q),total_variation(r,s)
    dab=product_tv(p,q,r,s)
    # Same second factor falsifies multiplicative D_AB=d1*d2.
    same=[Fraction(1,3),Fraction(2,3)]
    mult_dab=product_tv(p,q,same,same)
    return {
        "d1":d1,"d2":d2,"dab":dab,"naive_sum":d1+d2,
        "multiplicative_local_second":Fraction(0),"multiplicative_product":mult_dab
    }
