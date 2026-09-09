import numpy as np
from pdt_single_plane_reversibility import (
    dimension_filter_holds,
    maximal_skew_rank,
    noncommuting_reversibility,
    rank4_counterexample,
    spr_holds_for_full_so,
    stress_dimensions,
)


def test_exact_max_rank_formula_through_1000():
    for n in range(1, 1001):
        assert maximal_skew_rank(n) == 2 * (n // 2)


def test_spr_boundary():
    assert [n for n in range(1, 13) if spr_holds_for_full_so(n)] == [1, 2, 3]


def test_ncr_boundary():
    assert [n for n in range(1, 13) if noncommuting_reversibility(n)] == list(range(3, 13))


def test_combined_filter_selects_three():
    assert [n for n in range(1, 101) if dimension_filter_holds(n)] == [3]


def test_rank4_witness_all_higher_dimensions():
    for n in list(range(4, 13)) + [16, 24, 32, 64, 128]:
        a = rank4_counterexample(n)
        assert np.allclose(a + a.T, 0.0)
        assert np.linalg.matrix_rank(a) == 4


def test_random_stress_has_no_false_spr_violation():
    rows = stress_dimensions(range(1, 13), trials=50, seed=27)
    assert all(r["random_SPR_violations_when_SPR_predicted"] == 0 for r in rows)
