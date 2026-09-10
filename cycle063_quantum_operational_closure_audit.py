"""Cycle 063: operational-closure kill test for PDT-II same-input deviations.

This module does not prove the theorem numerically; the proof is in
``docs/cycle063_quantum_operational_closure_no_go.md``.  It provides an
independent finite-dimensional regression audit of the theorem's hypotheses:
standard density operators, POVMs, tensor products, CPTP/unitary dynamics and
classical stochastic resource-window post-processing.

A PDT candidate satisfying all of those hypotheses is only a re-description of
the same operational experiment and therefore cannot change outcome
probabilities.  Any genuine same-input deviation must explicitly leave this
closure class.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

import numpy as np

TOL = 5e-11


def _random_density(d: int, rng: np.random.Generator, pure: bool) -> np.ndarray:
    if pure:
        v = rng.normal(size=d) + 1j * rng.normal(size=d)
        v /= np.linalg.norm(v)
        return np.outer(v, v.conj())
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def _random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(a)
    phase = np.diag(r)
    phase = np.where(np.abs(phase) > 0, phase / np.abs(phase), 1.0)
    return q @ np.diag(phase.conj())


def _random_povm(d: int, m: int, rng: np.random.Generator) -> list[np.ndarray]:
    raw = []
    for _ in range(m):
        a = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        raw.append(a @ a.conj().T)
    s = sum(raw)
    vals, vecs = np.linalg.eigh(s)
    invsqrt = (vecs * (1.0 / np.sqrt(vals))) @ vecs.conj().T
    return [invsqrt @ x @ invsqrt for x in raw]


def _random_kernel(k: int, m: int, rng: np.random.Generator) -> np.ndarray:
    # K[y,x] = P(y|x); columns sum to one.
    kx = rng.random((k, m))
    return kx / np.sum(kx, axis=0, keepdims=True)


def qm_probabilities(rho: np.ndarray, effects: Iterable[np.ndarray]) -> np.ndarray:
    p = np.array([np.trace(rho @ e).real for e in effects], dtype=float)
    p[np.abs(p) < 1e-14] = 0.0
    return p


def pdt_closed_probabilities(rho: np.ndarray, effects: Iterable[np.ndarray]) -> np.ndarray:
    """Independent implementation under the closure hypotheses.

    If PDT keeps the same state and effects and retains the Born pairing, its
    probabilities are fixed by that pairing.  Computing via an eigendecomposition
    avoids merely calling ``qm_probabilities`` again.
    """
    vals, vecs = np.linalg.eigh(rho)
    out = []
    for e in effects:
        total = 0.0
        for lam, v in zip(vals, vecs.T):
            total += float(lam.real) * float(np.vdot(v, e @ v).real)
        out.append(total)
    p = np.asarray(out, dtype=float)
    p[np.abs(p) < 1e-14] = 0.0
    return p


@dataclass
class AuditRow:
    dimension: int
    pure: bool
    direct_gap: float
    resource_gap: float
    unitary_gap: float
    normalization_error: float


def run_audit(
    dimensions: Iterable[int] = tuple(range(1, 13)) + (16, 24, 32, 48, 64),
    trials_low: int = 100,
    trials_high: int = 20,
    seed: int = 63063,
) -> dict:
    rng = np.random.default_rng(seed)
    rows: list[AuditRow] = []
    for d in dimensions:
        trials = trials_low if d <= 12 else trials_high
        for t in range(trials):
            pure = bool(t % 2)
            rho = _random_density(d, rng, pure=pure)
            effects = _random_povm(d, 3, rng)
            p_qm = qm_probabilities(rho, effects)
            p_pdt = pdt_closed_probabilities(rho, effects)

            K = _random_kernel(2, 3, rng)
            r_qm = K @ p_qm
            r_pdt = K @ p_pdt

            U = _random_unitary(d, rng)
            rho_u = U @ rho @ U.conj().T
            p_u_qm = qm_probabilities(rho_u, effects)
            p_u_pdt = pdt_closed_probabilities(rho_u, effects)

            rows.append(
                AuditRow(
                    dimension=d,
                    pure=pure,
                    direct_gap=float(np.max(np.abs(p_qm - p_pdt))),
                    resource_gap=float(np.max(np.abs(r_qm - r_pdt))),
                    unitary_gap=float(np.max(np.abs(p_u_qm - p_u_pdt))),
                    normalization_error=float(abs(np.sum(p_qm) - 1.0)),
                )
            )

    max_direct = max(r.direct_gap for r in rows)
    max_resource = max(r.resource_gap for r in rows)
    max_unitary = max(r.unitary_gap for r in rows)
    max_norm = max(r.normalization_error for r in rows)
    return {
        "cycle": 63,
        "classification": ["PROVED", "IMPORTED/KNOWN", "FALSIFIED"],
        "falsified_route": "bookkeeping-only same-input deviation inside unchanged finite-dimensional quantum operational closure",
        "seed": seed,
        "cases": len(rows),
        "dimensions": sorted(set(r.dimension for r in rows)),
        "max_direct_gap": max_direct,
        "max_resource_gap": max_resource,
        "max_unitary_gap": max_unitary,
        "max_normalization_error": max_norm,
        "failures": int(sum(
            r.direct_gap > TOL or r.resource_gap > TOL or
            r.unitary_gap > TOL or r.normalization_error > TOL
            for r in rows
        )),
        "status": "PASS" if max(max_direct, max_resource, max_unitary, max_norm) <= TOL else "FAIL",
    }


def main() -> None:
    result = run_audit()
    out = Path("results") / "cycle063_quantum_operational_closure.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
