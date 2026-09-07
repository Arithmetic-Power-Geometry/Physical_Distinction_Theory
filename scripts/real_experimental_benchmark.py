"""Real experimental PDT/ADDE stress tests and baseline comparisons.

This script deliberately separates three evidential levels:
(1) an independently measured environment-record variable vs system coherence test;
(2) real open-system coherence data without an independent environment record;
(3) real Ramsey visibility data without an independent environment record.

It NEVER counts a rate inferred from the target coherence trace as a zero-parameter
PDT prediction.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""
from __future__ import annotations
from pathlib import Path
import ast, hashlib, io, json, math, re, urllib.request, zipfile

import numpy as np
import pandas as pd
from scipy.optimize import least_squares, minimize

OUT = Path("results/real_experimental")
OUT.mkdir(parents=True, exist_ok=True)
RAW = OUT / "raw_cache"
RAW.mkdir(parents=True, exist_ok=True)

NPL_URL = "https://zenodo.org/records/8363718/files/modelling_non_markovian_noise_in_driven_superconducting_qubits_experiment_results.csv?download=1"
RAMSEY_URL = "https://zenodo.org/records/15797402/files/Ramsey.zip?download=1"
QWPD_SUPP_URL = "https://mdpi-res.com/d_attachment/entropy/entropy-23-00122/article_deploy/entropy-23-00122-s001.pdf"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def download(url: str, path: Path) -> Path:
    if not path.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "PDT-reproducibility/2026"})
        with urllib.request.urlopen(req, timeout=120) as r, path.open("wb") as f:
            f.write(r.read())
    return path


def rmse(y, p):
    y, p = np.asarray(y, float), np.asarray(p, float)
    return float(np.sqrt(np.mean((y - p) ** 2)))


def mae(y, p):
    y, p = np.asarray(y, float), np.asarray(p, float)
    return float(np.mean(np.abs(y - p)))


# ---------------------------------------------------------------------------
# A. REAL INDEPENDENT RECORD -> COHERENCE STRESS TEST (photonic qubits)
# ---------------------------------------------------------------------------
# Supplementary Tables S1 and S2 of Wang et al., Entropy 23, 122 (2021).
# S1 and S2 were measured by different system/detector measurement settings.
# The exact pure-record PDT identity C=sqrt(1-D^2) is tested with ZERO fitted
# parameters. The source paper explicitly reports imperfect entanglement and
# mixed detector states, so failure of equality is NOT a valid PDT falsification;
# it is an applicability stress test and demonstrates why mixed-record closure
# requires more than a scalar D.

ANGLES = [0,10,20,30,40,50,60,70,80,90,100,110,120,125,130,140,150,160,170,180]
S1 = [
[12.8,156.6,54.3,72.1,57.1,59.0,107.6,9.8,50.0,66.7,51.3,67.2],
[12.8,171.5,61.9,123.1,102.8,75.8,109.2,8.1,60.4,67.9,61.0,67.7],
[17.3,180.3,48.1,152.8,110.8,84.4,106.7,7.4,59.3,66.0,58.3,60.9],
[23.4,170.4,35.3,134.8,105.5,78.3,100.9,6.5,54.0,56.0,61.0,54.1],
[35.0,169.9,24.6,184.0,116.0,78.0,85.7,5.4,40.8,55.4,51.2,45.2],
[42.3,154.2,16.6,194.5,107.3,71.3,70.8,4.9,31.2,44.2,47.2,29.0],
[51.5,126.0,6.8,180.0,106.0,61.3,44.5,4.0,18.0,34.1,28.5,24.8],
[59.6,103.5,3.2,174.6,98.0,47.1,28.7,3.9,14.8,20.7,16.1,19.5],
[69.3,81.5,2.1,161.0,64.7,79.6,14.0,4.6,4.5,11.4,8.4,8.3],
[72.6,65.4,4.5,145.1,59.4,63.4],
[38.0,54.8,1.6,90.4,41.3,48.1,14.1,3.8,8.8,10.3,9.9,9.1],
[43.0,29.3,5.4,69.3,35.7,32.8,7.8,6.0,11.3,3.5,4.9,8.7],
[39.6,17.3,20.8,33.9,40.5,11.6,23.3,7.0,21.3,10.7,8.6,23.7],
[22.2,2.4,14.3,15.5,9.0,6.9,28.2,3.8,16.7,14.2,15.4,14.8],
[31.1,40.1,32.3,52.1,65.1,3.9,50.5,7.1,33.8,29.0,13.1,45.1],
[10.9,13.7,21.0,2.4,7.5,10.4,51.7,3.8,29.7,29.6,13.0,9.9],
[10.6,20.2,26.6,3.6,11.1,12.7,64.6,3.7,27.8,29.8,19.3,24.3],
[20.8,86.8,53.6,50.3,78.2,12.4,117.2,7.4,71.8,62.4,36.1,83.7],
[12.7,94.7,55.6,55.3,80.3,22.4,123.8,6.8,70.5,69.4,36.7,87.7],
[8.4,115.8,54.5,69.9,60.3,49.8,132.0,6.4,75.3,75.3,64.0,67.2],
]
S2 = [
[11.6,121.1,116.0,8.7],[10.5,129.5,124.5,9.3],[8.5,123.2,131.5,9.0],[8.9,116.4,127.7,7.9],
[11.1,102.9,126.1,10.2],[10.7,88.9,105.2,11.1],[13.5,63.9,56.4,11.3],[17.7,43.3,65.9,12.4],
[24.8,27.6,43.2,14.1],[15.2,22.1,19.2,20.4],[9.2,50.8,12.5,17.4],[7.3,47.1,10.6,12.8],
[3.8,31.6,10.8,4.2],[6.7,58.3,11.7,7.3],[4.1,54.2,16.0,8.9],[7.1,45.3,20.6,6.3],
[6.4,56.4,53.9,8.7],[9.8,83.8,80.4,7.6],[8.2,91.3,94.0,5.4],[8.6,114.0,119.8,5.7],
]


def mle_bloch(H,V,D,A,R,L):
    """Physical single-qubit MLE from three binomial polarization bases."""
    pairs = [(H,V),(D,A),(R,L)]
    x0 = np.array([(D-A)/(D+A), (R-L)/(R+L), (H-V)/(H+V)], float)
    if np.dot(x0,x0) <= 1.0:
        return x0
    def nll(r):
        x,y,z = r
        ps = [(1+z)/2, (1+x)/2, (1+y)/2]
        s = 0.0
        for (a,b), p in zip(pairs,ps):
            p = float(np.clip(p,1e-12,1-1e-12))
            s -= a*math.log(p)+b*math.log(1-p)
        return s
    cons = {"type":"ineq", "fun":lambda r: 1.0-float(np.dot(r,r))}
    start = x0/np.linalg.norm(x0)*0.999
    res = minimize(nll,start,method="SLSQP",bounds=[(-1,1)]*3,constraints=cons,
                   options={"ftol":1e-12,"maxiter":1000})
    return np.asarray(res.x,float)


def qwpd_benchmark():
    rows=[]
    for a,s1,s2 in zip(ANGLES,S1,S2):
        if len(s1)==6:
            r = mle_bloch(*s1)
        else:
            HH,HV,HD,HA,HR,HL,VH,VV,VD,VA,VR,VL = s1
            pH = (HH+HV)/(HH+HV+VH+VV)
            rH = mle_bloch(HH,HV,HD,HA,HR,HL)
            rV = mle_bloch(VH,VV,VD,VA,VR,VL)
            r = pH*rH+(1-pH)*rV
        C = float(np.linalg.norm(r[:2]))
        H0,H1,V0,V1 = s2
        P = (V0+H1)/(V0+V1+H0+H1)
        D = float(2*P-1)
        C_pred = float(math.sqrt(max(0.0,1-D*D)))
        rows.append({
            "alpha_deg":a,
            "C_system_MLE":C,
            "D_detector_independent":D,
            "C_pred_pure_record_zero_fit":C_pred,
            "residual_C_minus_prediction":C-C_pred,
            "C2_plus_D2":C*C+D*D,
            "pure_record_condition_known_satisfied":False,
        })
    df=pd.DataFrame(rows)
    df.to_csv(OUT/"qwpd_independent_record_test.csv",index=False)
    s={
        "dataset":"Wang et al. 2021 quantum which-path detector, photonic qubits",
        "source":QWPD_SUPP_URL,
        "n_points":len(df),
        "environment_record_measured_independently":True,
        "system_coherence_measured_independently":True,
        "fitted_parameters_in_pure_record_prediction":0,
        "pure_record_assumption_satisfied_by_experiment":False,
        "reason":"Source paper reports imperfect entanglement and mixed detector states, especially at high D.",
        "zero_fit_pure_record_RMSE":rmse(df.C_system_MLE,df.C_pred_pure_record_zero_fit),
        "zero_fit_pure_record_MAE":mae(df.C_system_MLE,df.C_pred_pure_record_zero_fit),
        "max_C2_plus_D2_from_reconstructed_average_counts":float(df.C2_plus_D2.max()),
        "interpretation":"Real independent record/coherence stress test. It is not a decisive test of the exact pure-record equality because its purity hypothesis is known to fail. It does demonstrate why the mixed-record PDT branch needs the full conditional environment pair rather than D alone.",
    }
    (OUT/"qwpd_summary.json").write_text(json.dumps(s,indent=2))
    return s


# ---------------------------------------------------------------------------
# B. NPL SUPERCONDUCTING QUBIT DATA: REAL SYSTEM-DYNAMICS DIAGNOSTIC
# ---------------------------------------------------------------------------
def parse_n_array(s):
    return np.fromstring(str(s).strip().strip("[]"),sep=" ",dtype=float)

def parse_counts(s):
    return ast.literal_eval(s)

def exp_from_counts(lst):
    return np.array([(float(d.get("0",0))-float(d.get("1",0)))/(float(d.get("0",0))+float(d.get("1",0))) for d in lst])

def fit_gamma(t,c):
    c0=max(float(c[0]),1e-8)
    def residual(x): return c0*np.exp(-max(float(x[0]),0)*t)-c
    return max(float(least_squares(residual,[0.01],bounds=(0,np.inf)).x[0]),0.0)

def fit_nonmark(t,c):
    c0=max(float(c[0]),1e-8)
    def residual(x):
        g,a,w=x
        p=c0*np.exp(-g*t)*(1+a*np.sin(w*t))
        return p-c
    x=least_squares(residual,[0.01,0.1,0.1],bounds=([0,-0.8,0],[np.inf,0.8,np.inf]),max_nfev=5000).x
    return x

def npl_benchmark():
    p=download(NPL_URL,RAW/"npl_experiment_results.csv")
    df=pd.read_csv(p)
    basis_rows=[]
    for _,r in df.iterrows():
        if r.measurement_basis not in ("X","Y"): continue
        n=parse_n_array(r.n)
        vals=exp_from_counts(parse_counts(r.counts))
        basis_rows.append((str(r.job_id),float(r.theta_full),str(r.measurement_basis),n,vals))
    # average duplicate basis records within each job/theta
    groups={}
    for job,theta,b,n,v in basis_rows:
        key=(job,theta)
        groups.setdefault(key,{}).setdefault(b,[]).append(v)
    traces=[]; metrics=[]
    for (job,theta),g in groups.items():
        if "X" not in g or "Y" not in g: continue
        x=np.mean(np.stack(g["X"]),axis=0); y=np.mean(np.stack(g["Y"]),axis=0)
        c=np.sqrt(x*x+y*y); c=np.clip(c,0,1)
        n=np.arange(len(c),dtype=float)*10.0
        # Normalize time origin, not amplitude. Initial measured coherence is an initial-state observation, not a dynamic fit.
        t=n-n[0]
        sch=np.repeat(c[0],len(c))
        gamma=fit_gamma(t,c)
        exp_pred=c[0]*np.exp(-gamma*t)
        gn=fit_nonmark(t,c)
        nm_pred=c[0]*np.exp(-gn[0]*t)*(1+gn[1]*np.sin(gn[2]*t))
        metrics.append({
            "job_id":job,"theta_full":theta,"n_points":len(c),
            "schrodinger_RMSE":rmse(c,sch),
            "GKLS_constant_dephasing_RMSE":rmse(c,exp_pred),
            "PDT_ADDE_same_trace_fitted_rate_RMSE":rmse(c,exp_pred),
            "nonmarkovian_baseline_RMSE":rmse(c,nm_pred),
            "fitted_gamma_from_system_trace":gamma,
            "independent_environment_rate_available":False,
            "PDT_zero_parameter_prediction_valid":False,
        })
        for i in range(len(c)):
            traces.append({"job_id":job,"theta_full":theta,"n":n[i],"coherence_xy":c[i],"schrodinger":sch[i],"GKLS_fit":exp_pred[i],"PDT_ADDE_fit_same_as_GKLS":exp_pred[i],"nonmarkovian_fit":nm_pred[i]})
    m=pd.DataFrame(metrics); tr=pd.DataFrame(traces)
    m.to_csv(OUT/"npl_trace_metrics.csv",index=False); tr.to_csv(OUT/"npl_coherence_traces.csv",index=False)
    s={
        "dataset":"NPL experimental driven superconducting qubits (Zenodo 8363718)",
        "source":NPL_URL,"sha256":sha256(p),"raw_rows":int(len(df)),"usable_XY_traces":int(len(m)),
        "median_schrodinger_RMSE":float(m.schrodinger_RMSE.median()) if len(m) else None,
        "median_GKLS_RMSE":float(m.GKLS_constant_dephasing_RMSE.median()) if len(m) else None,
        "median_nonmarkovian_RMSE":float(m.nonmarkovian_baseline_RMSE.median()) if len(m) else None,
        "independent_environment_record_in_public_file":False,
        "PDT_zero_parameter_claim_allowed":False,
        "important_identifiability_result":"For a constant dephasing rate inferred from the same system trace, ADDE and GKLS are mathematically identical on this observable. Such a fit is not evidence for PDT-specific prediction.",
    }
    (OUT/"npl_summary.json").write_text(json.dumps(s,indent=2))
    return s


# ---------------------------------------------------------------------------
# C. RAMSEY REAL DATA: CROSS-PLATFORM COHERENCE/EXPOSURE DIAGNOSTIC
# ---------------------------------------------------------------------------
def spectral_visibility(y):
    y=np.asarray(y,float); y=y[np.isfinite(y)]
    if len(y)<8: return np.nan
    mean=float(np.mean(y)); z=y-mean
    spec=np.abs(np.fft.rfft(z)); spec[0]=0
    k=int(np.argmax(spec)); idx=np.arange(len(y),dtype=float)
    X=np.column_stack([np.ones(len(y)),np.cos(2*np.pi*k*idx/len(y)),np.sin(2*np.pi*k*idx/len(y))])
    coef=np.linalg.lstsq(X,y,rcond=None)[0]
    amp=float(np.hypot(coef[1],coef[2])); off=float(coef[0])
    return float(np.clip(amp/max(abs(off),1e-12),0,1))

def ramsey_benchmark():
    p=download(RAMSEY_URL,RAW/"ramsey_experimental.zip")
    rows=[]
    pat=re.compile(r"Ramsey/0\+1/step_2_delay_([0-9.]+)_ms\.xlsx$")
    with zipfile.ZipFile(p) as z:
        for name in z.namelist():
            mm=pat.match(name)
            if not mm: continue
            delay=float(mm.group(1)); data=z.read(name)
            d=pd.read_excel(io.BytesIO(data))
            col=pd.to_numeric(d.iloc[:,0],errors="coerce").dropna().to_numpy(float)
            rows.append({"delay_ms":delay,"visibility":spectral_visibility(col),"scan_points":len(col),"file":name})
    q=pd.DataFrame(rows).sort_values("delay_ms").reset_index(drop=True)
    q.to_csv(OUT/"ramsey_visibility.csv",index=False)
    if len(q)>=3:
        t=q.delay_ms.to_numpy(float)-q.delay_ms.iloc[0]
        c=q.visibility.to_numpy(float)
        sch=np.repeat(c[0],len(c)); gamma=fit_gamma(t,c); ex=c[0]*np.exp(-gamma*t)
        # PDT exposure reconstructed FROM target coherence is diagnostic only, not predictive.
        ratio=np.clip(c/max(c[0],1e-12),1e-12,None)
        exposure=-np.log2(ratio)
        q["distinction_exposure_from_system_not_predictive"] = exposure
        q["schrodinger"] = sch; q["GKLS_fit"] = ex; q["PDT_ADDE_fit_same_as_GKLS"] = ex
        q.to_csv(OUT/"ramsey_visibility.csv",index=False)
        rs=rmse(c,sch); rg=rmse(c,ex)
    else: rs=rg=None; gamma=None
    s={
        "dataset":"Ramsey experimental data, Zenodo 15797402",
        "source":RAMSEY_URL,"sha256":sha256(p),"n_delay_points":int(len(q)),
        "schrodinger_RMSE":rs,"GKLS_RMSE":rg,"fitted_gamma":gamma,
        "independent_environment_record_in_public_archive":False,
        "PDT_zero_parameter_claim_allowed":False,
        "interpretation":"Cross-platform real coherence diagnostic only. Distinction exposure computed from visibility is descriptive and may not be used to claim blind prediction.",
    }
    (OUT/"ramsey_summary.json").write_text(json.dumps(s,indent=2))
    return s


def main():
    qs=qwpd_benchmark(); ns=npl_benchmark(); rs=ramsey_benchmark()
    status=pd.DataFrame([
        {"dataset":"QWPD photonic qubits","real_experiment":True,"system_coherence":True,"independent_environment_record":True,"time_decay":False,"zero_fit_record_prediction_attempted":True,"decisive_ADDE_rate_test":False,"reason":"Independent C and D exist, but source reports mixed detector states; exact pure-record equality assumptions fail."},
        {"dataset":"NPL superconducting qubits","real_experiment":True,"system_coherence":True,"independent_environment_record":False,"time_decay":True,"zero_fit_record_prediction_attempted":False,"decisive_ADDE_rate_test":False,"reason":"Excellent open-system dynamics data, but no independent conditional environment record in public CSV."},
        {"dataset":"Ramsey atom-array experiment","real_experiment":True,"system_coherence":True,"independent_environment_record":False,"time_decay":True,"zero_fit_record_prediction_attempted":False,"decisive_ADDE_rate_test":False,"reason":"Real Ramsey visibility data, but no independent environment-record observable in public archive."},
    ])
    status.to_csv(OUT/"evidence_status_matrix.csv",index=False)
    final={
        "real_datasets_executed":3,
        "independent_record_dataset_count":1,
        "time_decay_dataset_count":2,
        "datasets_meeting_all_decisive_conditions":0,
        "decisive_condition":"real time-resolved coherence + independently measured environment distinction variable + rate fixed before seeing target coherence + no fitted decay parameter",
        "scientific_conclusion":"The public-data audit does NOT yet establish the decisive PDT-specific experimental claim. One real photonic dataset supplies independently measured record/coherence observables but violates the pure-record applicability condition; two real time-resolved datasets lack an independent environment record. This is a negative/qualification result, not a failed theory test. A dedicated blind controlled-dephasing experiment is still required.",
        "qwpd":qs,"npl":ns,"ramsey":rs,
    }
    (OUT/"REAL_EXPERIMENTAL_RESULT.json").write_text(json.dumps(final,indent=2))
    md=f"""# Real Experimental PDT/ADDE Audit\n\nCopyright (C) 2026 Mohammad Amir Khusru Akhtar\n\n## Result\n\nThree real experimental sources were executed. **Zero** currently satisfy all requirements for a decisive PDT-specific blind ADDE test simultaneously. This is an important identifiability result, not a positive experimental confirmation.\n\n### Independent record/coherence experiment\n\nThe QWPD photonic-qubit data provide separately measured detector distinguishability and system coherence with zero fitted parameters in the pure-record predictor. The raw-count reconstruction gives RMSE **{qs['zero_fit_pure_record_RMSE']:.6f}** and MAE **{qs['zero_fit_pure_record_MAE']:.6f}**. However, the source explicitly reports imperfect entanglement/mixed detector states, so the exact pure-record equality is outside its stated applicability domain.\n\n### Superconducting-qubit data\n\nThe NPL public CSV contains **{ns['raw_rows']}** experimental rows and yields **{ns['usable_XY_traces']}** usable X/Y transverse-coherence traces. Median RMSE: Schrodinger **{ns['median_schrodinger_RMSE']:.6f}**, constant-rate GKLS/ADDE-fit **{ns['median_GKLS_RMSE']:.6f}**, non-Markovian baseline **{ns['median_nonmarkovian_RMSE']:.6f}**. Because the public file does not independently measure the environment record, an ADDE rate fitted from the same system trace is not counted as PDT validation.\n\n### Ramsey cross-platform data\n\nThe Ramsey archive provides **{rs['n_delay_points']}** delay points in the selected 0+1 sequence. Schrodinger RMSE **{rs['schrodinger_RMSE']:.6f}** and fitted exponential/GKLS RMSE **{rs['GKLS_RMSE']:.6f}**. Again, no independent environment record is present, so this is a compatibility/diagnostic test only.\n\n## Required decisive experiment\n\nMeasure the conditional environment record pair (or a sufficient pure-record distinguishability D_E) independently, determine event statistics/rate, freeze\n\nGamma_A = -nu/2 ln(1-D_E^2)\n\nbefore the system coherence curve is revealed, and then compare the blind ADDE prediction against GKLS and non-Markovian baselines.\n"""
    (OUT/"README.md").write_text(md)
    print(json.dumps(final,indent=2))

if __name__=="__main__": main()
