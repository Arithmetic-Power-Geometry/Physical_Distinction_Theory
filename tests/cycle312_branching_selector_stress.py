"""Cycle 312 regression: Shannon exact branching identity across finite arities.

This is a falsification guard for the claim that exact branching privileges n=3.
It is not a novelty or experimental test.
"""
from fractions import Fraction
import math
import random


def H(p):
    return -sum(float(x) * math.log(float(x)) for x in p if x)


def refine(p, k, q):
    return p[:k] + tuple(p[k] * x for x in q) + p[k + 1 :]


def assert_chain(p, k, q, tol=2e-12):
    lhs = H(refine(p, k, q))
    rhs = H(p) + float(p[k]) * H(q)
    assert abs(lhs - rhs) <= tol * max(1.0, abs(lhs), abs(rhs)), (p, k, q, lhs, rhs)


def rational_distribution(n, rng):
    if n == 1:
        return (Fraction(1),)
    xs = [rng.randrange(0, 21) for _ in range(n)]
    if sum(xs) == 0:
        xs[0] = 1
    s = sum(xs)
    return tuple(Fraction(x, s) for x in xs)


def test_dimensions_1_through_12_and_edges():
    rng = random.Random(312)
    qs = [
        (Fraction(1),),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)),
        (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
    ]
    for n in range(1, 13):
        candidates = [tuple([Fraction(1)] + [Fraction(0)] * (n - 1))]
        candidates += [rational_distribution(n, rng) for _ in range(100)]
        for p in candidates:
            for k in range(n):
                for q in qs:
                    assert_chain(p, k, q)


def test_random_higher_dimensions():
    rng = random.Random(312312)
    for n in (16, 32, 64, 128):
        for _ in range(50):
            p = rational_distribution(n, rng)
            q = rational_distribution(rng.randrange(1, 13), rng)
            assert_chain(p, rng.randrange(n), q, tol=1e-11)


if __name__ == "__main__":
    test_dimensions_1_through_12_and_edges()
    test_random_higher_dimensions()
    print("cycle312: all branching identity stress tests passed")
