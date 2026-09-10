from fractions import Fraction
import random

from cycle061_chi2_revelation_conservation import verify_exact


def norm(vals):
    s=sum(vals); return [Fraction(v,s) for v in vals]


def kernel(m,n,rng):
    cols=[]
    for _ in range(n):
        v=[rng.randint(1,9) for _ in range(m)]; s=sum(v)
        cols.append([Fraction(x,s) for x in v])
    return [[cols[i][j] for i in range(n)] for j in range(m)]


def test_cycle061_exact_dimensions_1_to_12():
    rng=random.Random(61061)
    for n in range(1,13):
        for _ in range(25):
            p=norm([rng.randint(1,9) for _ in range(n)])
            q=norm([rng.randint(1,9) for _ in range(n)])
            m=max(1, min(n, 1+rng.randrange(max(1,n))))
            r=max(1, min(m, 1+rng.randrange(max(1,m))))
            k=kernel(m,n,rng); h=kernel(r,m,rng)
            assert verify_exact(p,q,k,h)


def test_cycle061_degenerate_identity_and_erasure():
    p=[Fraction(1,3),Fraction(2,3)]; q=[Fraction(1,2),Fraction(1,2)]
    identity=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    erase=[[Fraction(1),Fraction(1)]]
    assert verify_exact(p,q,identity,erase)
