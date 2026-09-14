import numpy as np

from experiments.cycle144_unequal_refinement import (
    nonseparable_resource_from_q,
    power_resource,
    refined_power_resource,
)


def test_quadratic_rule_survives_arbitrary_partitions():
    rng = np.random.default_rng(1441)
    for n in list(range(1, 13)) + [16, 24, 32]:
        for _ in range(20):
            r = float(10 ** rng.uniform(-3, 3))
            w = np.array([1.0]) if n == 1 else rng.dirichlet(np.ones(n))
            assert np.isclose(refined_power_resource(r, w, 2.0), power_resource(r, 2.0))


def test_nonquadratic_power_rules_fail_generic_unequal_split():
    w = np.array([0.25, 0.75])
    r = 2.0
    for p in [0.5, 1.0, 1.5, 3.0, 4.0]:
        assert not np.isclose(refined_power_resource(r, w, p), power_resource(r, p))


def test_nonseparable_deformation_survives_all_equal_splits():
    for n in list(range(1, 13)) + [16, 24, 32]:
        r = 3.25
        q = np.full(n, r * r / n)
        assert np.isclose(nonseparable_resource_from_q(q), r * r)


def test_nonseparable_deformation_fails_unequal_split_exact_witness():
    q = np.array([1.0, 3.0])
    assert np.isclose(q.sum(), 4.0)
    assert np.isclose(nonseparable_resource_from_q(q), 4.12)


def test_zero_padding_stability_of_counterfamily():
    q = np.array([1.0, 3.0])
    padded = np.array([1.0, 3.0, 0.0, 0.0])
    assert np.isclose(nonseparable_resource_from_q(q), nonseparable_resource_from_q(padded))
