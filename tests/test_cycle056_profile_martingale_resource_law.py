from fractions import Fraction

from cycle056_profile_martingale_resource_law import (
    coarse_likelihood_ratio,
    composition_resource_commutes,
    conditional_expectation_ratio,
    convex_functional,
    pushforward,
    tv_from_profile,
)


def test_conditional_expectation_identity():
    p = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    q = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
    k = [
        [Fraction(1), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(1)],
    ]
    assert coarse_likelihood_ratio(p, q, k) == conditional_expectation_ratio(p, q, k)


def test_convex_functionals_contract():
    p = [Fraction(3, 5), Fraction(1, 5), Fraction(1, 5)]
    q = [Fraction(1, 5), Fraction(2, 5), Fraction(2, 5)]
    k = [
        [Fraction(1), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(1)],
    ]
    kp, kq = pushforward(k, p), pushforward(k, q)
    for phi in (
        lambda x: (x - 1) * (x - 1),
        lambda x: x * x,
        lambda x: abs(x - 1),
    ):
        assert convex_functional(kp, kq, phi) <= convex_functional(p, q, phi)
    assert tv_from_profile(kp, kq) <= tv_from_profile(p, q)


def test_local_resource_maps_commute_with_independent_composition():
    pa = [Fraction(2, 3), Fraction(1, 3)]
    qa = [Fraction(1, 3), Fraction(2, 3)]
    pb = [Fraction(3, 4), Fraction(1, 4)]
    qb = [Fraction(1, 2), Fraction(1, 2)]
    ka = [[Fraction(3, 4), Fraction(1, 4)], [Fraction(1, 4), Fraction(3, 4)]]
    kb = [[Fraction(2, 3), Fraction(1, 3)], [Fraction(1, 3), Fraction(2, 3)]]
    assert composition_resource_commutes(pa, qa, pb, qb, ka, kb)
