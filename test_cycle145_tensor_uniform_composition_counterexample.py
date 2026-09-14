import numpy as np
from cycle145_tensor_uniform_composition_counterexample import resource, audit

def test_exact_simple_witness():
    assert resource([1,3])==5.0
    assert resource([1,3])!=4.0

def test_uniform_refinements_exact():
    for k in range(1,13):
        for total in [0.25,1.0,3.0,16.0]:
            assert np.isclose(resource(np.full(k,total/k)),total)

def test_zero_padding_and_permutation():
    q=np.array([1.0,0.0,3.0,2.0])
    assert np.isclose(resource(q),resource(np.r_[q,0.0,0.0]))
    assert np.isclose(resource(q),resource(q[[2,0,3,1]]))

def test_positive_homogeneity():
    q=np.array([1.0,0.0,3.0,2.0])
    for c in [1e-6,0.1,2.0,1e6]:
        assert np.isclose(resource(c*q),c*resource(q))

def test_tensor_multiplicativity():
    qs=[np.array([1.0]),np.array([1.0,3.0]),np.array([0.0,2.0,5.0]),np.array([1.0,1.0,1.0])]
    for q in qs:
        for r in qs:
            assert np.isclose(resource(np.kron(q,r)),resource(q)*resource(r))

def test_boundary_discontinuity():
    assert resource([1.0,0.0])==1.0
    assert resource([1.0,1e-12])>1.9

def test_frozen_audit_no_identity_failures():
    out=audit(); c=out["counts"]
    assert c["cases"]==980
    assert c["permutation_failures"]==0
    assert c["zero_padding_failures"]==0
    assert c["homogeneity_failures"]==0
    assert c["uniform_refinement_failures"]==0
    assert c["tensor_multiplicativity_failures"]==0
    assert c["unequal_composition_differences"]>0
