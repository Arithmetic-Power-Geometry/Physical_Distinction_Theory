from cycle128_composite_carrier_dimension_no_go import (
    DIMS,
    audit,
    kernel_lower_bound,
    lower_bound,
    same_carrier_possible,
)


def test_tensor_dimension_lower_bound():
    assert lower_bound(3, 5) == 15
    assert lower_bound(1, 7) == 7


def test_smallest_decisive_same_carrier_failure_is_n2():
    assert same_carrier_possible(1)
    assert not same_carrier_possible(2)


def test_all_requested_nontrivial_dimensions_fail_same_carrier_independence():
    for n in DIMS:
        if n > 1:
            assert not same_carrier_possible(n)


def test_rank_nullity_kernel_guard():
    assert kernel_lower_bound(2) == 2
    assert kernel_lower_bound(3) == 6
    assert kernel_lower_bound(12) == 132
    assert kernel_lower_bound(128) == 16256


def test_audit_has_no_guard_failures():
    result = audit()
    assert result["guard_failures"] == []
    assert result["smallest_decisive_case"] == {
        "n": 2,
        "required": 4,
        "same_carrier": 2,
        "minimum_kernel": 2,
    }
