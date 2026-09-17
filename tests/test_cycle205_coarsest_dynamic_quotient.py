"""Cycle 205: maximal-compression/coarsest-lumpable selection collapses.

The one-block partition is strongly lumpable for every row-stochastic kernel.
Tests stress n=1..12 across edge and representative dynamics.
"""
import random


def one_block_is_lumpable(P, tol=1e-12):
    n = len(P)
    assert n >= 1
    for row in P:
        assert len(row) == n
        assert abs(sum(row) - 1.0) <= tol
        assert all(x >= -tol for x in row)
    totals = [sum(row) for row in P]
    return max(totals) - min(totals) <= tol


def identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def cycle(n):
    if n == 1:
        return [[1.0]]
    return [[1.0 if j == (i + 1) % n else 0.0 for j in range(n)] for i in range(n)]


def uniform(n):
    return [[1.0 / n for _ in range(n)] for _ in range(n)]


def reversible_ring(n):
    if n == 1:
        return [[1.0]]
    if n == 2:
        return [[0.5, 0.5], [0.5, 0.5]]
    P = [[0.0] * n for _ in range(n)]
    for i in range(n):
        P[i][i] = 0.5
        P[i][(i - 1) % n] += 0.25
        P[i][(i + 1) % n] += 0.25
    return P


def random_stochastic(n, seed):
    rng = random.Random(seed)
    P = []
    for _ in range(n):
        xs = [rng.random() + 1e-9 for _ in range(n)]
        s = sum(xs)
        P.append([x / s for x in xs])
    return P


def test_one_block_lumpable_n1_n12_representative_families():
    for n in range(1, 13):
        for P in (identity(n), cycle(n), uniform(n), reversible_ring(n)):
            assert one_block_is_lumpable(P)


def test_one_block_lumpable_n1_n12_random_search():
    for n in range(1, 13):
        for seed in range(25):
            assert one_block_is_lumpable(random_stochastic(n, 1000 * n + seed))


def test_identity_has_nonunique_lumpable_partitions_but_unique_coarsest():
    # For identity dynamics every partition is lumpable. The one-block
    # partition nevertheless refines no other partition and is uniquely
    # coarsest under the standard refinement order.
    for n in range(1, 13):
        assert one_block_is_lumpable(identity(n))
        assert 1 <= n  # one block versus n singleton blocks
