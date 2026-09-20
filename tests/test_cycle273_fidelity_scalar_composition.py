from fractions import Fraction
from math import isqrt


def sqrt_fraction(x: Fraction) -> Fraction:
    """Exact square root for rational perfect squares used in this regression."""
    an, ad = isqrt(x.numerator), isqrt(x.denominator)
    assert an * an == x.numerator and ad * ad == x.denominator
    return Fraction(an, ad)


def bc(p, q):
    return sum((sqrt_fraction(a * b) for a, b in zip(p, q)), Fraction(0))


def tensor(p, r):
    return tuple(a * b for a in p for b in r)


def padded_pair(n):
    if n == 1:
        return (Fraction(1),), (Fraction(1),)
    # Products p_i q_i are perfect rational squares: 9/16 and 1/16.
    p = (Fraction(3, 4), Fraction(1, 4)) + (Fraction(0),) * (n - 2)
    q = (Fraction(3, 4), Fraction(1, 4)) + (Fraction(0),) * (n - 2)
    return p, q


def asymmetric_pair(n):
    if n == 1:
        return (Fraction(1),), (Fraction(1),)
    # p_i q_i = 4/25 and 4/25, again exact squares.
    p = (Fraction(1, 5), Fraction(4, 5)) + (Fraction(0),) * (n - 2)
    q = (Fraction(4, 5), Fraction(1, 5)) + (Fraction(0),) * (n - 2)
    return p, q


def test_bhattacharyya_and_hellinger_product_law_n1_to_n12():
    for n in range(1, 13):
        p, q = padded_pair(n)
        r, s = asymmetric_pair(n)
        b_a, b_b = bc(p, q), bc(r, s)
        b_ab = bc(tensor(p, r), tensor(q, s))
        assert b_ab == b_a * b_b
        h_a, h_b, h_ab = 1 - b_a, 1 - b_b, 1 - b_ab
        assert h_ab == h_a + h_b - h_a * h_b


def test_degenerate_edges():
    same = (Fraction(1), Fraction(0))
    orth = (Fraction(0), Fraction(1))
    assert bc(same, same) == 1
    assert bc(same, orth) == 0
    assert 1 - bc(tensor(same, same), tensor(orth, same)) == 1
