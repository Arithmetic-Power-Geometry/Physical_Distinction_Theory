import json, numpy as np

DIMS = list(range(1,13))+[16,24,32,48,64,96,128]
SEED = 147
TOL = 1e-10

def F146(q):
    q=np.asarray(q,dtype=float)
    if np.all(q==0): return 0.0
    s2=float(np.sum(q*q)); s3=float(np.sum(q*q*q))
    return s2*s2/s3

def majorization_prefixes(x):
    x=np.sort(np.asarray(x,dtype=float))[::-1]
    return np.cumsum(x)

def majorizes(x,y,tol=1e-10):
    x=np.asarray(x,dtype=float); y=np.asarray(y,dtype=float)
    if len(x)!=len(y) or abs(x.sum()-y.sum())>tol: return False
    return bool(np.all(majorization_prefixes(x)[:-1] >= majorization_prefixes(y)[:-1]-tol))

def audit():
    rng=np.random.default_rng(SEED)
    chains=0; endpoint_fail=0; convex_orientation_viol=0; concave_orientation_viol=0; nonadditive=0; max_endpoint_res=0.0
    for n in DIMS:
        reps=80 if n<=32 else 30
        S=1.0
        pure=np.zeros(n); pure[0]=S
        uniform=np.full(n,S/n)
        for _ in range(reps):
            p=pure.copy() if n==1 else rng.dirichlet(np.ones(n))
            assert majorizes(pure,p)
            assert majorizes(p,uniform)
            fp, fi, fu = F146(pure), F146(p), F146(uniform)
            max_endpoint_res=max(max_endpoint_res,abs(fp-S),abs(fu-S))
            endpoint_fail += int(abs(fp-S)>TOL or abs(fu-S)>TOL)
            convex_orientation_viol += int(not (fp+TOL >= fi and fi+TOL >= fu))
            concave_orientation_viol += int(not (fp <= fi+TOL and fi <= fu+TOL))
            nonadditive += int(abs(fi-S)>TOL)
            chains += 1
    return {
      "cycle":147,"seed":SEED,"dimensions":DIMS,"chains":chains,
      "endpoint_failures":endpoint_fail,
      "schur_convex_orientation_violations":convex_orientation_viol,
      "schur_concave_orientation_violations":concave_orientation_viol,
      "nonadditive_random_cases":nonadditive,
      "max_endpoint_residual":max_endpoint_res,
      "exact_witness":{"p":["3/4","1/4"],"phi":"25/28","pure_phi":"1","uniform_phi":"1","gap_from_endpoints":"-3/28"},
      "classification":{
        "proved":"If a resource on each fixed-sum simplex is Schur-monotone (either orientation) and has equal pure and uniform endpoint calibration, it equals the common endpoint value everywhere.",
        "falsified":"The Cycle-146 continuous multiplicative counterfamily can also satisfy majorization monotonicity.",
        "conditional":"PDT additive composition follows if PDT-native axioms imply majorization monotonicity plus pure/uniform calibration.",
        "imported_known":"Majorization/Schur monotonicity and endpoint ordering are classical.",
        "open":"Derive the required monotonicity from PDT operational primitives without assuming additivity.",
        "breakthrough_candidate":False
      }
    }

if __name__=="__main__":
    print(json.dumps(audit(),indent=2))
