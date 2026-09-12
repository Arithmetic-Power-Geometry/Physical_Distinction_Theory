import numpy as np
import cycle108_same_input_stochastic_window_no_go as c

def test_identity_exact():
    rows=c.exact_identity_audit()
    assert rows
    assert all(r["equal_postprocessed_counts"] for r in rows)
    assert max(r["postprocessed_l1_difference"] for r in rows)==0

def test_smallest_masking_witness():
    w=c.smallest_masking_witness()
    assert w["microscopic_tv"]==1.0
    assert w["resource_limited_tv"]==0.0

def test_tv_contraction_simple():
    p=np.array([1.,0.,0.])
    q=np.array([0.,1.,0.])
    K=np.array([[1.,1.,0.],[0.,0.,1.]])
    assert c.total_variation(K@p,K@q) <= c.total_variation(p,q)+1e-15

def test_random_audit():
    r=c.randomized_audit(trials=1200,seed=108)
    assert r["equal_input_output_violations_gt_1e-12"]==0
    assert r["tv_contraction_violations_gt_1e-12"]==0
    assert r["max_equal_input_output_gap"]==0.0
    assert r["max_tv_excess"] <= 1e-12

def test_equal_input_common_window():
    rng=np.random.default_rng(2)
    for n in range(1,13):
        p=rng.dirichlet(np.ones(n))
        K=c.random_stochastic_kernel(rng,max(1,n//2),n)
        assert np.allclose(K@p,K@p.copy(),atol=0,rtol=0)
