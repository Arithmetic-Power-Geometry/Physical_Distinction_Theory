from pdt_tpi_stabilizer_reduction import reduction_case, surviving_dimensions


def test_topological_reduction_through_100():
    assert surviving_dimensions(100) == [3]


def test_only_local_lie_sphere_candidates_are_three_and_five():
    candidates = [n for n in range(2, 30) if reduction_case(n).stabilizer_sphere_candidate]
    assert candidates == [3, 5]


def test_n5_is_removed_by_global_group_dimension_obstruction():
    c = reduction_case(5)
    assert c.stabilizer_sphere_candidate
    assert not c.post_global_obstruction
    assert not c.survives


def test_n2_edge_case_is_excluded_by_connected_tpi():
    c = reduction_case(2)
    assert not c.stabilizer_sphere_candidate
    assert not c.survives
