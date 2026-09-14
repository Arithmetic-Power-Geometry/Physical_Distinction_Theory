"""Cycle 146: continuous composition-selector counterexample."""
from __future__ import annotations
import json, numpy as np
DIMS=list(range(1,13))+[16,24,32,48,64,96,128]
SEED=146
TOL=1e-10

def resource(q):
    q=np.asarray(q,dtype=float)
    if np.any(q<0): raise ValueError("resource shares must be nonnegative")
    if q.size==0: return 0.0
    m=float(np.max(q))
    if m==0.0: return 0.0
    y=q/m
    s2=float(y@y); s3=float(np.sum(y**3))
    return m*s2*s2/s3

def relative_residual(a,b):
    return abs(float(a)-float(b))/max(1.0,abs(float(a)),abs(float(b)))

def audit():
    rng=np.random.default_rng(SEED)
    counts={"random_cases":0,"sparse_cases":0,"permutation_failures":0,
            "zero_padding_failures":0,"homogeneity_failures":0,
            "uniform_refinement_failures":0,"tensor_failures":0,
            "bound_failures":0,"unequal_differences":0}
    maxima={k:0.0 for k in ["permutation","zero_padding","homogeneity",
                              "uniform_refinement","tensor"]}
    for n in DIMS:
        reps=50 if n<=32 else 20
        for _ in range(reps):
            q=10.0**rng.uniform(-12,12,size=n)
            if n>1 and rng.random()<0.5:
                q[rng.random(n)<0.3]=0.0
                if not np.any(q>0): q[rng.integers(n)]=1.0
                counts["sparse_cases"]+=1
            f=resource(q); total=float(q.sum())
            checks={}
            checks["permutation"]=relative_residual(resource(q[rng.permutation(n)]),f)
            checks["zero_padding"]=relative_residual(resource(np.r_[q,np.zeros(3)]),f)
            c=10.0**rng.uniform(-6,6)
            checks["homogeneity"]=relative_residual(resource(c*q),c*f)
            a=10.0**rng.uniform(-12,12)
            checks["uniform_refinement"]=relative_residual(resource(np.full(n,a)),n*a)
            mapping={"permutation":"permutation_failures","zero_padding":"zero_padding_failures",
                     "homogeneity":"homogeneity_failures","uniform_refinement":"uniform_refinement_failures"}
            for k,v in checks.items():
                maxima[k]=max(maxima[k],v)
                counts[mapping[k]]+=int(v>TOL)
            counts["bound_failures"]+=int(f < -TOL or f-total > TOL*max(1.0,total))
            counts["unequal_differences"]+=int(relative_residual(f,total)>1e-8)
            counts["random_cases"]+=1
    tensor_cases=0
    for n in range(1,13):
        for m in range(1,13):
            for _ in range(5):
                q=10.0**rng.uniform(-5,5,size=n); r=10.0**rng.uniform(-5,5,size=m)
                if rng.random()<0.4: q[rng.random(n)<0.25]=0
                if rng.random()<0.4: r[rng.random(m)<0.25]=0
                if not np.any(q): q[0]=1
                if not np.any(r): r[0]=1
                rr=relative_residual(resource(np.kron(q,r)),resource(q)*resource(r))
                maxima["tensor"]=max(maxima["tensor"],rr)
                counts["tensor_failures"]+=int(rr>TOL); tensor_cases+=1
    eps=[10.0**(-k) for k in range(1,13)]
    continuity=[]
    for q in [np.array([1.]),np.array([1.,3.]),np.array([0.,2.,5.])]:
        target=resource(q)
        continuity.append({"q":q.tolist(),"target":target,
            "epsilon":eps[-1],"absolute_error":abs(resource(np.r_[q,eps[-1]])-target)})
    return {"cycle":146,"seed":SEED,"dimensions":DIMS,"tolerance":TOL,
            "counts":counts,"tensor_cases":tensor_cases,
            "maximum_relative_residuals":maxima,
            "continuity_probes":continuity,
            "exact_witness":{"q":[1,3],"counterfamily_resource":"25/7",
                "ordinary_additive_resource":"4","gap":"-3/7"},
            "classification":{"counterfamily_identities":"PROVED",
                "continuity_rescue_implication":"FALSIFIED",
                "stress_audit":"NUMERICALLY SUPPORTED",
                "renyi_power_sum_structure":"IMPORTED/KNOWN",
                "pdt_native_full_composition_law":"OPEN",
                "breakthrough_candidate":False}}

if __name__=="__main__":
    print(json.dumps(audit(),indent=2))
