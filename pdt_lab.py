"""
Physical Distinction Theory computational laboratory.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under Apache-2.0.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import json, math, urllib.request
import numpy as np
import pandas as pd
from scipy.linalg import expm, logm

KB=1.380649e-23
HBAR=1.054571817e-34

@dataclass(frozen=True)
class ResourceWindow:
    E: float
    tau: float
    actions: tuple[str,...]=()
    region: str=""
    epsilon: float=0.0

@dataclass(frozen=True)
class PhysicalDistinction:
    A: str
    B: str
    resource: ResourceWindow

def codebook_capacity_bits(n:int)->float:
    if n<1: raise ValueError("n>=1 required")
    return float(np.log2(n))

def max_admissible_capacity_bits(sizes)->float:
    vals=list(sizes)
    if not vals: raise ValueError("empty codebook family")
    return max(codebook_capacity_bits(int(n)) for n in vals)

def optimal_decision_value(omega, affine_payoffs):
    x=np.asarray(omega,float)
    return max(float(np.dot(np.asarray(w,float),x)+b) for w,b in affine_payoffs)

def quadratic_bregman_regret(omega,sigma,G=None):
    x,y=np.asarray(omega,float),np.asarray(sigma,float)
    G=np.eye(len(x)) if G is None else np.asarray(G,float)
    d=x-y
    return float(.5*d@G@d)

def p_norm(x,p): return float(np.linalg.norm(np.asarray(x,float),ord=p))
def parallelogram_defect(x,y,p=2.0):
    x,y=np.asarray(x,float),np.asarray(y,float)
    return p_norm(x+y,p)**2+p_norm(x-y,p)**2-2*p_norm(x,p)**2-2*p_norm(y,p)**2

def q_distinction(x,G=None):
    x=np.asarray(x,float); G=np.eye(len(x)) if G is None else np.asarray(G,float)
    return float(x@G@x)

def polarization(x,y,norm_sq=None):
    x,y=np.asarray(x,float),np.asarray(y,float)
    norm_sq=(lambda z: float(z@z)) if norm_sq is None else norm_sq
    return .25*(norm_sq(x+y)-norm_sq(x-y))

def finite_group_invariant_metric(group,auxiliary=None):
    mats=[np.asarray(g,float) for g in group]; n=mats[0].shape[0]
    G0=np.eye(n) if auxiliary is None else np.asarray(auxiliary,float)
    G=sum(g.T@G0@g for g in mats)/len(mats)
    return .5*(G+G.T)

def restricted_effect_norm(X,effects):
    X=np.asarray(X,complex)
    return float(max(abs(np.trace(np.asarray(E,complex)@X)) for E in effects))
def null_kernel(basis_ops,effects,tol=1e-12): return [i for i,X in enumerate(basis_ops) if restricted_effect_norm(X,effects)<=tol]
def ellipsoid_quadratic_form(axis_lengths):
    a=np.asarray(axis_lengths,float)
    if np.any(a<=0): raise ValueError("positive axes required")
    return np.diag(1/(a*a))
def reversible_covariance_residual(U,G): return float(np.linalg.norm(np.asarray(U).T@np.asarray(G)@np.asarray(U)-np.asarray(G)))
def stable_subspace_score(G,P): return float(np.trace(np.asarray(P,float)@np.asarray(G,float)))
def neutral_state_finite_group(alpha,transforms): return np.mean([np.asarray(g,float)@np.asarray(alpha,float) for g in transforms],axis=0)
def pair_erasure(alpha,beta): return .5*(np.asarray(alpha,float)+np.asarray(beta,float))
def radial_state(mu,alpha,p): return np.asarray(mu,float)+(2*p-1)*(np.asarray(alpha,float)-np.asarray(mu,float))
def bloch_density(x):
    x=np.asarray(x,float)
    if np.linalg.norm(x)>1+1e-12: raise ValueError("outside Bloch ball")
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,-1]],complex)
    return .5*(np.eye(2)+x[0]*sx+x[1]*sy+x[2]*sz)
def born_probabilities(a):
    a=np.asarray(a,complex); w=np.abs(a)**2
    if w.sum()==0: raise ValueError("zero vector")
    return w/w.sum()
def orthogonal_additivity_residual(s,t,F=lambda x:x): return float(F(s+t)-F(s)-F(t))
def chsh_value(a0,a1,b0,b1,G=None):
    v=[np.asarray(z,float) for z in [a0,a1,b0,b1]]; G=np.eye(len(v[0])) if G is None else np.asarray(G,float)
    ip=lambda x,y: float(x@G@y)
    return abs(ip(v[0],v[2]+v[3])+ip(v[1],v[2]-v[3]))
def tsirelson_bound(): return 2*np.sqrt(2)
def trace_distance(rho,sigma): return .5*float(np.sum(np.linalg.svd(np.asarray(rho,complex)-np.asarray(sigma,complex),compute_uv=False)))
def apply_kraus(rho,kraus): return sum(K@rho@K.conj().T for K in kraus)
def stinespring_from_kraus(kraus):
    ks=[np.asarray(K,complex) for K in kraus]; dout,din=ks[0].shape
    V=np.zeros((dout*len(ks),din),complex)
    for i,K in enumerate(ks): V[i*dout:(i+1)*dout]=K
    return V
def global_dilated_state(rho,kraus):
    V=stinespring_from_kraus(kraus); return V@rho@V.conj().T
def complementary_output(rho,kraus):
    ks=[np.asarray(K,complex) for K in kraus]; out=np.zeros((len(ks),len(ks)),complex)
    for i,Ki in enumerate(ks):
        for j,Kj in enumerate(ks): out[i,j]=np.trace(Ki@rho@Kj.conj().T)
    return out
def amplitude_damping_kraus(g):
    g=float(g); return [np.array([[1,0],[0,np.sqrt(1-g)]],complex),np.array([[0,np.sqrt(g)],[0,0]],complex)]
def dephasing_kraus(lam):
    p=(1+float(lam))/2; I=np.eye(2,dtype=complex); Z=np.diag([1,-1]).astype(complex)
    return [np.sqrt(p)*I,np.sqrt(1-p)*Z]
def global_distinction_residual(rho,sigma,kraus): return abs(trace_distance(global_dilated_state(rho,kraus),global_dilated_state(sigma,kraus))-trace_distance(rho,sigma))
def local_contraction_gap(rho,sigma,kraus): return trace_distance(rho,sigma)-trace_distance(apply_kraus(rho,kraus),apply_kraus(sigma,kraus))
def record_overlap(e0,e1): return complex(np.vdot(np.asarray(e1,complex),np.asarray(e0,complex)))
def coherence_record_bit(kappa):
    a=abs(kappa); return np.inf if a<=0 else float(-np.log2(a))
def pure_record_distinguishability(kappa): return float(np.sqrt(max(0.,1-abs(kappa)**2)))
def overlap_from_pure_distinguishability(D): return float(np.sqrt(max(0.,1-float(D)**2)))
def deterministic_rate(nu,kappa): return float(-nu*np.log(abs(kappa)))
def deterministic_rate_from_D(nu,D): return float(-.5*nu*np.log(1-float(D)**2))
def weak_record_rate(nu,D): return float(.5*nu*float(D)**2)
def poisson_rate(nu,kappa): return float(nu*(1-float(np.real(kappa))))
def cumulative_overlap(kappas): return complex(np.prod(np.asarray(kappas,complex)))
def cumulative_record_bits(kappas): return float(sum(coherence_record_bit(k) for k in kappas))
def resource_bounded_record_distinguishability(rho0,rho1,effects):
    d=np.asarray(rho0,complex)-np.asarray(rho1,complex)
    return float(max(abs(np.trace(np.asarray(T,complex)@d)) for T in effects))
def conditional_expectation_dephase(rho): return np.diag(np.diag(rho))
def akhtar_rhs(rho,H,gamma,expectation=conditional_expectation_dephase,hbar=1.0):
    rho,H=np.asarray(rho,complex),np.asarray(H,complex)
    return -1j/hbar*(H@rho-rho@H)+gamma*(expectation(rho)-rho)
def multi_constraint_rhs(rho,H,gammas,expectations,hbar=1.0):
    rho,H=np.asarray(rho,complex),np.asarray(H,complex); out=-1j/hbar*(H@rho-rho@H)
    for g,E in zip(gammas,expectations): out += g*(E(rho)-rho)
    return out
def schrodinger_rho_rhs(rho,H,hbar=1.0): return -1j/hbar*(np.asarray(H)@np.asarray(rho)-np.asarray(rho)@np.asarray(H))
def akhtar_dephasing_solution(t,c0,omega,gamma): return c0*np.exp(-(gamma+1j*omega)*np.asarray(t,float))
def nonmarkovian_coherence(t,c0,omega,gamma0,amp,freq):
    t=np.asarray(t,float); integ=gamma0*t+amp*(1-np.cos(freq*t))/freq
    return c0*np.exp(-integ-1j*omega*t)
def distinction_generator(G_series,times): return -.5*np.gradient(np.asarray(G_series,float),np.asarray(times,float),axis=0)
def directional_rate(metric_values,times): return -.5*np.gradient(np.log(np.asarray(metric_values,float)),np.asarray(times,float))
def contraction_rate(metric_values,times): return -np.gradient(np.asarray(metric_values,float),np.asarray(times,float))
def backflow_measure(times,distances):
    t,d=np.asarray(times,float),np.asarray(distances,float); der=np.gradient(d,t)
    return float(np.trapezoid(np.maximum(der,0),t))
def shannon_bits(p):
    p=np.asarray(p,float); p=p[p>0]; return float(-np.sum(p*np.log2(p)))
def conditional_entropy_bits(joint):
    j=np.asarray(joint,float); j=j/j.sum(); return shannon_bits(j.ravel())-shannon_bits(j.sum(axis=0))
def distinction_entropy_bound(Hd,Kd,tol=1e-12): return bool(-tol<=Hd<=Kd+tol)
def landauer_min_heat(Hd_bits,T,kb=KB): return float(kb*T*np.log(2)*Hd_bits)
def heat_rate_bound(phi_H,T,kb=KB): return float(kb*T*np.log(2)*phi_H)
def entropy_production_defect(qdot,T,phi_H,kb=KB): return float(qdot/T-kb*np.log(2)*phi_H)
def thermodynamic_efficiency(qdot,T,phi_H,kb=KB): return np.nan if qdot==0 else float(kb*T*np.log(2)*phi_H/qdot)
def gibbs_state(H,T,kb=KB):
    H=np.asarray(H,complex); X=expm(-H/(kb*T)); return X/np.trace(X)
def equilibrium_free_energy(H,T,kb=KB):
    Z=float(np.real(np.trace(expm(-np.asarray(H,complex)/(kb*T))))); return float(-kb*T*np.log(Z))
def classical_relative_entropy_bits(p,q):
    p,q=np.asarray(p,float),np.asarray(q,float); mask=p>0
    if np.any(q[mask]<=0): return np.inf
    return float(np.sum(p[mask]*np.log2(p[mask]/q[mask])))
def measured_relative_entropy_bits(rho,sigma,measurements):
    vals=[]
    for M in measurements:
        pr=np.array([np.real(np.trace(E@rho)) for E in M]); ps=np.array([np.real(np.trace(E@sigma)) for E in M])
        vals.append(classical_relative_entropy_bits(pr,ps))
    return float(max(vals))
def standard_free_energy(rho,H,T,kb=KB):
    rho,H=np.asarray(rho,complex),np.asarray(H,complex); vals=np.linalg.eigvalsh(rho); vals=vals[vals>1e-15]
    S=-kb*np.sum(vals*np.log(vals)); return float(np.real(np.trace(rho@H))-T*S)
def measured_distinction_free_energy(rho,H,T,measurements,kb=KB):
    g=gibbs_state(H,T,kb); return float(equilibrium_free_energy(H,T,kb)+kb*T*np.log(2)*measured_relative_entropy_bits(rho,g,measurements))
def hidden_free_energy(rho,H,T,measurements,kb=KB): return standard_free_energy(rho,H,T,kb)-measured_distinction_free_energy(rho,H,T,measurements,kb)
def hypothesis_testing_beta(rho,sigma,effects,epsilon):
    vals=[float(np.real(np.trace(T@sigma))) for T in effects if np.real(np.trace(T@rho))>=1-epsilon-1e-12]
    return min(vals) if vals else np.inf
def hypothesis_testing_divergence_bits(rho,sigma,effects,epsilon):
    b=hypothesis_testing_beta(rho,sigma,effects,epsilon)
    return np.inf if b==0 else (-np.inf if not np.isfinite(b) else float(-np.log2(b)))
def hypothesis_testing_distinction_free_energy(rho,H,T,effects,epsilon,kb=KB):
    g=gibbs_state(H,T,kb); D=hypothesis_testing_divergence_bits(rho,g,effects,epsilon)
    return float(equilibrium_free_energy(H,T,kb)+kb*T*np.log(2)*D)
def capacity_density(volume,kappa0): return float(kappa0*volume)
def distinction_deficit(K_curved,K_reference): return float(1-K_curved/K_reference)
def small_diamond_deficit(R_scalar,Ruu,tau): return float((R_scalar/180-Ruu/30)*tau*tau)
def planck_length_squared(hbar,G,c): return float(hbar*G/c**3)
def horizon_capacity_bits(area,l_planck): return float(area/(4*l_planck*l_planck*np.log(2)))
def rmse(y,yhat): return float(np.sqrt(np.mean((np.asarray(y)-np.asarray(yhat))**2)))
def mae(y,yhat): return float(np.mean(np.abs(np.asarray(y)-np.asarray(yhat))))
def aic_from_sse(y,yhat,k):
    n=len(y); sse=max(float(np.sum((np.asarray(y)-np.asarray(yhat))**2)),1e-300); return float(n*np.log(sse/n)+2*k)
def bic_from_sse(y,yhat,k):
    n=len(y); sse=max(float(np.sum((np.asarray(y)-np.asarray(yhat))**2)),1e-300); return float(n*np.log(sse/n)+k*np.log(n))
def synthetic_record_dataset(seed=7,n=240,nu=1.3,D=0.55,omega=1.7,noise=0.012,poisson=False):
    rng=np.random.default_rng(seed); t=np.linspace(0,6,n); kappa=overlap_from_pure_distinguishability(D)
    gamma=poisson_rate(nu,kappa) if poisson else deterministic_rate_from_D(nu,D)
    truth=np.exp(-gamma*t)*np.cos(omega*t); y=truth+rng.normal(0,noise,n)
    return pd.DataFrame({'t':t,'signal':y,'truth':truth}),{'nu':nu,'D_E':D,'omega':omega,'gamma':gamma,'kappa':kappa,'poisson':poisson}
def compare_models(df,meta):
    t,y=df.t.to_numpy(),df.signal.to_numpy(); w=meta['omega']; sch=np.cos(w*t)
    grid=np.linspace(0,1.5,601); gfit=min(grid,key=lambda g:np.sum((y-np.exp(-g*t)*np.cos(w*t))**2)); gk=np.exp(-gfit*t)*np.cos(w*t)
    best=(np.inf,None,None)
    for g0 in np.linspace(0,1,31):
      for amp in np.linspace(-.25,.25,21):
       for freq in np.linspace(.5,4,18):
        integ=g0*t+amp*(1-np.cos(freq*t))/freq; pred=np.exp(-integ)*np.cos(w*t); sse=np.sum((y-pred)**2)
        if sse<best[0]: best=(sse,(g0,amp,freq),pred)
    pdt=np.exp(-meta['gamma']*t)*np.cos(w*t)
    rows=[]
    for name,pred,k in [('Schrodinger',sch,0),('GKLS',gk,1),('NonMarkovian',best[2],3),('PDT_ADDE',pdt,0)]:
        rows.append({'model':name,'RMSE':rmse(y,pred),'MAE':mae(y,pred),'AIC':aic_from_sse(y,pred,k),'BIC':bic_from_sse(y,pred,k),'fitted_dynamic_parameters':k})
    return pd.DataFrame(rows).sort_values('RMSE').reset_index(drop=True)
PUBLIC_DATASETS={
 'npl_2023_nonmarkovian':('10.5281/zenodo.8363718','https://zenodo.org/records/8363718/files/modelling_non_markovian_noise_in_driven_superconducting_qubits_experiment_results.csv?download=1'),
 'kit_2026_environment_memory':('10.48550/arXiv.2603.11889','https://zenodo.org/records/21908500/files/CorrelationSpectroscopy_vs_Efield.ipynb?download=1')}
def download_public_dataset(key,destination):
    doi,url=PUBLIC_DATASETS[key]; path=Path(destination); path.parent.mkdir(parents=True,exist_ok=True); urllib.request.urlretrieve(url,path); return path
def reproduce(outdir='results'):
    out=Path(outdir); out.mkdir(parents=True,exist_ok=True)
    geom=pd.DataFrame([{'p':p,'parallelogram_defect':parallelogram_defect([1,0],[0,1],p)} for p in [1.25,1.5,2,3,4]])
    geom.to_csv(out/'geometry_audit.csv',index=False)
    rng=np.random.default_rng(42); maxS=0
    for _ in range(100000):
        v=[]
        for j in range(4):
            x=rng.normal(size=2); v.append(x/np.linalg.norm(x))
        maxS=max(maxS,chsh_value(*v))
    r=np.diag([1,0]).astype(complex); s=np.diag([0,1]).astype(complex); ks=amplitude_damping_kraus(.37)
    tables=[]
    for mode in [False,True]:
        df,meta=synthetic_record_dataset(poisson=mode); tab=compare_models(df,meta); tab.insert(0,'event_statistics','poisson' if mode else 'deterministic'); tables.append(tab)
    cmp=pd.concat(tables); cmp.to_csv(out/'model_comparison.csv',index=False)
    summary={'max_random_chsh':maxS,'tsirelson_bound':tsirelson_bound(),'stinespring_global_distinction_residual':global_distinction_residual(r,s,ks),'local_contraction_gap':local_contraction_gap(r,s,ks),'biased_bit_entropy_H2_0.01':shannon_bits([.99,.01]),'record_example':{'nu':1.3,'D_E':.55,'kappa':overlap_from_pure_distinguishability(.55),'exact_gamma':deterministic_rate_from_D(1.3,.55),'weak_gamma':weak_record_rate(1.3,.55)}}
    (out/'summary.json').write_text(json.dumps(summary,indent=2)); return summary,cmp
if __name__=='__main__':
    s,t=reproduce(); print(json.dumps(s,indent=2)); print(t.to_string(index=False))
