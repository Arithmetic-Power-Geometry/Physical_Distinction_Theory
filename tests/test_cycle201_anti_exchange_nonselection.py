"""Cycle 201 exact finite checks for the anti-exchange non-selection witness."""
from itertools import combinations


def powerset(xs):
    xs = tuple(xs)
    for r in range(len(xs) + 1):
        for s in combinations(xs, r):
            yield frozenset(s)


def c0(s):
    return frozenset(s)


def c1(s):
    s = frozenset(s)
    return s | ({"c"} if {"a", "b"} <= s else set())


def check_closure_axioms(cl, universe):
    subs = list(powerset(universe))
    assert cl(frozenset()) == frozenset()
    for a in subs:
        assert a <= cl(a)
        assert cl(cl(a)) == cl(a)
        for b in subs:
            if a <= b:
                assert cl(a) <= cl(b)


def check_anti_exchange(cl, universe):
    for a in powerset(universe):
        if cl(a) != a:
            continue
        outside = set(universe) - set(a)
        for x in outside:
            for y in outside - {x}:
                if x in cl(a | {y}):
                    assert y not in cl(a | {x})


def test_cycle201_smallest_witness():
    u = {"a", "b", "c"}
    for cl in (c0, c1):
        check_closure_axioms(cl, u)
        check_anti_exchange(cl, u)
    assert c0({"a", "b"}) == frozenset({"a", "b"})
    assert c1({"a", "b"}) == frozenset({"a", "b", "c"})


def test_cycle201_embedding_dimensions_3_through_12():
    for n in range(3, 13):
        inert = {f"u{i}" for i in range(n - 3)}
        u = {"a", "b", "c"} | inert
        for cl in (c0, c1):
            check_closure_axioms(cl, u)
            check_anti_exchange(cl, u)
        assert c0({"a", "b"}) != c1({"a", "b"})
