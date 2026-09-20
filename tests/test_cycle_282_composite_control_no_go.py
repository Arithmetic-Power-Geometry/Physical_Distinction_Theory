"""Cycle 282 regression: identical local controls do not fix composite controllability.

No external dependencies. Pauli strings are represented modulo phase; Lie closure of
Pauli generators corresponds to closure under commutators, where two nonidentity
Pauli strings generate their product iff they anticommute.
"""

PAULI = ("I", "X", "Y", "Z")


def anticommute(a, b):
    n = 0
    for x, y in zip(a, b):
        if x != "I" and y != "I" and x != y:
            n += 1
    return n % 2 == 1


def mul_char(x, y):
    if x == "I": return y
    if y == "I": return x
    if x == y: return "I"
    return ({"X", "Y", "Z"} - {x, y}).pop()


def product(a, b):
    return "".join(mul_char(x, y) for x, y in zip(a, b))


def lie_closure(gens):
    s = set(gens)
    changed = True
    while changed:
        changed = False
        cur = list(s)
        for i, a in enumerate(cur):
            for b in cur[i + 1:]:
                if anticommute(a, b):
                    c = product(a, b)
                    if c != "II" and c not in s:
                        s.add(c)
                        changed = True
    return s


def test_same_locals_different_joint_closure():
    local = {"XI", "YI", "ZI", "IX", "IY", "IZ"}
    c0 = lie_closure(local)
    c1 = lie_closure(local | {"ZZ"})
    assert c0 == local
    assert len(c0) == 6
    assert len(c1) == 15
    assert c1 == {a + b for a in PAULI for b in PAULI if a + b != "II"}
    assert "ZZ" not in c0 and "ZZ" in c1


def test_smallest_active_dimension_is_two_by_two():
    # One-dimensional factors have no nontrivial traceless local/control algebra;
    # the first entangling interaction witness therefore needs 2 x 2 active levels.
    assert len(lie_closure({"XI", "YI", "ZI", "IX", "IY", "IZ"})) == 6
