import numpy as np

from cycle067_noncommutative_word_moment_composition import (
    cycle066_witness,
    density_matrix,
    mixed_moment,
    shortest_separating_word,
    tensor_factorization_error,
)


def test_cycle066_family_is_separated_by_noncommutative_word():
    sep = shortest_separating_word(max_len=4)
    assert sep is not None
    word, a, b = sep
    assert word in {"rsrs", "srsr"}
    assert abs(a - b) > 2e-3 - 1e-12


def test_rsrs_values_for_exact_cycle066_parameters():
    rho0, sigma0 = cycle066_witness(0.0)
    rhopi, sigmapi = cycle066_witness(np.pi)
    assert np.isclose(mixed_moment(rho0, sigma0, "rsrs").real, 0.0303, atol=1e-12)
    assert np.isclose(mixed_moment(rhopi, sigmapi, "rsrs").real, 0.0282, atol=1e-12)


def test_tensor_word_moments_factorize_dimensions_1_to_12():
    rng = np.random.default_rng(6702)
    words = ["r", "s", "rs", "rrs", "rsrs", "rrssr", "rsrssr"]
    for d_a in range(1, 13):
        d_b = 1 if d_a == 1 else 2
        rho_a, sigma_a = density_matrix(d_a, rng), density_matrix(d_a, rng)
        rho_b, sigma_b = density_matrix(d_b, rng), density_matrix(d_b, rng)
        for word in words:
            assert tensor_factorization_error(rho_a, sigma_a, rho_b, sigma_b, word) < 1e-10
