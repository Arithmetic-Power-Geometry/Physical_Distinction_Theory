import numpy as np

from cycle125_hurwitz_norm_composition_no_go import (
    ALLOWED_HURWITZ_DIMS,
    basis_audit,
    cd_mul,
    norm2,
    random_norm_audit,
    run_audit,
    theorem_dimension_audit,
    unit,
)


def test_standard_composition_algebras_pass_basis_checks():
    for n in ALLOWED_HURWITZ_DIMS:
        r = basis_audit(n)
        assert r["unit_failures"] == 0
        assert r["basis_norm_failures"] == 0


def test_standard_composition_algebras_pass_random_norm_checks():
    for n in ALLOWED_HURWITZ_DIMS:
        r = random_norm_audit(n, trials=100, seed=9000 + n)
        assert r["failures_at_1e-12"] == 0


def test_n3_is_excluded_by_hurwitz_filter():
    rows = {row["dimension"]: row for row in theorem_dimension_audit()}
    assert rows[3]["compatible_with_positive_definite_unital_bilinear_norm_composition"] is False
    assert rows[1]["compatible_with_positive_definite_unital_bilinear_norm_composition"] is True
    assert rows[2]["compatible_with_positive_definite_unital_bilinear_norm_composition"] is True
    assert rows[4]["compatible_with_positive_definite_unital_bilinear_norm_composition"] is True
    assert rows[8]["compatible_with_positive_definite_unital_bilinear_norm_composition"] is True


def test_unit_and_zero_edges():
    for n in ALLOWED_HURWITZ_DIMS:
        one = unit(n)
        zero = np.zeros(n)
        x = np.arange(1, n + 1, dtype=float)
        assert np.array_equal(cd_mul(one, x), x)
        assert np.array_equal(cd_mul(x, one), x)
        assert np.array_equal(cd_mul(zero, x), zero)
        assert np.array_equal(cd_mul(x, zero), zero)


def test_norm_multiplicativity_examples():
    for n in ALLOWED_HURWITZ_DIMS:
        x = np.arange(1, n + 1, dtype=float)
        y = np.arange(n, 0, -1, dtype=float)
        assert np.isclose(norm2(cd_mul(x, y)), norm2(x) * norm2(y), rtol=1e-12, atol=1e-12)


def test_cycle125_classification_is_not_breakthrough():
    out = run_audit()
    assert out["allowed_dimensions"] == [1, 2, 4, 8]
    assert out["breakthrough_candidate"] is False
    assert "FALSIFIED" in out["status"]
    assert "IMPORTED/KNOWN" in out["status"]
