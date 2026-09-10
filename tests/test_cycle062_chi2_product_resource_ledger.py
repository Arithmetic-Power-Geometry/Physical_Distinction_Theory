from fractions import Fraction

from cycle062_chi2_product_resource_ledger import chi2, product, push


def test_exact_product_identity():
    p=[Fraction(1,3),Fraction(2,3)]
    q=[Fraction(1,2),Fraction(1,2)]
    r=[Fraction(3,4),Fraction(1,4)]
    s=[Fraction(2,5),Fraction(3,5)]
    ca,cb=chi2(p,q),chi2(r,s)
    cab=chi2(product(p,r),product(q,s))
    assert cab == ca + cb + ca*cb


def test_exact_local_resource_loss_identity():
    p=[Fraction(1,5),Fraction(4,5)]
    q=[Fraction(1,2),Fraction(1,2)]
    r=[Fraction(2,3),Fraction(1,3)]
    s=[Fraction(1,4),Fraction(3,4)]
    k=[
        [Fraction(3,4),Fraction(1,4)],
        [Fraction(1,4),Fraction(3,4)],
    ]
    ca,cb=chi2(p,q),chi2(r,s)
    cap=chi2(push(p,k),push(q,k))
    cbp=chi2(push(r,k),push(s,k))
    cab=chi2(product(p,r),product(q,s))
    cabp=chi2(product(push(p,k),push(r,k)),product(push(q,k),push(s,k)))
    da,db=ca-cap,cb-cbp
    assert cab-cabp == da*(1+cbp) + db*(1+cap) + da*db
    assert da >= 0 and db >= 0 and cab-cabp >= 0


def test_identity_resource_map_has_zero_loss():
    p=[Fraction(1,3),Fraction(2,3)]
    q=[Fraction(2,3),Fraction(1,3)]
    ident=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    assert chi2(p,q) == chi2(push(p,ident),push(q,ident))
