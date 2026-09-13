import math

from cycle131_composite_biorthogonal_revelation import (
    DIMS,
    minimal_witness,
    quadratic_revelation_gap,
    run_audit,
)


def test_minimal_counterexample_is_dimension_two():
    w = minimal_witness()
    assert w["dimension"] == 2
    assert math.isclose(w["p1_gap"], 2.0, abs_tol=1e-12)
    assert abs(w["p2_gap"]) < 1e-12
    assert math.isclose(w["p4_gap"], math.sqrt(2.0) - 2.0, abs_tol=1e-12)
    assert math.isclose(w["pinf_gap"], -1.0, abs_tol=1e-12)


def test_rank_one_cannot_distinguish_schatten_family():
    for p in (1.0, 2.0, 4.0, math.inf):
        assert abs(quadratic_revelation_gap([3.0, 0.0], p)) < 1e-12


def test_rank_two_distinguishes_nonquadratic_norms():
    assert abs(quadratic_revelation_gap([1.0, 1.0], 1.0)) > 1e-6
    assert abs(quadratic_revelation_gap([1.0, 1.0], 4.0)) > 1e-6
    assert abs(quadratic_revelation_gap([1.0, 1.0], math.inf)) > 1e-6


def test_dimension_sweep_includes_required_and_high_dimensions():
    assert DIMS[:12] == list(range(1, 13))
    assert DIMS[-7:] == [16, 24, 32, 48, 64, 96, 128]


def test_seeded_audit():
    out = run_audit()
    assert out["p_evaluations"] == 4540
    assert out["p2_failures"] == 0
    assert out["rank_le1_indistinguishability_failures"] == 0
    assert out["rank_ge2_non2_cases"] == out["rank_ge2_non2_distinguished"] == 2970
    assert out["svd_reconstruction_cases"] == 924
    assert out["max_relative_svd_residual"] < 1e-12
