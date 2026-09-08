from pdt_generator_economy import (
    audit_dimension,
    audit_range,
    generator_dimension,
    selected_dimensions,
    so_n_is_nonabelian,
)


def test_generator_dimension_formula():
    assert generator_dimension(1) == 0
    assert generator_dimension(2) == 1
    assert generator_dimension(3) == 3
    assert generator_dimension(4) == 6
    assert generator_dimension(12) == 66


def test_low_dimensional_commutation_status():
    assert not so_n_is_nonabelian(1)
    assert not so_n_is_nonabelian(2)
    assert so_n_is_nonabelian(3)
    assert so_n_is_nonabelian(12)


def test_ge_and_ncr_select_only_three_through_1000():
    assert selected_dimensions(1000) == [3]


def test_scan_one_to_twelve():
    rows = audit_range(1, 12)
    selected = [row.n for row in rows if row.selected]
    assert selected == [3]
    assert audit_dimension(2).generator_economy
    assert not audit_dimension(2).noncommuting_reversibility
    assert audit_dimension(3).selected
    assert not audit_dimension(4).generator_economy
