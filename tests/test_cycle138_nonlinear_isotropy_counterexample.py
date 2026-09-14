import numpy as np
from cycle138_nonlinear_isotropy_counterexample import B, random_so, relative_residual

def test_antisymmetry_and_self_null():
    rng = np.random.default_rng(1)
    for n in [1, 2, 3, 4, 7, 12]:
        for _ in range(20):
            x = rng.normal(size=n); y = rng.normal(size=n)
            assert np.allclose(B(y, x), -B(x, y))
            assert np.allclose(B(x, x), 0.0)

def test_so_covariance():
    rng = np.random.default_rng(2)
    for n in [1, 2, 3, 4, 7, 12]:
        for _ in range(20):
            x = rng.normal(size=n); y = rng.normal(size=n)
            R = random_so(rng, n)
            assert relative_residual(B(R @ x, R @ y), R @ B(x, y)) < 1e-10

def test_smallest_bilinearity_failure_n1():
    x = np.array([1.0]); y = np.array([2.0])
    assert np.allclose(B(x, y), [2.0])
    assert np.allclose(B(2*x, y), [0.0])
    assert not np.allclose(B(2*x, y), 2*B(x, y))

def test_nonzero_all_dimensions():
    for n in range(1, 13):
        x = np.zeros(n); y = np.zeros(n)
        x[0] = 1.0; y[0] = 2.0
        assert np.linalg.norm(B(x, y)) > 0.0
