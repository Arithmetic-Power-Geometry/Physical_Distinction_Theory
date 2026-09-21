"""Exact regression for PDT Cycle 290.

Verifies:
  * ordinary R^3 cross product has zero Jacobiator on basis triples;
  * the standard octonionic R^7 cross product has a nonzero Jacobiator,
    with J(e1,e2,e4) = -3 e7 for the Fano orientation used here.

No numerical tolerance is used: all arithmetic is integer exact.
"""
from itertools import product


def cross3(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


FANO = ((1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6),
        (2, 5, 7), (3, 4, 7), (3, 6, 5))


def basis(n, i):
    return tuple(int(j == i) for j in range(n))


def add(*vs):
    return tuple(sum(xs) for xs in zip(*vs))


def scale(c, v):
    return tuple(c * x for x in v)


def cross7_basis(i, j):
    if i == j:
        return (0,) * 7
    for a, b, c in FANO:
        cyc = ((a, b, c), (b, c, a), (c, a, b))
        if (i, j) in ((u, v) for u, v, _ in cyc):
            for u, v, w in cyc:
                if (i, j) == (u, v):
                    return basis(7, w - 1)
        if (j, i) in ((u, v) for u, v, _ in cyc):
            return scale(-1, cross7_basis(j, i))
    raise AssertionError((i, j))


def cross7(x, y):
    out = (0,) * 7
    for i, xi in enumerate(x, 1):
        for j, yj in enumerate(y, 1):
            if xi and yj:
                out = add(out, scale(xi * yj, cross7_basis(i, j)))
    return out


def jacobi(cross, x, y, z):
    return add(cross(x, cross(y, z)),
               cross(y, cross(z, x)),
               cross(z, cross(x, y)))


def main():
    e3 = [basis(3, i) for i in range(3)]
    for i, j, k in product(range(3), repeat=3):
        assert jacobi(cross3, e3[i], e3[j], e3[k]) == (0, 0, 0)

    e7 = [basis(7, i) for i in range(7)]
    witness = jacobi(cross7, e7[0], e7[1], e7[3])
    assert witness == (0, 0, 0, 0, 0, 0, -3), witness
    print("R3 basis Jacobi: PASS")
    print("R7 witness J(e1,e2,e4):", witness)


if __name__ == "__main__":
    main()
