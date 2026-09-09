import numpy as np
from pdt_multibranch_guessing_reserve import (
    classical_guess_probability, apply_common_channel,
    reserve_balance, run_dimension_audit
)

def test_guess_probability_perfect():
    p=np.array([.2,.3,.5]); q=np.eye(3)
    assert np.isclose(classical_guess_probability(p,q),1.0)

def test_no_record_returns_pmax():
    p=np.array([.2,.3,.5]); q=np.ones((3,1))
    assert np.isclose(classical_guess_probability(p,q),.5)

def test_exact_balance_hand_example():
    p=np.array([.5,.5])
    q0=np.array([[.5,0,.5,0],[0,.5,0,.5]])
    P=np.eye(4)[[0,2,1,3]]
    q1=apply_common_channel(q0,P)
    b=reserve_balance(p,q0,q1,2,2)
    assert np.isclose(b["G_joint_s"],1)
    assert np.isclose(b["G_joint_t"],1)
    assert abs(b["residual"]) < 1e-12
    assert b["delta_local"] <= b["R_s"] + 1e-12

def test_random_dimensions_1_to_12():
    rows=run_dimension_audit(seed=7,trials=20,dims=range(1,13))
    for r in rows:
        assert r["max_abs_balance_residual"] < 1e-12
        assert r["max_delta_minus_initial_reserve"] < 1e-12
        assert r["max_negative_global_loss"] < 1e-12
        assert r["max_abs_reversible_global_loss"] < 1e-12

def test_higher_dimensions():
    rows=run_dimension_audit(seed=8,trials=8,dims=[16,24,32,48])
    for r in rows:
        assert r["max_abs_balance_residual"] < 1e-12
        assert r["max_delta_minus_initial_reserve"] < 1e-12
