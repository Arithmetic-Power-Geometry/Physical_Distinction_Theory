from pdt_local_tomography_composite_no_go import (
    audit_row,
    chsh_pr,
    deterministic_local_chsh_max,
    normalization_ok,
    nonsignalling_ok,
    pr_probability,
)


def test_smallest_decisive_witness_is_two_settings():
    assert chsh_pr(1) is None
    assert chsh_pr(2) == 4
    assert deterministic_local_chsh_max() == 2


def test_exact_probability_constraints_through_12_settings():
    for n in range(1, 13):
        assert normalization_ok(n)
        assert nonsignalling_ok(n)
        for x in range(n):
            for y in range(n):
                for a in (0, 1):
                    for b in (0, 1):
                        p = pr_probability(n, x, y, a, b)
                        assert 0 <= p <= 1


def test_same_locally_tomographic_dimension_but_distinct_composites():
    for n in range(2, 13):
        row = audit_row(n)
        assert row["locally_tomographic_composite_dim"] == (n + 1) ** 2
        assert row["minimal_local_CHSH_bound"] == 2
        assert row["maximal_embedded_PR_CHSH"] == 4
        assert row["minimal_maximal_separated"] is True
