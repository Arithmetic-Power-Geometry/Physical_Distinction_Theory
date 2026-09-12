import numpy as np
from cycle098_compatible_refinement_defect_creation import (
    DIMS, canonical_compatible_case, dimension_stress,
    incompatible_record_counterexample, randomized_compatible_stress,
    refinement_ledger,
)


def test_exact_balances_and_bounds_across_dimensions():
    rows = dimension_stress()
    assert set(DIMS).issubset({r["coarse_dim"] for r in rows})
    assert all(r["exact_revealed_balance"] for r in rows)
    assert all(r["exact_hidden_balance"] for r in rows)
    assert all(r["compatible_consequences_hold"] for r in rows)


def test_fixed_space_reduces_to_hidden_monotonicity():
    for n in DIMS:
        r = canonical_compatible_case(n, 0)
        assert r["refined_revealed"] >= r["coarse_revealed"]
        assert r["refined_hidden"] <= r["coarse_hidden"]


def test_growth_bound_is_sharp():
    A = np.eye(2)
    B = np.array([[1., 0., 0., 0.], [0., 1., 0., 0.]])
    r = refinement_ledger(A, B, 2)
    assert r["hidden_delta"] == 2
    assert r["new_defect_dim"] == 2


def test_inherited_hidden_can_be_revealed():
    A = np.array([[1., 0.]])
    B = np.eye(2)
    r = refinement_ledger(A, B, 2)
    assert r["inherited_revelation_gain"] == 1
    assert r["hidden_delta"] == -1


def test_compatibility_is_essential():
    c = incompatible_record_counterexample()
    assert c["coarse_dim"] == 1
    assert c["coarse_revealed"] == 1
    assert c["refined_revealed"] == 0
    assert c["revealed_rank_decreases"]


def test_randomized_compatible_stress():
    out = randomized_compatible_stress(seed=98, trials=250)
    assert out["all_pass"]
    assert out["failures"] == []
