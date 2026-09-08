import numpy as np

from pdt_multibranch_gram_compatibility import (
    equal_visibility_bound,
    gram,
    phase_frustrated_counterexample,
    random_audit,
    triple_compatible,
    triple_minor,
)


def test_actual_record_grams_are_psd_through_dimension_12():
    for row in random_audit(max_dimension=12, trials=80, seed=16092026):
        assert row["violations_below_-1e-12"] == 0


def test_triple_minor_matches_direct_determinant():
    rng = np.random.default_rng(42)
    for d in range(1, 13):
        for _ in range(20):
            x = rng.normal(size=(3, d)) + 1j * rng.normal(size=(3, d))
            g = gram(x)
            direct = float(np.linalg.det(g).real)
            formula = triple_minor(g[0, 1], g[1, 2], g[2, 0])
            assert abs(direct - formula) < 1e-10


def test_pairwise_valid_assignments_can_be_globally_impossible():
    ex = phase_frustrated_counterexample(0.9)
    assert ex["pairwise_valid"]
    assert ex["triple_minor"] < 0
    assert not ex["globally_compatible"]


def test_pi_loop_phase_equal_visibility_threshold_is_half():
    assert abs(equal_visibility_bound(np.pi) - 0.5) <= 5.1e-5
    assert triple_compatible(0.5, 0.5, -0.5)
    assert not triple_compatible(0.5001, 0.5001, -0.5001)
