"""Cycle 107: sharp universal associator-resource bound no-go.

For any normed algebra with submultiplicative norm ||xy|| <= ||x||||y||,
the associator obeys

    ||(xy)z - x(yz)|| <= 2 ||x||||y||||z||.

This follows from the triangle inequality and submultiplicativity. The real
octonions saturate the constant 2 on primitive triples such as (e1,e2,e4),
so no smaller universal constant is valid even for a multiplicative norm.

PDT consequence: a composition-defect inequality derived only from
submultiplicativity and the triangle inequality cannot exclude the n=7
octonionic sector, cannot force associativity, and cannot by itself select n=3.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path
import numpy as np

FANO=[(1,2,3),(1,4,5),(1,7,6),(2,4,6),(2,5,7),(3,4,7),(3,6,5)]

def _table():
    m={}
    for a,b,c in FANO:
        for x,y,z in ((a,b,c),(b,c,a),(c,a,b)):
            m[(x,y)]=(1,z); m[(y,x)]=(-1,z)
    for i in range(1,8): m[(i,i)]=(-1,0)
    return m
M=_table()

def basis_mul(i,j):
    if i==0:return 1,j
    if j==0:return 1,i
    return M[(i,j)]

def mul(x,y):
    x=np.asarray(x,float); y=np.asarray(y,float)
    out=np.zeros(8,float)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            if a and b:
                s,k=basis_mul(i,j); out[k]+=a*b*s
    return out

def associator(x,y,z):
    return mul(mul(x,y),z)-mul(x,mul(y,z))

def normalized_defect(x,y,z):
    den=float(np.linalg.norm(x)*np.linalg.norm(y)*np.linalg.norm(z))
    if den==0.0:
        return 0.0
    return float(np.linalg.norm(associator(x,y,z))/den)

def exact_basis_audit():
    E=np.eye(8)
    nonzero=0; saturating=[]; maximum=0.0
    for i,j,k in itertools.product(range(1,8),repeat=3):
        r=normalized_defect(E[i],E[j],E[k])
        maximum=max(maximum,r)
        if r>0:
            nonzero+=1
        if abs(r-2.0)<1e-12:
            saturating.append([i,j,k])
    witness=associator(E[1],E[2],E[4])
    return {
        "ordered_imaginary_basis_triples":343,
        "nonzero_associators":nonzero,
        "saturating_triples":len(saturating),
        "maximum_normalized_defect":maximum,
        "witness_e1_e2_e4":witness.tolist(),
        "witness_normalized_defect":normalized_defect(E[1],E[2],E[4]),
        "first_saturating_triples":saturating[:12],
    }

def random_octonion_audit(trials=5000,seed=107):
    rng=np.random.default_rng(seed)
    maximum=0.0; violations=0
    for _ in range(trials):
        x,y,z=[rng.normal(size=8) for __ in range(3)]
        r=normalized_defect(x,y,z)
        maximum=max(maximum,r)
        if r>2.0+1e-10:
            violations+=1
    return {"trials":trials,"seed":seed,"maximum_normalized_defect":maximum,
            "violations_of_universal_bound":violations}

def dimension_ledger():
    dims=list(range(1,13))+[16,24,32,48,64,96,128]
    return [{"n":n,"bound_constant":2.0,
             "dimension_selective":False,
             "reason":"The proof uses only triangle inequality and submultiplicativity, not dimension."}
            for n in dims]

def generate():
    return {
      "cycle":107,
      "target":"PDT-II (1)/(2)/(5): can a universal resource-normalized three-history defect inequality force associativity, n=3, or an experimentally distinctive bound?",
      "classification":["PROVED","FALSIFIED","IMPORTED/KNOWN","NUMERICALLY_SUPPORTED","OPEN"],
      "breakthrough_candidate":False,
      "theorem":{"status":"PROVED",
        "statement":"In every normed algebra with submultiplicative norm, ||[x,y,z]|| <= 2||x||||y||||z||.",
        "proof":"Triangle inequality gives ||(xy)z-x(yz)|| <= ||(xy)z||+||x(yz)||; submultiplicativity bounds each term by ||x||||y||||z||."},
      "sharpness":{"status":"PROVED",
        "statement":"The universal constant 2 is sharp even among real composition algebras with multiplicative norm.",
        "witness":"Real octonions: [e1,e2,e4]=2e7 for unit inputs."},
      "candidate_no_go":{"status":"FALSIFIED",
        "candidate":"A dimension-independent defect/resource bound obtained only from norm submultiplicativity and triangle inequality can exclude the octonionic n=7 sector or select n=3.",
        "counterexample":"The octonions satisfy ||xy||=||x||||y|| and saturate the bound at normalized defect 2 while remaining alternative and nonassociative."},
      "exact_octonion_audit":exact_basis_audit(),
      "random_octonion_audit":random_octonion_audit(),
      "dimension_stress":dimension_ledger(),
      "prior_art_boundary":"Submultiplicative normed algebras and the multiplicative octonion norm are established mathematics. The factor-2 associator bound is an immediate standard inequality; no mathematical novelty is claimed.",
      "pdt_consequence":"Any PDT experimentally distinctive composition inequality must contain additional PDT-native structure beyond norm submultiplicativity/triangle inequality: e.g. a resource-dependent coefficient strictly below 2 on a declared operational domain, a coupling to revealed distinction, or a probability-level consequence under identical microscopic inputs.",
      "next_obligation":"Derive or falsify an independently motivated PDT coupling between normalized three-history defect and a measured revelation/resource quantity; only then compare the induced output probabilities with QM/GPT under identical inputs."
    }

if __name__=="__main__":
    out=generate(); p=Path("results/cycle107_sharp_associator_resource_bound.json")
    p.parent.mkdir(exist_ok=True); p.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
