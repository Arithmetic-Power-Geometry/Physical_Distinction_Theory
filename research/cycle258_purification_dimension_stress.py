"""Cycle 258: exact dimension stress for purification as a PDT-II selector.

No external numerical claims.  For each n=1..12 we construct a diagonal state
with full rank n and its canonical purification coefficients.  The identity
sum_i lambda_i = 1 and Schmidt rank n show purification exists uniformly; this
is a falsification harness for any claim that purification alone selects n=3.
"""
from fractions import Fraction


def full_rank_spectrum(n: int):
    # strictly positive rational spectrum, exactly normalized
    denom = n * (n + 1) // 2
    return [Fraction(i, denom) for i in range(1, n + 1)]


def audit(n: int):
    lam = full_rank_spectrum(n)
    assert sum(lam) == 1
    assert all(x > 0 for x in lam)
    # canonical purification |Psi> = sum sqrt(lambda_i)|i>|i> has
    # reduced spectrum lambda and Schmidt rank n.
    return {"n": n, "rank": len(lam), "normalized": sum(lam) == 1}


if __name__ == "__main__":
    rows = [audit(n) for n in range(1, 13)]
    assert all(r["rank"] == r["n"] and r["normalized"] for r in rows)
    for r in rows:
        print(r)
