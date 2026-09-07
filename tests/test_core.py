import numpy as np
from pdt.core import *

def test_trace_distance_orthogonal():
    z=pure_state(0); o=pure_state(np.pi)
    assert abs(trace_distance(z,o)-1)<1e-10 and abs(helstrom_error_binary(z,o))<1e-10

def test_capacity_orthogonal_qubit():
    k,idx=resource_bounded_code_capacity([pure_state(0),pure_state(np.pi)],epsilon=1e-9)
    assert abs(k-1)<1e-12 and len(idx)==2

def test_data_processing_depolarizing_random():
    rng=np.random.default_rng(1)
    for _ in range(200):
        a=random_density(2,rng); b=random_density(2,rng)
        assert trace_distance(depolarize(a,.37),depolarize(b,.37))<=trace_distance(a,b)+1e-10

def test_entropy_endpoints():
    assert von_neumann_entropy(pure_state(0))<1e-10
    assert abs(von_neumann_entropy(np.eye(2)/2)-1)<1e-10

def test_standard_quantum_tsirelson_setting():
    a0=np.array([1,0]); a1=np.array([0,1]); b0=np.array([1,1]); b1=np.array([1,-1])
    assert abs(chsh_value(a0,a1,b0,b1)-2*np.sqrt(2))<1e-10

def test_classical_and_pr_foils():
    assert classical_chsh_bound()==2 and pr_box_chsh()==4

def test_parallelogram_p2_exact():
    rng=np.random.default_rng(2)
    for _ in range(100):
        assert parallelogram_defect(rng.normal(size=7),rng.normal(size=7),2)<1e-10

def test_nonhilbert_p_norm_defect_exists():
    x=np.array([1.,0.]); y=np.array([0.,1.])
    assert parallelogram_defect(x,y,1)>0.1 and parallelogram_defect(x,y,4)>0.1

def test_conditional_tsirelson_bound():
    assert abs(tsirelson_bound_from_parallelogram()-2*np.sqrt(2))<1e-12

def test_born_refinement_q2_unique_local_grid():
    assert abs(refinement_objective(2))<1e-20
    assert refinement_objective(1.8)>1e-6 and refinement_objective(2.2)>1e-6

def test_complex_structure():
    a,b=complex_structure_residual(canonical_complex_structure(3)); assert a<1e-12 and b<1e-12

def test_homogeneous_capacity_additivity():
    assert homogeneous_capacity(3)+homogeneous_capacity(5)==homogeneous_capacity(8)

def test_screen_capacity_linear_area():
    a=np.array([1,2,10.]); k=screen_capacity(a); assert np.allclose(k/a,k[0]/a[0])

def test_planck_scaling_threshold():
    assert abs(planck_area_scaling(1)-1)<1e-12 and planck_area_scaling(2)<1
