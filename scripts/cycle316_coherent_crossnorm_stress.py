"""Cycle 316 regression: injective/projective Euclidean tensor norms separate on I_d.

For R^d ⊗ R^d represented as matrices, epsilon = operator norm and pi = nuclear norm.
This script checks d=1..12 and simple-tensor product exactness on deterministic vectors.
"""
import numpy as np


def norms(a: np.ndarray) -> tuple[float, float]:
    s = np.linalg.svd(a, compute_uv=False)
    return float(s.max(initial=0.0)), float(s.sum())


def run() -> None:
    for d in range(1, 13):
        eye = np.eye(d)
        eps, pi = norms(eye)
        assert np.isclose(eps, 1.0)
        assert np.isclose(pi, float(d))

        x = np.arange(1, d + 1, dtype=float)
        y = np.arange(d, 0, -1, dtype=float)
        simple = np.outer(x, y)
        eps_s, pi_s = norms(simple)
        target = np.linalg.norm(x) * np.linalg.norm(y)
        assert np.isclose(eps_s, target)
        assert np.isclose(pi_s, target)


if __name__ == "__main__":
    run()
    print("cycle316: d=1..12 coherent-crossnorm regression passed")
