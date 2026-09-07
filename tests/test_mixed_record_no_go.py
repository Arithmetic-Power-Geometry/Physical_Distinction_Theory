import numpy as np

from mixed_record_no_go import controlled_record_quantities, scalar_record_nonidentifiability_witness


def test_analytic_family_has_zero_environment_trace_distinguishability():
    for theta in np.linspace(0.0, np.pi, 17):
        q = controlled_record_quantities(theta)
        assert abs(q["D_E"]) < 1e-12
        assert abs(q["abs_chi"] - q["analytic_abs_chi"]) < 1e-12


def test_same_D_can_have_different_coherence_factor():
    w = scalar_record_nonidentifiability_witness()
    assert w["same_D"]
    assert w["different_abs_chi"]
    assert abs(w["D_case_a"]) < 1e-12
    assert abs(w["D_case_b"]) < 1e-12
    assert abs(w["abs_chi_case_a"] - 1.0) < 1e-12
    assert w["abs_chi_case_b"] < 1e-12
