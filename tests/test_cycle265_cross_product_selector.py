"""Cycle 265 regression: classical binary normed vector-cross-product dimensions.

The classification theorem says a nontrivial Euclidean binary vector cross product
exists exactly in dimensions 3 and 7 (0 and 1 admit only trivial cases).
This test prevents accidental promotion of the candidate to an n=3 selector.
"""


def nontrivial_binary_vcp_dimension(n: int) -> bool:
    if n < 1:
        raise ValueError("PDT dimension stress test expects n >= 1")
    return n in (3, 7)


def test_dimensions_1_through_12():
    observed = {n for n in range(1, 13) if nontrivial_binary_vcp_dimension(n)}
    assert observed == {3, 7}


def test_n7_is_decisive_counterexample_to_unique_n3():
    assert nontrivial_binary_vcp_dimension(3)
    assert nontrivial_binary_vcp_dimension(7)
    assert 7 != 3


def test_degenerate_and_nearby_dimensions_rejected():
    for n in (1, 2, 4, 5, 6, 8, 9, 10, 11, 12):
        assert not nontrivial_binary_vcp_dimension(n)
