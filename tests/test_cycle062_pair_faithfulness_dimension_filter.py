from cycle062_pair_faithfulness_dimension_filter import (
    ncr,
    pair_stabilizer_dimension,
    pif,
    selected,
)


def test_exact_dimensions_1_to_12():
    winners = [n for n in range(2, 13) if selected(n)]
    assert winners == [3]


def test_smallest_decisive_failure_above_three():
    assert pair_stabilizer_dimension(4) == 1
    assert ncr(4)
    assert not pif(4)
    assert not selected(4)


def test_higher_dimensions_remain_excluded():
    for n in [16, 24, 32, 48, 64, 96, 128, 256]:
        assert pair_stabilizer_dimension(n) > 0
        assert ncr(n)
        assert not pif(n)
        assert not selected(n)


def test_n2_excluded_by_noncommutativity():
    assert pair_stabilizer_dimension(2) == 0
    assert pif(2)
    assert not ncr(2)
    assert not selected(2)
