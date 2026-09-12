import numpy as np

from cycle092_tensor_parity_composition_obstruction import (
    AUDIT_DIMS,
    exact_parity,
    explicit_dimension_witness,
    multipartite_parity_table,
)


def test_exchange_parity_product_rule():
    assert exact_parity([-1]) == -1
    assert exact_parity([-1, -1]) == 1
    assert exact_parity([-1, 1]) == -1
    assert exact_parity([1, -1]) == -1
    assert exact_parity([1, 1]) == 1
    assert exact_parity([-1, -1, -1]) == -1


def test_bb_is_not_alternating_in_every_nondegenerate_audit_dimension():
    for n in AUDIT_DIMS:
        row = explicit_dimension_witness(n)
        if n == 1:
            assert row["degenerate"]
            assert row["bb_diagonal_witness_norm"] == 0.0
        else:
            assert not row["degenerate"]
            assert np.isclose(row["bb_diagonal_witness_norm"], 2.0)
            assert np.isclose(row["bb_swap_sum_norm"], 2.0)


def test_symmetric_companion_repairs_exchange_parity():
    for n in AUDIT_DIMS:
        row = explicit_dimension_witness(n)
        if n >= 2:
            assert row["parity_repair_swap_sum_norm"] <= 1e-12
            assert np.isclose(row["parity_repair_nonzero_norm"], 1.0)


def test_all_B_multipartite_parity_alternates_with_party_number():
    rows = multipartite_parity_table(12)
    for row in rows:
        expected = -1 if row["parties"] % 2 else 1
        assert row["exchange_parity"] == expected
        assert row["type"] == ("alternating" if expected == -1 else "symmetric")
