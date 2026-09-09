import numpy as np
import pytest

from pdt_resource_lattice import (
    coordinate_audit,
    effect_rank,
    join_rank,
    meet_rank,
    modular_residual,
    unique_revelation,
)


def test_coordinate_audit_n1_to_n12():
    for n in range(1, 13):
        row = coordinate_audit(n)
        assert row["residual"] == 0
        assert row["lhs"] == row["rhs"]
        assert 0 <= row["rank_meet"] <= min(row["rank_A"], row["rank_B"])
        assert max(row["rank_A"], row["rank_B"]) <= row["rank_join"] <= n


def test_redundant_effects_do_not_create_fake_revelation():
    a = np.array([[1, 0, 0], [2, 0, 0], [3, 0, 0]], dtype=float)
    b = np.array([[0, 1, 0], [0, 2, 0]], dtype=float)
    assert effect_rank(a) == 1
    assert effect_rank(b) == 1
    assert join_rank(a, b) == 2
    assert meet_rank(a, b) == 0
    assert modular_residual(a, b) == 0


def test_identical_resources_have_zero_unique_revelation():
    a = np.array([[1, 0, 0], [0, 1, 0]], dtype=float)
    ua, ub, shared = unique_revelation(a, a)
    assert (ua, ub, shared) == (0, 0, 2)


def test_nested_resources_reveal_only_new_rank():
    a = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=float)
    b = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], dtype=float)
    ua, ub, shared = unique_revelation(a, b)
    assert (ua, ub, shared) == (0, 1, 2)
    assert modular_residual(a, b) == 0


def test_random_integer_families_dimensions_1_to_12():
    for n in range(1, 13):
        rng = np.random.default_rng(1000 + n)
        for _ in range(20):
            a = rng.integers(-3, 4, size=(max(1, n // 2), n))
            b = rng.integers(-3, 4, size=(max(1, n // 3 + 1), n))
            assert modular_residual(a, b) == 0


def test_mismatched_ambient_dimensions_rejected():
    with pytest.raises(ValueError):
        join_rank(np.eye(2), np.eye(3))
