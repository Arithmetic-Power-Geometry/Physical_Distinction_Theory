from cycle117_finite_revelation_no_go import product, coarse_window, refined_window, run_audit


def test_smallest_counterexample_leaves_visible_sector_but_is_revealed():
    x = ([2], [0])
    y = ([3], [0])
    xy = product(x, y, lam=1)
    assert xy == ([6], [6])
    assert coarse_window(xy) == [6]
    assert refined_window(xy) == ([6], [6])


def test_associativity_exact_integer_example():
    x = ([2, -1], [3, 4])
    y = ([-2, 5], [1, -3])
    z = ([4, 2], [-1, 6])
    assert product(product(x, y), z) == product(x, product(y, z))


def test_audit_has_no_identity_failures_and_hidden_sector_is_generated():
    result = run_audit()
    assert result["associativity_failures"] == 0
    assert result["coarse_projection_failures"] == 0
    assert result["refined_revelation_failures"] == 0
    assert result["nonzero_hidden_generated"] > 0
    assert result["breakthrough_candidate"] is False
