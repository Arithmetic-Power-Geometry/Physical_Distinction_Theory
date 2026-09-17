"""Cycle 207 exact witness: scalar block budget does not select a unique quotient."""


def induced_map(f, partition):
    block_of = {}
    for j, block in enumerate(partition):
        for x in block:
            block_of[x] = j
    out = []
    for block in partition:
        targets = {block_of[f[x]] for x in block}
        assert len(targets) == 1, "partition is not dynamically admissible"
        out.append(next(iter(targets)))
    return tuple(out)


def fixed_points(qmap):
    return sum(i == qmap[i] for i in range(len(qmap)))


def witness(n):
    assert n >= 4
    # Core microscopic map; added dimensions are fixed points.
    f = {0: 0, 1: 0, 2: 2, 3: 2}
    for x in range(4, n):
        f[x] = x

    extra = set(range(4, n))
    # Put added fixed states in their own shared third block would change budget.
    # Instead map them to 0 so the two-block embedding remains admissible.
    for x in extra:
        f[x] = 0

    A = (frozenset({0, 1}) | extra, frozenset({2, 3}))
    B = (frozenset({0, 1, 2}) | extra, frozenset({3}))
    qa = induced_map(f, A)
    qb = induced_map(f, B)
    return A, B, qa, qb


def test_core_witness():
    A, B, qa, qb = witness(4)
    assert len(A) == len(B) == 2
    assert qa == (0, 1)       # identity quotient
    assert qb == (0, 0)       # constant quotient
    assert fixed_points(qa) == 2
    assert fixed_points(qb) == 1


def test_exact_embeddings_n4_to_n12():
    for n in range(4, 13):
        A, B, qa, qb = witness(n)
        assert len(A) == len(B) == 2
        assert qa == (0, 1)
        assert qb == (0, 0)
        # Different fixed-point counts prove non-isomorphism under quotient relabelling.
        assert fixed_points(qa) != fixed_points(qb)
