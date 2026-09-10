from cycle047_triad_correlation_kill_test import audit, capped_body_bound, op_body_bound, singlet_triad


def test_rank_bounds_exact():
    for r in range(0, 13):
        assert op_body_bound(r) == r
        assert capped_body_bound(r) == min(r, 2)


def test_smallest_separation_is_three():
    rows = audit(12)
    separated = [row["n"] for row in rows if row["separated"]]
    assert separated[0] == 3
    assert separated == list(range(3, 13))


def test_singlet_kills_capped_body():
    w = singlet_triad()
    assert w["in_C_op"] is True
    assert w["in_C_cap"] is False
    assert w["abs_M3"] == 3
    assert w["nuclear_norm"] == 3


def test_chsh_rank_two_is_not_separated_by_cap_two():
    assert op_body_bound(2) == 2
    assert capped_body_bound(2) == 2
