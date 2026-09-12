"""Cycle 106: composition-defect cost no-go.

Question: do natural resource laws for a three-history composition defect force
associativity or n=3? Answer: no.

For a trilinear alternating defect A(x,y,z), D=||A(x,y,z)|| is nonnegative,
absolutely homogeneous in each argument, permutation invariant up to sign before
taking the norm, zero on repeated arguments, and subadditive in each slot. None of
these properties forces A=0. The octonion associator supplies a genuine
nonassociative composition example in seven imaginary dimensions.
"""
from __future__ import annotations
import json, itertools
from pathlib import Path
import numpy as np

FANO=[(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]

def table():
    m={}
    for a,b,c in FANO:
        for x,y,z in ((a,b,c),(b,c,a),(c,a,b)):
            m[(x,y)]=(1,z); m[(y,x)]=(-1,z)
    for i in range(1,8): m[(i,i)]=(-1,0)
    return m
M=table()

def basis_mul(i,j):
    if i==0:return 1,j
    if j==0:return 1,i
    return M[(i,j)]

def mul(x,y):
    out=np.zeros(8,dtype=int)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            if a and b:
                s,k=basis_mul(i,j); out[k]+=int(a)*int(b)*s
    return out

def associator(x,y,z):
    return mul(mul(x,y),z)-mul(x,mul(y,z))

def exact_octonion_audit():
    E=np.eye(8,dtype=int)
    nonzero=[]; repeated_fail=0; permutation_fail=0
    for i,j,k in itertools.product(range(1,8), repeat=3):
        a=associator(E[i],E[j],E[k])
        if np.any(a): nonzero.append((i,j,k,a.tolist()))
        if (i==j or j==k or i==k) and np.any(a): repeated_fail+=1
    for i,j,k in itertools.combinations(range(1,8),3):
        a=associator(E[i],E[j],E[k])
        for perm in itertools.permutations((i,j,k)):
            inv=sum(perm[p]>perm[q] for p in range(3) for q in range(p+1,3))
            expected=(-1 if inv%2 else 1)*a
            if not np.array_equal(associator(E[perm[0]],E[perm[1]],E[perm[2]]), expected):
                permutation_fail+=1
    W=np.array([r[3] for r in nonzero],dtype=float)
    rank=int(np.linalg.matrix_rank(W)) if len(W) else 0
    witness=associator(E[1],E[2],E[4])
    return {"ordered_imaginary_basis_triples":343,"nonzero_associators":len(nonzero),
      "associator_span_rank":rank,"repeated_argument_failures":repeated_fail,
      "alternating_permutation_failures":permutation_fail,
      "witness_e1_e2_e4":witness.tolist(),"witness_norm":float(np.linalg.norm(witness))}

def random_cost_axiom_audit(trials=5000,seed=106):
    rng=np.random.default_rng(seed); max_tri=0.0; hom_fail=0; sub_fail=0
    for _ in range(trials):
        x,y,z,w=[rng.integers(-3,4,size=8) for __ in range(4)]
        a=associator(x,y,z)
        if not np.array_equal(associator(-2*x,y,z),-2*a): hom_fail+=1
        lhs=np.linalg.norm(associator(x+w,y,z))
        rhs=np.linalg.norm(associator(x,y,z))+np.linalg.norm(associator(w,y,z))
        gap=float(lhs-rhs); max_tri=max(max_tri,gap)
        if gap>1e-10: sub_fail+=1
    return {"trials":trials,"homogeneity_failures":hom_fail,
            "subadditivity_failures":sub_fail,"max_triangle_excess":max_tri}

def synthetic_dimension_audit(seed=106):
    rows=[]
    for n in list(range(1,13))+[16,24,32,48,64,96,128]:
        if n<3:
            rows.append({"n":n,"nonzero_alternating_trilinear_defect":False,"reason":"Lambda^3 dimension is zero"})
        else:
            rows.append({"n":n,"nonzero_alternating_trilinear_defect":True,
                         "lambda3_dimension":n*(n-1)*(n-2)//6})
    return rows

def generate():
    return {"cycle":106,
      "target":"PDT-II (1)/(2): can natural resource axioms on composition-defect cost force associativity or n=3?",
      "classification":["PROVED","FALSIFIED","IMPORTED/KNOWN","NUMERICALLY_SUPPORTED","OPEN"],
      "breakthrough_candidate":False,
      "result":{"status":"FALSIFIED",
        "candidate":"Nonnegativity + absolute homogeneity + slotwise subadditivity + permutation symmetry of defect cost + zero cost on repeated/two-generator alternative histories forces vanishing global associator.",
        "counterexample":"Real octonions with D(x,y,z)=||[x,y,z]||_2.",
        "small_exact_witness":"[e1,e2,e4]=2 e7",
        "surviving_theorem":"These cost axioms characterize a coherent seminorm-like cost on an alternating trilinear defect but do not imply that the defect vanishes."},
      "octonion_exact_audit":exact_octonion_audit(),
      "random_cost_axiom_audit":random_cost_axiom_audit(),
      "dimension_stress":synthetic_dimension_audit(),
      "prior_art_boundary":"Octonion alternativity/nonassociativity, alternating associators, and Artin's two-generator theorem are known mathematics; no novelty claimed.",
      "pdt_consequence":"A PDT-native composition law capable of selecting n=3 must constrain the existence/value of three-generator defects themselves, not merely assign them a well-behaved resource cost.",
      "next_obligation":"Derive or falsify a PDT principle that forces a quantitative upper/lower relation between three-history defect and independently measurable distinction/revelation quantities; then test whether QM obeys the same relation under identical inputs."}

if __name__=="__main__":
    out=generate(); p=Path("results/cycle106_composition_defect_cost_no_go.json"); p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,indent=2))
