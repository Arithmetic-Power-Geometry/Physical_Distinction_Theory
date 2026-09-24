"""Cycle 355 regression: information causality does not select local dimension three.

The boolean audit encodes the proved/imported analytic fact used in the cycle:
finite-dimensional complex quantum theory respects information causality in every
finite local dimension. These tests guard the logical dimension-selection result;
they are not a numerical simulation of the IC protocol.
"""


def quantum_ic_compatible(d: int) -> bool:
    return d >= 1


def test_ic_counterfamily_n1_n12():
    assert all(quantum_ic_compatible(d) for d in range(1, 13))


def test_smallest_nontrivial_counterexample_is_two():
    survivors = [d for d in range(2, 13) if quantum_ic_compatible(d)]
    assert min(survivors) == 2


def test_three_is_not_unique():
    survivors = [d for d in range(2, 13) if quantum_ic_compatible(d)]
    assert 2 in survivors
    assert 3 in survivors
    assert 4 in survivors
    assert len(survivors) == 11


def test_smallest_higher_dimension_counterexample_is_four():
    higher = [d for d in range(4, 13) if quantum_ic_compatible(d)]
    assert min(higher) == 4
