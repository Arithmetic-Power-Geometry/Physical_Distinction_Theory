import numpy as np

from cycle085_classical_postprocessing_naturality_no_go import (
    direct_singleton_identity,
    identity_map,
    naturality_residual,
    power_map,
    square_split_witness,
)


def test_singleton_channel_proof_instantiation():
    for n in range(1, 13):
        q = np.arange(1, n + 1, dtype=float)
        q /= q.sum()
        assert direct_singleton_identity(q) == 0.0


def test_identity_commutes_with_stochastic_postprocessing():
    q = np.array([0.2, 0.3, 0.5])
    T = np.array([[0.7, 0.1, 0.4], [0.3, 0.9, 0.6]])
    assert np.allclose(T.sum(axis=0), 1.0)
    assert naturality_residual(q, T, identity_map) < 1e-15


def test_quadratic_map_fails_small_split_witness():
    witness = square_split_witness()
    assert witness["max_residual"] > 0.08
    assert np.allclose(witness["F3_Tq"], [9 / 22, 9 / 22, 2 / 11])
    assert np.allclose(witness["T_F2_q"], [9 / 20, 9 / 20, 1 / 10])


def test_quadratic_map_is_not_natural_under_split():
    q = np.array([0.75, 0.25])
    T = np.array([[0.5, 0.0], [0.5, 0.0], [0.0, 1.0]])
    assert naturality_residual(q, T, lambda x: power_map(x, 2.0)) > 1e-3
