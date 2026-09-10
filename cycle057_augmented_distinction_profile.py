"""Cycle 057: singular-support repair for likelihood-ratio distinction profiles.

All arithmetic can be exact when inputs are fractions.Fraction values.
"""
from collections import defaultdict
from fractions import Fraction


def total_variation(p, q):
    return sum(abs(a-b) for a, b in zip(p, q)) / 2


def augmented_profile(p, q):
    """Return (singular_mass, finite likelihood-ratio profile).

    singular_mass = P({i: Q_i=0}).
    profile is a dict likelihood_ratio -> Q-weight.
    """
    singular_mass = sum(pi for pi, qi in zip(p, q) if qi == 0)
    prof = defaultdict(lambda: Fraction(0, 1))
    for pi, qi in zip(p, q):
        if qi != 0:
            prof[pi / qi] += qi
    return singular_mass, dict(prof)


def tv_from_augmented_profile(singular_mass, profile):
    return (singular_mass + sum(w * abs(lam - 1) for lam, w in profile.items())) / 2


def multiplicative_convolution(profile_a, profile_b):
    out = defaultdict(lambda: Fraction(0, 1))
    for la, wa in profile_a.items():
        for lb, wb in profile_b.items():
            out[la * lb] += wa * wb
    return dict(out)


def compose_augmented_profiles(a, b):
    sa, mua = a
    sb, mub = b
    singular = 1 - (1-sa) * (1-sb)
    return singular, multiplicative_convolution(mua, mub)


def product_distribution(p, r):
    return [a*b for a in p for b in r]
