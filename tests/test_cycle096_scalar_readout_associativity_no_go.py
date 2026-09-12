import numpy as np

from cycle095_octonion_alternative_boundary import associator
from cycle096_scalar_readout_associativity_no_go import exact_basis_audit, random_audit


def test_exact_basis_scalar_associator_vanishes():
    audit = exact_basis_audit()
    assert audit["basis_triples"] == 512
    assert audit["max_abs_scalar_associator"] == 0.0


def test_exact_basis_has_hidden_nonassociativity():
    audit = exact_basis_audit()
    assert audit["nonzero_full_associator_basis_triples"] == 168
    assert audit["max_full_associator_norm"] == 2.0


def test_decisive_witness_is_scalar_invisible():
    e = np.eye(8)
    a = associator(e[1], e[2], e[4])
    expected = np.zeros(8)
    expected[7] = 2.0
    assert np.array_equal(a, expected)
    assert a[0] == 0.0


def test_random_scalar_projection_is_numerically_zero():
    audit = random_audit(trials=500, seed=9607)
    assert audit["max_abs_scalar_associator"] < 1e-12
    assert audit["nonzero_full_associator_cases_gt_1e-10"] == 500


def test_random_full_associator_remains_visible():
    audit = random_audit(trials=500, seed=9607)
    assert audit["max_full_associator_norm"] > 0.1
