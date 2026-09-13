import numpy as np

from src.pdt.cycle124_so_bilinear_selector import (
    cross3_covariance_audit,
    dimension_sweep,
    o_equivariant_bilinear_dimension,
    reflection_counterexample,
    so_equivariant_bilinear_dimension,
)


def test_exact_dimension_selector_n1_to_n12():
    dims = {n: so_equivariant_bilinear_dimension(n) for n in range(1, 13)}
    assert dims[1] == 1
    assert dims[3] == 1
    assert all(v == 0 for n, v in dims.items() if n not in (1, 3))


def test_full_orthogonal_covariance_kills_all_dimensions():
    for n in list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]:
        assert o_equivariant_bilinear_dimension(n) == 0


def test_so3_cross_product_covariance_numeric():
    audit = cross3_covariance_audit(seed=124, trials=1000)
    assert audit["violations"] == 0
    assert audit["max_residual"] < 1e-10


def test_reflection_is_exact_counterexample():
    w = reflection_counterexample()
    assert w["det_R"] == -1.0
    assert w["lhs"] == [1.0, 0.0, 0.0]
    assert w["rhs"] == [-1.0, 0.0, 0.0]
    assert w["residual_norm"] == 2.0


def test_dimension_sweep_has_unique_nontrivial_so_case():
    rows = dimension_sweep()
    nontrivial = [r["n"] for r in rows if r["n"] >= 2 and r["dim_Hom_SO_VV_V"] > 0]
    assert nontrivial == [3]
