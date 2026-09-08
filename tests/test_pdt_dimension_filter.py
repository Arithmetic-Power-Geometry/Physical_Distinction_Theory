import numpy as np

import pdt_dimension_filter as d


def test_3d_cross_product_passes_norm_orthogonality_and_jacobi():
    rng = np.random.default_rng(42)
    for _ in range(100):
        a, b, c = rng.normal(size=(3, 3))
        assert d.norm_identity_residual(d.cross3, a, b) < 1e-10
        assert d.orthogonality_residual(d.cross3, a, b) < 1e-10
        assert d.jacobi_residual(d.cross3, a, b, c) < 1e-10
    assert d.basis_jacobi_max(3) < 1e-12


def test_7d_octonionic_cross_product_passes_norm_but_fails_jacobi():
    rng = np.random.default_rng(43)
    for _ in range(100):
        a, b, _ = rng.normal(size=(3, 7))
        assert d.norm_identity_residual(d.cross7, a, b) < 1e-9
        assert d.orthogonality_residual(d.cross7, a, b) < 1e-9
    assert abs(d.basis_jacobi_max(7) - 3.0) < 1e-12


def test_dimension_filter_1_through_12_leaves_only_three():
    table = d.dimension_filter_table(12)
    survivors = table.loc[table.jacobi_compatible_standard_model, "n"].tolist()
    assert survivors == [3]
    assert bool(table.loc[table.n == 7, "nontrivial_normed_cross_product"].iloc[0])
