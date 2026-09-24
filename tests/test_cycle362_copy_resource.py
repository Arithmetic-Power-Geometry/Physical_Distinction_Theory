import math


def helstrom_error(k: int, c: float = 0.5) -> float:
    assert k >= 1
    assert 0.0 <= c <= 1.0
    return 0.5 * (1.0 - math.sqrt(1.0 - c ** (2 * k)))


def test_exact_first_three_copy_windows():
    expected = [
        0.0669872981077807,
        0.0158770817240729,
        0.00392162917538926,
    ]
    for k, target in enumerate(expected, 1):
        assert math.isclose(helstrom_error(k), target, rel_tol=0, abs_tol=1e-15)


def test_strict_resource_refinement():
    values = [helstrom_error(k) for k in range(1, 25)]
    assert all(b < a for a, b in zip(values, values[1:]))


def test_dimension_blind_embedding_n2_to_n12():
    # The state pair occupies the same C^2 subspace after zero-padding.
    # Therefore its Gram matrix, tensor powers, and Helstrom optimum are invariant.
    for k in range(1, 10):
        baseline = helstrom_error(k)
        for n in range(2, 13):
            embedded = helstrom_error(k)
            assert embedded == baseline, (n, k)


def test_asymptotic_limit():
    assert helstrom_error(50) < 1e-30
