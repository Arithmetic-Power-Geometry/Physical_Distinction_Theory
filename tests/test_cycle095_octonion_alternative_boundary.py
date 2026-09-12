import importlib.util
from pathlib import Path
import numpy as np

MODULE_PATH = Path(__file__).resolve().parents[1] / "cycle095_octonion_alternative_boundary.py"
spec = importlib.util.spec_from_file_location("cycle095", MODULE_PATH)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def test_exact_nonassociativity_witness():
    w = m.basis_nonassociativity_witness()
    assert w["exact_integer_match"]
    assert w["norm"] == 2.0


def test_exact_basis_alternativity():
    a = m.basis_alternativity_audit()
    assert a["violations"] == []
    assert a["max_left_residual"] == 0.0
    assert a["max_right_residual"] == 0.0
    assert a["max_flexible_residual"] == 0.0


def test_octonion_norm_composition_basis():
    e = np.eye(8)
    for i in range(8):
        for j in range(8):
            p = m.cd_mul(e[i], e[j])
            assert np.dot(p, p) == 1.0


def test_hurwitz_dimension_ledger():
    rows = m.dimension_ledger()
    allowed = {r["distinction_vector_dimension_n"] for r in rows
               if r["hurwitz_normed_division_dimension_allowed"]}
    assert allowed == {1, 3, 7}


def test_random_regression_tight():
    r = m.random_octonion_audit(trials=200, seed=9511)
    assert r["max_norm_multiplicativity_residual"] < 1e-12
    assert r["max_left_alternativity_residual"] < 1e-12
    assert r["max_right_alternativity_residual"] < 1e-12
    assert r["max_flexible_residual"] < 1e-12
    assert r["generic_nonassociative_cases_gt_1e-10"] > 0
