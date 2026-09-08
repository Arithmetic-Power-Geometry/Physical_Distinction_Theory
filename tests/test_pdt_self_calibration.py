from pdt_self_calibration import (
    audit_dimensions,
    control_entropy_slope,
    noncommuting_reversibility_passes,
    osc_ncr_selects,
    osc_passes,
    state_entropy_slope,
)


def test_entropy_slopes_and_selection_1_to_12():
    rows = audit_dimensions(1, 12)
    assert len(rows) == 12
    assert [r["n"] for r in rows if r["selected"]] == [3]
    for row in rows:
        n = row["n"]
        assert state_entropy_slope(n) == n
        assert control_entropy_slope(n) == n * (n - 1) // 2


def test_osc_bound_and_noncommutativity_large_scan():
    selected = [n for n in range(1, 1001) if osc_ncr_selects(n)]
    assert selected == [3]
    assert osc_passes(1) and osc_passes(2) and osc_passes(3)
    assert not osc_passes(4)
    assert not noncommuting_reversibility_passes(1)
    assert not noncommuting_reversibility_passes(2)
    assert noncommuting_reversibility_passes(3)
