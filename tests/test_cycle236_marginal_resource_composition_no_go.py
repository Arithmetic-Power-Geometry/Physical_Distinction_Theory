"""Exact regression tests for Cycle 236 marginal-resource composition no-go."""
from fractions import Fraction


def marginal(joint, axis, n):
    out = [Fraction(0) for _ in range(n)]
    for (a, b), p in joint.items():
        out[a if axis == 0 else b] += p
    return tuple(out)


def equality_probability(joint):
    return sum((p for (a, b), p in joint.items() if a == b), Fraction(0))


def witnesses(n):
    assert n >= 2
    ind = {(a, b): Fraction(1, 4) for a in (0, 1) for b in (0, 1)}
    corr = {
        (0, 0): Fraction(1, 2),
        (1, 1): Fraction(1, 2),
        (0, 1): Fraction(0),
        (1, 0): Fraction(0),
    }
    return ind, corr


def test_n1_is_degenerate():
    joint = {(0, 0): Fraction(1)}
    assert marginal(joint, 0, 1) == (Fraction(1),)
    assert marginal(joint, 1, 1) == (Fraction(1),)


def test_exact_binary_embedding_n2_through_n12():
    for n in range(2, 13):
        ind, corr = witnesses(n)
        expected = (Fraction(1, 2), Fraction(1, 2)) + (Fraction(0),) * (n - 2)
        assert marginal(ind, 0, n) == expected
        assert marginal(ind, 1, n) == expected
        assert marginal(corr, 0, n) == expected
        assert marginal(corr, 1, n) == expected
        assert ind != corr
        assert equality_probability(ind) == Fraction(1, 2)
        assert equality_probability(corr) == Fraction(1)


def test_marginal_only_cost_cannot_separate_witnesses():
    # Arbitrary deterministic marginal-only cost surrogate; equality follows
    # because the marginal vectors themselves are exactly equal.
    def cost(p):
        return sum(x * x for x in p)

    for n in range(2, 13):
        ind, corr = witnesses(n)
        c_ind = cost(marginal(ind, 0, n)) + cost(marginal(ind, 1, n))
        c_corr = cost(marginal(corr, 0, n)) + cost(marginal(corr, 1, n))
        assert c_ind == c_corr
