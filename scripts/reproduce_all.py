from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from pdt.core import *
RES=ROOT/'results'; FIG=ROOT/'figures'; RES.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)
# finite-code capacity grid
rows=[]; base=equatorial_codebook(16)+[pure_state(0),pure_state(np.pi)]
for p in np.linspace(0,.85,18):
    noisy=[depolarize(s,float(p)) for s in base]
    for eps in [.025,.05,.10,.20,.30,.40]:
        k,idx=resource_bounded_code_capacity(noisy,epsilon=eps); rows.append((p,eps,k,len(idx)))
cap=pd.DataFrame(rows,columns=['noise_p','epsilon','K_bits','code_size']); cap.to_csv(RES/'capacity_noise.csv',index=False)
fig,ax=plt.subplots(); [ax.plot(g.noise_p,g.K_bits,marker='o',ms=3,label=f'eps={e:.3f}') for e,g in cap.groupby('epsilon')]; ax.set(xlabel='Depolarizing noise p',ylabel='Finite-code distinction capacity (bits)',title='Resource-bounded finite-code capacity under noise'); ax.legend(fontsize=7,ncol=2); fig.tight_layout(); fig.savefig(FIG/'capacity_noise.png',dpi=220); plt.close(fig)
# 5k data-processing audit
rng=np.random.default_rng(42); rows=[]
for i in range(5000):
    a=random_density(2,rng); b=random_density(2,rng); p=float(rng.uniform(0,.95)); d0=trace_distance(a,b); d1=trace_distance(depolarize(a,p),depolarize(b,p)); rows.append((i,p,d0,d1,d1-d0))
dp=pd.DataFrame(rows,columns=['trial','p','before','after','delta']); dp.to_csv(RES/'data_processing_audit.csv',index=False); viol=int((dp.delta>1e-10).sum())
fig,ax=plt.subplots(); ax.scatter(dp.before,dp.after,s=4,alpha=.25); x=np.linspace(0,1,100); ax.plot(x,x,'--'); ax.set(xlabel='Before',ylabel='After',title='Data-processing kill test: 5,000 random pairs'); fig.tight_layout(); fig.savefig(FIG/'data_processing.png',dpi=220); plt.close(fig)
# CHSH regimes and heavy standard-quantum search
best,_=vectorized_chsh_search(2_000_000,11); ch=pd.DataFrame([{'samples':2000000,'best_standard_quantum_random_search':best,'tsirelson':2*np.sqrt(2),'gap':2*np.sqrt(2)-best,'classical_bound':classical_chsh_bound(),'pr_box':pr_box_chsh()}]); ch.to_csv(RES/'chsh_boundary.csv',index=False)
pd.DataFrame([vars(x) for x in foil_models()]).to_csv(RES/'foil_models.csv',index=False)
fig,ax=plt.subplots(); vals=[2,2*np.sqrt(2),4]; ax.bar(['Classical','Quantum','PR box'],vals); ax.set(ylabel='CHSH S',title='Correlation regimes and PDT underdetermination'); fig.tight_layout(); fig.savefig(FIG/'chsh_regimes.png',dpi=220); plt.close(fig)
# parallelogram law audits
pvals=[1,1.25,1.5,1.75,2,2.25,2.5,3,4,np.inf]; defects=[max_parallelogram_defect(p,5,5000,19) for p in pvals]; pd.DataFrame({'p':[str(p) for p in pvals],'max_defect':defects}).to_csv(RES/'parallelogram_audit.csv',index=False)
fig,ax=plt.subplots(); ax.semilogy([10 if p==np.inf else p for p in pvals],np.maximum(defects,1e-15),marker='o'); ax.axvline(2,ls='--'); ax.set(xlabel='p norm',ylabel='Max parallelogram defect',title='Quadratic distinction law singles out Hilbertian norm geometry'); fig.tight_layout(); fig.savefig(FIG/'parallelogram_audit.png',dpi=220); plt.close(fig)
# Born exponent refinement
qs,obj,_,_=born_exponent_grid(points=1201); opt=minimize_scalar(refinement_objective,bounds=(.5,4.5),method='bounded',options={'xatol':1e-14}); pd.DataFrame({'q':qs,'objective':obj}).to_csv(RES/'born_refinement_grid.csv',index=False)
fig,ax=plt.subplots(); ax.semilogy(qs,np.maximum(obj,1e-30)); ax.axvline(2,ls='--'); ax.set(xlabel='Power q',ylabel='Refinement inconsistency',title='Equal orthogonal refinement selects q=2 within power-law family'); fig.tight_layout(); fig.savefig(FIG/'born_refinement.png',dpi=220); plt.close(fig)
# complex structure and geometry/screen scaling illustrations
J=canonical_complex_structure(4); jr1,jr2=complex_structure_residual(J); pd.DataFrame([{'dimension':8,'J2_plus_I_fro':jr1,'JTJ_minus_I_fro':jr2}]).to_csv(RES/'complex_structure.csv',index=False)
N=np.arange(1,201); K=homogeneous_capacity(N,.75); pd.DataFrame({'cell_count':N,'capacity':K}).to_csv(RES/'homogeneous_capacity.csv',index=False); fig,ax=plt.subplots(); ax.plot(N,K); ax.set(xlabel='Equivalent local cells',ylabel='Renormalized capacity',title='Homogeneous additive capacity measure'); fig.tight_layout(); fig.savefig(FIG/'capacity_volume.png',dpi=220); plt.close(fig)
A=np.logspace(0,5,200); Ks=screen_capacity(A); pd.DataFrame({'area_planck_units':A,'screen_capacity_bits':Ks}).to_csv(RES/'screen_capacity.csv',index=False); fig,ax=plt.subplots(); ax.loglog(A,Ks); ax.set(xlabel='Boundary area / Planck area',ylabel='Target accessible capacity (bits)',title='Horizon screen target scaling'); fig.tight_layout(); fig.savefig(FIG/'screen_capacity.png',dpi=220); plt.close(fig)
L=np.logspace(-1,1,300); sc=planck_area_scaling(L); pd.DataFrame({'L_planck':L,'rs_over_L_scaling':sc}).to_csv(RES/'planck_scaling.csv',index=False); fig,ax=plt.subplots(); ax.loglog(L,sc); ax.axhline(1,ls='--'); ax.axvline(1,ls='--'); ax.set(xlabel='L / l_P',ylabel='r_s/L scaling',title='Localization-collapse Planck-area threshold'); fig.tight_layout(); fig.savefig(FIG/'planck_scaling.png',dpi=220); plt.close(fig)
status=[('A1-A6 quantum-boundary sufficiency','proved false by foils'),('BQDC to inner-product norm','proved conditional'),('CHSH <= 2sqrt2','proved conditional'),('Born exponent q=2','proved conditional'),('Complex structure','partial conditional'),('Capacity-volume','proved conditional'),('Planck-area scaling','scaling argument'),('Exact horizon coefficient','open'),('Einstein equation','conditional known limit')]; pd.DataFrame(status,columns=['result','status']).to_csv(RES/'theorem_status.csv',index=False)
summary={'tests_expected':14,'capacity_noise_rows':len(cap),'data_processing_trials':len(dp),'data_processing_violations':viol,'chsh_random_samples':2000000,'chsh_best':float(best),'tsirelson':float(2*np.sqrt(2)),'chsh_gap':float(2*np.sqrt(2)-best),'classical_chsh':classical_chsh_bound(),'pr_box_chsh':pr_box_chsh(),'p2_max_parallelogram_defect':max_parallelogram_defect(2,5,5000,19),'born_refinement_minimizer_numeric':float(opt.x),'born_refinement_objective_at_2':refinement_objective(2),'complex_J_square_residual':jr1,'complex_J_orthogonality_residual':jr2,'scientific_status':{'tsirelson':'conditional analytic theorem; numerical search is consistency only','born':'conditional uniqueness within continuous power-law weights','capacity_volume':'conditional measure theorem','horizon':'Planck-area scaling only; exact coefficient remains open'}}
(RES/'summary.json').write_text(json.dumps(summary,indent=2)); print(json.dumps(summary,indent=2))
