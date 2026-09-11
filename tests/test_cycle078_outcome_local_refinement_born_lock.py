import math

from cycle078_outcome_local_refinement_born_lock import (
    additivity_defect,
    exact_qubit_witness,
    linear_score,
    quadratic_perturbation,
    refinement_defect,
    square_score,
    stress,
)


def test_exact_qubit_witness():
    w = exact_qubit_witness()
    assert math.isclose(w["candidate_before"], 9 / 10, abs_tol=1e-15)
    assert math.isclose(w["candidate_after_recoarse"], 9 / 11, abs_tol=1e-15)
    assert abs(w["refinement_defect"]) > 1e-3


def test_linear_score_is_exactly_additive_and_refinement_consistent():
    for x, y in [(0.1, 0.2), (0.25, 0.25), (0.01, 0.89)]:
        assert math.isclose(additivity_defect(x, y, linear_score), 0.0, abs_tol=1e-15)
    q = [0.2, 0.3, 0.5]
    for t in [0.1, 0.25, 0.5, 0.9]:
        assert math.isclose(refinement_defect(q, 1, t, linear_score), 0.0, abs_tol=1e-15)


def test_representative_nonlinear_scores_fail_refinement():
    q = [0.2, 0.3, 0.5]
    for score in [square_score, quadratic_perturbation]:
        assert abs(refinement_defect(q, 1, 0.5, score)) > 1e-6


def test_dimension_and_family_stress():
    out = stress(seed=78)
    assert out["linear_failures"] == 0
    assert out["max_linear_refinement_error"] < 1e-12
    assert out["all_sampled_nonlinear_scores_shifted_in_every_random_case"]
    assert out["random_cases"] == 380
    assert not out["breakthrough_candidate"]
