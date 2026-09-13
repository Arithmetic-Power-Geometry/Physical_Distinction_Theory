import numpy as np
import cycle113_bivector_closure_no_go as c113


def test_smallest_dimension_countermodel():
    x = np.array([1.0, 0.0])
    y = np.array([0.0, 1.0])
    assert c113.wedge_norm_sq(x, y) == 1.0
    assert c113.gram_area_sq(x, y) == 1.0
    assert c113.bivector_dim(2) == 1


def test_dimension_matching_only_nontrivial_positive_n3():
    assert c113.selector_solutions(128) == [0, 3]


def test_exact_dimension_ledger():
    rows = c113.exact_dimension_ledger()
    assert [r["n"] for r in rows] == c113.DIMS
    assert all(r["gram_identity_failures"] == 0 for r in rows)


def test_so_equivariance_explicit_n2():
    x = np.array([1.0, 0.0])
    y = np.array([0.0, 1.0])
    r = np.array([[0.0, -1.0], [1.0, 0.0]])
    w = c113.wedge_matrix(x, y)
    assert np.allclose(c113.wedge_matrix(r @ x, r @ y), r @ w @ r.T)


def test_randomized_audit():
    out = c113.randomized_audit(seed=113)
    assert out["gram_failures_gt_1e-9"] == 0
    assert out["equivariance_failures_gt_1e-9"] == 0


def test_composite_dimension_identity():
    out = c113.composite_dimension_audit()
    assert out["cases"] == 144
    assert out["failures"] == 0


def test_l1_boundary_witness():
    w = c113.l1_area_counterexample()
    assert w["wedge_coefficient_norm_squared"] == 4.0
    assert w["naive_l1_gram_rhs"] == 16.0
    assert not w["equal"]
