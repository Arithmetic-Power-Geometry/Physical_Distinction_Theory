import numpy as np

from primitive_spr_no_go import (
    coordinate_plane_basis,
    ncr_holds,
    plane_generator,
    primitive_spr_holds,
    primitive_spr_ncr_selects,
    spectator_normalized_rank,
)


def test_plane_generators_have_rank_two():
    for n in range(2, 101):
        for a in coordinate_plane_basis(n):
            assert np.linalg.matrix_rank(a) == 2


def test_primitive_spr_holds_all_dimensions_tested():
    assert primitive_spr_holds(1)
    for n in range(2, 101):
        assert primitive_spr_holds(n)


def test_ncr_threshold_is_three():
    assert not ncr_holds(1)
    assert not ncr_holds(2)
    for n in range(3, 101):
        assert ncr_holds(n)


def test_primitive_spr_plus_ncr_does_not_select_three():
    selected = [n for n in range(1, 13) if primitive_spr_ncr_selects(n)]
    assert selected == list(range(3, 13))


def test_explicit_noncommuting_rank_two_pair():
    for n in (3, 4, 5, 8, 12, 24, 64):
        a = plane_generator(n, 0, 1)
        b = plane_generator(n, 1, 2)
        comm = a @ b - b @ a
        assert np.linalg.matrix_rank(a) == 2
        assert np.linalg.matrix_rank(b) == 2
        assert np.linalg.norm(comm, ord="fro") > 0


def test_factor_local_rank_is_spectator_invariant():
    for n in (2, 3, 4, 8, 12):
        a = plane_generator(n, 0, 1)
        for spectator_dim in (1, 2, 3, 5, 12, 32):
            assert spectator_normalized_rank(a, spectator_dim) == 2.0
