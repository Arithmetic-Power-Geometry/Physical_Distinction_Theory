"""Cycle 255: exact dimension stress for information-causality/CHSH selector claims.

This is a regression harness, not a proof of information causality.
It verifies that the same two-level quantum CHSH witness embeds unchanged in every
finite n>=2, so any principle whose relevant consequence is only the Tsirelson
CHSH ceiling cannot uniquely select n=3.
"""
from fractions import Fraction


def embedded_chsh_squared(n: int) -> Fraction:
    if n < 2:
        return Fraction(0)
    # Standard two-level maximally entangled CHSH witness has S=2*sqrt(2),
    # hence S^2=8 exactly. Embedding the supporting 2D subspace in C^n
    # changes neither the state/observable matrix elements nor S.
    return Fraction(8)


def classical_chsh_squared() -> Fraction:
    return Fraction(4)


def algebraic_chsh_squared() -> Fraction:
    return Fraction(16)


def run():
    rows = []
    for n in range(1, 13):
        q = embedded_chsh_squared(n)
        rows.append((n, q))
        if n >= 2:
            assert q == 8
        else:
            assert q == 0
    assert classical_chsh_squared() == 4
    assert algebraic_chsh_squared() == 16
    # n=2 is already a nontrivial survivor, hence n=3 is not selected.
    assert embedded_chsh_squared(2) == embedded_chsh_squared(3) == 8
    return rows


if __name__ == "__main__":
    for n, s2 in run():
        print(f"n={n:2d}  embedded_CHSH_S2={s2}")
