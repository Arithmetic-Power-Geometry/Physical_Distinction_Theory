import numpy as np

from cycle097_associator_record_separation import (
    associator_matrix,
    expanding_defect_space_counterexample,
    octonion_exact_audit,
    octonion_refinement_curve,
    revelation_counts,
)


def test_octonion_associator_span_is_exactly_imaginary_seven_space():
    audit = octonion_exact_audit()
    assert audit["basis_triples"] == 512
    assert audit["nonzero_basis_associators"] == 168
    assert audit["associator_span_rank"] == 7
    assert audit["scalar_record_rank_on_associator_span"] == 0
    assert len(audit["basis_direction_witnesses"]) == 7


def test_all_octonion_basis_associators_have_zero_scalar_part():
    a = associator_matrix()
    assert np.array_equal(a[:, 0], np.zeros(512))


def test_seven_imaginary_coordinate_records_are_necessary_on_canonical_curve():
    curve = octonion_refinement_curve()
    assert [row["revealed_rank"] for row in curve] == list(range(8))
    assert [row["hidden_dimension"] for row in curve] == list(range(7, -1, -1))
    assert curve[6]["separating"] is False
    assert curve[7]["separating"] is True


def test_rank_nullity_revelation_identity():
    w = np.eye(5)
    records = np.eye(5)[:3]
    result = revelation_counts(records, w)
    assert result["revealed_rank"] == 3
    assert result["hidden_dimension"] == 2
    assert result["rank_nullity_sum"] == 5


def test_expanding_defect_space_breaks_hidden_monotonicity_without_compatibility():
    result = expanding_defect_space_counterexample()
    assert result["coarse"]["hidden_dimension"] == 0
    assert result["refined"]["hidden_dimension"] == 1
    assert result["hidden_dimension_increases"] is True
