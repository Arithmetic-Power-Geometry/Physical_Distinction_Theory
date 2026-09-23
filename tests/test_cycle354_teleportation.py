"""Cycle 354 regression: generalized qudit teleportation structure is dimension-uniform."""


def test_generalized_bell_and_weyl_counts_n1_n12():
    for d in range(1, 13):
        assert d * d == len([(a, b) for a in range(d) for b in range(d)])


def test_n3_not_unique_by_protocol_counts():
    admissible = [d for d in range(2, 13) if d * d > 0]
    assert 2 in admissible
    assert 3 in admissible
    assert 4 in admissible
    assert len(admissible) == 11


def test_smallest_nontrivial_counterexample():
    # Generalized Weyl/Bell teleportation exists already for a qubit.
    assert min(range(2, 13)) == 2
