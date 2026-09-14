import numpy as np
from cycle140_raywise_second_order_no_go import B, random_so, rel

def test_covariance_and_symmetries():
    rng=np.random.default_rng(1401)
    for n in [1,2,3,4,7,12]:
        for _ in range(20):
            x=rng.normal(size=n); y=rng.normal(size=n); R=random_so(rng,n)
            assert rel(B(R@x,R@y), R@B(x,y)) < 1e-10
            assert np.allclose(B(y,x), -B(x,y))
            assert np.allclose(B(x,np.zeros(n)), 0.0)
            assert np.allclose(B(np.zeros(n),y), 0.0)

def test_positive_quadratic_scaling():
    rng=np.random.default_rng(1402)
    for n in [1,2,3,7,12]:
        for _ in range(20):
            x=rng.normal(size=n); y=rng.normal(size=n); t=float(rng.uniform(0.01,4.0))
            assert rel(B(t*x,t*y), t*t*B(x,y)) < 1e-10

def test_smallest_non_hessian_witness():
    ux,uy=np.array([1.0]),np.array([0.0])
    vx,vy=np.array([0.0]),np.array([-1.0])
    gap=B(ux+vx,uy+vy)+B(ux-vx,uy-vy)-2*B(ux,uy)-2*B(vx,vy)
    assert np.allclose(gap, [2.0])

def test_counterfamily_exists_through_n12():
    for n in range(1,13):
        x=np.zeros(n); y=np.zeros(n)
        x[0]=1.0; y[0]=-1.0
        assert np.linalg.norm(B(x,y)) > 0.0
