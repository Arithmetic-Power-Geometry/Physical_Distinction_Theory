import numpy as np

from pdt_normed_composition_filter import (
    classification_row,
    cross3,
    cross7,
    explicit_7d_jacobi_witness,
    jacobiator,
    norm_identity_residual,
    orthogonality_residual,
    randomized_audit,
)


def test_dimension_filter_1_to_12_selects_only_three():
    selected=[n for n in range(1,13) if classification_row(n)["passes_NDC_plus_JSC"]]
    assert selected == [3]


def test_3d_exact_basis_jacobi():
    e=np.eye(3)
    j=jacobiator(e[0],e[1],e[2],cross3)
    assert np.allclose(j,0.0,atol=1e-12)


def test_7d_explicit_jacobi_counterexample():
    *_,j=explicit_7d_jacobi_witness()
    assert np.allclose(j,np.array([0,0,0,0,0,0,-3.0]),atol=1e-12)


def test_norm_and_orthogonality_3d_7d_random():
    rng=np.random.default_rng(30030)
    for d,cross in ((3,cross3),(7,cross7)):
        for _ in range(100):
            a=rng.normal(size=d); b=rng.normal(size=d)
            assert abs(norm_identity_residual(a,b,cross)) < 1e-9
            assert orthogonality_residual(a,b,cross) < 1e-9


def test_random_audit_separates_jacobi_behavior():
    a3=randomized_audit(3,trials=100,seed=9)
    a7=randomized_audit(7,trials=100,seed=9)
    assert a3["max_jacobiator_norm"] < 1e-9
    assert a7["max_jacobiator_norm"] > 1e-3


def test_known_classification_high_dimensions_rejected():
    for n in list(range(2,13))+[16,24,32,64,128,256]:
        if n not in (3,7):
            assert not classification_row(n)["nontrivial_normed_cross_product"]
