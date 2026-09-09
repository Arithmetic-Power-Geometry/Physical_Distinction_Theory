import math

from pdt_transitive_norm_euclideanization import (
    audit,
    equal_coordinate_euclidean_radius,
    euclidean_only_among_lp,
    lp_anisotropy_witness,
)


def test_p2_is_exactly_isotropic_for_dimensions_2_to_100():
    for n in range(2, 101):
        assert equal_coordinate_euclidean_radius(n, 2.0) == 1.0
        assert euclidean_only_among_lp(n, 2.0)


def test_non_euclidean_lp_witnesses_fail_for_dimensions_2_to_100():
    for n in range(2, 101):
        for p in (1.0, 1.5, 3.0, 4.0, 10.0):
            assert lp_anisotropy_witness(n, p) > 1e-12
            assert not euclidean_only_among_lp(n, p)


def test_dimension_12_stress_gap_is_large_for_p10():
    assert lp_anisotropy_witness(12, 10.0) > 1.7


def test_audit_has_expected_size_and_only_p2_passes():
    rows = audit(12)
    assert len(rows) == 66
    assert all((r["p"] == 2.0) == r["passes_two_point_transitivity_witness"] for r in rows)
