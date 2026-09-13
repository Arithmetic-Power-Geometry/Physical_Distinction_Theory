from cycle118_multiplicative_resource_no_go import (
    product,
    product_scalar,
    resource_scalar,
    run_audit,
    visible_state,
)


def test_smallest_explicit_witness_generates_auxiliary_sector():
    out = product_scalar((2, 0), (3, 0))
    assert out == (0, 12)
    assert out[1] != 0


def test_resource_is_exactly_multiplicative_on_witness():
    x = (2, 0)
    y = (3, 0)
    xy = product_scalar(x, y)
    assert resource_scalar(xy) == resource_scalar(x) * resource_scalar(y)
    assert resource_scalar(xy) == 144


def test_associativity_exact_integer_example():
    x = [(2, 1), (-1, 4)]
    y = [(-2, 3), (5, -3)]
    z = [(4, -1), (2, 6)]
    assert product(product(x, y), z) == product(x, product(y, z))


def test_visible_sector_is_not_closed():
    out = product(visible_state([1, 2, 0]), visible_state([3, -1, 5]))
    assert any(hidden != 0 for _, hidden in out)


def test_full_audit_has_no_identity_failures():
    result = run_audit()
    assert result["scalar_associativity_failures"] == 0
    assert result["scalar_resource_failures"] == 0
    assert result["vector_associativity_failures"] == 0
    assert result["vector_resource_failures"] == 0
    assert result["hidden_generation_trials"] > 0
    assert result["breakthrough_candidate"] is False
