"""PDT-II composition counterexample audit.

F(q)=k(q)*sum(q_i^2)/sum(q_i), with F(0)=0.
The family preserves symmetry, zero padding, positive homogeneity, all uniform
refinements, singleton calibration, and tensor multiplicativity, yet differs
from ordinary additive composition on unequal resource shares.
"""
from __future__ import annotations
import json
import numpy as np

DIMS=list(range(1,13))+[16,24,32,48,64,96,128]
SEED=145
TOL=1e-10

def resource(q):
    q=np.asarray(q,dtype=float)
    if np.any(q<0):
        raise ValueError("resource shares must be nonnegative")
    total=float(q.sum())
    if total==0.0:
        return 0.0
    support=int(np.count_nonzero(q>0.0))
    return support*float(q@q)/total

def relative_residual(a,b):
    return abs(float(a)-float(b))/max(1.0,abs(float(a)),abs(float(b)))

def audit():
    rng=np.random.default_rng(SEED)
    counts={"cases":0,"sparse_cases":0,"permutation_failures":0,
            "zero_padding_failures":0,"homogeneity_failures":0,
            "uniform_refinement_failures":0,
            "tensor_multiplicativity_failures":0,
            "unequal_composition_differences":0}
    maxima={k:0.0 for k in ["permutation","zero_padding","homogeneity",
                              "uniform_refinement","tensor_multiplicativity"]}
    for n in DIMS:
        reps=60 if n<=32 else 20
        for rep in range(reps):
            q=10.0**rng.uniform(-6.0,6.0,size=n)
            if n>1 and rep%3==0:
                q[rng.random(n)<0.35]=0.0
                if not np.any(q>0): q[rng.integers(n)]=1.0
                counts["sparse_cases"]+=1
            base=resource(q)
            tests={}
            tests["permutation"]=relative_residual(resource(q[rng.permutation(n)]),base)
            tests["zero_padding"]=relative_residual(resource(np.r_[q,np.zeros(3)]),base)
            c=10.0**rng.uniform(-4.0,4.0)
            tests["homogeneity"]=relative_residual(resource(c*q),c*base)
            total=10.0**rng.uniform(-6.0,6.0)
            tests["uniform_refinement"]=relative_residual(resource(np.full(n,total/n)),total)
            m=int(rng.integers(1,7))
            r=10.0**rng.uniform(-4.0,4.0,size=m)
            if m>1 and rep%4==0: r[rng.random(m)<0.30]=0.0
            if not np.any(r>0): r[0]=1.0
            tests["tensor_multiplicativity"]=relative_residual(resource(np.kron(q,r)),resource(q)*resource(r))
            keys={"permutation":"permutation_failures","zero_padding":"zero_padding_failures",
                  "homogeneity":"homogeneity_failures","uniform_refinement":"uniform_refinement_failures",
                  "tensor_multiplicativity":"tensor_multiplicativity_failures"}
            for name,residual in tests.items():
                maxima[name]=max(maxima[name],residual)
                if residual>TOL: counts[keys[name]]+=1
            if np.count_nonzero(q)>1 and relative_residual(base,q.sum())>TOL:
                counts["unequal_composition_differences"]+=1
            counts["cases"]+=1
    return {"cycle":145,"seed":SEED,"dimensions":DIMS,"tolerance":TOL,
            "counts":counts,"maximum_relative_residuals":maxima,
            "smallest_simple_unequal_witness":{"q":[1.0,3.0],
                "counterfamily_resource":resource([1.0,3.0]),
                "ordinary_additive_resource":4.0,
                "gap":resource([1.0,3.0])-4.0},
            "vanishing_channel_boundary":[{"epsilon":e,"resource":resource([1.0,e])}
                for e in [1.0,1e-1,1e-3,1e-6,1e-9,0.0]],
            "classification":{"candidate_package":"FALSIFIED","identities":"PROVED",
                "stress_test":"NUMERICALLY SUPPORTED","renyi2_collision_structure":"IMPORTED/KNOWN",
                "pdt_native_full_composition_law":"OPEN","breakthrough_candidate":False}}

if __name__=="__main__":
    print(json.dumps(audit(),indent=2))
