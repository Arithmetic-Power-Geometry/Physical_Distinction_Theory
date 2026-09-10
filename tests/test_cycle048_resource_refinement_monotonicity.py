from fractions import Fraction

from cycle048_resource_refinement_monotonicity import (
    deterministic_merge_first_two,
    exact_random_audit,
    pushforward,
    tv,
    witness,
)


def test_smallest_conservation_counterexample():
    fine, coarse = witness(2)
    assert fine == 1
    assert coarse == 0


def test_nontrivial_three_outcome_counterexample():
    fine, coarse = witness(3)
    assert fine == 1
    assert coarse == 0


def test_exact_data_processing_n1_to_n12():
    for n in range(1, 13):
        violation, _ = exact_random_audit(n, trials=100)
        assert violation == 0


def test_identity_kernel_preserves_tv():
    p = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    q = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]
    K = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    assert tv(pushforward(p, K), pushforward(q, K)) == tv(p, q)


def test_merge_kernel_is_stochastic():
    for n in range(2, 13):
        K = deterministic_merge_first_two(n)
        assert all(sum(row) == 1 for row in K)
        assert all(all(x >= 0 for x in row) for row in K)


def test_revelation_increment_bound_on_witnesses():
    for n in range(1, 13):
        fine, coarse = witness(n)
        delta = fine - coarse
        assert 0 <= delta <= 1 - coarse
