import numpy as np

from cycle065_relative_modular_spectrum_no_go import (
    exact_qubit_witness,
    modular_spectrum,
    stress,
    trace_distance,
)


def test_exact_qubit_witness():
    w = exact_qubit_witness()
    assert w["dimension"] == 2
    assert np.allclose(w["relative_modular_spectrum"], [0.375, 0.875, 1.5, 3.5])
    assert abs(w["trace_distance_commuting"] - 0.1) < 1e-14
    assert abs(w["trace_distance_swapped"] - 0.5) < 1e-14
    assert abs(w["separation"] - 0.4) < 1e-14


def test_relative_modular_spectrum_ignores_relative_basis():
    sigma = np.diag([0.8, 0.2])
    rho0 = np.diag([0.7, 0.3])
    rho1 = np.diag([0.3, 0.7])
    assert np.allclose(modular_spectrum(rho0, sigma), modular_spectrum(rho1, sigma))
    assert abs(trace_distance(rho0, sigma) - trace_distance(rho1, sigma)) > 0.39


def test_dimension_stress_has_no_spectrum_failures():
    out = stress(seed=65011)
    assert out["spectrum_failures"] == 0
    for rec in out["records"]:
        if rec["n"] >= 2:
            assert rec["trace_distance_spread"] > 1e-6
