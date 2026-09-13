from cycle116_extension_audit import audit, had, mul, zero


def test_scalar_counterexample_is_associative_and_leaves_sector():
    x = ((2,), zero(1))
    y = ((3,), zero(1))
    z = ((5,), zero(1))
    xy = mul(x, y)
    assert xy[0] == (6,)
    assert xy[1] == (6,)
    assert mul(xy, z) == mul(x, mul(y, z))


def test_visible_projection_exact():
    a = (1, -2, 3)
    b = (4, 5, -1)
    xy = mul((a, zero(3)), (b, zero(3)))
    assert xy[0] == had(a, b)


def test_dimension_stress_audit():
    result = audit()
    assert result["totals"]["trials"] == 2960
    assert result["totals"]["associativity_failures"] == 0
    assert result["totals"]["projection_failures"] == 0
    assert result["totals"]["extra_sector_nonzero"] > 0
    assert result["breakthrough_candidate"] is False
