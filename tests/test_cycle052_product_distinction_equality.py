from fractions import Fraction
from cycle052_product_distinction_equality import *

def test_exact_slack_identity_binary_grid():
    vals=[Fraction(i,6) for i in range(7)]
    pairs=[]
    for a in vals:
        p=[a,1-a]
        for b in vals:
            q=[b,1-b]
            pairs.append((p,q))
    for p,q in pairs:
        for r,s in pairs:
            lhs,rhs=audit_identity(p,q,r,s)
            assert lhs==rhs and lhs>=0

def test_strict_positive_nonidentical():
    p,q,r,s=strict_positive_witness()
    d1,d2=tv(p,q),tv(r,s); D=tv(tensor(p,r),tensor(q,s))
    assert D < composition_upper(d1,d2)

def test_boundary_saturation():
    p,q,r,s=boundary_saturation_witness()
    d1,d2=tv(p,q),tv(r,s); D=tv(tensor(p,r),tensor(q,s))
    assert D == composition_upper(d1,d2)
    assert slack_decomposition(p,q,r,s)==0

def test_degenerate_identical_factor():
    p=[Fraction(2,3),Fraction(1,3)]; q=[Fraction(1,3),Fraction(2,3)]
    r=s=[Fraction(1,2),Fraction(1,2)]
    lhs,rhs=audit_identity(p,q,r,s)
    assert lhs==rhs==0
