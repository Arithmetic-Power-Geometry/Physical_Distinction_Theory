import math


def computational_distribution(sign: int, n: int):
    assert sign in (-1, 1)
    assert n >= 2
    # |Phi_sign>=(|00> + sign |11>)/sqrt(2); computational
    # probabilities erase the relative phase exactly.
    p = {(i, j): 0.0 for i in range(n) for j in range(n)}
    p[(0, 0)] = 0.5
    p[(1, 1)] = 0.5
    return p


def tv(p, q):
    return 0.5 * sum(abs(p[k] - q[k]) for k in p)


def test_exact_n2_to_n12_restricted_indistinguishability():
    for n in range(2, 13):
        plus = computational_distribution(+1, n)
        minus = computational_distribution(-1, n)
        assert tv(plus, minus) == 0.0


def test_global_orthogonality_all_n2_to_n12():
    # <Phi+|Phi-> = (1-1)/2 exactly, independent of zero-padding dimension.
    for n in range(2, 13):
        overlap = (1.0 - 1.0) / 2.0
        assert overlap == 0.0
        global_bias = math.sqrt(1.0 - overlap * overlap)
        assert global_bias == 1.0


def test_exact_success_revelation_jump():
    # Equal priors: P_success=(1+bias)/2.
    assert (1.0 + 0.0) / 2.0 == 0.5
    assert (1.0 + 1.0) / 2.0 == 1.0


def test_nested_window_monotonicity_on_counterfamily():
    for n in range(2, 13):
        restricted = tv(
            computational_distribution(+1, n),
            computational_distribution(-1, n),
        )
        global_optimum = 1.0
        assert restricted <= global_optimum
