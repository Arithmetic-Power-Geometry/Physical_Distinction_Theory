"""Cycle 181 regression checks for finite distinction scalar composition laws."""
import math


def test_cardinality_disjoint_additivity_n1_to_n12():
    for n in range(1, 13):
        for a in range(0, n + 1):
            b = n - a
            assert a + b == n


def test_cardinality_cartesian_multiplicativity_n1_to_n12():
    for a in range(1, 13):
        for b in range(1, 13):
            assert len(range(a)) * len(range(b)) == a * b


def test_log_cardinality_product_additivity_n1_to_n12():
    for a in range(1, 13):
        for b in range(1, 13):
            lhs = math.log(a * b)
            rhs = math.log(a) + math.log(b)
            assert math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)


def test_log_cardinality_disjoint_additivity_smallest_counterexample():
    a = b = 1
    lhs = math.log(a + b)
    rhs = math.log(a) + math.log(b)
    assert not math.isclose(lhs, rhs, rel_tol=1e-12, abs_tol=1e-12)
    assert math.isclose(lhs, math.log(2.0))
    assert math.isclose(rhs, 0.0)


def test_normalized_counting_gives_uniform_n1_to_n12():
    for n in range(1, 13):
        p = [1.0 / n] * n
        assert math.isclose(sum(p), 1.0, rel_tol=1e-12, abs_tol=1e-12)
        assert all(math.isclose(x, 1.0 / n) for x in p)
