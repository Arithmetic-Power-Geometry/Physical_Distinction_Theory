"""Cycle 108: same-input stochastic-window no-go for PDT-vs-QM prediction.

Claim:
If PDT and QM assign the same microscopic outcome distribution p(.|I) for a
declared microscopic input I, and the declared resource window R acts on both
theories only through the same stochastic post-processing K_R, then the
resource-limited distributions are identical:

    P_PDT(.|I,R) = K_R p = P_QM(.|I,R).

More generally, total variation cannot increase under the common stochastic
window:
    TV(K_R p, K_R q) <= TV(p,q).

Hence resource coarse-graining alone cannot generate a same-input
PDT-vs-QM departure and cannot amplify a pre-existing departure.

This is standard stochastic-map/data-processing mathematics, not novel.
The PDT consequence is a no-go boundary for target (3)/(5).
"""

from __future__ import annotations
import json
from pathlib import Path
import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]

def total_variation(p, q):
    p=np.asarray(p,dtype=float); q=np.asarray(q,dtype=float)
    return 0.5*float(np.abs(p-q).sum())

def random_stochastic_kernel(rng, n_out, n_in):
    x = rng.gamma(shape=1.0, scale=1.0, size=(n_out,n_in))
    x /= x.sum(axis=0, keepdims=True)
    return x

def deterministic_partition_kernel(n_in, n_out):
    K=np.zeros((n_out,n_in), dtype=int)
    for j in range(n_in):
        K[j % n_out, j] = 1
    return K

def exact_identity_audit():
    rows=[]
    for n in DIMS:
        for kout in sorted(set([1, min(2,n), max(1,n//2), n])):
            K=deterministic_partition_kernel(n,kout)
            counts=np.arange(1,n+1,dtype=int)
            left=K @ counts
            right=K @ counts.copy()
            rows.append({
                "n_in":n, "n_out":kout,
                "equal_microscopic_counts": bool(np.array_equal(counts,counts.copy())),
                "equal_postprocessed_counts": bool(np.array_equal(left,right)),
                "postprocessed_l1_difference": int(np.abs(left-right).sum()),
            })
    return rows

def randomized_audit(trials=6000, seed=108108):
    rng=np.random.default_rng(seed)
    dims=list(range(1,13))+[16,24,32,48,64,96,128]
    max_equal_output_gap=0.0
    max_tv_excess=-1e99
    contraction_violations=0
    equality_violations=0
    strict_contractions=0
    masks_to_zero=0

    for _ in range(trials):
        n=int(rng.choice(dims))
        m=int(rng.integers(1,n+1))
        p=rng.dirichlet(np.ones(n))
        q=rng.dirichlet(np.ones(n))
        K=random_stochastic_kernel(rng,m,n)

        y=K@p
        y_same=K@p.copy()
        gap=float(np.max(np.abs(y-y_same))) if len(y) else 0.0
        max_equal_output_gap=max(max_equal_output_gap,gap)
        equality_violations += int(gap > 1e-12)

        tv0=total_variation(p,q)
        tv1=total_variation(K@p,K@q)
        excess=tv1-tv0
        max_tv_excess=max(max_tv_excess,excess)
        contraction_violations += int(excess > 1e-12)
        strict_contractions += int(tv1 < tv0 - 1e-8)
        masks_to_zero += int(tv1 < 1e-12 and tv0 > 1e-8)

    return {
        "trials":trials,
        "seed":seed,
        "dimensions_sampled":dims,
        "equal_input_output_violations_gt_1e-12":equality_violations,
        "max_equal_input_output_gap":max_equal_output_gap,
        "tv_contraction_violations_gt_1e-12":contraction_violations,
        "max_tv_excess":max_tv_excess,
        "strict_contractions":strict_contractions,
        "masked_nonzero_departures_to_zero":masks_to_zero,
    }

def smallest_masking_witness():
    p=np.array([1.0,0.0])
    q=np.array([0.0,1.0])
    K=np.array([[1.0,1.0]])
    return {
        "p":p.tolist(),"q":q.tolist(),"K":K.tolist(),
        "microscopic_tv":total_variation(p,q),
        "resource_limited_tv":total_variation(K@p,K@q),
    }

def generate():
    exact=exact_identity_audit()
    rnd=randomized_audit()
    out={
        "cycle":108,
        "targets":["(3) same-input PDT-vs-QM quantitative prediction","(5) experimentally distinctive inequalities"],
        "classification":["PROVED","IMPORTED/KNOWN","NUMERICALLY SUPPORTED","FALSIFIED","OPEN"],
        "breakthrough_candidate":False,
        "theorems":{
            "same_input_common_window_no_go":{
                "status":"PROVED",
                "statement":"If microscopic distributions are identical and the same stochastic resource channel K_R is applied to both, resource-limited distributions are exactly identical."
            },
            "tv_contraction":{
                "status":"PROVED",
                "statement":"For any column-stochastic K_R, TV(K_R p,K_R q) <= TV(p,q)."
            },
            "resource_window_only_generates_departure":{
                "status":"FALSIFIED",
                "statement":"A common stochastic resource coarse-graining can by itself generate or amplify a PDT-vs-QM probability difference.",
                "reason":"Equality is preserved exactly; existing total-variation separation can only contract."
            }
        },
        "smallest_masking_witness":smallest_masking_witness(),
        "exact_dimension_audit":{
            "dimensions":DIMS,
            "cases":len(exact),
            "all_equal":all(r["equal_postprocessed_counts"] for r in exact),
            "max_l1_difference":max(r["postprocessed_l1_difference"] for r in exact)
        },
        "randomized_audit":rnd,
        "pdt_consequence":"A falsifiable same-input PDT-vs-QM departure requires PDT-native microscopic dynamics/state/effect probabilities, or a resource action that is physically theory-dependent for independently justified reasons. Merely declaring a common detector/resource coarse-graining cannot supply target (3).",
        "prior_art_boundary":"This is ordinary stochastic-map/data-processing/Blackwell-garbling mathematics. Novelty is not claimed for the theorem.",
        "surviving_obligations":[
            "Specify and derive a PDT-native pre-window microscopic probability law or additional operational state variable.",
            "Apply exactly the same declared physical resource window to PDT and QM unless PDT independently predicts a different physical response of the apparatus.",
            "Search for a parameter-free or independently calibrated probability-level inequality that differs from QM under identical microscopic inputs."
        ]
    }
    return out

if __name__=="__main__":
    out=generate()
    Path("results").mkdir(exist_ok=True)
    Path("results/cycle108_same_input_stochastic_window_no_go.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))
