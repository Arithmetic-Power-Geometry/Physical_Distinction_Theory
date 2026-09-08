import numpy as np

from pdt_process_lock import (
    contraction_audit,
    memory_process_distribution,
    same_process_lock,
)


def test_same_process_lock_across_memory_strengths():
    kernel = np.array([[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0]])
    for m in np.linspace(-1.0, 1.0, 17):
        out = same_process_lock(theta=0.73, phi=1.19, memory_strength=float(m), kernel=kernel)
        assert out["equal_micro"]
        assert out["equal_resource"]
        assert out["tv_micro"] <= 1e-12
        assert out["tv_resource"] <= 1e-12


def test_resource_postprocessing_contracts_tv_randomized():
    rng = np.random.default_rng(260909)
    for n in range(1, 13):
        size = max(2, n)
        for _ in range(25):
            p = rng.dirichlet(np.ones(size))
            q = rng.dirichlet(np.ones(size))
            raw = rng.random((max(2, size // 2), size))
            kernel = raw / raw.sum(axis=0, keepdims=True)
            before, after = contraction_audit(kernel, p, q)
            assert after <= before + 1e-12


def test_memory_parameter_changes_process_but_not_framework_lock():
    p_markov_like = memory_process_distribution(0.9, 0.4, 0.0)
    p_memory = memory_process_distribution(0.9, 0.4, 0.8)
    assert not np.allclose(p_markov_like, p_memory)
    assert np.isclose(p_markov_like.sum(), 1.0)
    assert np.isclose(p_memory.sum(), 1.0)
