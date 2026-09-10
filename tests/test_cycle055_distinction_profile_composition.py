from fractions import Fraction as F

from cycle055_distinction_profile_composition import (
    distinction_profile, multiplicative_convolution, tensor_prob,
    total_variation, tv_from_profile, verify_product_law,
)


def test_binary_exact_product_profile():
    p=[F(3,4),F(1,4)]; q=[F(1,2),F(1,2)]
    r=[F(2,3),F(1,3)]; s=[F(1,3),F(2,3)]
    a=distinction_profile(p,q)
    b=distinction_profile(r,s)
    c=multiplicative_convolution(a,b)
    assert c == distinction_profile(tensor_prob(p,r), tensor_prob(q,s))
    assert tv_from_profile(c) == total_variation(tensor_prob(p,r), tensor_prob(q,s))


def test_identity_profile():
    p=[F(1,3),F(2,3)]
    assert distinction_profile(p,p) == {F(1): F(1)}


def test_associativity():
    a={F(1,2):F(1,2), F(3,2):F(1,2)}
    b={F(1):F(1,3), F(2):F(2,3)}
    c={F(1,4):F(1,5), F(19,16):F(4,5)}
    assert multiplicative_convolution(multiplicative_convolution(a,b),c) == multiplicative_convolution(a,multiplicative_convolution(b,c))


def test_verifier():
    p=[F(2,5),F(3,5)]; q=[F(1,4),F(3,4)]
    r=[F(4,7),F(3,7)]; s=[F(5,8),F(3,8)]
    assert verify_product_law(p,q,r,s) == (True, True)
