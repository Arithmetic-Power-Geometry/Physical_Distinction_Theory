"""Sharp purity-only coherence floor audit for PDT controlled sector."""
from __future__ import annotations
import math
import numpy as np


def sharp_purity_floor(P: float) -> float:
    P=float(P)
    if not 0 < P <= 1:
        raise ValueError("purity must lie in (0,1]")
    return math.sqrt(max(0.0, 2.0*P-1.0))


def spectral_floor(p) -> float:
    p=np.asarray(p,float)
    p=p/p.sum()
    return max(0.0,2.0*float(p.max())-1.0)


def audit(seed=20260908, samples_per_dimension=20000, max_dimension=12):
    rng=np.random.default_rng(seed)
    rows=[]
    max_violation=0.0
    for d in range(2,max_dimension+1):
        local=0.0
        for _ in range(samples_per_dimension):
            p=rng.dirichlet(np.ones(d))
            P=float(p@p)
            violation=sharp_purity_floor(P)-spectral_floor(p)
            local=max(local,violation)
        max_violation=max(max_violation,local)
        rows.append((d,local))
    return rows,max_violation


if __name__ == "__main__":
    rows,v=audit()
    for d,x in rows:
        print(f"d={d:2d} max(bound-exact)={x:.3e}")
    print(f"overall numerical violation={v:.3e}")
    # Tight rank-2 family: p=(m,1-m,0,...), m>=1/2.
    for m in np.linspace(.5,1,101):
        P=m*m+(1-m)*(1-m)
        assert abs(sharp_purity_floor(P)-(2*m-1)) < 2e-12
