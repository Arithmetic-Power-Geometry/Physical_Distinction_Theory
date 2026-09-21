from fractions import Fraction


def test_telescoping_revelation_budget():
    # Exact rational scores for one nested refinement path.
    d = [Fraction(0), Fraction(1, 4), Fraction(1, 4), Fraction(3, 4), Fraction(1)]
    delta = [d[k] - d[k - 1] for k in range(1, len(d))]
    assert all(x >= 0 for x in delta)
    assert sum(delta, Fraction(0)) == d[-1] - d[0]
    # Includes a strict but operationally redundant refinement (zero gain).
    assert delta[1] == 0


def test_different_paths_same_endpoint_budget():
    path_a = [Fraction(0), Fraction(1, 4), Fraction(1)]
    path_b = [Fraction(0), Fraction(3, 4), Fraction(1)]
    gain_a = sum((path_a[k] - path_a[k - 1] for k in range(1, len(path_a))), Fraction(0))
    gain_b = sum((path_b[k] - path_b[k - 1] for k in range(1, len(path_b))), Fraction(0))
    assert gain_a == gain_b == Fraction(1)
    assert path_a[1] - path_a[0] != path_b[1] - path_b[0]


def test_dimension_independent_exact_arithmetic():
    # The theorem has no dimension term; repeat representative exact chains n=1..12.
    for n in range(1, 13):
        d = [Fraction(0), Fraction(n, 4 * n), Fraction(3 * n, 4 * n)]
        delta = [d[k] - d[k - 1] for k in range(1, len(d))]
        assert all(x >= 0 for x in delta)
        assert sum(delta, Fraction(0)) == d[-1] - d[0]
