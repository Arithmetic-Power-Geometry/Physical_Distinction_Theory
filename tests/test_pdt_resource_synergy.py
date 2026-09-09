from itertools import combinations

import pytest

from pdt_resource_synergy import (
    parity_audit,
    parity_table,
    subset_revelation,
    two_resource_submodular_residual,
)


def test_xor_is_pure_synergy_and_violates_submodularity():
    assert subset_revelation(2, [0]) == pytest.approx(0.0, abs=1e-12)
    assert subset_revelation(2, [1]) == pytest.approx(0.0, abs=1e-12)
    assert subset_revelation(2, [0, 1]) == pytest.approx(1.0, abs=1e-12)
    assert subset_revelation(2, []) == pytest.approx(0.0, abs=1e-12)
    assert two_resource_submodular_residual() == pytest.approx(-1.0, abs=1e-12)


def test_every_strict_parity_projection_is_uninformative_through_m8():
    for m in range(2, 9):
        full = set(range(m))
        for r in range(m):
            for subset in combinations(range(m), r):
                assert set(subset) != full
                assert subset_revelation(m, subset) == pytest.approx(0.0, abs=1e-12)
        assert subset_revelation(m, range(m)) == pytest.approx(1.0, abs=1e-12)


def test_dimension_sweep_1_to_12():
    audit = parity_audit(12)
    assert len(audit) == 12
    for row in audit:
        assert row["full_information_bits"] == pytest.approx(1.0, abs=1e-12)
        if row["m"] > 1:
            assert row["max_audited_strict_subset_bits"] == pytest.approx(0.0, abs=1e-12)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        parity_table(0)
    with pytest.raises(ValueError):
        subset_revelation(3, [3])
    with pytest.raises(ValueError):
        parity_audit(0)
