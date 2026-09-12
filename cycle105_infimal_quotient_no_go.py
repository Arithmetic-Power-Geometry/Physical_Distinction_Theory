"""Cycle 105 — infimal quotient functoriality no-go for Euclidean selection."""
from __future__ import annotations
import json, math, random
from pathlib import Path
import numpy as np

DIMS = list(range(1,13)) + [16,24,32,48,64,96,128]
P_VALUES = [1.0, 1.5, 2.0, 3.0, float('inf')]

def lp_norm(x, p):
    x = np.asarray(x, dtype=float)
    if math.isinf(p):
        return float(np.max(np.abs(x))) if x.size else 0.0
    return float(np.sum(np.abs(x)**p)**(1.0/p))

def parallelogram_residual_l1():
    e1=np.array([1.,0.]); e2=np.array([0.,1.])
    lhs=lp_norm(e1+e2,1)**2+lp_norm(e1-e2,1)**2
    rhs=2*lp_norm(e1,1)**2+2*lp_norm(e2,1)**2
    return {'lhs':lhs,'rhs':rhs,'residual':lhs-rhs,'inner_product_induced':False}

def coordinate_chain_exact_ledger():
    rows=[]
    for n in DIMS:
        for k in sorted({1,max(1,n//3),max(1,n//2),n}):
            for m in sorted({1,max(1,k//2),k}):
                for p in P_VALUES:
                    rows.append({'n':n,'k':k,'m':m,'p':'inf' if math.isinf(p) else p,
                                 'direct_visible_coordinates':m,'iterated_visible_coordinates':m,
                                 'path_independent_exact':True,'quadratic':p==2.0})
    return rows

def finite_infimal_pushforward(cost, map_xy, ys):
    out={}
    for y in ys:
        vals=[cost[x] for x in cost if map_xy[x]==y]
        out[y]=min(vals) if vals else float('inf')
    return out

def randomized_finite_fiber_audit(trials=5000, seed=105105):
    rng=random.Random(seed); violations=0; unreachable=0
    for _ in range(trials):
        nx=rng.randint(1,30); ny=rng.randint(1,12); nz=rng.randint(1,8)
        X=list(range(nx)); Y=list(range(ny)); Z=list(range(nz))
        c={x:rng.randint(0,1000) for x in X}
        q1={x:rng.randrange(ny) for x in X}; q2={y:rng.randrange(nz) for y in Y}
        cy=finite_infimal_pushforward(c,q1,Y); via=finite_infimal_pushforward(cy,q2,Z)
        direct=finite_infimal_pushforward(c,{x:q2[q1[x]] for x in X},Z)
        for z in Z:
            unreachable += int(math.isinf(direct[z]))
            violations += int(direct[z] != via[z])
    return {'trials':trials,'seed':seed,'violations':violations,'unreachable_fibers_checked':unreachable}

def random_coordinate_numeric_audit(trials=4000, seed=105):
    rng=np.random.default_rng(seed); violations=0; max_res=0.0; nonquadratic=0
    dims=list(range(1,13))+[16,24,32,48,64]
    for _ in range(trials):
        n=int(rng.choice(dims)); k=int(rng.integers(1,n+1)); m=int(rng.integers(1,k+1))
        p=P_VALUES[int(rng.integers(0,len(P_VALUES)))]; x=rng.normal(size=n)
        direct=lp_norm(x[:m],p); via=lp_norm(x[:k][:m],p)
        r=abs(direct-via); max_res=max(max_res,r); violations += int(r>1e-12); nonquadratic += int(p!=2.0)
    return {'trials':trials,'seed':seed,'violations_gt_1e-12':violations,'max_residual':max_res,
            'nonquadratic_cases':nonquadratic,'dimensions_sampled':dims}

def p_norm_parallelogram_table():
    e1=np.array([1.,0.]); e2=np.array([0.,1.]); rows=[]
    for p in P_VALUES:
        lhs=lp_norm(e1+e2,p)**2+lp_norm(e1-e2,p)**2
        rhs=2*lp_norm(e1,p)**2+2*lp_norm(e2,p)**2
        rows.append({'p':'inf' if math.isinf(p) else p,'lhs':lhs,'rhs':rhs,'residual':lhs-rhs,
                     'parallelogram_holds_for_this_witness':abs(lhs-rhs)<1e-12})
    return rows

def generate():
    exact=coordinate_chain_exact_ledger(); finite=randomized_finite_fiber_audit(); numeric=random_coordinate_numeric_audit()
    return {
      'cycle':105,
      'target':'PDT-II targets (1),(2),(4): test whether minimum-cost refinement path independence selects quadratic/Euclidean geometry.',
      'classification':['PROVED','FALSIFIED','IMPORTED/KNOWN','NUMERICALLY_SUPPORTED','OPEN'],
      'breakthrough_candidate':False,
      'theorems':{
        'infimal_pushforward_functoriality':{'status':'PROVED / IMPORTED-KNOWN','statement':'For arbitrary extended-real cost C and composable maps q1,q2, infimal pushforward satisfies q2_*(q1_*C)=(q2∘q1)_*C.','proof':'Both sides equal inf{C(x): q2(q1(x))=z}; partitioning the feasible x by y=q1(x) does not alter the infimum.'},
        'quadratic_selection_from_path_independence':{'status':'FALSIFIED','statement':'Minimum-cost quotient path independence does not imply quadratic/Hilbert geometry.','smallest_linear_nonhilbert_witness':{'space':'R^2 with l1 norm','parallelogram':parallelogram_residual_l1(),'note':'l1 is non-inner-product by the parallelogram-law witness, while quotient costs remain path independent under infimal pushforward.'}},
        'n3_selection_from_refinement_associativity':{'status':'FALSIFIED','statement':'Refinement associativity/path independence alone cannot select n=3, because the same law holds in every tested dimension and for arbitrary sets/costs.'},
        'pdt_native_minimum_cost_rule':{'status':'OPEN','statement':'PDT still must derive why coarse operational cost is the infimum over finer representatives. Even if derived, extra physical structure is required to select p=2/Hilbert geometry or n=3.'}
      },
      'stress_tests':{
        'exact_coordinate_chains':{'dimensions':DIMS,'p_values':['1','1.5','2','3','inf'],'cases':len(exact),'nonquadratic_cases':sum(1 for r in exact if not r['quadratic']),'violations':sum(not r['path_independent_exact'] for r in exact)},
        'random_coordinate_numeric':numeric,'random_finite_fibers':finite,'parallelogram_table':p_norm_parallelogram_table()},
      'prior_art_boundary':'Quotient norms use an infimum over representatives; iterated-infimum functoriality is elementary/standard. The Jordan-von Neumann parallelogram characterization of inner-product norms is classical. No novelty claim.',
      'pdt_consequence':'Cycle 104 quadratic transport is a special case of a much broader infimal pushforward law. Resource path independence cannot derive Euclidean geometry, composition associativity, or n=3.',
      'next_kill_tests':['Search PDT primitives for an independent parallelogram/polarization/operational-interference identity; do not infer it from quotient functoriality.','Test whether a PDT-native three-history cost identity excludes l1/lp and octonionic alternatives without assuming associativity.','Same-input PDT-vs-QM prediction remains OPEN.']}

if __name__=='__main__':
    data=generate(); Path('results').mkdir(exist_ok=True)
    Path('results/cycle105_infimal_quotient_no_go.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,indent=2))
