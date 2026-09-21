from fractions import Fraction


def bern(p):
    return (p, 1 - p)


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def product(p, q):
    return tuple(a * b for a in p for b in q)


def test_same_local_tv_different_product_tv_exact():
    z = Fraction(0)
    q = Fraction(1, 4)

    a0, a1 = bern(z), bern(q)

    # X: both local changes have the same orientation.
    bx0, bx1 = bern(z), bern(q)
    # Y: B has the same local TV but reversed endpoints.
    by0, by1 = bern(q), bern(z)

    da = tv(a0, a1)
    db_x = tv(bx0, bx1)
    db_y = tv(by0, by1)
    assert da == db_x == db_y == q

    d_x = tv(product(a0, bx0), product(a1, bx1))
    d_y = tv(product(a0, by0), product(a1, by1))

    assert d_x == Fraction(7, 16)
    assert d_y == Fraction(1, 4)
    assert d_x != d_y


def test_multiplicative_complement_rule_is_not_universal_equality():
    q = Fraction(1, 4)
    proposed = 1 - (1 - q) * (1 - q)
    assert proposed == Fraction(7, 16)

    a0, a1 = bern(Fraction(0)), bern(q)
    b0, b1 = bern(q), bern(Fraction(0))
    actual = tv(product(a0, b0), product(a1, b1))
    assert actual == Fraction(1, 4)
    assert actual != proposed


def test_dimension_embeddings_n2_through_n12():
    q = Fraction(1, 4)
    base = (bern(Fraction(0)), bern(q), bern(q), bern(Fraction(0)))
    for n in range(2, 13):
        def pad(v):
            return tuple(v) + (Fraction(0),) * (n - 2)

        a0, a1, b0, b1 = map(pad, base)
        assert tv(a0, a1) == tv(b0, b1) == q
        assert tv(product(a0, b0), product(a1, b1)) == q


def test_surviving_product_bounds_on_rational_grid():
    vals = [Fraction(k, 4) for k in range(5)]
    for p in vals:
        for q in vals:
            for r in vals:
                for s in vals:
                    a0, a1 = bern(p), bern(q)
                    b0, b1 = bern(r), bern(s)
                    da, db = tv(a0, a1), tv(b0, b1)
                    dab = tv(product(a0, b0), product(a1, b1))
                    assert max(da, db) <= dab
                    assert dab <= 1 - (1 - da) * (1 - db)
