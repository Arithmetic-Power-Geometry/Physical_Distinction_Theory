"""Cycle 052: sharp equality audit for product total-variation composition.

For probability vectors p,q,r,s define d1=TV(p,q), d2=TV(r,s),
and D=TV(p⊗r,q⊗s).  The standard upper bound is
D <= d1+d2-d1*d2.

This module computes the exact nonnegative slack decomposition
upper-D = sum_ij [min(p_i r_j,q_i s_j)-min(p_i,q_i)min(r_j,s_j)].
All arithmetic can be exact Fractions.
"""
from fractions import Fraction
from itertools import product


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
    lhs = composition_upper(d1,d2)-D
    rhs = slack_decomposition(p,q,r,s)
    return lhs, rhs


def cross_evidence_witness():
    # Oppositely directed binary evidence gives strict inequality.
    p=[Fraction(3,4),Fraction(1,4)]
    q=[Fraction(1,4),Fraction(3,4)]
    r=[Fraction(1,4),Fraction(3,4)]
    s=[Fraction(3,4),Fraction(1,4)]
    return p,q,r,s


def aligned_evidence_witness():
    # Same directional likelihood ordering saturates the upper bound.
    p=[Fraction(3,4),Fraction(1,4)]
    q=[Fraction(1,4),Fraction(3,4)]
    r=[Fraction(3,4),Fraction(1,4)]
    s=[Fraction(1,4),Fraction(3,4)]
    return p,q,r,s


if __name__ == "__main__":
    for name, w in [("cross",cross_evidence_witness()),("aligned",aligned_evidence_witness())]:
        lhs,rhs=audit_identity(*w)
        p,q,r,s=w
        d1,d2=tv(p,q),tv(r,s)
        D=tv(tensor(p,r),tensor(q,s))
        print(name, "d1=",d1,"d2=",d2,"D=",D,"upper=",composition_upper(d1,d2),"slack=",lhs,"decomp=",rhs)
