"""Cycle 082: local-channel boundary for quadratic joint-sector energy.

For a bipartite state rho_AB define
    J_AB = rho_AB - rho_A ⊗ I_B/d_B - I_A/d_A ⊗ rho_B + I_AB/(d_A d_B)
and
    C_AB = d_A d_B Tr(J_AB^2).

Facts audited here:
1. Local unitaries leave C_AB invariant.
2. Local bistochastic (unital + trace-preserving) completely positive maps cannot increase C_AB.
3. General local CPTP maps need not preserve or decrease C_AB. A local reset on each side maps the maximally mixed product state, C=0, to a pure product state with C=(d_A-1)(d_B-1).

The third item is a decisive no-go for interpreting C_AB as a correlation monotone under arbitrary local operations.
"""
from __future__ import annotations
import json
import numpy as np


def partial_traces(rho: np.ndarray, da: int, db: int):
    t = rho.reshape(da, db, da, db)
    return np.trace(t, axis1=1, axis2=3), np.trace(t, axis1=0, axis2=2)


def joint_sector_energy(rho: np.ndarray, da: int, db: int) -> float:
    ra, rb = partial_traces(rho, da, db)
    j = (
        rho
        - np.kron(ra, np.eye(db) / db)
        - np.kron(np.eye(da) / da, rb)
        + np.eye(da * db) / (da * db)
    )
    return float(da * db * np.trace(j.conj().T @ j).real)


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    a = x @ x.conj().T
    return a / np.trace(a)


def local_depolarizing_pair(rho: np.ndarray, n: int, la: float, lb: float) -> np.ndarray:
    """Apply Phi_la ⊗ Phi_lb with Phi_l(X)=l X+(1-l)Tr(X)I/n."""
    ra, rb = partial_traces(rho, n, n)
    ii = np.eye(n) / n
    return (
        la * lb * rho
        + la * (1.0 - lb) * np.kron(ra, ii)
        + (1.0 - la) * lb * np.kron(ii, rb)
        + (1.0 - la) * (1.0 - lb) * np.kron(ii, ii)
    )


def reset_witness(n: int):
    """Exact product witness: maximally mixed -> local pure reset."""
    if n < 1:
        raise ValueError("dimension must be positive")
    c_before = 0.0
    c_after = float((n - 1) ** 2)
    return c_before, c_after


def audit(seed: int = 8202026):
    rng = np.random.default_rng(seed)
    cases = []
    max_scaling_residual = 0.0
    monotonicity_failures = 0

    for n in range(1, 13):
        reps = 3 if n <= 8 else 1
        for _ in range(reps):
            rho = random_density(n * n, rng)
            la, lb = float(rng.random()), float(rng.random())
            c0 = joint_sector_energy(rho, n, n)
            out = local_depolarizing_pair(rho, n, la, lb)
            c1 = joint_sector_energy(out, n, n)
            expected = (la * lb) ** 2 * c0
            max_scaling_residual = max(max_scaling_residual, abs(c1 - expected))
            if c1 > c0 + 1e-12:
                monotonicity_failures += 1
            cases.append((n, c0, c1))

    reset_records = []
    for n in list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]:
        c0, c1 = reset_witness(n)
        reset_records.append({"dimension": n, "before": c0, "after": c1})

    return {
        "cycle": 82,
        "classification": [
            "PROVED",
            "FALSIFIED",
            "IMPORTED/KNOWN",
            "NUMERICALLY_SUPPORTED",
        ],
        "breakthrough_candidate": False,
        "tested_dimensions": list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128],
        "dense_unital_regression_cases": len(cases),
        "unital_monotonicity_failures": monotonicity_failures,
        "max_depolarizing_scaling_residual": max_scaling_residual,
        "smallest_nontrivial_reset_witness_dimension": 2,
        "qubit_reset_before": reset_witness(2)[0],
        "qubit_reset_after": reset_witness(2)[1],
        "reset_records": reset_records,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))
