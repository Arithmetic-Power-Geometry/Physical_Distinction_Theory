import numpy as np

from pdt_resource_coarse_graining import (
    audit,
    coarse_grain,
    normalize_kernel_columns,
    normalize_probability,
    total_variation,
)


def test_same_postprocessing_is_exact_through_dimension_12():
    rows = audit(max_dimension=12)
    assert len(rows) == 12
    assert all(r["same_coarse_graining_max_abs_error"] <= 1e-15 for r in rows)
    assert all(r["nonlinear_deformation_tv_gap"] > 0.0 for r in rows)


def test_total_variation_contracts_under_stochastic_postprocessing():
    rng = np.random.default_rng(314159)
    for microscopic_outcomes in range(2, 30):
        for accessible_outcomes in range(2, 10):
            p = normalize_probability(rng.random(microscopic_outcomes))
            q = normalize_probability(rng.random(microscopic_outcomes))
            k = normalize_kernel_columns(
                rng.random((accessible_outcomes, microscopic_outcomes))
            )
            assert total_variation(coarse_grain(p, k), coarse_grain(q, k)) <= total_variation(p, q) + 1e-14
