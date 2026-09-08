"""Audit a conditional PDT dimension filter based on two-point isotropy (TPI).

This module does not claim new group-classification mathematics.  It encodes the
relevant connected linear sphere actions after the standard transitive-sphere
action classification is filtered by the stronger requirement that the point
stabilizer acts transitively on the tangent unit sphere.

PCC = an ordered pair of independent reference states has trivial pointwise
stabilizer. NCR = the connected reversible group is non-abelian.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class TPICase:
    family: str
    real_dimension: int
    pair_stabilizer: str
    pair_stabilizer_dimension: int
    noncommuting: bool

    @property
    def pcc(self) -> bool:
        return self.pair_stabilizer_dimension == 0

    @property
    def survives(self) -> bool:
        return self.pcc and self.noncommuting


def so_case(n: int) -> TPICase:
    if n < 2:
        raise ValueError("n must be >= 2")
    k = max(n - 2, 0)
    dim = k * (k - 1) // 2
    return TPICase(
        family=f"SO({n})",
        real_dimension=n,
        pair_stabilizer=f"SO({k})",
        pair_stabilizer_dimension=dim,
        noncommuting=n >= 3,
    )


def audited_tpi_cases(max_n: int = 12) -> list[TPICase]:
    """Return audited TPI candidates through the requested real dimension.

    Besides SO(n), two exceptional sphere actions relevant here are
    G2 on R^7 and Spin(7) on R^8.  Their ordered orthonormal-pair
    stabilizers are SU(2) and SU(3), respectively, hence PCC fails.
    """
    cases = [so_case(n) for n in range(2, max_n + 1)]
    if max_n >= 7:
        cases.append(TPICase("G2", 7, "SU(2)", 3, True))
    if max_n >= 8:
        cases.append(TPICase("Spin(7)", 8, "SU(3)", 8, True))
    return cases


def surviving_dimensions(max_n: int = 12) -> list[int]:
    return sorted({c.real_dimension for c in audited_tpi_cases(max_n) if c.survives})


def csv_rows(max_n: int = 12) -> list[dict[str, object]]:
    return [
        {
            "family": c.family,
            "real_dimension": c.real_dimension,
            "pair_stabilizer": c.pair_stabilizer,
            "pair_stabilizer_dimension": c.pair_stabilizer_dimension,
            "pcc": c.pcc,
            "noncommuting": c.noncommuting,
            "survives_TPI_PCC_NCR": c.survives,
        }
        for c in audited_tpi_cases(max_n)
    ]


if __name__ == "__main__":
    import csv
    import sys

    rows = csv_rows(12)
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
