import cycle109_jacobi_crossproduct_selector as c


def test_3d_exact_jacobi():
    a=c.exact_basis_audit(3)
    assert a["jacobi_failures"]==0


def test_7d_exact_jacobi_fails():
    a=c.exact_basis_audit(7)
    assert a["jacobi_failures"]==168
    assert a["first_failure"]["triple"]==[1,2,4]
    assert a["first_failure"]["jacobi"]==[0,0,0,0,0,0,-3]


def test_norm_cross_identity_basis():
    assert c.norm_cross_audit(3)["norm_identity_failures"]==0
    assert c.norm_cross_audit(7)["norm_identity_failures"]==0


def test_dimension_selector():
    rows={r["n"]:r for r in c.dimension_selector_ledger()}
    assert rows[3]["survives_cross_product_plus_jacobi"]
    assert not rows[7]["survives_cross_product_plus_jacobi"]


def test_random_boundary():
    out=c.random_jacobi_audit(trials=100,seed=109)
    assert out["3"]["nonzero_jacobi_gt_1e-9"]==0
    assert out["7"]["nonzero_jacobi_gt_1e-9"]>0
