import math
import pytest

from pdt_revelation_reset_tradeoff import (
    K_B,
    dimension_information_ceiling_bits,
    landauer_heat_for_bits,
    revelation_reset_ceiling_bits,
    perfect_uniform_revelation_heat_floor_j,
    perfect_uniform_revelation_dimension_possible,
)


def test_one_bit_landauer_floor_300k():
    expected = K_B * 300.0 * math.log(2.0)
    assert landauer_heat_for_bits(1.0, 300.0) == pytest.approx(expected)


def test_joint_ceiling_is_minimum_of_dimension_and_heat_budget():
    one_bit_heat = landauer_heat_for_bits(1.0, 300.0)
    assert revelation_reset_ceiling_bits(8, one_bit_heat, 300.0) == pytest.approx(1.0)
    large_heat = landauer_heat_for_bits(100.0, 300.0)
    assert revelation_reset_ceiling_bits(8, large_heat, 300.0) == pytest.approx(3.0)


def test_uniform_full_revelation_requires_dimension_at_least_branch_count():
    for k in range(1, 101):
        assert perfect_uniform_revelation_dimension_possible(k, k)
        if k > 1:
            assert not perfect_uniform_revelation_dimension_possible(k, k - 1)


def test_full_revelation_heat_scales_as_log_k():
    for k in range(1, 101):
        q = perfect_uniform_revelation_heat_floor_j(k, 300.0)
        assert q == pytest.approx(K_B * 300.0 * math.log(k))


def test_dimension_ceiling_1_to_1000():
    for d in range(1, 1001):
        assert dimension_information_ceiling_bits(d) == pytest.approx(math.log2(d))


def test_invalid_inputs():
    with pytest.raises(ValueError):
        dimension_information_ceiling_bits(0)
    with pytest.raises(ValueError):
        landauer_heat_for_bits(-1.0, 300.0)
    with pytest.raises(ValueError):
        revelation_reset_ceiling_bits(2, 1.0, 0.0)
