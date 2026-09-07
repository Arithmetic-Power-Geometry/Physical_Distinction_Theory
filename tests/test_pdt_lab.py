import numpy as np
import pdt_lab as p

def test_all_equations_and_benchmarks():
    assert p.codebook_capacity_bits(2)==1
    assert abs(p.parallelogram_defect([1,2],[3,-1],2))<1e-12
    assert abs(p.parallelogram_defect([1,0],[0,1],3))>1e-3
    assert abs(p.polarization([1,2],[3,4])-11)<1e-12
    R=np.array([[0,-1],[1,0]],float)
    assert np.allclose(p.finite_group_invariant_metric([np.eye(2),R,R@R,R@R@R]),np.eye(2))
    assert np.allclose(p.born_probabilities([1,1j]),[.5,.5])
    a0=np.array([1,0]); a1=np.array([0,1]); b0=np.array([1,1])/np.sqrt(2); b1=np.array([1,-1])/np.sqrt(2)
    assert abs(p.chsh_value(a0,a1,b0,b1)-p.tsirelson_bound())<1e-12
    r=np.diag([1,0]).astype(complex); s=np.diag([0,1]).astype(complex); k=p.amplitude_damping_kraus(.41)
    assert p.global_distinction_residual(r,s,k)<1e-12
    assert p.local_contraction_gap(r,s,k)>=-1e-12
    D=.6; kap=p.overlap_from_pure_distinguishability(D)
    assert abs(p.pure_record_distinguishability(kap)-D)<1e-12
    assert abs(2**(-p.coherence_record_bit(kap))-kap)<1e-12
    t=np.linspace(0,1,20)
    assert np.allclose(np.abs(p.akhtar_dephasing_solution(t,1,2,0)),1)
    assert p.shannon_bits([.99,.01])<1
    H=np.diag([0.,1e-23]); rho=np.diag([.8,.2]); M=[[np.diag([1.,0]),np.diag([0.,1])]]; T=300
    Fd=p.measured_distinction_free_energy(rho,H,T,M); Fs=p.standard_free_energy(rho,H,T); Fe=p.equilibrium_free_energy(H,T)
    assert Fe-1e-28<=Fd<=Fs+1e-28
    df,meta=p.synthetic_record_dataset(noise=.004); table=p.compare_models(df,meta); row=table[table.model=='PDT_ADDE'].iloc[0]
    assert row.fitted_dynamic_parameters==0 and row.RMSE<.01
    assert p.horizon_capacity_bits(1e-68,1.616255e-35)>0
