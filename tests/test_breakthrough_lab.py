import math

import pytest

from pdt_breakthrough import (
    dimension_identifiability_audit,
    euclidean_distinction_capacity_bounds,
    operational_dimension_slope_bounds,
)


def test_capacity_bounds_are_ordered():
    for n in (2, 3, 4, 7):
        for eps in (0.25, 0.1, 0.03, 0.01):
            b = euclidean_distinction_capacity_bounds(n, eps)
            assert b["lower_capacity_bits"] <= b["upper_capacity_bits"]
            assert math.isclose(b["lower_capacity_bits"], n * math.log2(1 / eps))


def test_dimension_slope_squeezes_toward_n():
    for n in (2, 3, 5):
        coarse = operational_dimension_slope_bounds(n, 0.1)
        fine = operational_dimension_slope_bounds(n, 1e-8)
        assert coarse["slope_lower"] == pytest.approx(float(n))
        assert fine["slope_lower"] == pytest.approx(float(n))
        assert fine["slope_upper"] < coarse["slope_upper"]
        assert abs(fine["slope_upper"] - n) < 0.25


def test_audit_contains_all_pairs():
    df = dimension_identifiability_audit(dimensions=(2, 3), epsilons=(0.1, 0.01))
    assert len(df) == 4
    assert set(df["target_dimension"]) == {2.0, 3.0}


def test_invalid_inputs_rejected():
    with pytest.raises(ValueError):
        euclidean_distinction_capacity_bounds(0, 0.1)
    with pytest.raises(ValueError):
        euclidean_distinction_capacity_bounds(3, 1.0)
