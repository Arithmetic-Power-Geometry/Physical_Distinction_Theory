import numpy as np
import cycle104_quotient_metric_transport as c104


def test_smallest_metric_mismatch_witness():
    w = c104.smallest_metric_mismatch_witness()
    assert w["fine_dimension"] == 2
    assert w["coarse_dimension"] == 1
    assert w["right_inverse_residual"] == 0.0
    assert w["isometry_residual_for_induced_metric"] == 0.0
    assert w["isometry_residual_for_declared_metric"] == 3.0
    assert not w["automatic_independent_metric_compatibility"]


def test_exact_coordinate_path_independence():
    rows = c104.exact_coordinate_chain_ledger()
    assert rows
    assert all(r["path_independent"] for r in rows)


def test_weighted_section_identities():
    q = np.array([[1.0, 2.0, 0.0], [0.0, 1.0, 1.0]])
    g = np.diag([2.0, 3.0, 5.0])
    s = c104.minimum_norm_section(q, g)
    h = c104.induced_quotient_metric(q, g)
    assert np.allclose(q @ s, np.eye(2), atol=1e-12)
    assert np.allclose(s.T @ g @ s, h, atol=1e-12)


def test_minimum_norm_property():
    q = np.array([[1.0, 0.0]])
    g = np.diag([2.0, 7.0])
    s = c104.minimum_norm_section(q, g)
    y = np.array([3.0])
    x0 = s @ y
    for a in [-5.0, -1.0, 0.0, 2.0, 9.0]:
        x = x0 + np.array([0.0, a])
        assert x @ g @ x >= x0 @ g @ x0 - 1e-12


def test_path_independence_nontrivial_weighted_case():
    q1 = np.array([[1.0, 1.0, 0.0], [0.0, 1.0, 1.0]])
    q2 = np.array([[1.0, -2.0]])
    g = np.array([[3.0, 0.2, 0.0], [0.2, 2.0, 0.1], [0.0, 0.1, 4.0]])
    h1 = c104.induced_quotient_metric(q1, g)
    h_via = c104.induced_quotient_metric(q2, h1)
    h_direct = c104.induced_quotient_metric(q2 @ q1, g)
    assert np.allclose(h_via, h_direct, atol=1e-11)


def test_random_transport_audit():
    out = c104.random_transport_audit(trials=120, seed=104)
    assert out["minimum_norm_violations_gt_1e-8"] == 0
    assert out["path_violations_gt_1e-8"] == 0
    assert out["max_right_inverse_residual"] < 1e-8
    assert out["max_isometry_residual"] < 1e-8
    assert out["max_G_orthogonality_residual"] < 1e-8
