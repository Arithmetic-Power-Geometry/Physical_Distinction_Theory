import numpy as np

from pdt_pairwise_calibration import (
    audit_table,
    minimal_reference_states,
    pairwise_calibration_possible,
    pcc_dimension_filter,
    pointwise_stabilizer_dimension,
    stabilizer_witness,
)


def test_minimal_reference_count():
    assert minimal_reference_states(1) == 0
    for n in range(2, 50):
        assert minimal_reference_states(n) == n - 1


def test_pairwise_plus_noncommuting_selects_three():
    passing = [n for n in range(1, 101) if pcc_dimension_filter(n)]
    assert passing == [3]


def test_two_reference_stabilizer_dimensions():
    for n in range(1, 20):
        m = max(0, n - min(n, 2))
        expected = m * (m - 1) // 2
        assert pointwise_stabilizer_dimension(n, 2) == expected


def test_explicit_nonidentity_stabilizer_witness_for_n_ge_4():
    for n in range(4, 13):
        Q = stabilizer_witness(n, 2)
        assert np.allclose(Q.T @ Q, np.eye(n), atol=1e-12)
        assert np.isclose(np.linalg.det(Q), 1.0, atol=1e-12)
        assert np.allclose(Q[:, :2], np.eye(n)[:, :2], atol=1e-12)
        assert not np.allclose(Q, np.eye(n), atol=1e-12)


def test_no_continuous_stabilizer_after_two_refs_in_n3():
    Q = stabilizer_witness(3, 2)
    assert np.allclose(Q, np.eye(3), atol=1e-12)
    assert pairwise_calibration_possible(3)


def test_audit_table_dimension_scan():
    df = audit_table(12)
    assert df.loc[df["passes_PCC_plus_noncommuting"], "n"].tolist() == [3]
