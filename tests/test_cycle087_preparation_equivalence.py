import numpy as np

from cycle087_preparation_equivalence_no_go import nonlinear_square_on_diagonal, run


def test_qubit_exact_witness():
    p = np.array([0.75, 0.25])
    direct = nonlinear_square_on_diagonal(p)
    assert np.allclose(direct, np.array([0.9, 0.1]))
    assert np.max(np.abs(direct - p)) == 0.15


def test_pure_states_are_fixed():
    for d in range(2, 13):
        for i in range(d):
            p = np.zeros(d)
            p[i] = 1.0
            assert np.allclose(nonlinear_square_on_diagonal(p), p)


def test_all_random_nontrivial_cases_break_preparation_equivalence():
    out = run()
    assert out["nontrivial_cases"] == 360
    assert out["preparation_equivalence_failures"] == 360


def test_dimension_one_is_degenerate():
    out = run()
    row = out["rows"][0]
    assert row["d"] == 1
    assert row["max_preparation_gap"] == 0.0
    assert row["failures"] == 0
