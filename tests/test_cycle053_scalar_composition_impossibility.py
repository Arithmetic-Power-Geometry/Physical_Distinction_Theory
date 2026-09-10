from fractions import Fraction as F


def tv_binary(a, b):
    return abs(a - b)


def product_tv(a, b, c, d):
    p = (a*c, a*(1-c), (1-a)*c, (1-a)*(1-c))
    q = (b*d, b*(1-d), (1-b)*d, (1-b)*(1-d))
    return sum(abs(x-y) for x, y in zip(p, q)) / 2


def test_same_scalar_inputs_different_composite_tv():
    a, b = F(0), F(1, 4)
    c1, d1 = F(0), F(1, 4)
    c2, d2 = F(1, 4), F(0)

    assert tv_binary(a, b) == F(1, 4)
    assert tv_binary(c1, d1) == F(1, 4)
    assert tv_binary(c2, d2) == F(1, 4)

    aligned = product_tv(a, b, c1, d1)
    reversed_orientation = product_tv(a, b, c2, d2)

    assert aligned == F(7, 16)
    assert reversed_orientation == F(1, 4)
    assert aligned != reversed_orientation


def test_grid_has_scalar_nonclosure_witnesses():
    grid = [F(i, 4) for i in range(5)]
    buckets = {}
    for a in grid:
        for b in grid:
            da = tv_binary(a, b)
            for c in grid:
                for d in grid:
                    db = tv_binary(c, d)
                    D = product_tv(a, b, c, d)
                    buckets.setdefault((da, db), set()).add(D)
    assert any(len(values) > 1 for values in buckets.values())
