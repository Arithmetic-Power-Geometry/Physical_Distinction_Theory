import numpy as np
import cycle094_scalar_unit_associativity as c94


def test_metric_only_smallest_witness():
    assert c94.witness_residual(1, 1.0) == 0.0
    assert c94.witness_residual(2, 1.0) == 1.0
    for n in c94.DIMS:
        if n >= 2:
            assert c94.witness_residual(n, 2.5) == 2.5


def test_quaternion_relation_random():
    assert c94.random_assoc_max(-1.0, 1.0, trials=300, seed=1) < 1e-12
    assert c94.random_assoc_max(-4.0, 2.0, trials=300, seed=2) < 1e-11
    assert c94.random_assoc_max(-0.25, 0.5, trials=300, seed=3) < 1e-12


def test_off_relation_fails():
    assert c94.random_assoc_max(1.0, 0.0, trials=30, seed=4) > 1e-3
    assert c94.random_assoc_max(-1.0, 0.5, trials=30, seed=5) > 1e-3


def test_exact_pure_vector_coefficient_witness():
    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    for alpha, beta in [(-1.0, 1.0), (1.0, 0.0), (-1.0, 0.5), (2.0, 3.0)]:
        ds, dv = c94.assoc((0.0,e1),(0.0,e1),(0.0,e2),alpha,beta)
        expected = (alpha + beta*beta) * e2
        assert abs(ds) < 1e-14
        assert np.allclose(dv, expected, atol=1e-14)


def test_generated_ledger():
    data = c94.generate()
    assert data["breakthrough_candidate"] is False
    assert data["exact_results"]["smallest_decisive_dimension"] == 2
    assert len(data["dimension_audit"]) == len(c94.DIMS)
