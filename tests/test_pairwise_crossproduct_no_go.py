import numpy as np
from pdt_pairwise_crossproduct_no_go import (
    cross3,cross7,pairwise_residuals,exact_basis_audit,dimension_status
)


def test_exact_basis_pairwise_package_holds_in_3_and_7():
    assert exact_basis_audit(3)["passes_pairwise_package"]
    assert exact_basis_audit(7)["passes_pairwise_package"]


def test_dimension_filter_does_not_select_three():
    assert dimension_status(3)["passes_pairwise_NDC_double_cross"]
    assert dimension_status(7)["passes_pairwise_NDC_double_cross"]


def test_random_integer_vectors_pairwise_identities():
    rng=np.random.default_rng(36036)
    for dim,cross in ((3,cross3),(7,cross7)):
        for _ in range(200):
            a=rng.integers(-3,4,size=dim).astype(float)
            b=rng.integers(-3,4,size=dim).astype(float)
            r=pairwise_residuals(a,b,cross)
            assert r["alternation"] < 1e-10
            assert r["orthogonality"] < 1e-10
            assert r["norm_identity"] < 1e-10
            assert r["double_cross"] < 1e-10


def test_other_dimensions_excluded_only_by_imported_classification():
    for n in range(1,13):
        if n not in (3,7):
            assert not dimension_status(n)["nontrivial_normed_cross_product"]
