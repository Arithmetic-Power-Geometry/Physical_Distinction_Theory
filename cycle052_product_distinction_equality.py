"""Cycle 052: sharp equality audit for product total-variation composition."""
from fractions import Fraction

def tv(p, q):
    return sum(abs(a-b) for a,b in zip(p,q)) / 2

def tensor(p, r):
    return [a*b for a in p for b in r]

def composition_upper(d1, d2):
    return d1 + d2 - d1*d2

def cell_slack(a,b,c,d):
    return min(a*c,b*d) - min(a,b)*min(c,d)

def slack_decomposition(p,q,r,s):
    return sum(cell_slack(a,b,c,d) for a,b in zip(p,q) for c,d in zip(r,s))

def audit_identity(p,q,r,s):
    d1, d2 = tv(p,q), tv(r,s)
    D = tv(tensor(p,r), tensor(q,s))
    return composition_upper(d1,d2)-D, slack_decomposition(p,q,r,s)

def strict_positive_witness():
    p=[Fraction(3,4),Fraction(1,4)]; q=[Fraction(1,4),Fraction(3,4)]
    r=[Fraction(2,3),Fraction(1,3)]; s=[Fraction(1,3),Fraction(2,3)]
    return p,q,r,s

def boundary_saturation_witness():
    p=[Fraction(1),Fraction(0)]; q=[Fraction(1,2),Fraction(1,2)]
    r=[Fraction(1),Fraction(0)]; s=[Fraction(1,2),Fraction(1,2)]
    return p,q,r,s

if __name__ == "__main__":
    for name,w in [("strict-positive",strict_positive_witness()),("boundary-saturation",boundary_saturation_witness())]:
        p,q,r,s=w; d1,d2=tv(p,q),tv(r,s); D=tv(tensor(p,r),tensor(q,s))
        lhs,rhs=audit_identity(*w)
        print(name,d1,d2,D,composition_upper(d1,d2),lhs,rhs)
