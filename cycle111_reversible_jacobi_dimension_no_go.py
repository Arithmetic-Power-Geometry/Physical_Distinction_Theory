"""Cycle 111: reversible-composition Jacobi is dimension-blind.

Purpose
-------
Cycle 109 isolated a conditional n=3 selector: a normed vector cross product plus
Jacobi coherence removes the octonionic n=7 branch. Cycle 110 showed that Jacobi
alone does not imply associativity outside alternativity.

This cycle attacks a possible PDT-native derivation of Jacobi from reversible
operational composition. Smooth reversible transformations naturally yield a Lie
algebra at the identity; in matrix realizations the bracket is the commutator.
The commutator Jacobi identity follows solely from associativity of matrix
multiplication and therefore holds for so(n) in every n.

Consequently:
    reversible composition + infinitesimal commutator closure + Jacobi
does NOT select n=3.
The dimension-selecting step remains the additional identification of the full
generator sector with the state/vector sector. For SO(n), dim so(n)=n(n-1)/2,
which equals n only at positive n=3 (besides n=0). Using that equality as a premise
would be an extra physical closure assumption, not a consequence of Jacobi.

Classification:
- Matrix-commutator Jacobi: IMPORTED/KNOWN + PROVED (elementary expansion).
- so(n) closure/Jacobi all n: IMPORTED/KNOWN + exactly/numerically verified.
- "Jacobi from reversible composition selects n=3": FALSIFIED.
- PDT-native generator-state identification: OPEN.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

DIMS = list(range(1,13)) + [16,24,32,48,64,96,128]

def comm(a,b):
    return a@b-b@a

def jacobi(a,b,c):
    return comm(a,comm(b,c))+comm(b,comm(c,a))+comm(c,comm(a,b))

def so_basis(n):
    out=[]
    for i in range(n):
        for j in range(i+1,n):
            a=np.zeros((n,n),dtype=np.int64)
            a[i,j]=1
            a[j,i]=-1
            out.append(a)
    return out

def exact_basis_audit(n:int):
    basis=so_basis(n)
    skew_closure_fail=0
    jacobi_fail=0
    triples=0
    if len(basis)<=15:
        triples_iter=((a,b,c) for a in basis for b in basis for c in basis)
    else:
        # The theorem is algebraic for all n; high dimensions are certificate checks.
        lim=min(len(basis),24)
        choices=[]
        for i in range(lim):
            choices.append((i,(i+1)%len(basis),(i+2)%len(basis)))
            choices.append((i,(2*i+1)%len(basis),(3*i+2)%len(basis)))
        triples_iter=((basis[i],basis[j],basis[k]) for i,j,k in choices)
    for a,b,c in triples_iter:
        triples+=1
        ab=comm(a,b)
        if not np.array_equal(ab.T,-ab):
            skew_closure_fail+=1
        if np.any(jacobi(a,b,c)):
            jacobi_fail+=1
    return {
        "n":n,
        "state_dimension":n,
        "generator_dimension":n*(n-1)//2,
        "dimension_match":n*(n-1)//2==n,
        "basis_size":len(basis),
        "triples_checked":triples,
        "skew_closure_failures":skew_closure_fail,
        "jacobi_failures":jacobi_fail,
    }

def random_so_audit(trials=250, seed=111111):
    rng=np.random.default_rng(seed)
    dims=list(range(2,13))+[16,24]
    max_j=0.0
    max_skew=0.0
    failures=0
    for _ in range(trials):
        n=int(rng.choice(dims))
        mats=[]
        for __ in range(3):
            m=rng.integers(-3,4,size=(n,n)).astype(np.int64)
            mats.append(m-m.T)
        a,b,c=mats
        j=jacobi(a,b,c)
        max_j=max(max_j,float(np.max(np.abs(j))) if j.size else 0.0)
        ab=comm(a,b)
        s=ab+ab.T
        max_skew=max(max_skew,float(np.max(np.abs(s))) if s.size else 0.0)
        failures += int(np.any(j) or np.any(s))
    return {
        "trials":trials,
        "seed":seed,
        "dimensions_sampled":dims,
        "failures":failures,
        "max_abs_jacobi_entry":max_j,
        "max_abs_skew_closure_entry":max_skew,
    }

def generator_state_match_solutions(max_n=128):
    return [n for n in range(1,max_n+1) if n*(n-1)//2==n]

def generate():
    ledger=[exact_basis_audit(n) for n in DIMS]
    rnd=random_so_audit()
    return {
        "cycle":111,
        "target":"PDT-II (1)/(2): test whether Jacobi derived from smooth reversible composition can non-circularly select n=3.",
        "classification":["PROVED","IMPORTED/KNOWN","NUMERICALLY SUPPORTED","FALSIFIED","OPEN"],
        "breakthrough_candidate":False,
        "theorem_status":{
            "matrix_commutator_jacobi":{
                "status":"PROVED + IMPORTED/KNOWN",
                "statement":"In every associative matrix algebra, [A,[B,C]]+[B,[C,A]]+[C,[A,B]]=0 by direct expansion."
            },
            "so_n_closure":{
                "status":"PROVED + IMPORTED/KNOWN",
                "statement":"For skew-symmetric A,B, [A,B] is skew-symmetric, so so(n) is closed under the commutator for every n."
            },
            "jacobi_dimension_selector":{
                "status":"FALSIFIED",
                "statement":"Jacobi coherence inherited from reversible matrix composition is satisfied by so(n) for every n and therefore cannot select n=3."
            },
            "generator_state_dimension_match":{
                "status":"PROVED but EXTRA PREMISE",
                "statement":"dim so(n)=n(n-1)/2 equals state dimension n only at positive n=3; identifying the complete generator sector with the state/vector sector is not derived by Jacobi and remains a PDT-native obligation."
            },
            "pdt_native_closure":{
                "status":"OPEN",
                "statement":"PDT must derive, rather than assume, why physically primitive reversible generators should be exhausted by an n-dimensional state-like sector."
            }
        },
        "dimension_ledger":ledger,
        "dimension_match_solutions_1_to_128":generator_state_match_solutions(),
        "random_integer_audit":rnd,
        "smallest_non3_counterexample":{
            "n":2,
            "generator_dimension":1,
            "statement":"so(2) is a Lie algebra and satisfies Jacobi, so Jacobi already survives outside n=3 at the smallest nontrivial rotation dimension."
        },
        "prior_art_boundary":"Lie groups/Lie algebras, matrix-commutator Jacobi, and dim so(n)=n(n-1)/2 are standard mathematics. No novelty is claimed for these facts.",
        "surviving_obligation":"Find a PDT-native operational/resource argument for generator-state closure or another pre-Hodge dimension-sensitive principle; Jacobi obtained from reversible composition is dimension-blind."
    }

if __name__=="__main__":
    out=generate()
    p=Path("results/cycle111_reversible_jacobi_dimension_no_go.json")
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
