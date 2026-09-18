"""Cycle 244: exact stress test for multiplicative capacity/state-parameter laws.

Purpose: test whether composition multiplicativity plus subspace monotonicity can
select a unique PDT composition exponent or n=3.  It cannot: K_r(n)=n**r is an
exact family for every positive integer r.
"""


def K(n: int, r: int) -> int:
    assert n >= 1 and r >= 1
    return n ** r


def verify(max_n: int = 12, max_r: int = 8) -> None:
    for r in range(1, max_r + 1):
        # Degenerate unit system.
        assert K(1, r) == 1
        # Strict subspace/capacity monotonicity.
        for n in range(1, max_n):
            assert K(n + 1, r) > K(n, r)
        # Exact multiplicative composition.
        for a in range(1, max_n + 1):
            for b in range(1, max_n + 1):
                assert K(a * b, r) == K(a, r) * K(b, r)

    # The hypotheses do not single out r, and therefore cannot single out n=3.
    signatures = {r: tuple(K(n, r) for n in range(1, max_n + 1))
                  for r in range(1, max_r + 1)}
    assert len(set(signatures.values())) == max_r
    for r in range(1, max_r + 1):
        assert K(3, r) == 3 ** r


if __name__ == "__main__":
    verify()
    print("PASS: multiplicativity+monotonicity admits K_r(n)=n^r for r=1..8; no unique exponent or n=3 selector.")
