"""Exact checks for Cycle 212 refinement/revelation boundary."""


def signature(obs_family, x):
    return tuple(obs[x] for obs in obs_family)


def equivalent(obs_family, x, y):
    return signature(obs_family, x) == signature(obs_family, y)


def quotient_count(n, obs_family):
    return len({signature(obs_family, x) for x in range(n)})


def base_q(n):
    # Permanent hidden pair 0~1; all other states may be exposed.
    if n == 1:
        return (0,)
    return tuple(0 if x in (0, 1) else x - 1 for x in range(n))


def refinement_family(n, k):
    """Nested observations, all factoring through q; labelled postprocessings grow."""
    q = base_q(n)
    fam = []
    for j in range(1, k + 1):
        fam.append(tuple((q[x], q[x] % (j + 1)) for x in range(n)))
    return fam


def test_refinement_monotonicity_n1_to_n12():
    for n in range(1, 13):
        prev = 0
        for k in range(1, 8):
            fam = refinement_family(n, k)
            count = quotient_count(n, fam)
            assert count >= prev
            prev = count


def test_permanent_hidden_pair_n2_to_n12():
    for n in range(2, 13):
        for k in range(1, 20):
            assert equivalent(refinement_family(n, k), 0, 1)


def test_hidden_pair_can_be_dynamically_distinct():
    # Minimal nontrivial n=3 witness from theorem note.
    F = (0, 1, 0)
    assert F[0] != F[1]
    for k in range(1, 20):
        assert equivalent(refinement_family(3, k), 0, 1)


def test_separation_axiom_repairs_revelation():
    for n in range(1, 13):
        # Identity observation separates every microscopic state.
        identity = tuple(range(n))
        assert quotient_count(n, [identity]) == n
