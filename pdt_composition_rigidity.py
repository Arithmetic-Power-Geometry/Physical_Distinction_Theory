"""Cycle 040: infinitesimal-independence rigidity for scalar PDT composition.

This module audits a conditional uniqueness theorem for a continuously extended
accessible-capacity composition law F(a,b).  The theorem is elementary:

If F is C^1, associative, has identity 1, and satisfies
    d/db F(a,b)|_{b=1} = a
for every a>=1, then F(a,b)=a*b.

The final hypothesis is called Independent Marginal Revelation (IMR) in the
PDT notes.  It is an additional physical axiom candidate, not a derived PDT
principle.  The underlying associativity/semigroup mathematics is established
prior art and no historical novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random


def product_law(a: float, b: float) -> float:
    return a * b


def holism_family(a: float, b: float, k: float) -> float:
    """Associative family F_k(a,b)=ab+k(a-1)(b-1) from Cycle 039."""
    return a * b + k * (a - 1.0) * (b - 1.0)


def holism_unit_derivative(a: float, k: float) -> float:
    """Exact partial derivative dF_k(a,b)/db at b=1."""
    return a + k * (a - 1.0)


def imr_residual_holism(a: float, k: float) -> float:
    """Residual of IMR: partial_2 F(a,1)-a."""
    return holism_unit_derivative(a, k) - a


def associativity_residual_holism(a: float, b: float, c: float, k: float) -> float:
    lhs = holism_family(holism_family(a, b, k), c, k)
    rhs = holism_family(a, holism_family(b, c, k), k)
    return lhs - rhs


def finite_difference_unit_derivative(a: float, k: float, h: float = 1e-7) -> float:
    return (holism_family(a, 1.0 + h, k) - holism_family(a, 1.0, k)) / h


@dataclass(frozen=True)
class AuditRow:
    a: int
    k: int
    derivative: float
    target: float
    imr_holds: bool
    associativity_max_abs_residual: float


def audit_dimensions(max_dimension: int = 12, max_k: int = 5, seed: int = 40040) -> list[AuditRow]:
    """Audit the Cycle-039 associative family and the new IMR constraint.

    For each integer capacity a=1..max_dimension and k=0..max_k, associativity
    is randomly stress-tested.  IMR is evaluated exactly from the derivative.
    For every nontrivial a>1, IMR eliminates all k!=0 in this family.
    """
    rng = random.Random(seed)
    out: list[AuditRow] = []
    for a in range(1, max_dimension + 1):
        for k in range(max_k + 1):
            max_res = 0.0
            for _ in range(50):
                b = 1.0 + 20.0 * rng.random()
                c = 1.0 + 20.0 * rng.random()
                max_res = max(max_res, abs(associativity_residual_holism(a, b, c, k)))
            deriv = holism_unit_derivative(float(a), float(k))
            out.append(
                AuditRow(
                    a=a,
                    k=k,
                    derivative=deriv,
                    target=float(a),
                    imr_holds=math.isclose(deriv, float(a), rel_tol=0.0, abs_tol=1e-12),
                    associativity_max_abs_residual=max_res,
                )
            )
    return out


def theorem_identity_check(a: float, b: float) -> bool:
    """Reference check for the unique law selected by the conditional theorem."""
    return math.isclose(product_law(a, b), a * b, rel_tol=0.0, abs_tol=0.0)
