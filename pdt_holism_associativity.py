"""Cycle 039: associative holism dimension-law audit.

This module studies composition laws for the dimension q_X of a finite-dimensional
PDT accessible quotient.  It is intentionally only a parameter-counting layer:
it does not assert existence of a physical GPT/state-space realization for every
law below.
"""

from __future__ import annotations

from dataclasses import dataclass


def compose_dimension(a: int, b: int, k: int = 0) -> int:
    """Associative commutative unital family F_k(a,b).

    F_k(a,b) = ab + k(a-1)(b-1), for positive integer dimensions and k>=0.
    k=0 is the locally-tomographic parameter-counting law.  k>0 adds a
    nonnegative holistic excess while preserving unit, symmetry and associativity.
    """
    if a < 1 or b < 1:
        raise ValueError("accessible quotient dimensions must be positive")
    if k < 0:
        raise ValueError("k must be nonnegative")
    return a * b + k * (a - 1) * (b - 1)


def holism_excess(a: int, b: int, k: int = 0) -> int:
    """Return h(a,b)=F_k(a,b)-ab."""
    return compose_dimension(a, b, k) - a * b


def associativity_residual(a: int, b: int, c: int, k: int = 0) -> int:
    """Return F(F(a,b),c)-F(a,F(b,c)); theorem predicts exactly zero."""
    return compose_dimension(compose_dimension(a, b, k), c, k) - compose_dimension(
        a, compose_dimension(b, c, k), k
    )


def holism_balance_residual(a: int, b: int, c: int, k: int = 0) -> int:
    """Exact associativity balance in excess variables.

    For q_AB=q_A q_B+h_AB, associativity requires
      h_AB*q_C + h_(AB),C = q_A*h_BC + h_A,(BC).
    """
    ab = compose_dimension(a, b, k)
    bc = compose_dimension(b, c, k)
    lhs = holism_excess(a, b, k) * c + holism_excess(ab, c, k)
    rhs = a * holism_excess(b, c, k) + holism_excess(a, bc, k)
    return lhs - rhs


def transformed_coordinate(q: int, k: int) -> int:
    """Coordinate T_k(q)=1+(k+1)(q-1) that multiplicatively linearizes F_k."""
    if q < 1 or k < 0:
        raise ValueError("q>=1 and k>=0 required")
    return 1 + (k + 1) * (q - 1)


def multiplicative_transform_residual(a: int, b: int, k: int = 0) -> int:
    """Check T_k(F_k(a,b)) = T_k(a) T_k(b)."""
    return transformed_coordinate(compose_dimension(a, b, k), k) - (
        transformed_coordinate(a, k) * transformed_coordinate(b, k)
    )


@dataclass(frozen=True)
class AuditRow:
    a: int
    b: int
    c: int
    k: int
    q_ab: int
    h_ab: int
    assoc_residual: int
    balance_residual: int
    transform_residual: int


def audit(max_dim: int = 12, max_k: int = 4) -> list[AuditRow]:
    rows: list[AuditRow] = []
    for k in range(max_k + 1):
        for a in range(1, max_dim + 1):
            for b in range(1, max_dim + 1):
                for c in range(1, max_dim + 1):
                    rows.append(
                        AuditRow(
                            a=a,
                            b=b,
                            c=c,
                            k=k,
                            q_ab=compose_dimension(a, b, k),
                            h_ab=holism_excess(a, b, k),
                            assoc_residual=associativity_residual(a, b, c, k),
                            balance_residual=holism_balance_residual(a, b, c, k),
                            transform_residual=multiplicative_transform_residual(a, b, k),
                        )
                    )
    return rows


if __name__ == "__main__":
    rows = audit()
    assert all(r.assoc_residual == 0 for r in rows)
    assert all(r.balance_residual == 0 for r in rows)
    assert all(r.transform_residual == 0 for r in rows)
    print(f"audited {len(rows)} triples; all exact residuals are zero")
