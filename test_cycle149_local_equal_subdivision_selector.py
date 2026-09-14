from fractions import Fraction

from cycle149_local_equal_subdivision_selector import (
    additive_ledger,
    cycle146_phi,
    run_audit,
    split_component,
)


def test_exact_local_split_invariance():
    q = [Fraction(1, 3), Fraction(5, 7), Fraction(9, 11)]
    refined = split_component(q, 1, 5)
    assert additive_ledger(refined) == additive_ledger(q)


def test_zero_component_split():
    q = [Fraction(2), Fraction(0), Fraction(3)]
    refined = split_component(q, 1, 7)
    assert additive_ledger(refined) == additive_ledger(q)


def test_cycle146_exact_counterexample_is_killed():
    q = [Fraction(1), Fraction(3)]
    refined = split_component(q, 1, 2)
    assert cycle146_phi(q) == Fraction(25, 7)
    assert cycle146_phi(refined) == Fraction(121, 31)
    assert cycle146_phi(refined) - cycle146_phi(q) == Fraction(72, 217)


def test_seeded_audit_has_no_additive_failures():
    result = run_audit()
    assert result["exact_random_cases"] == 740
    assert result["additive_split_failures"] == 0
    assert result["max_exact_error"] == "0"


def test_prior_counterfamily_is_stressed():
    result = run_audit()
    assert result["cycle146_phi_changed_cases"] > 0
