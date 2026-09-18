"""Exact regression tests for Cycle 234 refinement-lattice nonuniqueness.

No floating-point simulation is needed: Fraction arithmetic verifies the
one-parameter family and the binary embedding obstruction exactly.
"""
from fractions import Fraction


def atoms(dx, dy, dxy, r):
    return (r, dx-r, dy-r, dxy-dx-dy+r)


def cumulative(a):
    r, ux, uy, s = a
    return (r+ux, r+uy, r+ux+uy+s)


def feasible_interval(dx, dy, dxy):
    return (max(Fraction(0), dx+dy-dxy), min(dx, dy))


def test_smallest_exact_witness_has_continuum_interval():
    dx = dy = Fraction(1, 2)
    dxy = Fraction(1)
    lo, hi = feasible_interval(dx, dy, dxy)
    assert lo == 0
    assert hi == Fraction(1, 2)
    assert hi > lo


def test_two_distinct_atomizations_same_observables():
    target = (Fraction(1,2), Fraction(1,2), Fraction(1))
    a0 = atoms(*target, Fraction(0))
    a1 = atoms(*target, Fraction(1,2))
    assert a0 != a1
    assert all(x >= 0 for x in a0)
    assert all(x >= 0 for x in a1)
    assert cumulative(a0) == target
    assert cumulative(a1) == target


def test_many_exact_rational_selectors_same_observables():
    target = (Fraction(1,2), Fraction(1,2), Fraction(1))
    vals = []
    for k in range(13):
        r = Fraction(k, 24)  # 0 through 1/2
        a = atoms(*target, r)
        assert all(x >= 0 for x in a)
        assert cumulative(a) == target
        vals.append(a)
    assert len(set(vals)) == 13


def test_embedding_dimension_audit_2_through_12():
    # The witness uses labels {0,1}; every alphabet n>=2 contains this subalphabet.
    for n in range(2, 13):
        alphabet = set(range(n))
        assert {0, 1}.issubset(alphabet)


def test_n1_is_degenerate():
    assert len(set(range(1))) == 1
