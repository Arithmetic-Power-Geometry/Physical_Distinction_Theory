from cycle135_replication_gauge_fix import (
    doubling_periodic_gauge,
    linear_gauge,
    monotonicity_lower_bound,
    run_audit,
)


def test_linear_gauge_obeys_two_and_three_copy_extensivity():
    for q in (0.0, 0.125, 1.0, 7.25, 100.0):
        assert linear_gauge(2*q) == 2*linear_gauge(q)
        assert linear_gauge(3*q) == 3*linear_gauge(q)


def test_doubling_periodic_gauge_is_positive_and_strictly_increasing_by_bound():
    assert monotonicity_lower_bound() > 0.0
    for q in (1e-6, 0.1, 1.0, 10.0, 1e6):
        assert doubling_periodic_gauge(q) > 0.0


def test_doubling_alone_has_non_linear_counterexample():
    q = 1.37
    lhs = doubling_periodic_gauge(2*q)
    rhs = 2*doubling_periodic_gauge(q)
    assert abs(lhs-rhs) < 1e-12
    assert abs(doubling_periodic_gauge(q)-q) > 1e-6


def test_three_copy_breaks_doubling_periodic_counterexample():
    q = 1.37
    lhs = doubling_periodic_gauge(3*q)
    rhs = 3*doubling_periodic_gauge(q)
    assert abs(lhs-rhs) > 1e-6


def test_stress_audit():
    audit = run_audit()
    assert audit.cases == 380
    assert audit.linear_two_copy_failures == 0
    assert audit.linear_three_copy_failures == 0
    assert audit.periodic_two_copy_failures == 0
    assert audit.periodic_three_copy_violations == 380
    assert audit.max_periodic_two_copy_relative_residual < 1e-10
    assert audit.max_periodic_three_copy_relative_residual > 1e-3
