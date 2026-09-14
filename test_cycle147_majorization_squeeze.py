import numpy as np
from cycle147_majorization_squeeze import F146, majorizes

def test_majorization_chain():
    for n in range(2,13):
        pure=np.zeros(n); pure[0]=1
        uniform=np.full(n,1/n)
        p=np.arange(1,n+1,dtype=float); p/=p.sum()
        assert majorizes(pure,p)
        assert majorizes(p,uniform)

def test_cycle146_endpoints_equal():
    for n in range(1,13):
        pure=np.zeros(n); pure[0]=1
        uniform=np.full(n,1/n)
        assert np.isclose(F146(pure),1)
        assert np.isclose(F146(uniform),1)

def test_exact_interior_witness():
    p=np.array([.75,.25])
    assert np.isclose(F146(p),25/28)
    assert F146(p)<1

def test_not_schur_convex():
    pure=np.array([1.,0.]); p=np.array([.75,.25]); uniform=np.array([.5,.5])
    assert majorizes(pure,p) and majorizes(p,uniform)
    assert F146(p) < F146(uniform)

def test_not_schur_concave():
    pure=np.array([1.,0.]); p=np.array([.75,.25])
    assert majorizes(pure,p)
    assert F146(pure) > F146(p)

def test_squeeze_logic_random():
    rng=np.random.default_rng(7)
    for n in range(2,13):
        pure=np.zeros(n); pure[0]=1
        uniform=np.full(n,1/n)
        for _ in range(20):
            p=rng.dirichlet(np.ones(n))
            assert majorizes(pure,p)
            assert majorizes(p,uniform)
