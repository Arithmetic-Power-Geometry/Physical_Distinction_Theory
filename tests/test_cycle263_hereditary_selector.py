from fractions import Fraction

from pdt.cycle263_hereditary_selector import exact_embedding_regression


def test_exact_embedding_n1_to_n12():
    base, rows = exact_embedding_regression(12)
    assert base == Fraction(10, 21)
    assert rows[0] == (1, "DEGENERATE", None)
    assert len(rows) == 12
    for n, status, value in rows[1:]:
        assert 2 <= n <= 12
        assert status == "PRESERVED"
        assert value == base
