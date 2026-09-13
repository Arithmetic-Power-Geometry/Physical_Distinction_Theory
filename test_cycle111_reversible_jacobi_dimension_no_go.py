import cycle111_reversible_jacobi_dimension_no_go as c


def test_dimension_match_only_three():
    assert c.generator_state_match_solutions(128) == [3]


def test_so2_jacobi_counterexample_to_dimension_selection():
    r = c.exact_basis_audit(2)
    assert r["jacobi_failures"] == 0
    assert not r["dimension_match"]


def test_so3_exact():
    r = c.exact_basis_audit(3)
    assert r["jacobi_failures"] == 0
    assert r["skew_closure_failures"] == 0
    assert r["dimension_match"]


def test_exact_ledger_all_zero_failures():
    rows = [c.exact_basis_audit(n) for n in range(1, 13)]
    assert all(r["jacobi_failures"] == 0 for r in rows)
    assert all(r["skew_closure_failures"] == 0 for r in rows)


def test_random_integer_audit():
    r = c.random_so_audit(trials=400, seed=111)
    assert r["failures"] == 0
    assert r["max_abs_jacobi_entry"] == 0.0
    assert r["max_abs_skew_closure_entry"] == 0.0
