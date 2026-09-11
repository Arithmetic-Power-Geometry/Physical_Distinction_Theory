import numpy as np

from cycle084_proper_marginal_composition_no_go import (
    analytic_full_energy,
    analytic_hidden_full_sector_increment,
    ghz_coherence_state,
    partial_trace_keep,
    run_audit,
)


def test_three_qubit_smallest_witness_has_identical_proper_marginals():
    rho0 = ghz_coherence_state(2, 3, 0.0)
    rho1 = ghz_coherence_state(2, 3, 0.5)
    for mask in range(1, 7):
        keep = [i for i in range(3) if mask & (1 << i)]
        a = partial_trace_keep(rho0, [2, 2, 2], keep)
        b = partial_trace_keep(rho1, [2, 2, 2], keep)
        assert np.allclose(a, b, atol=1e-12)


def test_three_qubit_full_distinction_differs_by_four():
    assert analytic_full_energy(2, 3, 0.0) == 3.0
    assert analytic_full_energy(2, 3, 0.5) == 7.0
    assert analytic_hidden_full_sector_increment(2, 3, 0.5) == 4.0


def test_dimension_sweep_reports_no_proper_marginal_difference():
    out = run_audit()
    assert out["breakthrough_candidate"] == "NO"
    assert out["max_proper_marginal_difference"] <= 1e-12
    assert out["max_full_energy_formula_residual"] <= 1e-12
    assert out["smallest_decisive_witness"]["all_party_sector_increment"] == 4.0
