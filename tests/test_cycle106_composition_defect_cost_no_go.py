import cycle106_composition_defect_cost_no_go as c

def test_exact_witness():
    a=c.exact_octonion_audit()
    assert a["witness_e1_e2_e4"] == [0,0,0,0,0,0,0,2]
    assert a["witness_norm"] == 2.0

def test_alternativity_and_span():
    a=c.exact_octonion_audit()
    assert a["repeated_argument_failures"] == 0
    assert a["alternating_permutation_failures"] == 0
    assert a["associator_span_rank"] == 7
    assert a["nonzero_associators"] == 168

def test_cost_axioms_random():
    r=c.random_cost_axiom_audit(trials=500,seed=106)
    assert r["homogeneity_failures"] == 0
    assert r["subadditivity_failures"] == 0

def test_dimension_no_selector():
    rows=c.synthetic_dimension_audit()
    assert all(not r["nonzero_alternating_trilinear_defect"] for r in rows if r["n"]<3)
    assert all(r["nonzero_alternating_trilinear_defect"] for r in rows if r["n"]>=3)

def test_basis_count():
    assert c.exact_octonion_audit()["ordered_imaginary_basis_triples"] == 343
