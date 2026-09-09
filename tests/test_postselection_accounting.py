import numpy as np

from pdt_postselection_accounting import (
    evaluate_postselected_discrimination,
    perfect_postselection_witness,
    postselected_conditional_accuracy_bound,
    postselected_joint_correct_bound,
    random_density_matrix,
    random_povm,
    uniform_postselection_bound,
)


def test_uniform_formula():
    for d in range(1, 101):
        for k in (d + 1, d + 7):
            for s in (0.1, 0.5, 1.0):
                expected = min(1.0, d / (k * s))
                assert abs(uniform_postselection_bound(d, k, s) - expected) < 1e-15


def test_perfect_postselection_witness():
    for k in range(2, 30):
        p, states, effects, inc = perfect_postselection_witness(k, 2)
        joint, retention, conditional = evaluate_postselected_discrimination(states, effects, inc, p)
        assert abs(joint - 1.0 / k) < 1e-12
        assert abs(retention - 1.0 / k) < 1e-12
        assert abs(conditional - 1.0) < 1e-12


def test_random_subpovm_joint_bound_dimensions_1_to_12():
    for d in range(1, 13):
        rng = np.random.default_rng(9917 + d)
        k = d + 4
        for _ in range(40):
            p = rng.dirichlet(np.ones(k))
            states = [random_density_matrix(d, rng) for _ in range(k)]
            povm = random_povm(d, k + 1, rng)
            joint, retention, conditional = evaluate_postselected_discrimination(states, povm[:k], povm[k], p)
            assert joint <= postselected_joint_correct_bound(p, d) + 1e-10
            if retention > 1e-12:
                assert conditional <= postselected_conditional_accuracy_bound(p, d, retention) + 1e-10


def test_retention_cost_closes_apparent_advantage():
    p, states, effects, inc = perfect_postselection_witness(20, 2)
    joint, retention, conditional = evaluate_postselected_discrimination(states, effects, inc, p)
    assert conditional == 1.0
    assert retention == 0.05
    assert joint == 0.05
    assert joint <= 2 / 20 + 1e-12


def test_invalid_retention():
    p = np.array([0.5, 0.5])
    for bad in (0.0, -0.1, 1.1):
        try:
            postselected_conditional_accuracy_bound(p, 2, bad)
            assert False
        except ValueError:
            pass
