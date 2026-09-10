import numpy as np
import pytest

from pdt_postselection_same_input_lock import (
    conditional_from_joint,
    postselection_same_input_lock,
    rare_event_witness,
    stress_audit,
)


def test_exact_same_joint_lock():
    q = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=float)
    assert postselection_same_input_lock(q, q.copy(), [1])
    expected = np.array([0.2, 0.4]) / 0.6
    assert np.allclose(conditional_from_joint(q, [1]), expected)


def test_different_joint_is_not_same_input_lock():
    q = np.array([[0.1, 0.2], [0.3, 0.4]], dtype=float)
    r = q.copy()
    r[0, 1] += 0.01
    r[1, 1] -= 0.01
    assert not postselection_same_input_lock(q, r, [1])


def test_zero_probability_selection_rejected():
    q = np.array([[0.5, 0.0], [0.5, 0.0]], dtype=float)
    with pytest.raises(ValueError):
        conditional_from_joint(q, [1])


def test_dimension_stress_1_to_12():
    rows = stress_audit(seed=1234, trials=100)
    assert [r.dimension for r in rows] == list(range(1, 13))
    assert max(r.max_same_joint_error for r in rows) <= 1e-15
    assert max(r.max_normalization_error for r in rows) <= 1e-15


def test_rare_event_can_change_conditional_but_not_theory_gap():
    w = rare_event_witness(1e-6)
    assert 0 < w["success_probability"] < 1e-4
    assert w["conditional_P_O1_given_keep"] > 0.999
    assert w["qm_pdt_conditional_gap_same_joint"] == 0.0
