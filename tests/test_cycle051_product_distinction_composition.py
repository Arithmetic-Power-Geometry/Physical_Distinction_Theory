from fractions import Fraction
import random

from cycle051_product_distinction_composition import (
    normalize,total_variation,tensor,product_tv,lower_bound,upper_bound,
    k_factor_upper,upper_saturating_witness,falsify_naive_rules,
)


def test_exact_bounds_random_dimensions_1_to_12():
    rng=random.Random(51051)
    for n in range(1,13):
        for _ in range(100):
            raw=[]
            for m in (n,n,n+1,n+1):
                x=[rng.randrange(10) for _ in range(m)]
                if not any(x): x[0]=1
                raw.append(normalize(x))
            p,q,r,s=raw
            d1,d2=total_variation(p,q),total_variation(r,s)
            dab=product_tv(p,q,r,s)
            assert lower_bound(d1,d2) <= dab <= upper_bound(d1,d2)


def test_upper_bound_is_exactly_attainable():
    for d1 in (Fraction(0),Fraction(1,5),Fraction(1,2),Fraction(1)):
        for d2 in (Fraction(0),Fraction(1,7),Fraction(3,4),Fraction(1)):
            p,q,r,s=upper_saturating_witness(d1,d2)
            assert product_tv(p,q,r,s)==upper_bound(d1,d2)


def test_k_factor_upper_special_case():
    ds=[Fraction(1,10),Fraction(1,5),Fraction(1,4)]
    assert k_factor_upper(ds)==1-(Fraction(9,10)*Fraction(4,5)*Fraction(3,4))


def test_naive_additive_and_multiplicative_rules_fail():
    w=falsify_naive_rules()
    assert w["dab"] != w["naive_sum"]
    assert w["multiplicative_product"] > 0
    assert w["multiplicative_local_second"] == 0


def test_degenerate_and_maximal_cases():
    p=[Fraction(1)]
    assert total_variation(p,p)==0
    a=[Fraction(1),Fraction(0)]
    b=[Fraction(0),Fraction(1)]
    assert total_variation(a,b)==1
    assert product_tv(a,b,p,p)==1
