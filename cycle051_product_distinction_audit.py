"""Regenerate cycle051 product-composition audit with exact rational arithmetic."""
import csv, random
from fractions import Fraction
from cycle051_product_distinction_composition import normalize,total_variation,product_tv,lower_bound,upper_bound

SEED=51051


def trial_rows(dimensions=range(1,13), samples=200):
    rng=random.Random(SEED)
    rows=[]
    for n in dimensions:
        lf=uf=0
        for _ in range(samples):
            raw=[]
            for m in (n,n,n+1,n+1):
                x=[rng.randrange(10) for _ in range(m)]
                if not any(x): x[0]=1
                raw.append(normalize(x))
            p,q,r,s=raw
            d1,d2=total_variation(p,q),total_variation(r,s)
            dab=product_tv(p,q,r,s)
            lf += int(dab < lower_bound(d1,d2))
            uf += int(dab > upper_bound(d1,d2))
        rows.append((n,samples,lf,uf))
    return rows


def main(path="results/cycle051_product_distinction_composition_audit_regenerated.csv"):
    rows=trial_rows()
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["alphabet_dimension","samples","lower_bound_failures","upper_bound_failures"])
        w.writerows(rows)
    assert all(r[2]==0 and r[3]==0 for r in rows)
    print(path)

if __name__=="__main__":
    main()
