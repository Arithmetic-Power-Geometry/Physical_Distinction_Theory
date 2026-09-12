import numpy as np
from cycle089_so_n_equivariant_n3_selector import selector_status, randomized_so3_check


def test_selector_exact_dimensions_1_to_12():
    selected = []
    for n in range(1, 13):
        row = selector_status(n)
        if row["equivariant_map_dimension"] > 0:
            selected.append(n)
        if n > 3:
            assert row["killed_components"] == row["triple_components"]
    assert selected == [3]


def test_high_dimension_selector_boundary():
    for n in (16, 24, 32, 48, 64, 96, 128):
        row = selector_status(n)
        assert row["equivariant_map_dimension"] == 0
        assert row["killed_components"] == row["triple_components"]


def test_so3_cross_product_equivariance_numerically():
    assert randomized_so3_check(seed=8903, trials=500) < 1e-12
