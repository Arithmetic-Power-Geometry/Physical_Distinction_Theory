from cycle088_composition_stable_dimension3_no_go import (
    DIMS,
    prime_elementary_families,
    run_audit,
    singleton_is_tensor_closed,
    tensor_dimension,
    tensor_power_dimensions,
)


def test_smallest_dimension3_counterexample():
    assert tensor_dimension(3, 3) == 9
    assert singleton_is_tensor_closed(3) is False


def test_only_trivial_singleton_is_tensor_closed_in_scan():
    assert singleton_is_tensor_closed(1) is True
    for d in DIMS:
        if d > 1:
            assert singleton_is_tensor_closed(d) is False


def test_repeated_composition_generates_unbounded_power_family():
    assert tensor_power_dimensions(3, 6) == [3, 9, 27, 81, 243, 729]


def test_tensor_closure_alone_does_not_select_prime_three():
    families = prime_elementary_families(4)
    assert families["2"] == [2, 4, 8, 16]
    assert families["3"] == [3, 9, 27, 81]
    assert families["5"] == [5, 25, 125, 625]
    assert len({tuple(v) for v in families.values()}) == len(families)


def test_ledger_classification_is_conservative():
    result = run_audit()
    assert result["breakthrough_candidate"] is False
    assert "PROVED" in result["status"]
    assert "FALSIFIED" in result["status"]
    assert result["smallest_decisive_counterexample"]["two_copy_composite_dimension"] == 9
