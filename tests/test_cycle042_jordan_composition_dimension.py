from pdt_cycle042_jordan_composition_dimension import (
    audit_associative_division_algebras,
    dimension_scan,
    equality_residual,
    hermitian_dimension,
)


def test_hermitian_dimensions():
    assert hermitian_dimension(2, 1) == 3
    assert hermitian_dimension(2, 2) == 4
    assert hermitian_dimension(2, 4) == 6
    assert hermitian_dimension(4, 1) == 10
    assert hermitian_dimension(4, 2) == 16
    assert hermitian_dimension(4, 4) == 28


def test_exact_filter_selects_complex_case():
    rows = audit_associative_division_algebras()
    passing = [r for r in rows if r.locally_tomographic]
    assert len(passing) == 1
    assert passing[0].algebra == "C"
    assert passing[0].d == 2
    assert passing[0].bloch_dimension == 3


def test_residual_factorization_for_many_positive_d():
    for d in range(1, 101):
        assert equality_residual(d) == d * (2 - d)
        assert (equality_residual(d) == 0) == (d == 2)


def test_dimension_scan_one_to_twelve():
    rows = dimension_scan(12)
    assert [r["n"] for r in rows] == list(range(1, 13))
    selected = [r["n"] for r in rows if r["selected_by_assumptions"]]
    assert selected == [3]
    n9 = next(r for r in rows if r["n"] == 9)
    assert n9["route_applicable"] is False
    assert "H4(O)" in n9["status"]
