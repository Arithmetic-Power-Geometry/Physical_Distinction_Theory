"""Cycle 204: exact tests for non-unique dynamically closed resource quotients."""
from fractions import Fraction


def kernel(a):
    states = range(4)
    P = [[Fraction(0) for _ in states] for _ in states]
    for x in states:
        P[x][x] += 1 - 2*a
        P[x][x ^ 1] += a
        P[x][x ^ 2] += a
    return P


def is_lumpable(P, blocks):
    for source in blocks:
        for target in blocks:
            vals = {sum(P[x][u] for u in target) for x in source}
            if len(vals) != 1:
                return False
    return True


def test_two_inequivalent_quotients_same_nondegenerate_microdynamics():
    P = kernel(Fraction(1, 4))
    parity = [{0, 3}, {1, 2}]
    weight = [{0}, {1, 2}, {3}]
    assert is_lumpable(P, parity)
    assert is_lumpable(P, weight)
    assert len(parity) != len(weight)


def test_edge_parameters():
    parity = [{0, 3}, {1, 2}]
    weight = [{0}, {1, 2}, {3}]
    for a in (Fraction(0), Fraction(1, 8), Fraction(1, 2)):
        P = kernel(a)
        assert is_lumpable(P, parity)
        assert is_lumpable(P, weight)
        assert all(sum(row) == 1 for row in P)


def test_identity_dynamics_all_partitions_lumpable_n1_to_n12():
    # Degenerate edge case: identity dynamics supplies no quotient selection.
    for n in range(1, 13):
        P = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
        singleton = [{i} for i in range(n)]
        universal = [set(range(n))]
        assert is_lumpable(P, singleton)
        assert is_lumpable(P, universal)


def test_nondegenerate_witness_embeds_n4_to_n12():
    # Four-state witness plus absorbing singleton states. Both quotient families
    # retain the added states as singleton blocks.
    a = Fraction(1, 4)
    base = kernel(a)
    for n in range(4, 13):
        P = [[Fraction(0) for _ in range(n)] for _ in range(n)]
        for i in range(4):
            for j in range(4):
                P[i][j] = base[i][j]
        for i in range(4, n):
            P[i][i] = 1
        tail = [{i} for i in range(4, n)]
        parity = [{0, 3}, {1, 2}] + tail
        weight = [{0}, {1, 2}, {3}] + tail
        assert is_lumpable(P, parity)
        assert is_lumpable(P, weight)
        assert len(parity) != len(weight)
