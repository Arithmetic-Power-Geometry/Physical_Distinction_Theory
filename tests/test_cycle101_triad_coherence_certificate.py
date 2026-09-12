import importlib.util
from pathlib import Path

import numpy as np

MODULE = Path(__file__).resolve().parents[1] / "cycle101_triad_coherence_certificate.py"
spec = importlib.util.spec_from_file_location("cycle101", MODULE)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_octonion_triad_count_and_boundary():
    audit = m.octonion_unordered_triad_audit()
    assert audit["unordered_imaginary_basis_triads"] == 35
    assert audit["nonzero_associator_triads"] == 28
    assert audit["zero_associator_triads"] == 7
    assert audit["all_nonzero_squared_norms"] == [4]


def test_canonical_witness():
    e = np.eye(8, dtype=int)
    got = m.associator(e[1], e[2], e[4])
    expected = np.zeros(8, dtype=int)
    expected[7] = 2
    assert np.array_equal(got, expected)


def test_associator_alternates_exactly_on_basis():
    audit = m.permutation_alternation_audit()
    assert audit["permutation_checks"] == 210
    assert audit["violations"] == 0


def test_alternative_repeated_argument_identities():
    assert m.repeated_argument_audit()["violations"] == 0


def test_random_trilinear_reconstruction():
    audit = m.random_trilinear_reconstruction_audit(trials=200, seed=123)
    assert audit["violations_gt_1e-9"] == 0


def test_dimension_ledger():
    rows = m.dimension_certificate_ledger()
    lookup = {r["distinction_vector_dimension_n"]: r["unordered_primitive_triad_checks"] for r in rows}
    assert lookup[1] == 0
    assert lookup[2] == 0
    assert lookup[3] == 1
    assert lookup[7] == 35
    assert lookup[12] == 220
