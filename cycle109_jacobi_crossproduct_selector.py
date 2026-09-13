"""Cycle 109: Jacobi-coherent vector composition selector.

Purpose
-------
Test whether a primitive vector-valued composition law can sharpen the surviving
n=3 problem without silently importing associativity.

Known mathematical boundary
---------------------------
A Euclidean bilinear vector cross product satisfying
  (i) x×y is orthogonal to x,y and
  (ii) ||x×y||^2 = ||x||^2||y||^2 - <x,y>^2
exists nontrivially only in dimensions 3 and 7 (Brown-Gray/Hurwitz boundary).
The standard 3D product satisfies Jacobi. The 7D octonionic product does not.

Thus: cross-product axioms + Jacobi => n=3 among nontrivial dimensions.
This is IMPORTED/KNOWN mathematics. It is not yet a PDT-native derivation because
PDT has not independently derived either the vector-valued normed-cross-product
axioms or Jacobi from distinction/resource primitives.
"""
from itertools import product
import json
import numpy as np

FANO = [(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]
MUL = {}
for a,b,c in FANO:
    for i,j,k in ((a,b,c),(b,c,a),(c,a,b)):
        MUL[(i,j)] = (1,k)
        MUL[(j,i)] = (-1,k)
for i in range(1,8):
    MUL[(i,i)] = (-1,0)

DIMS = list(range(1,13)) + [16,24,32,48,64,96,128]

def basis(n,i):
    v=np.zeros(n,dtype=int); v[i-1]=1; return v

def cross3(x,y):
    return np.cross(x,y)

def cross7(x,y):
    out=np.zeros(7,dtype=int)
    for i,a in enumerate(x,1):
        if not a: continue
        for j,b in enumerate(y,1):
            if not b: continue
            s,k=MUL[(i,j)]
            if k:
                out[k-1]+=int(a)*int(b)*s
    return out

def jacobi(cross,x,y,z):
    return cross(x,cross(y,z))+cross(y,cross(z,x))+cross(z,cross(x,y))

def exact_basis_audit(n):
    cross = cross3 if n==3 else cross7
    total=n**3
    failures=[]
    max_sq=0
    for i,j,k in product(range(1,n+1),repeat=3):
        J=jacobi(cross,basis(n,i),basis(n,j),basis(n,k))
        sq=int(J@J)
        max_sq=max(max_sq,sq)
        if sq:
            failures.append({"triple":[i,j,k],"jacobi":J.tolist(),"norm_sq":sq})
    return {
        "dimension": n,
        "ordered_basis_triples": total,
        "jacobi_failures": len(failures),
        "max_jacobi_norm_sq": max_sq,
        "first_failure": failures[0] if failures else None,
    }

def norm_cross_audit(n):
    cross = cross3 if n==3 else cross7
    failures=0
    total=0
    for i,j in product(range(1,n+1),repeat=2):
        x,y=basis(n,i),basis(n,j)
        lhs=int(cross(x,y)@cross(x,y))
        rhs=int((x@x)*(y@y)-(x@y)**2)
        total+=1
        failures += int(lhs != rhs)
    return {"dimension":n,"basis_pairs":total,"norm_identity_failures":failures}

def dimension_selector_ledger():
    rows=[]
    for n in DIMS:
        cross_product_candidate = n in (3,7)
        jacobi_candidate = n == 3
        rows.append({
            "n":n,
            "nontrivial_normed_binary_vector_cross_product_possible":
                cross_product_candidate if n in (3,7) else False,
            "survives_cross_product_plus_jacobi": jacobi_candidate,
            "status":"IMPORTED/KNOWN classification boundary",
        })
    return rows

def random_jacobi_audit(trials=4000,seed=109109):
    rng=np.random.default_rng(seed)
    out={}
    for n,cross in ((3,cross3),(7,cross7)):
        nonzero=0; maxnorm=0.0
        for _ in range(trials):
            x=rng.normal(size=n); y=rng.normal(size=n); z=rng.normal(size=n)
            J=jacobi(cross,x,y,z)
            val=float(np.linalg.norm(J))
            maxnorm=max(maxnorm,val)
            nonzero += int(val>1e-9)
        out[str(n)]={"trials":trials,"nonzero_jacobi_gt_1e-9":nonzero,
                     "max_jacobi_norm":maxnorm}
    return out

def generate():
    a3=exact_basis_audit(3)
    a7=exact_basis_audit(7)
    return {
      "cycle":109,
      "target":"PDT-II (1)/(2): test Jacobi-coherent vector composition as an n=3 selector.",
      "classification":["PROVED","CONDITIONAL","IMPORTED/KNOWN","NUMERICALLY SUPPORTED","OPEN"],
      "breakthrough_candidate":False,
      "exact": {
        "cross3":a3,
        "cross7":a7,
        "norm3":norm_cross_audit(3),
        "norm7":norm_cross_audit(7),
      },
      "random":random_jacobi_audit(),
      "dimension_ledger":dimension_selector_ledger(),
      "conditional_selector": {
        "status":"CONDITIONAL + IMPORTED/KNOWN",
        "statement":"Among nontrivial Euclidean binary vector cross products, dimensions are 3 or 7; imposing Jacobi removes the standard 7D octonionic branch, leaving n=3.",
      },
      "pdt_native_gap": {
        "status":"OPEN",
        "statement":"PDT has not derived from its own distinction/resource primitives that primitive composition must be a normed vector cross product or must satisfy Jacobi. Using those as axioms would not be a non-circular PDT-native derivation."
      },
      "prior_art_boundary":"Vector-cross-product dimension restriction and 7D Jacobi failure are established mathematics; no novelty claim.",
    }

if __name__=="__main__":
    print(json.dumps(generate(),indent=2))
