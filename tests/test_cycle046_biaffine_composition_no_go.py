from fractions import Fraction
from itertools import product

from pdt_cycle046_biaffine_composition_no_go import (
    associativity_residual,
    coefficients_from_alpha,
    compose,
    evaluate_coefficients,
    exact_audit,
    k_from_alpha,
    monotone_on_capacity_domain,
    product_lower_bound_on_capacity_domain,
    rational_classification_audit,
)


def test_associativity_dimensions_1_to_12_and_k_0_to_11():
    for k in range(12):
        for a, b, c in product(range(1, 13), repeat=3):
            assert associativity_residual(a, b, c, k) == 0


def test_exhaustive_biaffine_coefficient_reduction_examples():
    for alpha in [Fraction(-2), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(7, 3), Fraction(9)]:
        coeffs = coefficients_from_alpha(alpha)
        k = k_from_alpha(alpha)
        for a, b in product(range(1, 13), repeat=2):
            lhs = evaluate_coefficients(Fraction(a), Fraction(b), coeffs)
            rhs = compose(Fraction(a), Fraction(b), k)
            assert lhs == rhs


def test_unit_symmetry_lower_bound_audit():
    rows = exact_audit(12, 11)
    assert len(rows) == 12
    assert all(r["assoc_exact"] for r in rows)
    assert all(r["unit_exact"] for r in rows)
    assert all(r["symmetry_exact"] for r in rows)
    assert all(r["product_lower_bound"] for r in rows)
    assert [r["F_2_2"] for r in rows] == list(range(4, 16))


def test_global_domain_conditions_are_sharp():
    assert monotone_on_capacity_domain(Fraction(-1))
    assert not monotone_on_capacity_domain(Fraction(-3, 2))
    assert product_lower_bound_on_capacity_domain(Fraction(0))
    assert product_lower_bound_on_capacity_domain(Fraction(1, 100))
    assert not product_lower_bound_on_capacity_domain(Fraction(-1, 100))


def test_noninteger_exact_classification():
    assert all(ok for _, _, ok in rational_classification_audit())
