def tv(p, q):
    return 0.5 * sum(abs(a-b) for a, b in zip(p, q))


def replacement_channel(p, n, target=0):
    out = [0.0] * n
    out[target] = sum(p)
    return out


def test_erasure_counterfamily_n2_to_n12():
    for n in range(2, 13):
        p = [1.0] + [0.0] * (n-1)
        q = [0.0, 1.0] + [0.0] * (n-2)
        assert tv(p, q) == 1.0
        tp = replacement_channel(p, n)
        tq = replacement_channel(q, n)
        assert tv(tp, tq) == 0.0


def test_identity_saturates_not_strict_revelation():
    p = [0.8, 0.2]
    q = [0.3, 0.7]
    assert tv(p, q) == tv(list(p), list(q))
