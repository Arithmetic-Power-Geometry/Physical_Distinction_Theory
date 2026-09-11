import numpy as np

from cycle070_resource_quotient_composition import (
    annihilator_error,
    orthonormal_accessible_space,
    product_coordinate_error,
    random_density,
    restriction_error,
    run_audit,
)


def test_nested_resource_restriction_dimensions_1_through_12():
    rng = np.random.default_rng(701)
    for d in range(1, 13):
        k = min(6, d * d)
        kp = min(d * d, k + min(2, d * d - k))
        fine = orthonormal_accessible_space(d, kp, rng)
        rho = random_density(d, rng)
        assert restriction_error(rho, fine, k) < 1e-12
        if kp > k:
            assert annihilator_error(fine[k], fine[:k]) < 1e-12


def test_product_state_coordinates_factorize():
    rng = np.random.default_rng(702)
    for da in range(1, 7):
        for db in range(1, 7):
            ba = orthonormal_accessible_space(da, min(4, da * da), rng)
            bb = orthonormal_accessible_space(db, min(4, db * db), rng)
            ra = random_density(da, rng)
            rb = random_density(db, rng)
            assert product_coordinate_error(ra, rb, ba, bb) < 1e-12


def test_audit_has_no_large_numeric_failures():
    result = run_audit()
    assert result["refinement_cases"] == 265
    assert result["product_cases"] == 288
    assert result["max_restriction_error"] < 1e-12
    assert result["max_annihilator_error"] < 1e-12
    assert result["max_product_coordinate_error"] < 1e-12
    assert result["breakthrough_candidate"] is False
