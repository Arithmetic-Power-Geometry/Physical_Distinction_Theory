import cycle114_clifford_recursive_closure_no_go as c114


def test_basic_euclidean_relations():
    e1, e2 = 1, 2
    assert c114.gp_blades(e1, e1) == (1, 0)
    assert c114.gp_blades(e2, e2) == (1, 0)
    assert c114.gp_blades(e1, e2) == (1, 3)
    assert c114.gp_blades(e2, e1) == (-1, 3)


def test_smallest_same_sector_countermodels():
    assert c114.gp_blades(1, 1)[1] == 0
    assert c114.gp_blades(1, 2)[1].bit_count() == 2


def test_generator_audits_n1_to_n12():
    for n in range(1, 13):
        out = c114.exact_generator_audit(n)
        assert out["generator_relation_failures"] == 0
        assert out["generator_triple_associativity_failures"] == 0
        assert out["clifford_dimension"] == 2 ** n


def test_signed_permutation_automorphism_exact():
    n = 6
    perm = [2, 5, 1, 4, 0, 3]
    signs = [1, -1, 1, -1, -1, 1]
    for a in range(1 << n):
        for b in range(1 << n):
            assert c114.signed_permutation_automorphism_check(a, b, perm, signs)


def test_associativity_all_blades_n4():
    n = 4
    for a in range(1 << n):
        for b in range(1 << n):
            for c in range(1 << n):
                s1, m1 = c114.gp_blades(a, b)
                left = c114.scale_product(s1, m1, 1, c)
                s2, m2 = c114.gp_blades(b, c)
                right = c114.scale_product(1, a, s2, m2)
                assert left == right


def test_randomized_high_dimension_audit():
    out = c114.randomized_audit(trials=1200, seed=114)
    assert out["associativity_failures"] == 0
    assert out["signed_orthogonal_equivariance_failures"] == 0
    assert set(out["dimensions"]) >= set(range(1, 13))
