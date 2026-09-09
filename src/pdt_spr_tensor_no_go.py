"""Cycle 028: tensor-composition no-go test for universal Single-Plane Reversibility (SPR).

SPR requires rank(A) <= 2 for every elementary infinitesimal reversible generator A.
Under standard tensor-product composition, a local generator A on subsystem A lifts to
A \otimes I_B. Matrix-rank multiplicativity gives
rank(A \otimes I_B) = rank(A) * dim(B).
Thus any nonzero single-plane generator with rank(A)=2 violates universal SPR on the
composite whenever dim(B)>=2.
"""
from __future__ import annotations

import numpy as np


def single_plane_generator(n: int, i: int = 0, j: int = 1) -> np.ndarray:
    if n < 2:
        raise ValueError("n must be at least 2")
    if i == j or min(i, j) < 0 or max(i, j) >= n:
        raise ValueError("invalid plane indices")
    A = np.zeros((n, n), dtype=float)
    A[i, j] = -1.0
    A[j, i] = 1.0
    return A


def tensor_lift_local_generator(A: np.ndarray, dim_b: int) -> np.ndarray:
    if dim_b < 1:
        raise ValueError("dim_b must be positive")
    return np.kron(A, np.eye(dim_b))


def predicted_tensor_rank(local_rank: int, dim_b: int) -> int:
    if local_rank < 0 or dim_b < 1:
        raise ValueError("invalid rank or dimension")
    return local_rank * dim_b


def universal_spr_survives_tensor_lift(local_rank: int, dim_b: int) -> bool:
    return predicted_tensor_rank(local_rank, dim_b) <= 2


def factor_local_normalized_rank(lifted_rank: int, spectator_dim: int) -> float:
    """Composition-compatible diagnostic that removes spectator multiplicity."""
    if spectator_dim < 1:
        raise ValueError("spectator_dim must be positive")
    return lifted_rank / spectator_dim


if __name__ == "__main__":
    for n in range(2, 13):
        A = single_plane_generator(n)
        rA = int(np.linalg.matrix_rank(A))
        for d in range(1, 13):
            lifted = tensor_lift_local_generator(A, d)
            r = int(np.linalg.matrix_rank(lifted))
            expected = predicted_tensor_rank(rA, d)
            assert r == expected
            assert universal_spr_survives_tensor_lift(rA, d) == (d == 1)
    print("Cycle 028 tensor-rank checks passed for local n=2..12, spectator d=1..12")
