from fractions import Fraction
from cycle057_augmented_distinction_profile import (
    augmented_profile,
    compose_augmented_profiles,
    product_distribution,
    total_variation,
    tv_from_augmented_profile,
)


def F(n, d=1):
    return Fraction(n, d)


def test_minimal_singular_counterexample_to_unaugmented_profile():
    p=[F(0),F(1)]; q=[F(1),F(0)]
    s, mu = augmented_profile(p,q)
    naive = sum(w*abs(lam-1) for lam,w in mu.items())/2
    assert naive == F(1,2)
    assert total_variation(p,q) == F(1)
    assert tv_from_augmented_profile(s,mu) == F(1)


def test_augmented_profile_recovers_tv_with_singular_support():
    cases = [
        ([F(0),F(1)],[F(1),F(0)]),
        ([F(1,2),F(1,2)],[F(1),F(0)]),
        ([F(1),F(0),F(0)],[F(0),F(1,2),F(1,2)]),
        ([F(1,3),F(2,3),F(0)],[F(1,2),F(0),F(1,2)]),
    ]
    for p,q in cases:
        s,mu=augmented_profile(p,q)
        assert tv_from_augmented_profile(s,mu)==total_variation(p,q)


def test_augmented_profile_composes_exactly():
    p=[F(1,2),F(1,2),F(0)]; q=[F(1),F(0),F(0)]
    r=[F(0),F(1,3),F(2,3)]; s=[F(1,2),F(1,2),F(0)]
    lhs=augmented_profile(product_distribution(p,r), product_distribution(q,s))
    rhs=compose_augmented_profiles(augmented_profile(p,q), augmented_profile(r,s))
    assert lhs == rhs
    assert tv_from_augmented_profile(*lhs) == total_variation(product_distribution(p,r), product_distribution(q,s))
