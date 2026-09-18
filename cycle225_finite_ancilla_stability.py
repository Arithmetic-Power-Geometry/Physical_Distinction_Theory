"""Cycle 225: exact finite-ancilla obstruction for d=1..12.

No floating-point eigensolver is needed.  For d>=2, embed the Bell state in
the first two levels. Partial transpose has exact eigenvalues
{1/2, 1/2, 1/2, -1/2} on that 4D support and zeros elsewhere.
"""
from fractions import Fraction


def partial_transpose_spectrum(d: int):
    if d < 1:
        raise ValueError("d must be >=1")
    if d == 1:
        return [Fraction(1, 1)]
    # id_2 tensor transpose_d acting on an embedded Bell projector.
    return [Fraction(-1, 2)] + [Fraction(1, 2)] * 3 + [Fraction(0, 1)] * (2*d - 4)


def audit():
    rows = []
    for d in range(1, 13):
        spectrum = partial_transpose_spectrum(d)
        min_eig = min(spectrum)
        rows.append((d, min_eig, min_eig >= 0))
    return rows


def test_exact_cycle225():
    rows = audit()
    assert rows[0] == (1, Fraction(1, 1), True)
    for d, min_eig, remains_positive in rows[1:]:
        assert 2 <= d <= 12
        assert min_eig == Fraction(-1, 2)
        assert remains_positive is False


if __name__ == "__main__":
    for d, lam_min, ok in audit():
        print(f"d={d:2d} min_eigenvalue={lam_min!s:>4s} extension_positive={ok}")
