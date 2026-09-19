"""Cycle 248: exact finite stress test for dimension blindness of sharp-purification thermodynamic structure.

This is deliberately a theorem-regression test, not evidence for a new physical law.
For each n>=1 we construct probability spectra p on n distinguishable levels and verify
normalisation plus the elementary majorization/refinement identities used in the note.
The scientific conclusion is negative: dimension-uniform spectral/majorization laws do
not select n=3.
"""
from fractions import Fraction


def uniform(n):
    assert n >= 1
    return tuple(Fraction(1, n) for _ in range(n))


def delta(n):
    assert n >= 1
    return (Fraction(1),) + tuple(Fraction(0) for _ in range(n - 1))


def majorizes(p, q):
    p = sorted(p, reverse=True)
    q = sorted(q, reverse=True)
    if sum(p) != sum(q):
        return False
    return all(sum(p[:k]) >= sum(q[:k]) for k in range(1, len(p) + 1))


def split_refinement(p, i):
    """Split one weight exactly in half; total weight is conserved."""
    x = p[i]
    return p[:i] + (x / 2, x / 2) + p[i + 1:]


def test_dimensions_1_to_12():
    for n in range(1, 13):
        u = uniform(n)
        d = delta(n)
        assert sum(u) == 1 == sum(d)
        assert majorizes(d, u)
        for i in range(n):
            r = split_refinement(u, i)
            assert sum(r) == sum(u) == 1
            assert len(r) == n + 1


if __name__ == "__main__":
    test_dimensions_1_to_12()
    print("PASS: exact Fraction checks n=1..12; no dimension-specific selector appears.")
