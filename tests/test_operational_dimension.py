import math
import pytest

from pdt_dimension import euclidean_capacity_bounds, operational_dimension_interval, dimension_audit


def test_capacity_bounds_have_correct_asymptotic_slope():
    n = 3
    ratios = []
    for eps in (1e-2, 1e-4, 1e-6, 1e-8):
        lo, hi = operational_dimension_interval(n, eps)
        assert lo == pytest.approx(float(n))
        assert hi >= n
        ratios.append(hi)
    assert ratios[-1] < ratios[0]
    assert ratios[-1] - n < 0.25


def test_dimension_audit_separates_dimensions_at_fixed_resolution():
    df = dimension_audit(ns=(2, 3, 4), epsilons=(0.01,))
    lowers = df.set_index("n")["lower_capacity_bits"].to_dict()
    assert lowers[2] < lowers[3] < lowers[4]
    scale = math.log2(100.0)
    assert lowers[3] / scale == pytest.approx(3.0)


def test_invalid_inputs_fail():
    with pytest.raises(ValueError):
        euclidean_capacity_bounds(0, 0.1)
    with pytest.raises(ValueError):
        euclidean_capacity_bounds(3, 0.0)
    with pytest.raises(ValueError):
        operational_dimension_interval(3, 1.0)
