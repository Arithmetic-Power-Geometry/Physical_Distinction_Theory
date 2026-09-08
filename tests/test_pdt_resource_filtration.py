import numpy as np

from pdt_resource_filtration import (
    chain_revelation,
    fibre_diameter,
    is_refinement,
    revelation_increment,
)


def test_refinement_contracts_ambiguity():
    predictions = [
        [1.0, 0.0],
        [0.8, 0.2],
        [0.2, 0.8],
        [0.0, 1.0],
    ]
    coarse = [0, 0, 0, 0]
    middle = [0, 0, 1, 1]
    fine = [0, 1, 2, 3]
    assert is_refinement(coarse, middle)
    assert is_refinement(middle, fine)
    a0 = fibre_diameter(coarse, predictions)
    a1 = fibre_diameter(middle, predictions)
    a2 = fibre_diameter(fine, predictions)
    assert a0 >= a1 >= a2
    assert np.isclose(a2, 0.0)


def test_revelation_telescopes_exactly():
    predictions = [
        [0.95, 0.05],
        [0.75, 0.25],
        [0.25, 0.75],
        [0.05, 0.95],
    ]
    chain = [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 1, 2, 3],
    ]
    drops, total = chain_revelation(chain, predictions)
    assert all(x >= -1e-15 for x in drops)
    assert np.isclose(sum(drops), total)
    assert np.isclose(total, fibre_diameter(chain[0], predictions))


def test_non_refinement_is_rejected():
    coarse = [0, 0, 1, 1]
    crossing = [0, 1, 0, 1]
    assert not is_refinement(coarse, crossing)
