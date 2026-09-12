from __future__ import annotations

import numpy as np

from cycle099_record_completeness_not_associativity import (
    exact_octonion_audit,
    full_imaginary_records,
    generic_rank_stress,
    random_octonion_record_audit,
)
from cycle095_octonion_alternative_boundary import associator


def test_full_records_are_separating_on_octonion_associator_sector():
    audit = exact_octonion_audit()
    assert audit["associator_span_rank"] == 7
    assert audit["full_record_rank_on_defect_sector"] == 7
    assert audit["missed_nonzero_basis_associators"] == 0


def test_exact_nonassociative_witness_remains_visible():
    e = np.eye(8)
    a = associator(e[1], e[2], e[4])
    expected = np.zeros(8)
    expected[7] = 2.0
    assert np.array_equal(a, expected)
    record = full_imaginary_records(a)
    assert np.linalg.norm(record) == 2.0


def test_complete_records_do_not_make_octonions_associative():
    audit = exact_octonion_audit()
    assert audit["full_record_rank_on_defect_sector"] == 7
    assert audit["witness_record_norm"] == 2.0
    assert audit["associative_despite_separating_records"] is False


def test_dimension_rank_stress_is_exactly_separating():
    rows = generic_rank_stress()
    assert rows
    assert all(row["record_rank"] == row["defect_dimension"] for row in rows)
    assert all(row["separating"] for row in rows)
    assert all(row["nonzero_defect_exists"] for row in rows)
    assert all(row["nonzero_record_exists"] for row in rows)


def test_random_nonzero_associators_are_detected_by_full_records():
    audit = random_octonion_record_audit(trials=500, seed=9907)
    assert audit["detected_nonzero_associators_gt_1e-10"] == 500
    assert audit["max_scalar_component_abs"] < 1e-12
    assert audit["max_record_vs_full_norm_gap"] < 1e-12
