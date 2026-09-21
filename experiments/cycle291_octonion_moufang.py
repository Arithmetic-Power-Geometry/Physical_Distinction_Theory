"""Exact PDT Cycle 291 regression.

Checks on the real octonions using integer arithmetic:
  * the Moufang identity (xy)(zx) = x((yz)x) on all signed basis triples;
  * a nonzero associator witness, showing Moufang != associativity;
  * a nonzero Jacobiator for imaginary-octonion commutator/cross-product structure.

No floating-point tolerance is used.
"""
from itertools import product

# Fano orientation kept consistent with Cycle 290.
FANO = ((1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6),
        (2, 5, 7), (3, 4, 7), (3, 6, 5))


def basis(i):
    v = [0] * 8
    v[i] = 1
    return tuple(v)


def add(*vs):
    return tuple(sum(xs) for xs in zip(*vs))


def scale(c, v):
    return tuple(c * x for x in v)


def mul_basis(i, j):
    # e0 = 1; e_i^2 = -1 for imaginary units.
    if i == 0:
        return basis(j)
    if j == 0:
        return basis(i)
    if i == j:
        return scale(-1, basis(0))
    for a, b, c in FANO:
        cyc = ((a, b, c), (b, c, a), (c, a, b))
        for u, v, w in cyc:
            if (i, j) == (u, v):
                return basis(w)
            if (i, j) == (v, u):
                return scale(-1, basis(w))
    raise AssertionError((i, j))


def mul(x, y):
    out = (0,) * 8
    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            if xi and yj:
                out = add(out, scale(xi * yj, mul_basis(i, j)))
    return out


def assoc(x, y, z):
    return add(mul(mul(x, y), z), scale(-1, mul(x, mul(y, z))))


def comm(x, y):
    return add(mul(x, y), scale(-1, mul(y, x)))


def jacobi(x, y, z):
    return add(comm(x, comm(y, z)),
               comm(y, comm(z, x)),
               comm(z, comm(x, y)))


def main():
    signed_basis = [scale(s, basis(i)) for i in range(8) for s in (-1, 1)]

    # Exhaustive 16^3 exact check of one standard Moufang identity.
    for x, y, z in product(signed_basis, repeat=3):
        lhs = mul(mul(x, y), mul(z, x))
        rhs = mul(x, mul(mul(y, z), x))
        assert lhs == rhs, (x, y, z, lhs, rhs)

    e1, e2, e4 = basis(1), basis(2), basis(4)
    a = assoc(e1, e2, e4)
    j = jacobi(e1, e2, e4)
    assert any(a), a
    assert any(j), j

    print("Moufang signed-basis triples: PASS", len(signed_basis) ** 3)
    print("Associator witness [e1,e2,e4]:", a)
    print("Commutator Jacobiator witness:", j)


if __name__ == "__main__":
    main()
