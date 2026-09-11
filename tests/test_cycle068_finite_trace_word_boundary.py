import numpy as np

from cycle068_finite_trace_word_boundary import (
    density_matrix,
    tensor_factorization_error,
    trace_word,
)


def test_trace_word_rejects_bad_letter():
    rho = np.eye(2) / 2
    try:
        trace_word(rho, rho, "rx")
    except ValueError:
        return
    raise AssertionError("bad word letter must raise ValueError")


def test_exact_tensor_factorization_random_cases():
    rng = np.random.default_rng(6802)
    for d in range(1, 13):
        db = 1 if d == 1 else 2
        for _ in range(3):
            ra, sa = density_matrix(d, rng), density_matrix(d, rng)
            rb, sb = density_matrix(db, rng), density_matrix(db, rng)
            for word in ("r", "s", "rs", "rsrs", "rrssr", "rsrssr"):
                assert tensor_factorization_error(ra, sa, rb, sb, word) < 1e-10


def test_degenerate_dimension_one():
    rho = np.array([[1.0]])
    sigma = np.array([[1.0]])
    assert trace_word(rho, sigma, "rsrs") == 1.0 + 0.0j
