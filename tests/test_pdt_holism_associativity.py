from pdt_holism_associativity import (
    associativity_residual,
    compose_dimension,
    holism_balance_residual,
    holism_excess,
    multiplicative_transform_residual,
)


def test_unit_commutativity_and_product_lower_bound():
    for k in range(5):
        for a in range(1, 101):
            assert compose_dimension(a, 1, k) == a
            for b in range(1, 101):
                assert compose_dimension(a, b, k) == compose_dimension(b, a, k)
                assert compose_dimension(a, b, k) >= a * b
                assert holism_excess(a, b, k) >= 0


def test_exact_associativity_dimensions_1_through_12():
    for k in range(5):
        for a in range(1, 13):
            for b in range(1, 13):
                for c in range(1, 13):
                    assert associativity_residual(a, b, c, k) == 0
                    assert holism_balance_residual(a, b, c, k) == 0
                    assert multiplicative_transform_residual(a, b, k) == 0


def test_infinitely_many_distinct_laws_have_same_basic_axioms():
    # Already the elementary pair (2,2) separates every nonnegative integer k:
    # F_k(2,2)=4+k.
    values = [compose_dimension(2, 2, k) for k in range(50)]
    assert values == list(range(4, 54))
    assert len(set(values)) == 50


def test_k_zero_recovers_product_dimension():
    for a in range(1, 50):
        for b in range(1, 50):
            assert compose_dimension(a, b, 0) == a * b
            assert holism_excess(a, b, 0) == 0


def test_invalid_inputs_rejected():
    import pytest

    with pytest.raises(ValueError):
        compose_dimension(0, 2, 0)
    with pytest.raises(ValueError):
        compose_dimension(2, 2, -1)
