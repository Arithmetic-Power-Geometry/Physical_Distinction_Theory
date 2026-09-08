from pdt_pairwise_group_counterexamples import (
    audit_table,
    su_minimal_reference_states,
    su_pairwise_calibration_possible,
    su_pcc_counterexample,
)


def test_su_minimal_reference_count():
    assert su_minimal_reference_states(1) == 0
    for m in range(2, 20):
        assert su_minimal_reference_states(m) == m - 1


def test_explicit_higher_dimensional_counterexamples():
    assert su_pcc_counterexample(2)  # SU(2) on R^4
    assert su_pcc_counterexample(3)  # SU(3) on R^6
    assert not su_pcc_counterexample(4)


def test_pairwise_cutoff_for_natural_su_action():
    passing = [m for m in range(1, 20) if su_pairwise_calibration_possible(m)]
    assert passing == [1, 2, 3]


def test_audit_table_counterexample_dimensions():
    df = audit_table(8)
    dims = df.loc[df["higher_dim_PCC_counterexample"], "real_state_dimension_n"].tolist()
    assert dims == [4, 6]
