"""Cycle 042: conditional composition-based dimension filter.

This module audits a deliberately narrow theorem.  Let K be one of the
associative real normed division algebras R,C,H with real dimension d=1,2,4.
The normalized state space of the 2x2 Hermitian Jordan algebra H_2(K) is a
Euclidean ball of Bloch dimension n=d+1.  If the self-composite is taken to be
the corresponding 4x4 Hermitian matrix model H_4(K), then local tomography
requires

    dim_R H_4(K) = (dim_R H_2(K))**2.

Since dim H_2(K)=2+d and dim H_4(K)=4+6d, equality is equivalent to

    4+6d = (2+d)^2  <=>  d(2-d)=0.

For positive d this forces d=2, hence K=C and n=3.

This is IMPORTED/KNOWN Jordan/GPT mathematics packaged as a PDT kill/filter
result.  It is NOT a PDT-native derivation because the Jordan matrix composite
and local tomography are extra assumptions.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class AuditRow:
    algebra: str
    d: int
    bloch_dimension: int
    local_order_dimension: int
    expected_locally_tomographic_composite_dimension: int
    standard_matrix_composite_dimension: int
    tomography_gap: int
    locally_tomographic: bool


def hermitian_dimension(matrix_size: int, d: int) -> int:
    """Real dimension of H_m(K) for associative K of real dimension d."""
    if matrix_size < 1 or d < 1:
        raise ValueError("matrix_size and d must be positive")
    # m real diagonal coordinates plus C(m,2) off-diagonal K coordinates.
    return matrix_size + (matrix_size * (matrix_size - 1) // 2) * d


def audit_associative_division_algebras() -> List[AuditRow]:
    rows: List[AuditRow] = []
    for algebra, d in (("R", 1), ("C", 2), ("H", 4)):
        local_dim = hermitian_dimension(2, d)
        standard_composite_dim = hermitian_dimension(4, d)
        expected = local_dim * local_dim
        rows.append(
            AuditRow(
                algebra=algebra,
                d=d,
                bloch_dimension=d + 1,
                local_order_dimension=local_dim,
                expected_locally_tomographic_composite_dimension=expected,
                standard_matrix_composite_dimension=standard_composite_dim,
                tomography_gap=standard_composite_dim - expected,
                locally_tomographic=(standard_composite_dim == expected),
            )
        )
    return rows


def equality_residual(d: int) -> int:
    """Return dim H_4(K) - dim(H_2(K))^2 = d(2-d)."""
    return (4 + 6 * d) - (2 + d) ** 2


def dimension_scan(n_max: int = 12) -> List[Dict[str, object]]:
    """Audit n=1..n_max without pretending the route applies to every n.

    The normed-division-algebra bit dimensions are n=2,3,5,9.  The octonionic
    n=9 bit H_2(O) exists as a spin factor, but H_4(O) is not an Euclidean
    Jordan matrix algebra, so the assumed standard self-composite route is not
    available there.
    """
    if n_max < 1:
        raise ValueError("n_max must be positive")
    labels = {
        2: ("R", "fails local tomography under standard H4(R) composite"),
        3: ("C", "passes local tomography under standard H4(C) composite"),
        5: ("H", "fails local tomography under standard H4(H) dimension count"),
        9: ("O", "route unavailable: H4(O) is not an EJA matrix model"),
    }
    result: List[Dict[str, object]] = []
    for n in range(1, n_max + 1):
        if n in labels:
            algebra, status = labels[n]
            applicable = n in (2, 3, 5)
            selected = n == 3
        else:
            algebra, status, applicable, selected = None, "not in division-algebra bit subfamily", False, False
        result.append(
            {
                "n": n,
                "algebra": algebra,
                "route_applicable": applicable,
                "selected_by_assumptions": selected,
                "status": status,
            }
        )
    return result


if __name__ == "__main__":
    for row in audit_associative_division_algebras():
        print(row)
