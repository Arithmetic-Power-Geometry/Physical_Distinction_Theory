import numpy as np

from conditional_output_no_go import full_output_pair_witness, phase_family


def test_full_output_pair_no_go_dimensions_2_to_8():
    for d in range(2, 9):
        w = full_output_pair_witness(d)
        assert w["same_complete_conditional_outputs"]
        assert w["different_coherence"]
        assert w["conditional_pair_residual"] < 1e-12
        assert abs(w["abs_chi_model_A"] - 1.0) < 1e-12
        assert w["abs_chi_model_B"] < 1e-12


def test_continuous_phase_family_keeps_outputs_fixed():
    rows = phase_family(2, np.linspace(0.0, np.pi, 17))
    assert max(r["conditional_output_residual"] for r in rows) < 1e-12
    assert abs(rows[0]["abs_chi"] - 1.0) < 1e-12
    assert rows[-1]["abs_chi"] < 1e-12
    vals = [r["abs_chi"] for r in rows]
    assert all(vals[i] >= vals[i+1] - 1e-12 for i in range(len(vals)-1))
