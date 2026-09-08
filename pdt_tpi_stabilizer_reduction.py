"""Topological audit for the conditional TPI+PCC PDT dimension filter.

The mathematics used here is established Lie-group topology, not claimed as PDT
novelty.  If a compact connected reversible group acts transitively on the pure
state sphere and TPI+PCC hold, then the stabilizer H of one reference acts
freely and transitively on the equal-angle sphere S^(n-2).  Hence H is itself
diffeomorphic to S^(n-2).  Connected spheres that are Lie groups leave n=3 or
n=5.  The n=5 branch would force a compact simply connected Lie group G of
real dimension 7; low-dimensional compact simple-Lie-group classification
rules this out.  Thus the structural candidate is n=3.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ReductionCase:
    n: int
    latitude_dimension: int
    stabilizer_sphere_candidate: bool
    post_global_obstruction: bool
    survives: bool
    note: str


def reduction_case(n: int) -> ReductionCase:
    if n < 2:
        raise ValueError("n must be >= 2")
    k = n - 2
    if k == 0:
        return ReductionCase(n, k, False, False, False,
                             "connected one-point stabilizer cannot act transitively on S^0")
    if k == 1:
        return ReductionCase(n, k, True, True, True,
                             "H is diffeomorphic to S^1; no dimension obstruction")
    if k == 3:
        return ReductionCase(n, k, True, False, False,
                             "H would be S^3 and dim(G)=7; compact simply connected G of dimension 7 is impossible")
    return ReductionCase(n, k, False, False, False,
                         "S^(n-2) is not a connected Lie group")


def surviving_dimensions(max_n: int = 12) -> list[int]:
    if max_n < 2:
        return []
    return [n for n in range(2, max_n + 1) if reduction_case(n).survives]


def audit_rows(max_n: int = 12) -> list[dict[str, object]]:
    rows = []
    for n in range(2, max_n + 1):
        c = reduction_case(n)
        rows.append({
            "n": c.n,
            "latitude_dimension": c.latitude_dimension,
            "stabilizer_sphere_candidate": c.stabilizer_sphere_candidate,
            "post_global_obstruction": c.post_global_obstruction,
            "survives_TPI_PCC": c.survives,
            "note": c.note,
        })
    return rows


if __name__ == "__main__":
    import csv
    import sys

    rows = audit_rows(12)
    writer = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
