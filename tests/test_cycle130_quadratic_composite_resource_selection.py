import math
import numpy as np

from cycle130_quadratic_composite_resource_selection import parallelogram_gap, run_audit


def units():
    a = np.zeros((2, 2)); a[0, 0] = 1.0
    b = np.zeros((2, 2)); b[1, 1] = 1.0
    return a, b


def test_frobenius_passes_exact_witness():
    a, b = units()
    assert abs(parallelogram_gap(a, b, 2.0)) < 1e-12


def test_nuclear_fails_parallelogram():
    a, b = units()
    assert abs(parallelogram_gap(a, b, 1.0) - 4.0) < 1e-12


def test_schatten4_fails_parallelogram():
    a, b = units()
    expected = 2.0 * math.sqrt(2.0) - 4.0
    assert abs(parallelogram_gap(a, b, 4.0) - expected) < 1e-12


def test_spectral_fails_parallelogram():
    a, b = units()
    assert abs(parallelogram_gap(a, b, math.inf) + 2.0) < 1e-12


def test_dimension_stress_audit():
    out = run_audit(130)
    assert out["frobenius_parallelogram_failures"] == 0
    assert out["frobenius_covariance_failures"] == 0
    assert out["breakthrough_candidate"] is False
    assert out["dimensions"][:12] == list(range(1, 13))
