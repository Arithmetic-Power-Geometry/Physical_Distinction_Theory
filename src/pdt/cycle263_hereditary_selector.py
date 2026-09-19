"""Cycle 263: exact stress checks for the hereditary selector obstruction.

No simulation claim: all arithmetic uses fractions.Fraction.
"""
from fractions import Fraction


def born_diag(rho, effect):
    assert len(rho) == len(effect)
    return sum((r * e for r, e in zip(rho, effect)), Fraction(0))


def pad(v, n):
    assert n >= len(v)
    return tuple(v) + (Fraction(0),) * (n - len(v))


def exact_embedding_regression(max_n=12):
    # Mixed qubit state and nonprojective diagonal effect, deliberately rational.
    rho2 = (Fraction(2, 5), Fraction(3, 5))
    e2 = (Fraction(1, 3), Fraction(4, 7))
    base = born_diag(rho2, e2)
    rows = []
    for n in range(1, max_n + 1):
        if n < 2:
            rows.append((n, "DEGENERATE", None))
            continue
        got = born_diag(pad(rho2, n), pad(e2, n))
        assert got == base
        rows.append((n, "PRESERVED", got))
    return base, rows


if __name__ == "__main__":
    base, rows = exact_embedding_regression()
    print("base_probability", base)
    for row in rows:
        print(*row)
