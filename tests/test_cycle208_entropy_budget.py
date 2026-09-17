import math


def entropy(block_sizes):
    n = sum(block_sizes)
    return -sum((s/n)*math.log2(s/n) for s in block_sizes if s)


def induced_map(f, blocks):
    owner = {}
    for j, block in enumerate(blocks):
        for x in block:
            owner[x] = j
    out = []
    for block in blocks:
        images = {owner[f[x]] for x in block}
        assert len(images) == 1
        out.append(next(iter(images)))
    return tuple(out)


def fixed_points(g):
    return sum(i == g[i] for i in range(len(g)))


def witness(n):
    assert 4 <= n <= 12
    # f(0..n-2)=0; f(n-1)=n-1
    f = {x: 0 for x in range(n)}
    f[n-1] = n-1
    # Same (n-1,1) block-size profile, but inequivalent quotient dynamics.
    pi_a = (set(range(n-1)), {n-1})
    pi_b = (set(range(n)) - {n-2}, {n-2})
    return f, pi_a, pi_b


def test_exact_n4_n12_entropy_budget_witness():
    for n in range(4, 13):
        f, a, b = witness(n)
        ga = induced_map(f, a)
        gb = induced_map(f, b)
        assert math.isclose(entropy([len(x) for x in a]), entropy([len(x) for x in b]), rel_tol=0, abs_tol=1e-15)
        assert math.isclose(entropy([len(x) for x in a]), entropy([n-1, 1]), rel_tol=0, abs_tol=1e-15)
        assert fixed_points(ga) == 2
        assert fixed_points(gb) == 1
        assert ga != gb


def test_n4_value():
    assert math.isclose(entropy([3,1]), 0.8112781244591328, rel_tol=0, abs_tol=1e-15)
