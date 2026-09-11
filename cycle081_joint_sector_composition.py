"""Cycle 081: exact quadratic local/joint-sector composition audit.

The theorem audited here is
    E_AB = E_A + E_B + C_AB,
where E_d(rho)=d Tr(rho^2)-1 and
    C_AB=d_A d_B ||J_AB||_2^2 >= 0,
    J_AB=rho_AB-rho_A\otimes I_B/d_B-I_A/d_A\otimes rho_B+I_AB/(d_A d_B).
For product states C_AB=E_A E_B.
"""
from __future__ import annotations
import json
import numpy as np


def partial_traces(rho: np.ndarray, da: int, db: int):
    t = rho.reshape(da, db, da, db)
    return np.trace(t, axis1=1, axis2=3), np.trace(t, axis1=0, axis2=2)


def energy(rho: np.ndarray, d: int) -> float:
    return float(d * np.trace(rho @ rho).real - 1.0)


def joint_sector(rho: np.ndarray, da: int, db: int):
    ra, rb = partial_traces(rho, da, db)
    ia, ib = np.eye(da), np.eye(db)
    j = rho - np.kron(ra, ib / db) - np.kron(ia / da, rb) + np.eye(da * db) / (da * db)
    c = float(da * db * np.trace(j @ j).real)
    return ra, rb, j, c


def random_density(d: int, rng: np.random.Generator):
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def audit(seed: int = 8102026):
    rng = np.random.default_rng(seed)
    records = []
    for n in range(1, 13):
        reps = 6 if n <= 8 else 3
        for _ in range(reps):
            rho = random_density(n * n, rng)
            ra, rb, _, c = joint_sector(rho, n, n)
            eab, ea, eb = energy(rho, n * n), energy(ra, n), energy(rb, n)
            records.append((n, "full_random", c, abs(eab - ea - eb - c)))
    # Higher dimensions: exact same orthogonal decomposition in the commuting/diagonal sector.
    for n in (16, 24, 32, 48, 64, 96, 128):
        for _ in range(8):
            p = rng.random((n, n)); p /= p.sum()
            pa, pb = p.sum(1), p.sum(0)
            j = p - pa[:, None] / n - pb[None, :] / n + 1.0 / (n * n)
            eab = n * n * np.sum(p * p) - 1.0
            ea, eb = n * np.sum(pa * pa) - 1.0, n * np.sum(pb * pb) - 1.0
            c = n * n * np.sum(j * j)
            records.append((n, "classical_diagonal", float(c), float(abs(eab - ea - eb - c))))
    return {
        "cycle": 81,
        "classification": ["PROVED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED"],
        "breakthrough_candidate": False,
        "dimensions": sorted(set(r[0] for r in records)),
        "full_random_cases": sum(r[1] == "full_random" for r in records),
        "high_dim_commuting_cases": sum(r[1] == "classical_diagonal" for r in records),
        "min_joint_sector_energy": min(r[2] for r in records),
        "max_composition_residual": max(r[3] for r in records),
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
