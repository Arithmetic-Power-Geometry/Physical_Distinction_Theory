"""Exact regressions for Cycle 274 composition-selector non-uniqueness."""
from fractions import Fraction
from itertools import product


def s2(p, q):
    assert len(p) == len(q)
    assert all(x > 0 for x in q)
    return sum((x * x) / y for x, y in zip(p, q))


def d2(p, q):
    return Fraction(1) - Fraction(1, 1) / s2(p, q)


def tensor(p, r):
    return tuple(x * y for x in p for y in r)


def test_small_decisive_binary_example_exact():
    p = (Fraction(1, 2), Fraction(1, 2))
    q = (Fraction(3, 4), Fraction(1, 4))
    assert s2(p, q) == Fraction(4, 3)
    assert d2(p, q) == Fraction(1, 4)
    pp, qq = tensor(p, p), tensor(q, q)
    assert s2(pp, qq) == Fraction(16, 9)
    assert d2(pp, qq) == Fraction(7, 16)
    assert d2(pp, qq) == d2(p, q) + d2(p, q) - d2(p, q) ** 2


def positive_pair(n):
    # Strictly positive rational states for every n>=2.
    # p is uniform; q has weights 1,...,n normalized exactly.
    p = tuple(Fraction(1, n) for _ in range(n))
    z = Fraction(n * (n + 1), 2)
    q = tuple(Fraction(i, 1) / z for i in range(1, n + 1))
    return p, q


def test_product_factorization_and_probabilistic_sum_n1_to_n12():
    # n=1 is the degenerate identity case; n>=2 are nontrivial.
    for n in range(1, 13):
        p, q = positive_pair(n) if n >= 2 else ((Fraction(1),), (Fraction(1),))
        r, s = positive_pair(n) if n >= 2 else ((Fraction(1),), (Fraction(1),))
        lhs_s = s2(tensor(p, r), tensor(q, s))
        rhs_s = s2(p, q) * s2(r, s)
        assert lhs_s == rhs_s
        lhs_d = d2(tensor(p, r), tensor(q, s))
        da, db = d2(p, q), d2(r, s)
        assert lhs_d == da + db - da * db


def test_associativity_on_exact_rational_grid():
    vals = [Fraction(i, 8) for i in range(9)]
    op = lambda a, b: a + b - a * b
    for a, b, c in product(vals, repeat=3):
        assert op(op(a, b), c) == op(a, op(b, c))
        assert op(a, b) == op(b, a)
        assert op(a, Fraction(0)) == a
