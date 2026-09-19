"""Cycle 259: exact dimension stress test for bit-symmetry as an n=3 selector.

For each n>=2 construct two logical bits (ordered pairs of orthogonal pure
states) in C^n and an explicit permutation unitary mapping one bit to the
other.  This is an exact witness: no floating-point inference is used.
"""
from fractions import Fraction


def permutation_matrix(n, perm):
    return [[Fraction(int(perm[j] == i), 1) for j in range(n)] for i in range(n)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(x) for x in zip(*a)]


def identity(n):
    return [[Fraction(int(i == j), 1) for j in range(n)] for i in range(n)]


def check_n(n):
    if n == 1:
        return {"n": 1, "nontrivial_logical_bit": False, "classification": "degenerate"}
    # Map ordered bit (e0,e1) to (e1,e0); for n>2 fix all other basis rays.
    perm = list(range(n))
    perm[0], perm[1] = 1, 0
    u = permutation_matrix(n, perm)
    orthogonal = matmul(transpose(u), u) == identity(n)
    maps_bit = u[1][0] == 1 and u[0][1] == 1
    return {"n": n, "nontrivial_logical_bit": True, "reversible_map_exists": orthogonal and maps_bit, "classification": "survives" if orthogonal and maps_bit else "fails"}


if __name__ == "__main__":
    rows = [check_n(n) for n in range(1, 13)]
    assert rows[0]["classification"] == "degenerate"
    assert all(r["reversible_map_exists"] for r in rows[1:])
    for row in rows:
        print(row)
