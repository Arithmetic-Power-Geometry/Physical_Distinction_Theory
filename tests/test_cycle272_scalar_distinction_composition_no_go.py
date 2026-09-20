from fractions import Fraction


def bernoulli(t):
    return (t, 1 - t)


def tv(p, q):
    return sum(abs(x - y) for x, y in zip(p, q)) / 2


def tensor(p, q):
    return tuple(x * y for x in p for y in q)


def pad(p, n):
    assert n >= len(p)
    return tuple(p) + (Fraction(0),) * (n - len(p))


def test_exact_binary_scalar_composition_counterexample():
    z = Fraction(0)
    a = Fraction(1, 4)

    pA, qA = bernoulli(z), bernoulli(a)
    pB1, qB1 = bernoulli(z), bernoulli(a)
    pB2, qB2 = bernoulli(a), bernoulli(z)

    assert tv(pA, qA) == a
    assert tv(pB1, qB1) == a
    assert tv(pB2, qB2) == a

    d1 = tv(tensor(pA, pB1), tensor(qA, qB1))
    d2 = tv(tensor(pA, pB2), tensor(qA, qB2))

    assert d1 == Fraction(7, 16)
    assert d2 == Fraction(1, 4)
    assert d1 != d2


def test_zero_padding_preserves_counterexample_n2_to_n12():
    z = Fraction(0)
    a = Fraction(1, 4)
    pA2, qA2 = bernoulli(z), bernoulli(a)
    pB12, qB12 = bernoulli(z), bernoulli(a)
    pB22, qB22 = bernoulli(a), bernoulli(z)

    for n in range(2, 13):
        pA, qA = pad(pA2, n), pad(qA2, n)
        pB1, qB1 = pad(pB12, n), pad(qB12, n)
        pB2, qB2 = pad(pB22, n), pad(qB22, n)

        assert tv(pA, qA) == Fraction(1, 4)
        assert tv(pB1, qB1) == Fraction(1, 4)
        assert tv(pB2, qB2) == Fraction(1, 4)
        assert tv(tensor(pA, pB1), tensor(qA, qB1)) == Fraction(7, 16)
        assert tv(tensor(pA, pB2), tensor(qA, qB2)) == Fraction(1, 4)
