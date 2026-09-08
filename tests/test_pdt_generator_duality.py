from pdt_generator_duality import audit_dimension, audit_range, generator_dimension, positive_integer_solutions


def test_generator_dimension_formula():
    assert generator_dimension(1) == 0
    assert generator_dimension(3) == 3
    assert generator_dimension(7) == 21
    assert generator_dimension(12) == 66


def test_only_three_matches_through_12():
    matches = [row.n for row in audit_range(1, 12) if row.dimension_match]
    assert matches == [3]


def test_only_three_matches_through_large_scan():
    assert positive_integer_solutions(1000) == [3]


def test_expected_mismatch_signs():
    assert audit_dimension(1).mismatch == -1
    assert audit_dimension(2).mismatch == -1
    assert audit_dimension(3).mismatch == 0
    assert audit_dimension(4).mismatch == 2
