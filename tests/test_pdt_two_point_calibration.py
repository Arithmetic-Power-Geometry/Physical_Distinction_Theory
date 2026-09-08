from pdt_two_point_calibration import (
    audit,
    exceptional_cases,
    so_case,
    standard_counterexample_families,
    surviving_dimensions,
)


def test_so_pair_stabilizer_formula():
    assert so_case(3).pair_stabilizer_dimension == 0
    assert so_case(4).pair_stabilizer_dimension == 1
    assert so_case(5).pair_stabilizer_dimension == 3
    assert so_case(12).pair_stabilizer_dimension == 45


def test_filter_selects_three_in_audit():
    assert surviving_dimensions(12) == [3]


def test_exceptional_isotropic_actions_fail_pairwise_calibration():
    for case in exceptional_cases():
        assert case.two_point_isotropic
        assert case.noncommuting
        assert not case.pcc
        assert not case.survives_filter


def test_previous_su_counterexamples_are_removed_by_two_point_isotropy():
    for case in standard_counterexample_families():
        assert case.pcc
        assert case.noncommuting
        assert not case.two_point_isotropic
        assert not case.survives_filter


def test_scan_dimensions_1_to_100():
    survivors = [so_case(n).real_dimension for n in range(1, 101) if so_case(n).survives_filter]
    assert survivors == [3]


def test_audit_contains_required_edge_cases():
    rows = audit(12)
    assert any(c.real_dimension == 1 for c in rows)
    assert any(c.real_dimension == 12 for c in rows)
    assert any(c.group == "G2" for c in rows)
    assert any(c.group == "Spin(7)" for c in rows)
