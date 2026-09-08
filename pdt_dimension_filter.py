"""Dimension-filter audit for a candidate PDT interaction principle.

This module does NOT claim a PDT-native derivation of n=3. It implements the
known mathematical filter obtained by combining a normed binary vector cross
product with the Jacobi identity. Nontrivial normed vector cross products
exist only in dimensions 3 and 7; the standard 7D octonionic product fails
Jacobi, while the 3D product satisfies it.
"""
from __future__ import annotations

import itertools
import numpy as np
import pandas as pd

_FANO_TRIPLES = [
    (0, 1, 2),
    (0, 3, 4),
    (0, 6, 5),
    (1, 3, 5),
    (1, 4, 6),
    (2, 3, 6),
    (2, 5, 4),
]


def cross3(a, b):
    return np.cross(np.asarray(a, float), np.asarray(b, float))


def cross7(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    if a.shape != (7,) or b.shape != (7,):
        raise ValueError("cross7 expects 7-vectors")
    c = np.zeros(7, dtype=float)
    for i, j, k in _FANO_TRIPLES:
        c[k] += a[i] * b[j] - a[j] * b[i]
        c[i] += a[j] * b[k] - a[k] * b[j]
        c[j] += a[k] * b[i] - a[i] * b[k]
    return c


def jacobi_residual(cross, a, b, c):
    J = cross(a, cross(b, c)) + cross(b, cross(c, a)) + cross(c, cross(a, b))
    return float(np.linalg.norm(J))


def norm_identity_residual(cross, a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    x = cross(a, b)
    rhs = float(a @ a) * float(b @ b) - float(a @ b) ** 2
    return float(abs(float(x @ x) - rhs))


def orthogonality_residual(cross, a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    x = cross(a, b)
    return float(max(abs(a @ x), abs(b @ x)))


def basis_jacobi_max(dimension: int) -> float:
    if dimension == 3:
        cross = cross3
    elif dimension == 7:
        cross = cross7
    else:
        raise ValueError("explicit audit is available only in dimensions 3 and 7")
    E = np.eye(dimension)
    values = [jacobi_residual(cross, E[i], E[j], E[k])
              for i, j, k in itertools.combinations(range(dimension), 3)]
    return max(values, default=0.0)


def randomized_audit(dimension: int, trials: int = 2000, seed: int = 20260908):
    if dimension == 3:
        cross = cross3
    elif dimension == 7:
        cross = cross7
    else:
        raise ValueError("explicit audit is available only in dimensions 3 and 7")
    rng = np.random.default_rng(seed + dimension)
    max_norm = 0.0
    max_orth = 0.0
    max_jacobi = 0.0
    for _ in range(trials):
        a, b, c = rng.normal(size=(3, dimension))
        max_norm = max(max_norm, norm_identity_residual(cross, a, b))
        max_orth = max(max_orth, orthogonality_residual(cross, a, b))
        max_jacobi = max(max_jacobi, jacobi_residual(cross, a, b, c))
    return {
        "dimension": dimension,
        "trials": trials,
        "max_norm_identity_residual": max_norm,
        "max_orthogonality_residual": max_orth,
        "max_jacobi_residual": max_jacobi,
        "basis_max_jacobi_residual": basis_jacobi_max(dimension),
    }


def dimension_filter_table(max_dimension: int = 12) -> pd.DataFrame:
    rows = []
    for n in range(1, max_dimension + 1):
        if n == 3:
            rows.append({"n": n, "nontrivial_normed_cross_product": True,
                         "jacobi_compatible_standard_model": True,
                         "status": "passes known algebraic filter"})
        elif n == 7:
            rows.append({"n": n, "nontrivial_normed_cross_product": True,
                         "jacobi_compatible_standard_model": False,
                         "status": "fails Jacobi in octonionic model"})
        else:
            rows.append({"n": n, "nontrivial_normed_cross_product": False,
                         "jacobi_compatible_standard_model": False,
                         "status": "excluded by known cross-product classification"})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    print(dimension_filter_table(12).to_string(index=False))
    print(randomized_audit(3))
    print(randomized_audit(7))
