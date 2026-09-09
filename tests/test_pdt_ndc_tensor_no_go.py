from pdt_ndc_tensor_no_go import (
    NONTRIVIAL_NDC_DIMS,
    admits_nontrivial_ndc,
    nontrivial_tensor_closure_witnesses,
    self_tensor_row,
    tensor_dimension,
    theorem_holds,
)


def test_classical_nontrivial_dimension_set_encoded():
    assert NONTRIVIAL_NDC_DIMS == frozenset({3, 7})
    assert admits_nontrivial_ndc(3)
    assert admits_nontrivial_ndc(7)
    for n in [1, 2, 4, 5, 6, 8, 9, 12, 16, 21, 49, 128]:
        assert not admits_nontrivial_ndc(n)


def test_tensor_dimension_is_multiplicative():
    for n in range(1, 13):
        for m in range(1, 13):
            assert tensor_dimension(n, m) == n * m


def test_self_composition_kills_nontrivial_ndc():
    assert self_tensor_row(3)["tensor_dimension"] == 9
    assert self_tensor_row(7)["tensor_dimension"] == 49
    assert not self_tensor_row(3)["tensor_nontrivial_ndc"]
    assert not self_tensor_row(7)["tensor_nontrivial_ndc"]


def test_all_nontrivial_pair_products_leave_allowed_set():
    expected = {(3, 3, 9), (3, 7, 21), (7, 7, 49)}
    actual = {(r["n"], r["m"], r["tensor_dimension"]) for r in nontrivial_tensor_closure_witnesses()}
    assert actual == expected
    assert theorem_holds()


def test_no_nontrivial_multiplicatively_closed_subset():
    # Any nontrivial subset of {3,7} contains x; closure under tensor self-composition
    # would require x^2 in {3,7}, but 9 and 49 are absent.
    for x in (3, 7):
        assert x * x not in NONTRIVIAL_NDC_DIMS
