from fractions import Fraction

import cycle136_coarse_graining_no_go as c136


def test_exact_quadratic_witness():
    w = c136.exact_quadratic_witness()
    assert w["fine_merged"] == "5/14"
    assert w["coarse_merged"] == "1/2"
    assert w["gap"] == "1/7"


def test_linear_rule_preserves_coarse_graining():
    samples = [
        [1.0, 2.0, 3.0],
        [0.25, 0.75, 2.5, 1.25],
        [1e-6, 1.0, 1e6],
    ]
    for weights in samples:
        fine, coarse = c136.merged_event_probabilities(weights, 1.0)
        assert abs(fine - coarse) < 1e-12


def test_quadratic_rule_fails_at_smallest_nontrivial_cardinality():
    fine, coarse = c136.merged_event_probabilities([1.0, 2.0, 3.0], 2.0)
    assert abs(fine - 5.0 / 14.0) < 1e-15
    assert abs(coarse - 0.5) < 1e-15
    assert abs(coarse - fine - 1.0 / 7.0) < 1e-15


def test_degenerate_zero_weight_merge_is_not_a_counterexample_to_the_theorem():
    fine, coarse = c136.merged_event_probabilities([0.0, 2.0, 3.0], 2.0)
    assert abs(fine - coarse) < 1e-15


def test_seeded_stress_audit():
    audit = c136.run_audit()
    assert audit.total_cases_per_alpha == 1280
    assert audit.linear_failures == 0
    assert audit.nonlinear_cases == 3840
    assert audit.nonlinear_violations == 3840
    assert audit.alpha_half_violations == 1280
    assert audit.alpha_two_violations == 1280
    assert audit.alpha_three_violations == 1280
    assert audit.max_linear_residual < 2e-15
    assert audit.smallest_observed_nonlinear_gap > 1e-6
