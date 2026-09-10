"""Cycle 062: exact chi^2 product/resource ledger.

For full-support finite binary experiments define
    C(P,Q) = chi^2(P||Q) = sum_i (P_i-Q_i)^2/Q_i.
For independent products:
    1 + C_AB = (1 + C_A)(1 + C_B).
Thus K=log(1+C) is additive (the order-2 Renyi divergence).

If local stochastic resource maps produce C_A', C_B' and losses
Delta_A=C_A-C_A', Delta_B=C_B-C_B', then
    Delta_AB = Delta_A(1+C_B') + Delta_B(1+C_A') + Delta_A Delta_B,
and the log-budget loss is exactly additive.

The mathematics is known information theory; this file is a PDT bookkeeping
bridge and a novelty boundary, not a breakthrough claim.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
import random
from pathlib import Path


def normalize(xs: list[int]) -> list[Fraction]:
    s = sum(xs)
    if s <= 0:
        raise ValueError("positive total required")
    return [Fraction(x, s) for x in xs]


def chi2(p: list[Fraction], q: list[Fraction]) -> Fraction:
    if len(p) != len(q) or any(x <= 0 for x in q):
        raise ValueError("matching lengths and full-support q required")
    return sum(((a-b)*(a-b))/b for a,b in zip(p,q))


def product(p: list[Fraction], r: list[Fraction]) -> list[Fraction]:
    return [a*b for a in p for b in r]


def random_kernel(n_in: int, n_out: int, rng: random.Random) -> list[list[Fraction]]:
    rows=[]
    for _ in range(n_in):
        rows.append(normalize([rng.randint(1,9) for _ in range(n_out)]))
    return rows


def push(p: list[Fraction], k: list[list[Fraction]]) -> list[Fraction]:
    n_out=len(k[0])
    return [sum(p[i]*k[i][j] for i in range(len(p))) for j in range(n_out)]


def verify_case(n: int, rng: random.Random) -> dict:
    p=normalize([rng.randint(1,20) for _ in range(n)])
    q=normalize([rng.randint(1,20) for _ in range(n)])
    r=normalize([rng.randint(1,20) for _ in range(n)])
    s=normalize([rng.randint(1,20) for _ in range(n)])
    ca, cb = chi2(p,q), chi2(r,s)
    cab = chi2(product(p,r), product(q,s))
    product_ok = cab == ca + cb + ca*cb

    m=max(1, min(n, 4))
    ka=random_kernel(n,m,rng)
    kb=random_kernel(n,m,rng)
    pp, qq = push(p,ka), push(q,ka)
    rr, ss = push(r,kb), push(s,kb)
    cap, cbp = chi2(pp,qq), chi2(rr,ss)
    cabp = chi2(product(pp,rr), product(qq,ss))
    da, db = ca-cap, cb-cbp
    dab = cab-cabp
    resource_ok = dab == da*(1+cbp) + db*(1+cap) + da*db
    monotone_ok = da >= 0 and db >= 0 and dab >= 0
    return {"product_ok":product_ok,"resource_ok":resource_ok,"monotone_ok":monotone_ok}


def audit() -> dict:
    rng=random.Random(62026)
    rows=[]
    failures=0
    for n in range(1,13):
        local=0
        for _ in range(200):
            x=verify_case(n,rng)
            local += int(not all(x.values()))
        failures += local
        rows.append({"n":n,"trials":200,"failures":local})
    for n in [16,24,32,48,64,96,128]:
        local=0
        for _ in range(50):
            x=verify_case(n,rng)
            local += int(not all(x.values()))
        failures += local
        rows.append({"n":n,"trials":50,"failures":local})
    return {"rows":rows,"failures":failures,"pass":failures==0}


def main() -> None:
    result=audit()
    out=Path("results")/"cycle062_chi2_product_resource_ledger.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    if not result["pass"]:
        raise SystemExit("cycle062 audit failed")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
