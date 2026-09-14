import numpy as np

from cycle148_uniformization_not_schur import resource, uniform


def test_equal_support_calibration_many_k():
    for k in list(range(1, 13)) + [16, 24, 32, 64, 128]:
        q = np.full(k, 7.25 / k)
        assert np.isclose(resource(q), 7.25, rtol=1e-12, atol=1e-12)


def test_zero_padding_stability():
    q = np.array([0.1, 0.2, 0.7])
    assert np.isclose(resource(q), resource(np.r_[q, np.zeros(10)]))


def test_positive_homogeneity():
    q = np.array([1.0, 2.0, 5.0])
    for a in [1e-6, 0.1, 2.0, 1e6]:
        assert np.isclose(resource(a * q), a * resource(q), rtol=1e-12, atol=1e-12)


def test_complete_uniformization_never_increases():
    rng = np.random.default_rng(7)
    for n in range(2, 13):
        for _ in range(50):
            q = rng.random(n)
            assert resource(uniform(q.sum(), n)) <= resource(q) + 1e-12


def test_majorization_chain_breaks_schur_convexity():
    vertex = np.array([1.0, 0.0])
    interior = np.array([0.75, 0.25])
    assert resource(vertex) < resource(interior)


def test_majorization_chain_breaks_schur_concavity():
    interior = np.array([0.75, 0.25])
    equal = np.array([0.5, 0.5])
    assert resource(interior) > resource(equal)
