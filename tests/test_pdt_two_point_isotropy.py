from pdt_two_point_isotropy import audited_tpi_cases, so_case, surviving_dimensions


def test_so_pair_stabilizer_formula_through_100():
    for n in range(2, 101):
        c = so_case(n)
        k = max(n - 2, 0)
        assert c.pair_stabilizer_dimension == k * (k - 1) // 2


def test_tpi_pcc_ncr_leaves_three_in_audited_set():
    assert surviving_dimensions(12) == [3]


def test_exceptional_tpi_actions_fail_pairwise_calibration():
    cases = {c.family: c for c in audited_tpi_cases(12)}
    assert cases["G2"].pair_stabilizer == "SU(2)"
    assert cases["G2"].pair_stabilizer_dimension == 3
    assert not cases["G2"].pcc
    assert cases["Spin(7)"].pair_stabilizer == "SU(3)"
    assert cases["Spin(7)"].pair_stabilizer_dimension == 8
    assert not cases["Spin(7)"].pcc


def test_so3_survives_but_neighbors_do_not():
    assert not so_case(2).survives  # connected rotations commute
    assert so_case(3).survives
    assert not so_case(4).survives  # nontrivial SO(2) pair stabilizer
