from pdt_quotient_composition import QuotientCompositionAudit, admissible_composite_quotient_dimensions, sweep


def test_exact_quotient_tensor_identity_n1_to_n12():
    for row in sweep(12):
        assert row["identity_ok"]
        assert row["product_q"] + row["product_null"] == row["tensor_dim"]


def test_no_nulls_leave_no_extra_linear_direction():
    a = QuotientCompositionAudit(3, 4, 0, 0)
    assert a.product_accessible_dim == 12
    assert admissible_composite_quotient_dimensions(3, 4, 0, 0) == [12]


def test_hidden_local_directions_leave_global_composition_freedom():
    # Same local quotients qV=qW=1. Product-accessible composite has dimension 1,
    # but independent global effects can reveal additional tensor directions.
    dims = admissible_composite_quotient_dimensions(2, 2, 1, 1)
    assert dims == [1, 2, 3, 4]


def test_asymmetric_edge_case():
    a = QuotientCompositionAudit(12, 7, 11, 0)
    assert a.local_q_v == 1 and a.local_q_w == 7
    assert a.product_accessible_dim == 7
    assert a.product_null_dim == 77
    assert a.validate()
