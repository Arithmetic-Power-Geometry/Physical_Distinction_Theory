"""Cycle 206: extremal strong-lumpability selectors are dynamics-independent.

The singleton partition is always strongly lumpable (finest extreme), while the
one-block partition is always strongly lumpable (coarsest extreme).  Stress-test
n=1..12 on structured and random stochastic kernels.
"""

import numpy as np


def is_lumpable(P, blocks, tol=1e-11):
    P = np.asarray(P, dtype=float)
    for source in blocks:
        for i in source:
            for j in source:
                for target in blocks:
                    lhs = P[i, target].sum()
                    rhs = P[j, target].sum()
                    if abs(lhs - rhs) > tol:
                        return False
    return True


def kernels(n, seed):
    I = np.eye(n)
    yield I

    cycle = np.zeros((n, n))
    for i in range(n):
        cycle[i, (i + 1) % n] = 1.0
    yield cycle

    yield np.full((n, n), 1.0 / n)

    # Symmetric/reversible random walk on a ring with self-loop.
    ring = np.zeros((n, n))
    if n == 1:
        ring[0, 0] = 1.0
    elif n == 2:
        ring[0] = [0.5, 0.5]
        ring[1] = [0.5, 0.5]
    else:
        for i in range(n):
            ring[i, i] = 0.5
            ring[i, (i - 1) % n] += 0.25
            ring[i, (i + 1) % n] += 0.25
    yield ring

    rng = np.random.default_rng(seed)
    for _ in range(25):
        A = rng.random((n, n))
        yield A / A.sum(axis=1, keepdims=True)


def test_extremal_partitions_n1_to_n12():
    for n in range(1, 13):
        finest = [[i] for i in range(n)]
        coarsest = [list(range(n))]
        for P in kernels(n, seed=206000 + n):
            assert np.allclose(P.sum(axis=1), 1.0)
            assert is_lumpable(P, finest)
            assert is_lumpable(P, coarsest)
            assert len(finest) == n
            assert len(coarsest) == 1


def test_nontrivial_gap_for_n_ge_2():
    for n in range(2, 13):
        assert len([[i] for i in range(n)]) > len([list(range(n))])
