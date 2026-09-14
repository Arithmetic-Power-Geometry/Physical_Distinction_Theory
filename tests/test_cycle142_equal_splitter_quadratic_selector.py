import math

from cycle142_equal_splitter_quadratic_selector import (
    DIMS,
    audit,
    g_binary_only_counterexample,
    g_quadratic,
)


def test_quadratic_obeys_binary_and_ternary_splitters():
    for r in [0.0, 1e-9, 0.1, 1.0, 3.7, 1e6]:
        assert math.isclose(g_quadratic(r), 2.0 * g_quadratic(r / math.sqrt(2.0)), rel_tol=1e-12, abs_tol=1e-12)
        assert math.isclose(g_quadratic(r), 3.0 * g_quadratic(r / math.sqrt(3.0)), rel_tol=1e-12, abs_tol=1e-12)


def test_binary_only_counterexample_obeys_binary_split_exactly_numerically():
    for r in [1e-9, 0.1, 1.0, 1.23456789, 3.7, 1e6]:
        assert math.isclose(
            g_binary_only_counterexample(r),
            2.0 * g_binary_only_counterexample(r / math.sqrt(2.0)),
            rel_tol=1e-12,
            abs_tol=1e-12,
        )


def test_binary_only_counterexample_violates_ternary_splitter():
    r = 1.23456789
    lhs = g_binary_only_counterexample(r)
    rhs = 3.0 * g_binary_only_counterexample(r / math.sqrt(3.0))
    assert abs(lhs - rhs) > 1e-3


def test_audit_has_no_quadratic_failures_and_detects_counterexample():
    out = audit()
    assert out["stats"]["quadratic"]["binary_failures"] == 0
    assert out["stats"]["quadratic"]["ternary_failures"] == 0
    assert out["stats"]["binary_only_counterexample"]["binary_failures"] == 0
    assert out["stats"]["binary_only_counterexample"]["ternary_failures"] > 0


def test_required_dimension_stress_grid_is_present():
    assert DIMS[:12] == list(range(1, 13))
    assert DIMS[-7:] == [16, 24, 32, 48, 64, 96, 128]
