"""Generator–Distinction Self-Duality (GDSD) audit.

This module tests the necessary dimension condition for an equivariant linear
identification between an n-dimensional Euclidean distinction space V and the
Lie algebra so(n) of its full connected reversible isotropy group SO(n).

The mathematics is elementary/known: dim so(n) = n(n-1)/2.  GDSD can only
hold if n = dim so(n), which for positive integer n gives n=3.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GDSDRow:
    n: int
    distinction_dim: int
    generator_dim: int
    mismatch: int
    dimension_match: bool


def generator_dimension(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    return n * (n - 1) // 2


def audit_dimension(n: int) -> GDSDRow:
    g = generator_dimension(n)
    return GDSDRow(
        n=n,
        distinction_dim=n,
        generator_dim=g,
        mismatch=g - n,
        dimension_match=(g == n),
    )


def audit_range(n_min: int = 1, n_max: int = 12):
    if n_min < 1 or n_max < n_min:
        raise ValueError("require 1 <= n_min <= n_max")
    return [audit_dimension(n) for n in range(n_min, n_max + 1)]


def positive_integer_solutions(n_max: int = 1000):
    return [row.n for row in audit_range(1, n_max) if row.dimension_match]


if __name__ == "__main__":
    for row in audit_range():
        print(row)
