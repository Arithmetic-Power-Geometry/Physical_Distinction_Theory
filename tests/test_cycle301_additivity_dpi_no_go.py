import math


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def renyi_half(p, q):
    return -2.0 * math.log(sum(math.sqrt(pi * qi) for pi, qi in zip(p, q)))


def tensor(p, r):
    return [x * y for x in p for y in r]


def binary_channel(p, a, b):
    # T(0|0)=a, T(0|1)=b
    return [a * p[0] + b * p[1], (1-a) * p[0] + (1-b) * p[1]]


def test_distinct_additive_selectors_binary():
    p = [0.9, 0.1]
    q = [0.6, 0.4]
    assert abs(kl(p, q) - renyi_half(p, q)) > 1e-6


def test_product_additivity_for_both_selectors():
    p, q = [0.9, 0.1], [0.6, 0.4]
    r, s = [0.7, 0.3], [0.2, 0.8]
    assert abs(kl(tensor(p, r), tensor(q, s)) - kl(p, q) - kl(r, s)) < 1e-12
    assert abs(renyi_half(tensor(p, r), tensor(q, s)) - renyi_half(p, q) - renyi_half(r, s)) < 1e-12


def test_binary_stochastic_data_processing_grid():
    p, q = [0.9, 0.1], [0.6, 0.4]
    for ia in range(11):
        for ib in range(11):
            a, b = ia / 10.0, ib / 10.0
            tp, tq = binary_channel(p, a, b), binary_channel(q, a, b)
            assert kl(tp, tq) <= kl(p, q) + 1e-12
            assert renyi_half(tp, tq) <= renyi_half(p, q) + 1e-12


def test_dimension_embeddings_2_through_12():
    eps = 1e-8
    for n in range(2, 13):
        if n == 2:
            p, q = [0.9, 0.1], [0.6, 0.4]
        else:
            tail = [eps] * (n - 2)
            scale = 1.0 - eps * (n - 2)
            p = [0.9 * scale, 0.1 * scale] + tail
            q = [0.6 * scale, 0.4 * scale] + tail
        assert abs(sum(p) - 1.0) < 1e-12
        assert abs(sum(q) - 1.0) < 1e-12
        assert abs(kl(p, q) - renyi_half(p, q)) > 1e-6
