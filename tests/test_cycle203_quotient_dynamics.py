"""Cycle 203 exact tests: microscopic dynamics does not select resource quotient."""


def full(bits):
    return bits


def parity(bits):
    out = 0
    for b in bits:
        out ^= b
    return out


def identity(bits):
    return bits


def reverse(bits):
    return tuple(reversed(bits))


def compatible(states, q, u):
    for x in states:
        for y in states:
            if q(x) == q(y) and q(u(x)) != q(u(y)):
                return False
    return True


def classes(states, q):
    return {q(x) for x in states}


def test_smallest_two_bit_witness():
    states = [(a, b) for a in (0, 1) for b in (0, 1)]
    assert compatible(states, full, identity)
    assert compatible(states, parity, identity)
    assert compatible(states, full, reverse)
    assert compatible(states, parity, reverse)
    assert len(classes(states, full)) == 4
    assert len(classes(states, parity)) == 2


def test_embedding_dimensions_1_to_12():
    # n counts inert coordinates appended to the decisive two-bit subsystem.
    for n in range(1, 13):
        states = []
        for a in (0, 1):
            for b in (0, 1):
                states.append((a, b) + (0,) * n)

        def u(x):
            return (x[1], x[0]) + x[2:]

        def q_full(x):
            return x

        def q_parity(x):
            return x[0] ^ x[1]

        assert compatible(states, q_full, u)
        assert compatible(states, q_parity, u)
        assert len(classes(states, q_full)) == 4
        assert len(classes(states, q_parity)) == 2


def test_incompatible_quotient_detected():
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]

    def q_first(x):
        return x[0]

    def controlled_flip(x):
        a, b = x
        return (a ^ b, b)

    assert not compatible(states, q_first, controlled_flip)
