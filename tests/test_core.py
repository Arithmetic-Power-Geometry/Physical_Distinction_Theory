import numpy as np
from pdt.core import *

def test_trace_distance_orthogonal():
    z=pure_state(0); o=pure_state(np.pi)
    assert abs(trace_distance(z,o)-1)<1e-10
    assert abs(helstrom_error_binary(z,o))<1e-10

def test_capacity_orthogonal_qubit():
    states=[pure_state(0), pure_state(np.pi)]
    k,idx=resource_bounded_code_capacity(states, epsilon=1e-9)
    assert abs(k-1)<1e-12 and len(idx)==2

def test_data_processing_depolarizing_random():
    rng=np.random.default_rng(1)
    for _ in range(50):
        a=random_density(2,rng); b=random_density(2,rng)
        d0=trace_distance(a,b)
        d1=trace_distance(depolarize(a,0.3), depolarize(b,0.3))
        assert d1 <= d0 + 1e-10

def test_entropy_pure_and_maxmixed():
    assert von_neumann_entropy(pure_state(0)) < 1e-10
    assert abs(von_neumann_entropy(np.eye(2)/2)-1)<1e-10

def test_chsh_quantum_settings():
    a0=np.array([1,0]); a1=np.array([0,1])
    b0=np.array([1,1]); b1=np.array([1,-1])
    s=chsh_value(a0,a1,b0,b1)
    assert abs(s-2*np.sqrt(2))<1e-10

def test_capacity_monotonic_budget():
    states=equatorial_codebook(8)+[pure_state(0),pure_state(np.pi)]
    kfull,_=resource_bounded_code_capacity(states,epsilon=0.2)
    mask=[i%2==0 for i in range(len(states))]
    kres,_=resource_bounded_code_capacity(states,epsilon=0.2,budget=mask)
    assert kres <= kfull + 1e-12
