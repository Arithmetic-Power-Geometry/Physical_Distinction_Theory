"""Cycle 275: exact tensor-factorization stress tests for the Rényi selector no-go."""
from fractions import Fraction


def moment(p, q, alpha):
    """Pre-log Rényi moment for positive rational states, integer alpha >= 2."""
    assert len(p) == len(q)
    assert alpha >= 2
    assert sum(p) == 1 and sum(q) == 1
    assert all(x > 0 for x in p + q)
    return sum((x ** alpha) / (y ** (alpha - 1)) for x, y in zip(p, q))


def tensor(p, r):
    return tuple(x * y for x in p for y in r)


def positive_pair(n):
    assert n >= 2
    # Two different, strictly positive exact rational states.
    p_raw = tuple(Fraction(i + 1) for i in range(n))
    q_raw = tuple(Fraction((i + 1) ** 2) for i in range(n))
    zp, zq = sum(p_raw), sum(q_raw)
    return tuple(x / zp for x in p_raw), tuple(x / zq for x in q_raw)


def test_exact_product_factorization_n2_to_n12_orders2_and3():
    for n in range(2, 13):
        p, q = positive_pair(n)
        # Use a reversed second factor to avoid relying on identical-copy symmetry.
        r, s = tuple(reversed(p)), tuple(reversed(q))
        for alpha in (2, 3):
            lhs = moment(tensor(p, r), tensor(q, s), alpha)
            rhs = moment(p, q, alpha) * moment(r, s, alpha)
            assert lhs == rhs


def test_orders_are_not_same_functional_exactly():
    # Exact pre-log witness. If D2 == D3, then M2^2 == M3 because
    # D2=log M2 and D3=(1/2)log M3.
    p = (Fraction(2, 3), Fraction(1, 3))
    q = (Fraction(1, 4), Fraction(3, 4))
    m2 = moment(p, q, 2)
    m3 = moment(p, q, 3)
    assert m2 * m2 != m3


def test_permutation_invariance_exact():
    for n in range(2, 13):
        p, q = positive_pair(n)
        perm_p, perm_q = tuple(reversed(p)), tuple(reversed(q))
        for alpha in (2, 3):
            assert moment(p, q, alpha) == moment(perm_p, perm_q, alpha)
