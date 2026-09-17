"""Cycle 202 exact tests: generic interaction-map axioms do not select composition."""


def g0(A, B):
    return frozenset()


def g1(A, B):
    A, B = set(A), set(B)
    if ("a" in A and "b" in B) or ("b" in A and "a" in B):
        return frozenset({"c"})
    return frozenset()


def powerset(xs):
    xs = list(xs)
    for mask in range(1 << len(xs)):
        yield frozenset(x for i, x in enumerate(xs) if mask & (1 << i))


def test_smallest_decisive_witness():
    assert g0({"a"}, {"b"}) == frozenset()
    assert g1({"a"}, {"b"}) == frozenset({"c"})


def test_symmetry_and_null_exact_on_core():
    X = {"a", "b", "c"}
    subsets = list(powerset(X))
    for G in (g0, g1):
        for A in subsets:
            assert G(A, frozenset()) == frozenset()
            for B in subsets:
                assert G(A, B) == G(B, A)


def test_monotonicity_exact_on_core():
    X = {"a", "b", "c"}
    subsets = list(powerset(X))
    for G in (g0, g1):
        for A in subsets:
            for Ap in subsets:
                if not A <= Ap:
                    continue
                for B in subsets:
                    for Bp in subsets:
                        if B <= Bp:
                            assert G(A, B) <= G(Ap, Bp)


def test_embedding_n3_through_n12():
    for n in range(3, 13):
        inert = {f"x{i}" for i in range(4, n + 1)}
        X = {"a", "b", "c"} | inert
        assert len(X) == n
        assert g0({"a"}, {"b"}) != g1({"a"}, {"b"})
        # Inert coordinates cannot change the witness.
        assert g1({"a"} | inert, {"b"}) == frozenset({"c"})
