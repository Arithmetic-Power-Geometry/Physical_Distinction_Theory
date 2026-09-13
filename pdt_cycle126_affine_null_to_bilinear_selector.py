"""Cycle 126: separate affinity + null absorption forces bilinearity.

For a finite-dimensional vector carrier V, any separately affine map
C: V x V -> V has the form

    C(x,y) = B(x,y) + Lx + My + c,

with B bilinear. If the null distinction is absorbing on both axes,
C(x,0)=C(0,y)=0 for every x,y, then c=L=M=0 and C=B is bilinear.

Combined with the Cycle 124 imported/known SO(n)-equivariant bilinear
selector, a nonzero proper-rotation-covariant composition selects n=3
among n>=2. This module audits the algebraic bridge and dimension guard.
"""

from __future__ import annotations

from itertools import product
import numpy as np


def biaffine_eval(x, y, B, L, M, c):
    """Evaluate C(x,y)=B(x,y)+Lx+My+c."""
    return np.einsum("oij,i,j->o", B, x, y) + L @ x + M @ y + c


def bilinear_eval(x, y, B):
    return np.einsum("oij,i,j->o", B, x, y)


def null_axis_residuals(B, L, M, c, vectors):
    """Return maximum residuals on C(x,0)=0 and C(0,y)=0."""
    d = B.shape[1]
    z = np.zeros(d)
    left = max(float(np.linalg.norm(biaffine_eval(x, z, B, L, M, c))) for x in vectors)
    right = max(float(np.linalg.norm(biaffine_eval(z, y, B, L, M, c))) for y in vectors)
    return left, right


def exact_sign_survivor_count(n: int) -> int:
    """Exact rank-3 tensor coordinates surviving all even sign flips.

    SO(n) contains every diagonal sign matrix with an even number of minus
    signs. Invariance under all two-coordinate sign flips requires the parity
    of the occurrence count of every coordinate in (i,j,k) to be identical.
    For rank 3 this leaves 1 coordinate for n=1, none for n=2, six
    permutations of (0,1,2) for n=3, and none for n>=4.
    """
    if n < 1:
        raise ValueError("n must be positive")
    count = 0
    for idx in product(range(n), repeat=3):
        parity = [0] * n
        for a in idx:
            parity[a] ^= 1
        if all(p == parity[0] for p in parity):
            count += 1
    return count


def random_so3(rng):
    A = rng.normal(size=(3, 3))
    Q, _ = np.linalg.qr(A)
    if np.linalg.det(Q) < 0:
        Q[:, 0] *= -1
    return Q


def so3_cross_covariance_audit(seed: int = 126, trials: int = 2000, tol: float = 1e-10):
    rng = np.random.default_rng(seed)
    max_residual = 0.0
    violations = 0
    for _ in range(trials):
        R = random_so3(rng)
        x = rng.normal(size=3)
        y = rng.normal(size=3)
        residual = float(np.linalg.norm(np.cross(R @ x, R @ y) - R @ np.cross(x, y)))
        max_residual = max(max_residual, residual)
        violations += residual > tol
    return {"trials": trials, "violations": int(violations), "max_residual": max_residual, "tol": tol}


def affine_null_regression(seed: int = 126, max_dim: int = 12):
    """Regression witness that removing affine offsets leaves exact bilinearity."""
    rng = np.random.default_rng(seed)
    rows = []
    for n in range(1, max_dim + 1):
        B = rng.integers(-3, 4, size=(n, n, n)).astype(float)
        L = np.zeros((n, n))
        M = np.zeros((n, n))
        c = np.zeros(n)
        basis = [np.eye(n)[i] for i in range(n)] + [np.zeros(n)]
        left, right = null_axis_residuals(B, L, M, c, basis)
        x = rng.integers(-3, 4, size=n).astype(float)
        y = rng.integers(-3, 4, size=n).astype(float)
        equality = float(np.linalg.norm(biaffine_eval(x, y, B, L, M, c) - bilinear_eval(x, y, B)))
        rows.append({"n": n, "left_null_residual": left, "right_null_residual": right, "bilinear_residual": equality})
    return rows


def run_audit():
    exact = {str(n): exact_sign_survivor_count(n) for n in range(1, 13)}
    higher = {str(n): (1 if n == 1 else 6 if n == 3 else 0) for n in [16, 24, 32, 48, 64, 96, 128]}
    return {
        "theorem": "separate affinity + two-sided null absorption => bilinearity",
        "exact_even_sign_rank3_survivors_n1_to_n12": exact,
        "higher_dimension_analytic_survivors": higher,
        "affine_null_regression": affine_null_regression(),
        "so3_cross_covariance": so3_cross_covariance_audit(),
        "classification": ["PROVED", "CONDITIONAL", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_audit(), indent=2))
