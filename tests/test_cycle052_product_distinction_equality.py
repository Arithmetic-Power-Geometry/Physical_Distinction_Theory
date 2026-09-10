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
            assert lhs==rhs
            assert lhs>=0


def test_cross_evidence_is_strict():
    p,q,r,s=cross_evidence_witness()
    d1,d2=tv(p,q),tv(r,s)
    D=tv(tensor(p,r),tensor(q,s))
    assert D < composition_upper(d1,d2)
    assert composition_upper(d1,d2)-D == slack_decomposition(p,q,r,s)


def test_aligned_evidence_saturates():
    p,q,r,s=aligned_evidence_witness()
    d1,d2=tv(p,q),tv(r,s)
    D=tv(tensor(p,r),tensor(q,s))
    assert D == composition_upper(d1,d2)
    assert slack_decomposition(p,q,r,s)==0


def test_degenerate_factor():
    p=[Fraction(2,3),Fraction(1,3)]
    q=[Fraction(1,3),Fraction(2,3)]
    r=s=[Fraction(1,2),Fraction(1,2)]
    lhs,rhs=audit_identity(p,q,r,s)
    assert lhs==rhs==0
