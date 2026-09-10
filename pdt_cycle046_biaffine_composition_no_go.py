"""Cycle 046: exact classification of symmetric biaffine scalar composition laws.

This module is intentionally dependency-free.  It audits the theorem that every
separately affine, symmetric composition law with identity 1 has the form

    F_k(a,b) = a*b + k*(a-1)*(b-1),

and that every member of this family is associative.  Hence separate affinity
cannot select the product law k=0.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def compose(a, b, k=0):
    """Biaffine family F_k(a,b)=ab+k(a-1)(b-1)."""
    return a * b + k * (a - 1) * (b - 1)


def coefficients_from_alpha(alpha):
    """Return (alpha,beta,gamma,delta) for the general symmetric unit law."""
    beta = 1 - alpha
    return alpha, beta, beta, alpha - 1


def evaluate_coefficients(a, b, coeffs):
    alpha, beta, gamma, delta = coeffs
    return alpha * a * b + beta * a + gamma * b + delta


def k_from_alpha(alpha):
    return alpha - 1


def associativity_residual(a, b, c, k=0):
    return compose(compose(a, b, k), c, k) - compose(a, compose(b, c, k), k)


def unit_residual(a, k=0):
    return compose(a, 1, k) - a


def symmetry_residual(a, b, k=0):
    return compose(a, b, k) - compose(b, a, k)


def product_excess(a, b, k=0):
    return compose(a, b, k) - a * b


def monotone_on_capacity_domain(k):
    """For domain [1,infinity), global coordinate monotonicity iff k>=-1.

    dF/da = b + k(b-1) = 1 + (1+k)(b-1), so this is nonnegative for every
    b>=1 exactly when 1+k>=0.
    """
    return k >= -1


def product_lower_bound_on_capacity_domain(k):
    """F_k(a,b)>=ab for every a,b>=1 iff k>=0."""
    return k >= 0


def exact_audit(max_dim: int = 12, max_k: int = 11):
    rows = []
    for k in range(max_k + 1):
        assoc_ok = all(
            associativity_residual(a, b, c, k) == 0
            for a, b, c in product(range(1, max_dim + 1), repeat=3)
        )
        unit_ok = all(unit_residual(a, k) == 0 for a in range(1, max_dim + 1))
        symmetry_ok = all(
            symmetry_residual(a, b, k) == 0
            for a, b in product(range(1, max_dim + 1), repeat=2)
        )
        lower_ok = all(
            product_excess(a, b, k) >= 0
            for a, b in product(range(1, max_dim + 1), repeat=2)
        )
        rows.append(
            {
                "k": k,
                "F_2_2": compose(2, 2, k),
                "assoc_exact": assoc_ok,
                "unit_exact": unit_ok,
                "symmetry_exact": symmetry_ok,
                "product_lower_bound": lower_ok,
            }
        )
    return rows


def rational_classification_audit():
    """Check coefficient reduction for noninteger exact examples."""
    alphas = [Fraction(1, 2), Fraction(1, 1), Fraction(3, 2), Fraction(7, 3)]
    rows = []
    for alpha in alphas:
        coeffs = coefficients_from_alpha(alpha)
        k = k_from_alpha(alpha)
        exact = True
        for a, b in product(range(1, 8), repeat=2):
            if evaluate_coefficients(Fraction(a), Fraction(b), coeffs) != compose(
                Fraction(a), Fraction(b), k
            ):
                exact = False
                break
        rows.append((alpha, k, exact))
    return rows


if __name__ == "__main__":
    for row in exact_audit():
        print(row)
    print(rational_classification_audit())
