import cycle100_two_generator_coherence_no_go as c100


def test_three_generator_exact_witness():
    w = c100.canonical_three_generator_witness()
    assert w["exact_match"]
    assert w["associator"] == [0, 0, 0, 0, 0, 0, 0, 2]
    assert w["squared_norm"] == 4


def test_all_21_basis_pairs_generate_associative_quaternionic_subalgebras():
    audit = c100.basis_pair_subalgebra_audit()
    assert audit["imaginary_basis_pairs"] == 21
    assert audit["tested_basis_triples_total"] == 21 * 64
    assert audit["associator_violations_total"] == 0
    assert all(r["generated_basis_rank"] == 4 for r in audit["rows"])


def test_random_two_generator_closures_are_four_dimensional():
    audit = c100.random_two_generator_audit(pairs=100, triples_per_pair=4, seed=17)
    assert audit["min_generated_subalgebra_rank"] == 4
    assert audit["max_generated_subalgebra_rank"] == 4


def test_random_two_generator_associators_are_numerically_zero():
    audit = c100.random_two_generator_audit(pairs=100, triples_per_pair=4, seed=18)
    assert audit["violations_gt_1e-9"] == 0
    assert audit["max_associator_residual"] < 1e-9


def test_n7_is_explicit_selector_counterexample():
    rows = c100.dimension_ledger()
    n7 = next(r for r in rows if r["distinction_vector_dimension_n"] == 7)
    assert n7["candidate_n3_selector_survives_this_dimension"] is True
    assert "nonassociative" in n7["audit_status"]


def test_generate_classification_is_conservative():
    out = c100.generate()
    assert out["breakthrough_candidate"] is False
    assert "FALSIFIED" in out["classification"]
    assert "IMPORTED/KNOWN" in out["classification"]
    assert out["surviving_theorem"]["minimal_arity_needed_to_witness_octonionic_nonassociativity"] == 3
