import numpy as np

from cycle080_resource_visibility_dichotomy import run_audit


def test_cycle080_resource_visibility_dichotomy_regression():
    result = run_audit()
    assert result["breakthrough_candidate"] is False
    assert result["nondegenerate_cases"] == 18
    assert result["max_accessible_probability_gap"] <= 1e-12
    assert result["max_inaccessible_witness_gap"] > 0.0


def test_informational_completeness_annihilator_is_zero_d2():
    # Hermitian basis for d=2: I, X, Y, Z. Any Hermitian delta orthogonal
    # to all four basis elements must vanish.
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    basis = [I, X, Y, Z]

    # Vectorize real Hermitian coordinates (a,b,c,d) for [[a,b+ic],[b-ic,d]].
    rows = []
    for e in basis:
        coeffs = []
        for delta in [
            np.array([[1, 0], [0, 0]], complex),
            np.array([[0, 1], [1, 0]], complex),
            np.array([[0, 1j], [-1j, 0]], complex),
            np.array([[0, 0], [0, 1]], complex),
        ]:
            coeffs.append(float(np.real(np.trace(delta @ e))))
        rows.append(coeffs)
    M = np.asarray(rows)
    assert np.linalg.matrix_rank(M) == 4
