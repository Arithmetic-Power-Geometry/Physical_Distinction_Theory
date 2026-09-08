"""Two-point-isotropy + pairwise-calibration dimension audit.

This module does not claim new Lie-group classification. It encodes the
standard compact connected linear sphere-action cases relevant to the PDT
kill-test and records whether the isotropy action is transitive on the unit
sphere orthogonal to a fixed reference direction (two-point isotropy), plus
the dimension of the generic stabilizer after fixing two orthonormal
references.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ActionCase:
    group: str
    real_dimension: int
    two_point_isotropic: bool
    pair_stabilizer_dimension: int
    noncommuting: bool

    @property
    def pcc(self) -> bool:
        return self.pair_stabilizer_dimension == 0

    @property
    def survives_filter(self) -> bool:
        return self.two_point_isotropic and self.pcc and self.noncommuting


def so_case(n: int) -> ActionCase:
    if n < 1:
        raise ValueError("n must be positive")
    # Fixing two independent orthonormal vectors leaves SO(n-2), interpreted
    # as trivial for n <= 3. dim SO(k)=k(k-1)/2.
    k = max(n - 2, 0)
    stabilizer_dim = k * (k - 1) // 2
    noncommuting = n >= 3
    return ActionCase(
        group=f"SO({n})",
        real_dimension=n,
        two_point_isotropic=True,
        pair_stabilizer_dimension=stabilizer_dim,
        noncommuting=noncommuting,
    )


def exceptional_cases() -> tuple[ActionCase, ...]:
    # Standard exceptional isotropic chains:
    # G2 -> SU(3) -> SU(2) after fixing two orthonormal directions in R^7;
    # Spin(7) -> G2 -> SU(3) after fixing two in R^8.
    return (
        ActionCase("G2", 7, True, 3, True),       # dim SU(2)=3
        ActionCase("Spin(7)", 8, True, 8, True),  # dim SU(3)=8
    )


def standard_counterexample_families() -> tuple[ActionCase, ...]:
    # Earlier PCC counterexamples SU(2) on R^4 and SU(3) on R^6 are sphere
    # transitive but not two-point isotropic: the first-point stabilizer does
    # not act transitively on the full orthogonal unit sphere.
    return (
        ActionCase("SU(2) natural", 4, False, 0, True),
        ActionCase("SU(3) natural", 6, False, 0, True),
    )


def audit(max_dimension: int = 12) -> list[ActionCase]:
    rows = [so_case(n) for n in range(1, max_dimension + 1)]
    rows.extend(exceptional_cases())
    rows.extend(standard_counterexample_families())
    return rows


def surviving_dimensions(max_dimension: int = 12) -> list[int]:
    return sorted({c.real_dimension for c in audit(max_dimension) if c.survives_filter})


if __name__ == "__main__":
    for case in audit():
        print(case)
    print("survivors:", surviving_dimensions())
