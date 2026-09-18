"""Exact structural regression tests for Cycle 237 MaxEnt composition no-go.

The information-theoretic MaxEnt theorem is proved analytically in the cycle note.
These tests preserve its smallest physical witness and n=1..12 embeddings without
using floating-point entropy calculations.
"""
from fractions import Fraction


def marginal(joint, axis, n):
    out = [Fraction(0) for _ in range(n)]
    for (a, b), p in joint.items():
        out[a if axis == 0 else b] += p
    return tuple(out)


def product_coupling(pa, pb):
    return {(a, b): x * y for a, x in enumerate(pa) for b, y in enumerate(pb) if x * y}


def equality_probability(joint):
    return sum((p for (a, b), p in joint.items() if a == b), Fraction(0))


def correlated_binary_embedding(n):
    assert n >= 2
    return {(0, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)}


def test_n1_degenerate_unique_coupling():
    p = (Fraction(1),)
    assert product_coupling(p, p) == {(0, 0): Fraction(1)}


def test_n2_through_n12_same_marginals_different_physical_joint():
    for n in range(2, 13):
        p = (Fraction(1, 2), Fraction(1, 2)) + (Fraction(0),) * (n - 2)
        product = product_coupling(p, p)
        correlated = correlated_binary_embedding(n)
        assert marginal(product, 0, n) == p
        assert marginal(product, 1, n) == p
        assert marginal(correlated, 0, n) == p
        assert marginal(correlated, 1, n) == p
        assert product != correlated
        assert equality_probability(product) == Fraction(1, 2)
        assert equality_probability(correlated) == Fraction(1)


def test_correlation_constraint_changes_feasible_selector():
    # P(A=B)=1 excludes the fixed-marginal MaxEnt/product completion.
    for n in range(2, 13):
        p = (Fraction(1, 2), Fraction(1, 2)) + (Fraction(0),) * (n - 2)
        product = product_coupling(p, p)
        correlated = correlated_binary_embedding(n)
        assert equality_probability(product) != Fraction(1)
        assert equality_probability(correlated) == Fraction(1)
