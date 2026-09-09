import math

from pdt_scalar_composition_gauge import (
    additive_residual,
    associativity_residual,
    audit,
    shifted_logarithm,
    shifted_phi,
    shifted_product_law,
)


def test_identity_and_associativity_integer_grid():
    for k in range(13):
        for a in range(1, 13):
            assert shifted_product_law(a, 1, k) == a
            assert shifted_product_law(1, a, k) == a
            for b in range(1, 13):
                for c in (1, 2, 12):
                    assert associativity_residual(a, b, c, k) == 0


def test_calibration_linearizes_cycle039_family():
    for k in range(13):
        for a in range(1, 13):
            for b in range(1, 13):
                assert abs(additive_residual(a, b, k)) < 1e-12


def test_invariant_differential_matches_phi():
    # L'(x)=1/phi(x) checked by centered finite differences away from boundary.
    h = 1e-6
    for k in (0, 1, 3, 12):
        for x in (1.25, 2.0, 5.0, 12.0):
            num = (shifted_logarithm(x + h, k) - shifted_logarithm(x - h, k)) / (2 * h)
            assert math.isclose(num, 1.0 / shifted_phi(x, k), rel_tol=1e-8, abs_tol=1e-9)


def test_product_is_imr_gauge():
    for x in (1.0, 2.0, 7.0, 12.0):
        assert shifted_phi(x, 0) == x
    for k in (1, 2, 12):
        assert shifted_phi(2.0, k) != 2.0


def test_cycle041_audit():
    result = audit(max_dim=12, max_k=12)
    assert result["pass"]
    assert result["worst_additive_coordinate_residual"] < 1e-12
