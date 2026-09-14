from cycle137_full_isotropy_n3_selector import (
    cross3, cross7, exact_7d_failure, audit3, dimension_status, maxabs
)


def test_cross3_basis_orientation():
    assert cross3([1,0,0],[0,1,0]) == [0,0,1]


def test_so3_seeded_equivariance():
    r=audit3(samples=100)
    assert r["failures"] == 0
    assert r["max_abs_residual"] < 1e-10


def test_7d_full_isotropy_fails_exactly():
    w=exact_7d_failure()
    assert w["equivariant"] is False
    assert w["gap_norm2"] == 2.0


def test_dimension_selector_1_to_12():
    survivors=[n for n in range(1,13) if dimension_status(n).startswith("SURVIVES")]
    assert survivors == [3]


def test_7d_cross_product_itself_nontrivial():
    e1=[1,0,0,0,0,0,0]
    e4=[0,0,0,1,0,0,0]
    assert maxabs(cross7(e1,e4)) == 1.0
