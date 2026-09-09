import numpy as np

from src.pdt_spr_tensor_no_go import (
    factor_local_normalized_rank,
    predicted_tensor_rank,
    single_plane_generator,
    tensor_lift_local_generator,
    universal_spr_survives_tensor_lift,
)


def test_single_plane_generator_has_rank_two():
    for n in range(2, 101):
        assert np.linalg.matrix_rank(single_plane_generator(n)) == 2


def test_tensor_rank_formula_dimensions_1_to_12():
    for n in range(2, 13):
        A = single_plane_generator(n)
        for d in range(1, 13):
            lifted = tensor_lift_local_generator(A, d)
            assert np.linalg.matrix_rank(lifted) == predicted_tensor_rank(2, d) == 2 * d


def test_universal_spr_fails_for_every_nontrivial_spectator():
    for d in range(2, 101):
        assert not universal_spr_survives_tensor_lift(2, d)


def test_trivial_spectator_preserves_spr():
    assert universal_spr_survives_tensor_lift(2, 1)


def test_factor_local_normalization_removes_spectator_multiplicity():
    for d in range(1, 101):
        assert factor_local_normalized_rank(2 * d, d) == 2


def test_degenerate_zero_generator_does_not_create_false_violation():
    for d in range(1, 13):
        Z = np.zeros((3, 3))
        lifted = tensor_lift_local_generator(Z, d)
        assert np.linalg.matrix_rank(lifted) == 0
        assert universal_spr_survives_tensor_lift(0, d)
