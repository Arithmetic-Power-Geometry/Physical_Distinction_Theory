import numpy as np

from pdt_scalar_isotropy_no_go import audit, verify_witness, witness


def test_witnesses_real_dimensions_4_through_12_even():
    rows = audit(range(2, 7))
    assert [r["real_dimension"] for r in rows] == [4, 6, 8, 10, 12]
    assert all(r["tpi_fails"] for r in rows)
    assert all(r["same_scalar_distance"] for r in rows)


def test_equal_real_angle_but_different_complex_invariant():
    for m in range(2, 20):
        row = verify_witness(m, a=0.37)
        assert row["same_real_angle"]
        assert row["complex_inner_y_abs"] == 0.0
        assert np.isclose(row["complex_inner_z_abs"], 0.37)
        assert row["tpi_fails"]


def test_edge_validation():
    for bad_m in (0, 1):
        try:
            witness(bad_m)
        except ValueError:
            pass
        else:
            raise AssertionError("m<2 must be rejected")

    for bad_a in (0.0, 1.0, -0.1, 1.1):
        try:
            witness(2, bad_a)
        except ValueError:
            pass
        else:
            raise AssertionError("a outside (0,1) must be rejected")
