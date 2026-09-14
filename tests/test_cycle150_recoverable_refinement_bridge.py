from fractions import Fraction

from cycle150_recoverable_refinement_bridge import (
    additive_ledger,
    cycle146_phi,
    merge_daughters,
    normalize_weights,
    refine_component,
    run_audit,
)


def test_normalized_weights_are_exact():
    ws = normalize_weights([Fraction(1, 4), Fraction(3, 4)])
    assert ws == [Fraction(1, 4), Fraction(3, 4)]
    assert sum(ws, Fraction(0)) == 1


def test_refine_merge_is_exact_left_inverse():
    q = [Fraction(2, 3), Fraction(5, 7), Fraction(11, 13)]
    r = refine_component(q, 1, [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)])
    assert merge_daughters(r, 1, 3) == q


def test_additive_ledger_is_invariant_under_arbitrary_local_split():
    q = [Fraction(1), Fraction(3)]
    r = refine_component(q, 1, [Fraction(1, 4), Fraction(3, 4)])
    assert additive_ledger(r) == additive_ledger(q) == 4


def test_recoverability_alone_does_not_force_phi_invariance():
    q = [Fraction(1), Fraction(3)]
    r = refine_component(q, 1, [Fraction(1, 4), Fraction(3, 4)])
    assert merge_daughters(r, 1, 2) == q
    assert cycle146_phi(q) == Fraction(25, 7)
    assert cycle146_phi(r) == Fraction(2809, 820)
    assert cycle146_phi(r) - cycle146_phi(q) == Fraction(-837, 5740)


def test_frozen_audit_has_no_recovery_or_additive_failures():
    result = run_audit()
    assert result["exact_random_cases"] == 740
    assert result["exact_recovery_failures"] == 0
    assert result["additive_invariance_failures"] == 0
    assert result["cycle146_phi_changed_cases"] == 705
