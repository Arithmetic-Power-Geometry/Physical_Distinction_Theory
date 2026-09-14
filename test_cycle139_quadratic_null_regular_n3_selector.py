import numpy as np
from cycle139_quadratic_null_regular_n3_selector import (
    degree2_counterfamily, cubic_counterfamily, random_so, rel
)

def test_degree2_family_exact_properties():
    rng=np.random.default_rng(1)
    for n in [1,2,3,4,7,12]:
        for _ in range(20):
            x=rng.normal(size=n); y=rng.normal(size=n); R=random_so(rng,n); t=1.7
            z=np.zeros(n)
            assert rel(degree2_counterfamily(R@x,R@y),R@degree2_counterfamily(x,y)) < 1e-10
            assert np.allclose(degree2_counterfamily(y,x),-degree2_counterfamily(x,y))
            assert np.allclose(degree2_counterfamily(x,z),0)
            assert np.allclose(degree2_counterfamily(z,y),0)
            assert np.allclose(degree2_counterfamily(t*x,t*y),t*t*degree2_counterfamily(x,y))

def test_degree2_family_is_not_quadratic():
    def F(z):
        return degree2_counterfamily(np.array([z[0]],float), np.array([z[1]],float))[0]
    u=np.array([1.,1.]); v=np.array([1.,-1.])
    assert F(u+v)+F(u-v) == 0.0
    assert 2*F(u)+2*F(v) == 4.0

def test_cubic_family_is_smooth_but_wrong_degree():
    x=np.array([1.,2.]); y=np.array([3.,-1.]); t=2.0
    assert np.allclose(cubic_counterfamily(t*x,t*y), t**3*cubic_counterfamily(x,y))
    assert not np.allclose(cubic_counterfamily(t*x,t*y), t**2*cubic_counterfamily(x,y))
