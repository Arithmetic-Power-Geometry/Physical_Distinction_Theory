import numpy as np

from pdt_record_capacity_welch import (
    audit_random_records,
    average_squared_overlap,
    orthonormal_records,
    repeated_records,
    revelation_average_ceiling,
    welch_average_floor,
)


def test_exact_edge_cases():
    assert welch_average_floor(4, 1) == 1.0
    assert average_squared_overlap(repeated_records(4)) == 1.0
    assert welch_average_floor(3, 3) == 0.0
    assert average_squared_overlap(orthonormal_records(3)) == 0.0
    assert revelation_average_ceiling(4, 1) == 0.0


def test_formula_dimensions_1_to_100():
    for d in range(1, 101):
        k = d + 3
        floor = welch_average_floor(k, d)
        assert 0.0 <= floor <= 1.0
        assert np.isclose(floor, 3.0 / (d * (d + 2)))


def test_randomized_welch_stress_1_to_12():
    for d in range(1, 13):
        result = audit_random_records(d, d + 3, trials=120, seed=20260909)
        assert result["min_average_margin"] >= -2e-12
        assert result["min_maximum_margin"] >= -2e-12
