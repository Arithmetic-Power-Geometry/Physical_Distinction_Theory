"""PDT Cycle 141: composition-law counterfamily audit.

Tests whether direct-sum additivity + tensor-product multiplicativity +
left/right reversible invariance + rank-one calibration select the quadratic
resource law. They do not: R_p(A)=sum_i sigma_i(A)^p satisfies all four for
all finite p>=1.
"""
import json
import numpy as np

DIMS=list(range(1,13))+[16,24,32,48,64,96,128]
PS=[1,2,3,4]
SEED=141
TOL=1e-10

def resource(A,p):
    s=np.linalg.svd(np.asarray(A,dtype=float),compute_uv=False)
    return float(np.sum(s**p))

def relerr(a,b):
    return float(abs(a-b)/max(1.0,abs(a),abs(b)))

def random_orthogonal(rng,n):
    q,_=np.linalg.qr(rng.normal(size=(n,n)))
    return q

def direct_sum(A,B):
    A=np.asarray(A,dtype=float); B=np.asarray(B,dtype=float)
    out=np.zeros((A.shape[0]+B.shape[0],A.shape[1]+B.shape[1]))
    out[:A.shape[0],:A.shape[1]]=A
    out[A.shape[0]:,A.shape[1]:]=B
    return out

def run():
    rng=np.random.default_rng(SEED)
    s={"cycle":141,"seed":SEED,"tolerance":TOL,"dimensions":DIMS,"p_values":PS,
       "resource_definition":"R_p(A)=sum_i sigma_i(A)^p","total_p_cases":0,
       "orthogonal_invariance_failures":0,"direct_sum_additivity_failures":0,
       "tensor_multiplicativity_failures":0,"rank_one_formula_failures":0,
       "max_relative_orthogonal_residual":0.0,"max_relative_direct_sum_residual":0.0,
       "max_relative_tensor_residual":0.0,"max_relative_rank_one_residual":0.0}
    for n in DIMS:
        reps=10 if n<=32 else 4
        for _ in range(reps):
            A=rng.normal(size=(n,n)); B=rng.normal(size=(2,2))
            U=random_orthogonal(rng,n); V=random_orthogonal(rng,n)
            for p in PS:
                r=relerr(resource(U@A@V.T,p),resource(A,p)); s["max_relative_orthogonal_residual"]=max(s["max_relative_orthogonal_residual"],r); s["orthogonal_invariance_failures"]+=int(r>TOL)
                r=relerr(resource(direct_sum(A,B),p),resource(A,p)+resource(B,p)); s["max_relative_direct_sum_residual"]=max(s["max_relative_direct_sum_residual"],r); s["direct_sum_additivity_failures"]+=int(r>TOL)
                r=relerr(resource(np.kron(A,B),p),resource(A,p)*resource(B,p)); s["max_relative_tensor_residual"]=max(s["max_relative_tensor_residual"],r); s["tensor_multiplicativity_failures"]+=int(r>TOL)
                x=rng.normal(size=n); y=rng.normal(size=n); rank1=np.outer(x,y); expected=(np.linalg.norm(x)*np.linalg.norm(y))**p
                r=relerr(resource(rank1,p),expected); s["max_relative_rank_one_residual"]=max(s["max_relative_rank_one_residual"],r); s["rank_one_formula_failures"]+=int(r>TOL); s["total_p_cases"]+=1
    A=np.diag([1.0,2.0])
    s["exact_distinguishing_witness"]={"A":[[1,0],[0,2]],"R_1":resource(A,1),"R_2":resource(A,2),"R_3":resource(A,3),"R_4":resource(A,4)}
    return s

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
