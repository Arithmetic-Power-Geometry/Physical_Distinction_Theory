import numpy as np
from cycle146_continuous_composition_counterexample import resource

def test_exact_witness():
    assert np.isclose(resource([1,3]),25/7)
    assert not np.isclose(resource([1,3]),4)

def test_singleton_and_uniform():
    for n in range(1,13):
        assert np.isclose(resource([2.5]*n),2.5*n)

def test_permutation_and_zero_padding():
    q=np.array([0.,1.,3.,7.])
    assert np.isclose(resource(q),resource(q[::-1]))
    assert np.isclose(resource(q),resource(np.r_[q,0,0]))

def test_positive_homogeneity():
    q=np.array([1.,3.,4.])
    for c in [1e-6,.3,2.,1e6]:
        assert np.isclose(resource(c*q),c*resource(q))

def test_tensor_multiplicativity():
    q=np.array([1.,3.,0.]); r=np.array([2.,5.])
    assert np.isclose(resource(np.kron(q,r)),resource(q)*resource(r))

def test_bound_and_origin_continuity():
    for q in [np.array([1.,3.]),np.array([0.,2.,5.]),np.array([1e-12,2e-12])]:
        assert 0 <= resource(q) <= q.sum()+1e-12
    assert resource([0,0])==0

def test_vanishing_channel_continuity():
    q=np.array([1.,3.]); target=resource(q)
    assert abs(resource(np.r_[q,1e-8])-target)<1e-7
