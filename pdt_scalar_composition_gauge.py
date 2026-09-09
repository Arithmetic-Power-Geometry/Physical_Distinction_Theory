"""Cycle 041: smooth scalar-composition linearization audits.

The theorem is analytic; this module supplies exact/numerical witnesses for
representative associative laws and verifies their calibration logarithms.
"""
from __future__ import annotations

import math


def product_law(a: float, b: float) -> float:
    return a * b


def shifted_product_law(a: float, b: float, k: float) -> float:
    """Cycle-039 family F_k = ab + k(a-1)(b-1)."""
    return a * b + k * (a - 1.0) * (b - 1.0)


def shifted_transform(x: float, k: float) -> float:
    """T_k(x)=1+(k+1)(x-1), multiplicative coordinate."""
    return 1.0 + (k + 1.0) * (x - 1.0)


def shifted_logarithm(x: float, k: float) -> float:
    """Additive calibration coordinate L_k = log(T_k)/(k+1).

    Constant rescaling of an additive generator is immaterial. This choice
    matches the invariant differential 1/phi exactly.
    """
    t = shifted_transform(x, k)
    if t <= 0:
        raise ValueError("outside positive calibration domain")
    return math.log(t) / (k + 1.0)


def shifted_phi(x: float, k: float) -> float:
    """partial_2 F_k(x,1)."""
    return x + k * (x - 1.0)


def additive_residual(a: float, b: float, k: float) -> float:
    f = shifted_product_law(a, b, k)
    return shifted_logarithm(f, k) - shifted_logarithm(a, k) - shifted_logarithm(b, k)


def associativity_residual(a: float, b: float, c: float, k: float) -> float:
    left = shifted_product_law(shifted_product_law(a, b, k), c, k)
    right = shifted_product_law(a, shifted_product_law(b, c, k), k)
    return left - right


def audit(max_dim: int = 12, max_k: int = 12, tol: float = 1e-12) -> dict:
    worst_assoc = 0.0
    worst_add = 0.0
    cases = 0
    for k in range(max_k + 1):
        for a in range(1, max_dim + 1):
            for b in range(1, max_dim + 1):
                worst_add = max(worst_add, abs(additive_residual(a, b, k)))
                for c in (1, 2, max_dim):
                    worst_assoc = max(worst_assoc, abs(associativity_residual(a, b, c, k)))
                    cases += 1
    return {
        "max_dim": max_dim,
        "max_k": max_k,
        "cases": cases,
        "worst_associativity_residual": worst_assoc,
        "worst_additive_coordinate_residual": worst_add,
        "pass": worst_assoc <= tol and worst_add <= tol,
    }


if __name__ == "__main__":
    print(audit())
