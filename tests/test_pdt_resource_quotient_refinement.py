import numpy as np
import pytest

from pdt_resource_quotient_refinement import (
    chain_revelation_dimensions,
    coordinate_chain,
    is_refinement,
    nullity,
    quotient_dimension,
    refinement_audit,
)


def test_coordinate_chains_n1_to_n12():
    for n in range(1, 13):
        chain = coordinate_chain(n)
        assert len(chain) == n + 1
        for k, a in enumerate(chain):
            assert quotient_dimension(a) == k
            assert nullity(a) == n - k
        assert chain_revelation_dimensions(chain) == [1] * n


def test_random_nested_row_spaces_n1_to_n12():
    for n in range(1, 13):
        rng = np.random.default_rng(1000 + n)
        a = rng.normal(size=(n, n))
        for k in range(n):
            coarse = a[:k, :]
            fine = a[: k + 1, :]
            audit = refinement_audit(coarse, fine)
            assert audit["is_refinement"]
            assert audit["quotient_monotone"]
            assert audit["nullity_antitone"]
            assert audit["revealed_dimensions"] >= 0


def test_degenerate_redundant_test_has_zero_gain():
    coarse = np.array([[1.0, 0.0, 0.0]])
    fine = np.array([[1.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
    audit = refinement_audit(coarse, fine)
    assert audit["is_refinement"]
    assert audit["revealed_dimensions"] == 0
    assert audit["fine_quotient_dim"] == audit["coarse_quotient_dim"] == 1


def test_nonrefining_crossed_resources_rejected():
    coarse = np.array([[1.0, 0.0]])
    fine = np.array([[0.0, 1.0]])
    assert not is_refinement(coarse, fine)
    audit = refinement_audit(coarse, fine)
    assert audit["quotient_monotone"] is None
    assert audit["nullity_antitone"] is None
    assert audit["revealed_dimensions"] is None


def test_telescoping_dimension_gain():
    for n in range(1, 13):
        chain = coordinate_chain(n)
        gains = chain_revelation_dimensions(chain)
        assert sum(gains) == quotient_dimension(chain[-1]) - quotient_dimension(chain[0])


def test_invalid_dimension():
    with pytest.raises(ValueError):
        coordinate_chain(0)
