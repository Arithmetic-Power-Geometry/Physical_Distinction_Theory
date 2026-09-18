"""Cycle 238: exact no-signalling composition-selector no-go.

For each output alphabet size n, compare two bipartite boxes with binary inputs:
  PROD: P(a,b|x,y)=1/n^2.
  MOD-n: P(a,b|x,y)=1/n iff b-a = x*y (mod n), else 0.
Both have identical uniform local marginals and are exactly non-signalling.
For n>=2 they are distinct joint/composite models. Hence local data +
normalization + positivity + no-signalling do not uniquely select composition.
All arithmetic uses Fraction.
"""
from fractions import Fraction


def prod(n, x, y, a, b):
    return Fraction(1, n*n)


def modn(n, x, y, a, b):
    return Fraction(1, n) if (b-a-x*y) % n == 0 else Fraction(0)


def marginal_A(box, n, x, y, a):
    return sum((box(n,x,y,a,b) for b in range(n)), Fraction(0))


def marginal_B(box, n, x, y, b):
    return sum((box(n,x,y,a,b) for a in range(n)), Fraction(0))


def audit(box, n):
    for x in (0,1):
        for y in (0,1):
            assert sum((box(n,x,y,a,b) for a in range(n) for b in range(n)), Fraction(0)) == 1
            assert all(box(n,x,y,a,b) >= 0 for a in range(n) for b in range(n))
    # A independent of y; B independent of x
    for x in (0,1):
        for a in range(n):
            assert marginal_A(box,n,x,0,a) == marginal_A(box,n,x,1,a)
    for y in (0,1):
        for b in range(n):
            assert marginal_B(box,n,0,y,b) == marginal_B(box,n,1,y,b)


def relation_success(box, n):
    total = Fraction(0)
    for x in (0,1):
        for y in (0,1):
            p = sum((box(n,x,y,a,b) for a in range(n) for b in range(n)
                     if (b-a-x*y) % n == 0), Fraction(0))
            total += p / 4
    return total


def test_n1_to_12():
    for n in range(1,13):
        audit(prod,n); audit(modn,n)
        for x in (0,1):
            for y in (0,1):
                for a in range(n):
                    assert marginal_A(prod,n,x,y,a) == marginal_A(modn,n,x,y,a) == Fraction(1,n)
                for b in range(n):
                    assert marginal_B(prod,n,x,y,b) == marginal_B(modn,n,x,y,b) == Fraction(1,n)
        if n == 1:
            assert relation_success(prod,n) == relation_success(modn,n) == 1
        else:
            assert relation_success(prod,n) == Fraction(1,n)
            assert relation_success(modn,n) == 1


if __name__ == '__main__':
    test_n1_to_12()
    for n in range(1,13):
        print(n, relation_success(prod,n), relation_success(modn,n))
