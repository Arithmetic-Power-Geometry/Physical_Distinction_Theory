import numpy as np

from pdt_record_identification_bound import (
    discrimination_success,
    error_lower_bound,
    random_stress,
    saturation_ensemble,
    success_upper_bound,
)


def test_formula_edge_cases():
    assert success_upper_bound(1, 1) == 1.0
    assert success_upper_bound(3, 2) == 1.0
    assert success_upper_bound(3, 6) == 0.5
    assert error_lower_bound(3, 6) == 0.5


def test_exact_saturation_family_through_dimension_100():
    for d in range(1, 101):
        for q in (1, 2, 3):
            states, povm = saturation_ensemble(d, q)
            got = discrimination_success(states, povm)
            want = success_upper_bound(d, q * d)
            assert np.isclose(got, want, atol=1e-12)


def test_random_mixed_states_and_povms_dimensions_1_to_12():
    for d in range(1, 13):
        k = d + 3
        out = random_stress(d, k, trials=40, seed=260909)
        assert out["max_violation"] <= 1e-12


def test_bound_for_large_label_overload():
    for d in (1, 2, 3, 7, 12, 50, 100):
        k = 10 * d
        assert np.isclose(success_upper_bound(d, k), 0.1)
        assert np.isclose(error_lower_bound(d, k), 0.9)
