"""Exact stress test for PDT-II Cycle 222 control-architecture no-go.

For n>=2, compare a local architecture (coordinatewise unary maps only)
with one that additionally permits a reversible XOR/CNOT-style gate on the
embedded binary face.  The script verifies that the latter reaches a map
that the former cannot generate, while local cardinalities/resource labels
are held fixed.
"""
from itertools import product


def unary_maps(n):
    """All maps [n]->[n], represented as tuples."""
    return list(product(range(n), repeat=n))


def local_product_maps(n):
    """All independent product maps (x,y)->(f(x),g(y))."""
    ums = unary_maps(n)
    maps = set()
    for f in ums:
        for g in ums:
            maps.add(tuple((f[x], g[y]) for x in range(n) for y in range(n)))
    return maps


def embedded_cnot(n):
    """CNOT on {0,1}^2, identity outside that binary face."""
    out = []
    for x in range(n):
        for y in range(n):
            if x < 2 and y < 2:
                out.append((x, x ^ y))
            else:
                out.append((x, y))
    return tuple(out)


def run():
    rows = []
    for n in range(1, 13):
        if n == 1:
            rows.append((n, True, "degenerate"))
            continue
        # Full enumeration is intentionally limited to n<=3; the product
        # family has n^(2n) members. For n>3 use the exact structural test:
        # a product map's second output depends only on y, whereas embedded
        # CNOT has second output 0 at (0,0) and 1 at (1,0).
        if n <= 3:
            absent = embedded_cnot(n) not in local_product_maps(n)
        else:
            gate = embedded_cnot(n)
            idx00 = 0 * n + 0
            idx10 = 1 * n + 0
            absent = gate[idx00][1] != gate[idx10][1]
        assert absent
        rows.append((n, True, "exact obstruction"))
    return rows


if __name__ == "__main__":
    for row in run():
        print(*row, sep=",")
