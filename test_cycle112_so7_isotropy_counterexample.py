import numpy as np
import cycle112_so7_isotropy_counterexample as c112


def test_octonion_basis_anticommutativity():
    for i in range(7):
        assert np.allclose(c112.cross7_basis(i, i), np.zeros(7))
        for j in range(7):
            assert np.allclose(c112.cross7_basis(i, j), -c112.cross7_basis(j, i))


def test_reference_fano_product():
    assert np.allclose(c112.cross7_basis(0, 1), np.array([0, 0, 1, 0, 0, 0, 0], dtype=float))
    assert np.allclose(c112.cross7_basis(1, 0), np.array([0, 0, -1, 0, 0, 0, 0], dtype=float))


def test_explicit_rotation_is_in_so7():
    w = c112.explicit_so7_witness()
    assert w["is_SO7"]
    assert w["det_R"] == 1.0
    assert w["orthogonality_residual"] == 0.0


def test_explicit_rotation_breaks_cross_covariance():
    w = c112.explicit_so7_witness()
    assert abs(w["covariance_residual"] - 2.0) < 1e-12


def test_dimension_stress_ledger():
    rows = c112.dimension_stress_ledger()
    assert [r["n"] for r in rows if r["full_SO_n_vector_cross_product_candidate"]] == [3]
    assert set(c112.DIMS) >= set(range(1, 13))
    assert max(c112.DIMS) >= 128


def test_no_breakthrough_claim():
    out = c112.generate()
    assert out["breakthrough_candidate"] is False
    assert "FALSIFIED" in out["classification"]
    assert "IMPORTED/KNOWN" in out["classification"]
