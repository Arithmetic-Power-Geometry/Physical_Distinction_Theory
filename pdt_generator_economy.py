"""Generator-economy + noncommuting-reversibility dimension filter.

This module audits a weaker dimension-selection proposal than exact
Generator–Distinction Self-Duality (GDSD).

Assume an n-dimensional Euclidean elementary distinction space with full
connected reversible isotropy SO(n). Its infinitesimal generator space has
known dimension n(n-1)/2.

Two candidate operational conditions are tested:

1. Generator economy (GE): the number of independent infinitesimal reversible
   generator coordinates does not exceed the number of elementary distinction
   coordinates, dim so(n) <= n.
2. Noncommuting reversibility (NCR): the connected reversible generator algebra
   is non-abelian.

For SO(n), NCR holds exactly for n >= 3. GE gives n <= 3 for positive n.
Together they isolate n=3. The Lie-algebra mathematics is standard; the
physical status of GE and NCR as PDT principles is conditional.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GeneratorEconomyRow:
    n: int
    distinction_dim: int
    generator_dim: int
    generator_economy: bool
    noncommuting_reversibility: bool
    selected: bool


def generator_dimension(n: int) -> int:
    if n < 1:
        raise ValueError("n must be a positive integer")
    return n * (n - 1) // 2


def so_n_is_nonabelian(n: int) -> bool:
    if n < 1:
        raise ValueError("n must be a positive integer")
    # so(1) is trivial and so(2) is one-dimensional/abelian; so(n) is
    # non-abelian for every n >= 3.
    return n >= 3


def audit_dimension(n: int) -> GeneratorEconomyRow:
    g = generator_dimension(n)
    ge = g <= n
    ncr = so_n_is_nonabelian(n)
    return GeneratorEconomyRow(
        n=n,
        distinction_dim=n,
        generator_dim=g,
        generator_economy=ge,
        noncommuting_reversibility=ncr,
        selected=(ge and ncr),
    )


def audit_range(n_min: int = 1, n_max: int = 12):
    if n_min < 1 or n_max < n_min:
        raise ValueError("require 1 <= n_min <= n_max")
    return [audit_dimension(n) for n in range(n_min, n_max + 1)]


def selected_dimensions(n_max: int = 1000):
    return [row.n for row in audit_range(1, n_max) if row.selected]


if __name__ == "__main__":
    for row in audit_range():
        print(row)
