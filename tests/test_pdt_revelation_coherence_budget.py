import numpy as np

from pdt_revelation_coherence_budget import (
    audit_dimensions,
    budget_terms,
    random_density,
    random_unitary,
)


def test_random_budget_holds_dimensions_1_to_12():
    rows = audit_dimensions(max_d=12, trials=80, seed=1209)
    assert len(rows) == 12
    for row in rows:
        assert row["max_lhs"] <= 1.0 + 1e-10
        assert row["min_margin"] >= -1e-10


def test_pure_record_saturates_budget():
    # eta = |0><0| and V rotates |0> into cos(theta)|0>+sin(theta)|1>.
    theta = 0.37
    eta = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
    v = np.array(
        [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]],
        dtype=complex,
    )
    terms = budget_terms(eta, v)
    lhs = terms["trace_distance"] ** 2 + terms["abs_chi"] ** 2
    assert abs(lhs - 1.0) < 1e-10


def test_mixed_random_cases_obey_both_intermediate_bounds():
    rng = np.random.default_rng(991)
    for d in range(2, 20):
        for _ in range(12):
            eta = random_density(d, rng)
            v = random_unitary(d, rng)
            terms = budget_terms(eta, v)
            assert terms["chi_le_f_margin"] >= -1e-10
            assert terms["fvdg_margin"] >= -1e-10
