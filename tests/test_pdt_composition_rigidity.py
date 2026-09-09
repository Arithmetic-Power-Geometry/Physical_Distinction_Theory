import math

from pdt_composition_rigidity import (
    associativity_residual_holism,
    audit_dimensions,
    finite_difference_unit_derivative,
    holism_family,
    holism_unit_derivative,
    imr_residual_holism,
    product_law,
)


def test_holism_family_has_unit_and_is_commutative():
    for k in range(6):
        for a in range(1, 13):
            assert holism_family(a, 1, k) == a
            assert holism_family(1, a, k) == a
            for b in range(1, 13):
                assert holism_family(a, b, k) == holism_family(b, a, k)


def test_holism_family_associative_dimensions_1_to_12():
    for k in range(6):
        for a in range(1, 13):
            for b in range(1, 13):
                for c in range(1, 13):
                    assert associativity_residual_holism(a, b, c, k) == 0


def test_imr_eliminates_nonzero_holism_for_nontrivial_capacity():
    for a in range(2, 13):
        assert imr_residual_holism(a, 0) == 0
        for k in range(1, 20):
            assert imr_residual_holism(a, k) != 0


def test_exact_unit_derivative_and_finite_difference_agree():
    for a in range(1, 13):
        for k in range(6):
            exact = holism_unit_derivative(a, k)
            approx = finite_difference_unit_derivative(a, k)
            assert math.isclose(exact, approx, rel_tol=1e-7, abs_tol=2e-7)


def test_product_law_satisfies_imr_reference():
    for a in range(1, 101):
        assert product_law(a, 1.0) == a
        h = 1e-7
        approx = (product_law(a, 1.0 + h) - product_law(a, 1.0)) / h
        assert math.isclose(approx, a, rel_tol=1e-7, abs_tol=2e-7)


def test_audit_nontrivial_rows_select_only_k_zero():
    rows = audit_dimensions(max_dimension=12, max_k=5)
    assert len(rows) == 72
    for row in rows:
        if row.a > 1:
            assert row.imr_holds == (row.k == 0)
        # floating associativity residual can accumulate roundoff only
        assert row.associativity_max_abs_residual < 1e-9
