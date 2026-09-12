import numpy as np
import cycle107_sharp_associator_resource_bound as c107


def test_exact_octonion_sharpness():
    out=c107.exact_basis_audit()
    assert out["nonzero_associators"]==168
    assert out["saturating_triples"]==168
    assert out["maximum_normalized_defect"]==2.0
    assert out["witness_e1_e2_e4"]==[0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0]


def test_witness_saturates_factor_two():
    E=np.eye(8)
    assert abs(c107.normalized_defect(E[1],E[2],E[4])-2.0)<1e-12


def test_zero_input_is_degenerate_safe():
    E=np.eye(8)
    z=np.zeros(8)
    assert c107.normalized_defect(z,E[1],E[2])==0.0


def test_random_octonions_respect_bound():
    out=c107.random_octonion_audit(trials=800,seed=107)
    assert out["violations_of_universal_bound"]==0
    assert out["maximum_normalized_defect"]<=2.0+1e-10


def test_dimension_ledger_is_explicitly_nonselective():
    rows=c107.dimension_ledger()
    assert [r["n"] for r in rows[:12]]==list(range(1,13))
    assert {16,24,32,48,64,96,128}.issubset({r["n"] for r in rows})
    assert all(r["bound_constant"]==2.0 for r in rows)
    assert not any(r["dimension_selective"] for r in rows)
