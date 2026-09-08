"""Purity-accessible corollary of the spectral coherence annulus theorem."""
from __future__ import annotations
import numpy as np


def purity(probabilities) -> float:
    p = np.asarray(probabilities, dtype=float)
    p = p / p.sum()
    return float(np.sum(p*p))


def spectral_floor(probabilities) -> float:
    p = np.asarray(probabilities, dtype=float)
    p = p / p.sum()
    return float(max(0.0, 2.0*np.max(p)-1.0))


def purity_floor(probabilities) -> float:
    """Observable lower bound |chi| >= max(0, 2 Tr(eta^2)-1)."""
    return float(max(0.0, 2.0*purity(probabilities)-1.0))


def audit(samples: int = 10000, max_dim: int = 12, seed: int = 260908):
    rng = np.random.default_rng(seed)
    worst = 0.0
    rows = []
    for d in range(2, max_dim + 1):
        for _ in range(samples // (max_dim-1)):
            p = rng.dirichlet(np.ones(d))
            pf, sf = purity_floor(p), spectral_floor(p)
            violation = pf - sf
            worst = max(worst, violation)
        rows.append((d, worst))
    return rows


if __name__ == "__main__":
    rows = audit()
    print("dimension,worst_bound_violation")
    for d, v in rows:
        print(f"{d},{v:.3e}")
    assert max(v for _, v in rows) <= 1e-12
