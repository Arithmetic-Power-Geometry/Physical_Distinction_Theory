import math
import numpy as np

from pdt_record_information_capacity import (
    accessible_information_ceiling_bits,
    random_pure_ensemble,
    repeated_basis_ensemble,
    residual_label_uncertainty_floor_bits,
    uniform_pure_holevo,
)


def test_capacity_ceiling_dimensions_1_to_100():
    for d in range(1, 101):
        for k in (1, d, d + 1, 2 * d, 3 * d):
            cap = accessible_information_ceiling_bits(k, d)
            assert cap <= math.log2(k) + 1e-12
            assert cap <= math.log2(d) + 1e-12
            assert residual_label_uncertainty_floor_bits(k, d) >= -1e-12


def test_random_pure_ensembles_obey_holevo_dimension_ceiling():
    rng = np.random.default_rng(1909)
    for d in range(1, 13):
        k = d + 3
        for _ in range(100):
            vectors = random_pure_ensemble(k, d, rng)
            chi = uniform_pure_holevo(vectors)
            assert chi <= math.log2(d) + 1e-10
            assert chi <= math.log2(k) + 1e-10


def test_repeated_basis_saturates_information_ceiling_when_k_multiple_of_d():
    for d in range(1, 13):
        k = 3 * d
        vectors = repeated_basis_ensemble(k, d)
        chi = uniform_pure_holevo(vectors)
        assert abs(chi - math.log2(d)) < 1e-10
        # Basis measurement reveals log2(d) bits and leaves log2(k/d) bits.
        assert abs(math.log2(k) - chi - math.log2(k / d)) < 1e-10


def test_perfect_uniform_label_revelation_requires_d_at_least_k():
    for k in range(2, 50):
        for d in range(1, k):
            assert residual_label_uncertainty_floor_bits(k, d) > 0
