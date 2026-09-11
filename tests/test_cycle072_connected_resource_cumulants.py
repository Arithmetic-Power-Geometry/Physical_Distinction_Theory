from fractions import Fraction

from cycle072_connected_resource_cumulants import (
    C_VALUES,
    connected_cumulants,
    exact_independent_cut_audit,
    ghz_coherence_witness,
    reconstruct_moments,
)


def test_partition_cumulant_roundtrip_exact():
    moments = {
        frozenset({0}): Fraction(1, 3),
        frozenset({1}): Fraction(-2, 5),
        frozenset({2}): Fraction(3, 7),
        frozenset({0, 1}): Fraction(4, 9),
        frozenset({0, 2}): Fraction(-1, 8),
        frozenset({1, 2}): Fraction(2, 11),
        frozenset({0, 1, 2}): Fraction(5, 13),
    }
    kappa = connected_cumulants(moments, range(3))
    assert reconstruct_moments(kappa, range(3)) == moments


def test_independent_cut_connected_sectors_vanish_exactly():
    audit = exact_independent_cut_audit(trials=20, max_parties=5)
    assert audit["cross_cut_connected_sectors_checked"] > 0
    assert audit["cross_cut_failures"] == 0
    assert audit["reconstruction_failures"] == 0


def test_ghz_family_has_hidden_triad_sector():
    for d in range(2, 13):
        rows = [ghz_coherence_witness(d, c) for c in C_VALUES]
        assert all(r["proper_marginal_c_dependence"] == "0" for r in rows)
        assert rows[0]["connected_kappa_123_X"] == "-1"
        assert rows[-1]["connected_kappa_123_X"] == "1"


def test_dimension_one_is_explicitly_degenerate():
    row = ghz_coherence_witness(1, Fraction(1))
    assert row["classification"] == "DEGENERATE"
