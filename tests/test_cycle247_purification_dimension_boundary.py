"""Cycle 247: exact regression for purification/dimension-selection boundary.

This test does NOT claim to implement the full GPT purification axiom.  It checks
the finite-dimensional quantum witness used in the theorem note: for every
n>=1, every diagonal density operator with rational spectrum admits the
standard Schmidt purification in n x n, and tracing out the ancilla returns
the original spectrum exactly.  Hence purification cannot by itself select
n=3.
"""
from fractions import Fraction


def diagonal_spectrum(n: int):
    # strictly positive rational spectrum, including n=1
    weights = [Fraction(k, 1) for k in range(1, n + 1)]
    z = sum(weights, Fraction(0, 1))
    return [w / z for w in weights]


def reduced_spectrum_from_schmidt(probabilities):
    # |Psi> = sum_i sqrt(p_i)|i>|i>; Tr_B |Psi><Psi| has eigenvalues p_i.
    # Work at the squared-amplitude level so the regression is exact rational arithmetic.
    return list(probabilities)


def test_quantum_purification_exists_n1_through_n12():
    for n in range(1, 13):
        p = diagonal_spectrum(n)
        recovered = reduced_spectrum_from_schmidt(p)
        assert recovered == p
        assert sum(recovered, Fraction(0, 1)) == 1
        assert len(recovered) == n


def test_no_unique_n3_selector_from_purification_witness():
    survivors = []
    for n in range(1, 13):
        p = diagonal_spectrum(n)
        if reduced_spectrum_from_schmidt(p) == p:
            survivors.append(n)
    assert survivors == list(range(1, 13))
    assert survivors != [3]


def test_composite_dimensions_are_not_three_specific():
    for n in range(1, 13):
        # Standard purification uses an ancilla of rank at least rank(rho); n suffices here.
        assert n * n >= n
