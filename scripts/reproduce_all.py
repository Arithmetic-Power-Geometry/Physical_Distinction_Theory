from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pdt.core import *

ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'results'; FIG=ROOT/'figures'
RES.mkdir(exist_ok=True); FIG.mkdir(exist_ok=True)

# 1. Capacity under depolarizing noise for finite equatorial codebooks
rows=[]
base=equatorial_codebook(12)+[pure_state(0), pure_state(np.pi)]
for p in np.linspace(0,0.8,9):
    noisy=[depolarize(s,p) for s in base]
    for eps in [0.05,0.10,0.20,0.30]:
        k,idx=resource_bounded_code_capacity(noisy,epsilon=eps)
        rows.append({'noise_p':p,'epsilon':eps,'K_bits':k,'code_size':len(idx)})
cap=pd.DataFrame(rows)
cap.to_csv(RES/'capacity_noise.csv',index=False)

fig,ax=plt.subplots(figsize=(7,4.5))
for eps,g in cap.groupby('epsilon'):
    ax.plot(g['noise_p'],g['K_bits'],marker='o',label=f'eps={eps:.2f}')
ax.set_xlabel('Depolarizing noise p'); ax.set_ylabel('Finite-code distinction capacity K (bits)')
ax.set_title('Resource-bounded distinction capacity under noise'); ax.legend()
fig.tight_layout(); fig.savefig(FIG/'capacity_noise.png',dpi=220); plt.close(fig)

# 2. Data-processing audit over random states
rng=np.random.default_rng(42)
rows=[]
viol=0
for i in range(500):
    a=random_density(2,rng); b=random_density(2,rng)
    p=float(rng.uniform(0,0.9))
    d0=trace_distance(a,b); d1=trace_distance(depolarize(a,p),depolarize(b,p))
    delta=d1-d0
    viol += delta>1e-10
    rows.append({'trial':i,'p':p,'before':d0,'after':d1,'delta':delta})
dp=pd.DataFrame(rows); dp.to_csv(RES/'data_processing_audit.csv',index=False)

fig,ax=plt.subplots(figsize=(6.5,4.5))
ax.scatter(dp['before'],dp['after'],s=10,alpha=.5)
xx=np.linspace(0,1,100); ax.plot(xx,xx,'--')
ax.set_xlabel('Trace distance before channel'); ax.set_ylabel('Trace distance after channel')
ax.set_title('Data-processing stress test (500 random pairs)')
fig.tight_layout(); fig.savefig(FIG/'data_processing.png',dpi=220); plt.close(fig)

# 3. CHSH search: empirical maximum under standard qubit/singlet realization
best,arg=random_chsh_search(samples=120000,seed=11)
chsh=pd.DataFrame([{'samples':120000,'best_CHSH':best,'tsirelson':2*np.sqrt(2),'gap':2*np.sqrt(2)-best}])
chsh.to_csv(RES/'chsh_search.csv',index=False)

# 4. Decoherence / record-strength toy model
rows=[]
for n in range(1,21):
    overlap=np.exp(-0.28*n)
    fidelity_env=overlap**2
    strength=-np.log(max(fidelity_env,1e-300))
    rows.append({'fragments':n,'overlap':overlap,'fidelity':fidelity_env,'record_strength':strength})
rec=pd.DataFrame(rows); rec.to_csv(RES/'record_stability.csv',index=False)
fig,ax=plt.subplots(figsize=(6.5,4.5))
ax.plot(rec['fragments'],rec['record_strength'],marker='o')
ax.set_xlabel('Independent environment fragments'); ax.set_ylabel('Record strength -ln F')
ax.set_title('Redundant record stabilization toy model')
fig.tight_layout(); fig.savefig(FIG/'record_stability.png',dpi=220); plt.close(fig)

# 5. Causal-diamond curvature scaling toy consistency audit
rows=[]
for Ruu in [0.1,0.5,1.0,2.0]:
    for L in np.linspace(0.02,0.4,20):
        xi=causal_diamond_capacity_deficit(Ruu,L)
        rows.append({'Ruu':Ruu,'L':L,'Xi':xi,'Xi_over_L2':xi/L**2})
cd=pd.DataFrame(rows); cd.to_csv(RES/'causal_diamond_scaling.csv',index=False)
fig,ax=plt.subplots(figsize=(6.5,4.5))
for Ruu,g in cd.groupby('Ruu'):
    ax.plot(g['L']**2,g['Xi'],marker='.',label=f'Ruu={Ruu:g}')
ax.set_xlabel('L^2'); ax.set_ylabel('Toy capacity deficit Xi')
ax.set_title('Leading-order curvature/capacity scaling model'); ax.legend()
fig.tight_layout(); fig.savefig(FIG/'causal_diamond_scaling.png',dpi=220); plt.close(fig)

# 6. Capacity vs entropy comparison
rows=[]
for r in np.linspace(0,1,21):
    rho=np.array([[(1+r)/2,0],[0,(1-r)/2]],complex)
    s=von_neumann_entropy(rho)
    d=trace_distance(rho,np.eye(2)/2)
    rows.append({'bloch_r':r,'entropy_bits':s,'distance_to_mixed':d})
ce=pd.DataFrame(rows); ce.to_csv(RES/'entropy_distinction_comparison.csv',index=False)
fig,ax=plt.subplots(figsize=(6.5,4.5))
ax.plot(ce['bloch_r'],ce['entropy_bits'],marker='o',label='von Neumann entropy')
ax.plot(ce['bloch_r'],ce['distance_to_mixed'],marker='s',label='distinction to maximally mixed')
ax.set_xlabel('Bloch radius r'); ax.set_ylabel('Value'); ax.set_title('Entropy and operational distinction encode different questions'); ax.legend()
fig.tight_layout(); fig.savefig(FIG/'entropy_vs_distinction.png',dpi=220); plt.close(fig)

summary={
 'data_processing_trials':len(dp),
 'data_processing_violations':int(viol),
 'chsh_best':float(best),
 'tsirelson':float(2*np.sqrt(2)),
 'chsh_gap':float(2*np.sqrt(2)-best),
 'capacity_rows':len(cap),
 'causal_scaling_max_relative_spread':float(cd.groupby('Ruu')['Xi_over_L2'].std().fillna(0).max()),
 'notes':[
   'CHSH computation is a consistency check within standard qubit quantum mechanics; it is not a derivation of the Tsirelson bound from PDT axioms.',
   'Causal-diamond capacity scaling is a toy model used to test the proposed L^2 structure; it is not experimental evidence.',
   'Finite-code capacity is a reproducible operational proxy for the proposed resource-bounded distinction capacity.'
 ]
}
(RES/'summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
