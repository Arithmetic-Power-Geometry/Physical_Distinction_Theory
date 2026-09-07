"""Dimension-selection no-go audit for Physical Distinction Theory.

The current local axioms CEU, CER and RDE are satisfied by Euclidean balls B^n
for every n >= 2. Therefore these local assumptions alone cannot select n=3.
This script numerically stress-tests the constructive proof across dimensions.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def householder_map(x: np.ndarray, z: np.ndarray) -> np.ndarray:
    """Return an orthogonal map taking unit vector x to unit vector z."""
    x = np.asarray(x, float)
    z = np.asarray(z, float)
    if np.linalg.norm(x - z) < 1e-14:
        return np.eye(len(x))
    v = x - z
    v /= np.linalg.norm(v)
    return np.eye(len(x)) - 2.0 * np.outer(v, v)


def audit_dimensions(n_min: int = 2, n_max: int = 10, samples: int = 100, seed: int = 20260907) -> pd.DataFrame:
    rows = []
    for n in range(n_min, n_max + 1):
        rng = np.random.default_rng(seed + n)
        ceu_res = 0.0
        cer_res = 0.0
        rde_res = 0.0
        for _ in range(samples):
            a = rng.normal(size=n)
            a /= np.linalg.norm(a)

            # CEU: antipodal maximal pair erases to the center.
            ceu_res = max(ceu_res, float(np.linalg.norm(0.5 * (a + (-a)))))

            # CER: every radial point r a is a mixture of a and -a.
            r = float(rng.random())
            q = 0.5 * (1.0 + r)
            x = r * a
            x_reconstructed = q * a + (1.0 - q) * (-a)
            cer_res = max(cer_res, float(np.linalg.norm(x - x_reconstructed)))

            # RDE: O(n) acts transitively on the unit sphere. Constructive witness.
            b = rng.normal(size=n)
            b /= np.linalg.norm(b)
            H = householder_map(a, b)
            rde_res = max(
                rde_res,
                float(np.linalg.norm(H @ a - b)),
                float(np.linalg.norm(H.T @ H - np.eye(n))),
            )

        rows.append({
            "dimension_n": n,
            "CEU_max_residual": ceu_res,
            "CER_max_residual": cer_res,
            "RDE_max_residual": rde_res,
            "all_local_axioms_pass": bool(max(ceu_res, cer_res, rde_res) < 1e-10),
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    df = audit_dimensions()
    print(df.to_string(index=False))
    assert df["all_local_axioms_pass"].all()
