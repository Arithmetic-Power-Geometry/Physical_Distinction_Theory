"""Cycle 137: full-isotropy selector audit for PDT-II.

Tests the conditional theorem:
A nonzero alternating bilinear B: R^n x R^n -> R^n that is equivariant
under every proper rotation SO(n) can exist only for n=3.

The theorem itself is proved in the accompanying research note. This script
provides exact/symbolic-style finite witnesses and seeded numerical checks.
"""
from __future__ import annotations
import json, math, random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 137137

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm2(a): return dot(a,a)
def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def matvec(M,x): return [sum(M[i][j]*x[j] for j in range(len(x))) for i in range(len(M))]
def maxabs(a): return max((abs(x) for x in a), default=0.0)

def cross3(a,b):
    return [a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]

FANO = [(0,1,2),(0,3,4),(0,6,5),(1,3,5),(1,4,6),(2,3,6),(2,5,4)]
def cross7(a,b):
    z=[0.0]*7
    for i,j,k in FANO:
        rules=((i,j,k,1),(j,k,i,1),(k,i,j,1),
               (j,i,k,-1),(k,j,i,-1),(i,k,j,-1))
        for p,q,r,s in rules:
            z[r] += s*a[p]*b[q]
    return z

def plane_quarter_turn(n,i,j):
    M=[[1.0 if r==c else 0.0 for c in range(n)] for r in range(n)]
    M[i][i]=M[j][j]=0.0
    M[j][i]=1.0
    M[i][j]=-1.0
    return M

def rodrigues(axis,theta):
    x,y,z=axis
    m=math.sqrt(x*x+y*y+z*z)
    x,y,z=x/m,y/m,z/m
    c,s=math.cos(theta),math.sin(theta)
    C=1-c
    return [
        [c+x*x*C, x*y*C-z*s, x*z*C+y*s],
        [y*x*C+z*s, c+y*y*C, y*z*C-x*s],
        [z*x*C-y*s, z*y*C+x*s, c+z*z*C],
    ]

def audit3(samples=500):
    rng=random.Random(SEED)
    max_res=0.0
    for _ in range(samples):
        axis=[rng.uniform(-1,1) for _ in range(3)]
        if norm2(axis)<1e-12: axis=[1.0,0.0,0.0]
        R=rodrigues(axis,rng.uniform(-math.pi,math.pi))
        a=[rng.uniform(-3,3) for _ in range(3)]
        b=[rng.uniform(-3,3) for _ in range(3)]
        lhs=cross3(matvec(R,a),matvec(R,b))
        rhs=matvec(R,cross3(a,b))
        max_res=max(max_res,maxabs(sub(lhs,rhs)))
    return {"samples":samples,"failures":0 if max_res<1e-10 else None,"max_abs_residual":max_res}

def exact_7d_failure():
    e=[[1.0 if i==j else 0.0 for i in range(7)] for j in range(7)]
    R=plane_quarter_turn(7,0,1)  # determinant +1
    lhs=cross7(matvec(R,e[0]),matvec(R,e[3]))
    rhs=matvec(R,cross7(e[0],e[3]))
    gap=sub(lhs,rhs)
    return {
        "rotation":"quarter-turn in (e1,e2): e1->e2, e2->-e1",
        "input_pair":["e1","e4"],
        "B(Re1,Re4)":lhs,
        "R_B(e1,e4)":rhs,
        "gap":gap,
        "gap_norm2":norm2(gap),
        "equivariant": maxabs(gap)==0.0,
    }

def dimension_status(n):
    if n==3:
        return "SURVIVES: standard cross product is nonzero, alternating, bilinear, SO(3)-equivariant"
    return "EXCLUDED by stabilizer theorem for nonzero fully SO(n)-equivariant alternating bilinear VxV->V"

def run():
    result={
        "cycle":137,
        "claim":"full-SO(n)-equivariant nonzero alternating bilinear vector selector exists only at n=3",
        "classification":{
            "theorem":"PROVED (conditional on stated hypotheses)",
            "mathematical_novelty":"IMPORTED/KNOWN boundary; not claimed novel",
            "pdt_native_derivation":"OPEN: PDT must derive bilinearity, alternation, and full proper-rotation covariance",
            "numerics":"NUMERICALLY SUPPORTED",
            "breakthrough_candidate":"NO",
        },
        "dimensions":{str(n):dimension_status(n) for n in DIMS},
        "so3_random_audit":audit3(),
        "so7_decisive_counterexample":exact_7d_failure(),
    }
    out=Path("results/cycle137_full_isotropy_n3_selector.json")
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    return result

if __name__=="__main__":
    r=run()
    print(json.dumps(r,indent=2))
