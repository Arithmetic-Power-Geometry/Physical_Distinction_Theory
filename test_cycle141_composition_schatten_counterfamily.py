import numpy as np
from cycle141_composition_schatten_counterfamily import resource,direct_sum,random_orthogonal

def test_exact_diagonal_witness():
    A=np.diag([1.0,2.0])
    assert resource(A,1)==3.0
    assert resource(A,2)==5.0
    assert resource(A,3)==9.0
    assert resource(A,4)==17.0

def test_direct_sum_exact_diagonal_cases():
    A=np.diag([1.0,2.0]); B=np.diag([3.0,4.0])
    for p in [1,2,3,4]:
        assert np.isclose(resource(direct_sum(A,B),p),resource(A,p)+resource(B,p))

def test_tensor_multiplicativity():
    A=np.diag([1.0,2.0]); B=np.diag([3.0,5.0])
    for p in [1,2,3,4]:
        assert np.isclose(resource(np.kron(A,B),p),resource(A,p)*resource(B,p))

def test_reversible_invariance():
    rng=np.random.default_rng(141)
    for n in [1,2,3,4,7,12]:
        A=rng.normal(size=(n,n)); U=random_orthogonal(rng,n); V=random_orthogonal(rng,n)
        for p in [1,2,3,4]:
            assert np.isclose(resource(U@A@V.T,p),resource(A,p),rtol=1e-10,atol=1e-10)

def test_rank_one_and_zero_edges():
    rng=np.random.default_rng(142)
    for n in range(1,13):
        x=rng.normal(size=n); y=rng.normal(size=n); A=np.outer(x,y)
        for p in [1,2,3,4]:
            assert np.isclose(resource(A,p),(np.linalg.norm(x)*np.linalg.norm(y))**p,rtol=1e-10,atol=1e-10)
            assert resource(np.zeros((n,n)),p)==0.0
