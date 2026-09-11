from fractions import Fraction

from cycle064_nonlinear_probability_contextuality import (
    exact_qubit_witness,
    split_context_witness,
)


def test_exact_qubit_contextuality_witness():
    w = exact_qubit_witness()
    assert w["p_same_effect_M2"] == Fraction(1, 2)
    assert w["p_same_effect_M3"] == Fraction(2, 3)
    assert w["gap"] == Fraction(1, 6)


def test_born_rule_is_completion_invariant_under_split():
    for x in (0.1, 0.2, 0.5, 0.8):
        a, b = split_context_witness(x, [(1-x)/3, 2*(1-x)/3], 1.0)
        assert abs(a-b) < 1e-12


def test_nonlinear_power_rules_fail_generic_completion_invariance():
    x = 0.5
    parts = [0.25, 0.25]
    for alpha in (0.5, 1.5, 2.0, 3.0):
        a, b = split_context_witness(x, parts, alpha)
        assert abs(a-b) > 1e-12
