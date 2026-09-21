import math
import random


def affinity_alpha(p, q, alpha):
    return sum((a ** alpha) * (b ** (1.0 - alpha)) for a, b in zip(p, q))


def symmetric_affinity(p, q, alpha):
    a = affinity_alpha(p, q, alpha)
    b = affinity_alpha(p, q, 1.0 - alpha)
    return math.sqrt(a * b)


def product(p, q):
    return tuple(a * b for a in p for b in q)


def random_prob(n, rng):
    xs = [0.01 + rng.random() for _ in range(n)]
    s = sum(xs)
    return tuple(x / s for x in xs)


def test_binary_decisive_witness_not_bhattacharyya():
    p = (0.9, 0.1)
    q = (0.6, 0.4)
    bh = symmetric_affinity(p, q, 0.5)
    alt = symmetric_affinity(p, q, 0.25)
    assert not math.isclose(bh, alt, rel_tol=0.0, abs_tol=1e-8)
    assert math.isclose(alt, symmetric_affinity(q, p, 0.25), rel_tol=0.0, abs_tol=1e-14)


def test_alpha_family_tensorizes_n1_through_n12():
    rng = random.Random(300)
    for alpha in (0.1, 0.25, 0.5, 0.75, 0.9):
        for n in range(1, 13):
            for m in (1, 2, 5, 12):
                p, q = random_prob(n, rng), random_prob(n, rng)
                r, s = random_prob(m, rng), random_prob(m, rng)
                lhs = affinity_alpha(product(p, r), product(q, s), alpha)
                rhs = affinity_alpha(p, q, alpha) * affinity_alpha(r, s, alpha)
                assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)


def test_symmetric_family_tensorizes_n1_through_n12():
    rng = random.Random(30001)
    for alpha in (0.1, 0.25, 0.4):
        for n in range(1, 13):
            p, q = random_prob(n, rng), random_prob(n, rng)
            r, s = random_prob(13 - n, rng), random_prob(13 - n, rng)
            lhs = symmetric_affinity(product(p, r), product(q, s), alpha)
            rhs = symmetric_affinity(p, q, alpha) * symmetric_affinity(r, s, alpha)
            assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)
            assert math.isclose(symmetric_affinity(p, q, alpha), symmetric_affinity(q, p, alpha), rel_tol=1e-12, abs_tol=1e-12)


def test_higher_dimension_random_stress():
    rng = random.Random(30099)
    for n, m in ((16, 17), (31, 23), (64, 19)):
        p, q = random_prob(n, rng), random_prob(n, rng)
        r, s = random_prob(m, rng), random_prob(m, rng)
        for alpha in (0.2, 0.37, 0.5, 0.81):
            lhs = symmetric_affinity(product(p, r), product(q, s), alpha)
            rhs = symmetric_affinity(p, q, alpha) * symmetric_affinity(r, s, alpha)
            assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)
