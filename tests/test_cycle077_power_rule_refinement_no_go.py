import math

from cycle077_power_rule_refinement_no_go import (
    analytic_split_factor,
    exact_qubit_witness,
    refined_coarse_probability,
    coarse_event_probability,
    stress,
)


def test_exact_qubit_witness():
    w = exact_qubit_witness()
    assert math.isclose(w["candidate_first_event_before_split"], 9/10, abs_tol=1e-15)
    assert math.isclose(w["candidate_first_event_after_split_and_recoarse"], 9/11, abs_tol=1e-15)
    assert not w["refinement_consistent"]


def test_alpha_one_is_refinement_consistent():
    q = [0.3, 0.2, 0.5]
    for t in [0.1, 0.25, 0.5, 0.9]:
        before = coarse_event_probability(q, 1.0, 1)
        after = refined_coarse_probability(q, 1.0, 1, t)
        assert math.isclose(before, after, abs_tol=1e-15)
        assert math.isclose(analytic_split_factor(1.0, t), 1.0, abs_tol=1e-15)


def test_nonunit_power_rules_shift_under_nontrivial_split():
    q = [0.3, 0.2, 0.5]
    for alpha in [0.5, 0.75, 1.5, 2.0, 3.0]:
        before = coarse_event_probability(q, alpha, 1)
        after = refined_coarse_probability(q, alpha, 1, 0.5)
        assert abs(before - after) > 1e-6
        assert not math.isclose(analytic_split_factor(alpha, 0.5), 1.0, abs_tol=1e-12)


def test_dimension_stress():
    out = stress(seed=77)
    assert out["alpha1_failures"] == 0
    assert out["max_alpha1_refinement_error"] < 1e-12
    assert out["all_nonunit_candidates_falsified_in_random_stress"]
