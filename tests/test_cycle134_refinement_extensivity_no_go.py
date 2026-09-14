import numpy as np

from cycle134_refinement_extensivity_no_go import resource, run_audit


def test_unit_channel_calibration():
    e = np.zeros((3, 3))
    e[1, 2] = 1.0
    for alpha in (0.5, 1.0, 2.0, 3.0):
        assert resource(e, alpha) == 1.0


def test_smallest_resolved_additivity_counterexample():
    e11 = np.zeros((2, 2)); e11[0, 0] = 1.0
    e22 = np.zeros((2, 2)); e22[1, 1] = 1.0
    whole = e11 + e22
    assert resource(whole, 2.0) == 4.0
    assert resource(e11, 2.0) + resource(e22, 2.0) == 2.0


def test_alpha_one_is_additive_on_orthogonal_channels():
    e11 = np.zeros((2, 2)); e11[0, 0] = 1.0
    e22 = np.zeros((2, 2)); e22[1, 1] = 1.0
    assert resource(e11 + e22, 1.0) == resource(e11, 1.0) + resource(e22, 1.0)


def test_covariance_stress_audit():
    audit = run_audit()
    assert audit.covariance_cases == 1520
    assert audit.covariance_failures == 0
    assert audit.max_relative_covariance_residual < 1e-10


def test_counterfamily_has_nonadditive_members():
    audit = run_audit()
    assert audit.smallest_witness_dimension == 2
    assert audit.exact_nonadditive_witnesses == 3
