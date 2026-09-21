import math
import random


def affinity(p, q):
    return sum(math.sqrt(a * b) for a, b in zip(p, q))


def product(p, q):
    return tuple(a * b for a in p for b in q)


def random_prob(n, rng):
    xs = [rng.random() for _ in range(n)]
    s = sum(xs)
    return tuple(x / s for x in xs)


def test_exact_boundary_degenerate_cases():
    cases = [
        ((1.0,), (1.0,)),
        ((1.0, 0.0), (0.0, 1.0)),
        ((1.0, 0.0), (1.0, 0.0)),
        ((0.5, 0.5), (1.0, 0.0)),
    ]
    for p, q in cases:
        for r, s in cases:
            lhs = affinity(product(p, r), product(q, s))
            rhs = affinity(p, q) * affinity(r, s)
            assert math.isclose(lhs, rhs, rel_tol=0.0, abs_tol=1e-14)


def test_dimensions_n1_through_n12_randomized():
    rng = random.Random(299)
    for n in range(1, 13):
        for m in range(1, 13):
            for _ in range(20):
                p, q = random_prob(n, rng), random_prob(n, rng)
                r, s = random_prob(m, rng), random_prob(m, rng)
                lhs = affinity(product(p, r), product(q, s))
                rhs = affinity(p, q) * affinity(r, s)
                assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)


def test_h2_complement_composition():
    rng = random.Random(29901)
    for _ in range(100):
        p, q = random_prob(7, rng), random_prob(7, rng)
        r, s = random_prob(11, rng), random_prob(11, rng)
        ha = 1.0 - affinity(p, q)
        hb = 1.0 - affinity(r, s)
        hab = 1.0 - affinity(product(p, r), product(q, s))
        expected = ha + hb - ha * hb
        assert math.isclose(hab, expected, rel_tol=1e-12, abs_tol=1e-12)


def test_higher_dimension_stress():
    rng = random.Random(29999)
    for n, m in [(16, 17), (31, 23), (64, 19)]:
        p, q = random_prob(n, rng), random_prob(n, rng)
        r, s = random_prob(m, rng), random_prob(m, rng)
        lhs = affinity(product(p, r), product(q, s))
        rhs = affinity(p, q) * affinity(r, s)
        assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)
