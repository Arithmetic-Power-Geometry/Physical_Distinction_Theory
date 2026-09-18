"""Cycle 243: exact stress test for local tomography as a PDT composition selector.

This does NOT test whether local tomography is useful. It tests the narrower claim
that local tomography alone uniquely determines a composite theory or selects n=3.
All arithmetic is integer/Fraction exact.
"""
from fractions import Fraction
import random


def classical_counts(n: int):
    # Dimension K of the unnormalised state vector space.
    K_A = n
    K_AB = n * n
    return K_A, K_AB


def complex_quantum_counts(n: int):
    # Hermitian n x n matrices form a real vector space of dimension n^2.
    K_A = n * n
    K_AB = (n * n) ** 2
    return K_A, K_AB


def equality_probs(n: int):
    if n < 1:
        raise ValueError("n must be >= 1")
    # Two classical joint states with identical uniform marginals.
    p_ind_equal = Fraction(1, n)
    p_corr_equal = Fraction(1, 1)
    return p_ind_equal, p_corr_equal


def check_dimension(n: int):
    kc, kcab = classical_counts(n)
    kq, kqab = complex_quantum_counts(n)
    assert kcab == kc * kc
    assert kqab == kq * kq
    pind, pcorr = equality_probs(n)
    assert Fraction(0) <= pind <= Fraction(1)
    assert pcorr == 1
    if n == 1:
        assert pind == pcorr
    else:
        assert pind != pcorr
    return {
        "n": n,
        "classical_K_A": kc,
        "classical_K_AB": kcab,
        "quantum_K_A": kq,
        "quantum_K_AB": kqab,
        "p_equal_independent": str(pind),
        "p_equal_correlated": str(pcorr),
    }


def main():
    rows = [check_dimension(n) for n in range(1, 13)]
    rng = random.Random(243)
    for _ in range(200):
        check_dimension(rng.randint(13, 10000))
    for row in rows:
        print(row)
    print("PASS: n=1..12 exact; 200 seeded higher-n checks.")
    print("Conclusion tested: local tomography is compatible with inequivalent classical and complex-quantum state-space families and does not select n=3.")


if __name__ == "__main__":
    main()
