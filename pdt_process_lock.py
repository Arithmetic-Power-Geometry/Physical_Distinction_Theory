"""PDT multi-time same-process lock audit.

The theorem encoded here is deliberately a no-go result: if PDT and standard
quantum mechanics use the same multi-time process and the same intervention
sequence, non-Markovian memory by itself cannot create a same-input prediction
difference.  Any common classical resource post-processing preserves equality
and contracts total-variation distance.
"""

from __future__ import annotations

import numpy as np


def total_variation(p: np.ndarray, q: np.ndarray) -> float:
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    return 0.5 * float(np.sum(np.abs(p - q)))


def apply_stochastic_kernel(kernel: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Apply a column-stochastic classical post-processing kernel."""
    kernel = np.asarray(kernel, dtype=float)
    p = np.asarray(p, dtype=float)
    if kernel.ndim != 2 or p.ndim != 1 or kernel.shape[1] != p.size:
        raise ValueError("incompatible kernel/distribution dimensions")
    if np.any(kernel < -1e-12):
        raise ValueError("kernel must be nonnegative")
    if not np.allclose(kernel.sum(axis=0), 1.0, atol=1e-10):
        raise ValueError("kernel must be column stochastic")
    return kernel @ p


def memory_process_distribution(theta: float, phi: float, memory_strength: float) -> np.ndarray:
    """A normalized four-outcome two-time toy process with explicit memory.

    This is not presented as experimental data or a new physical model.  It is
    a deterministic stress-test family whose second-time bias depends on the
    first outcome whenever ``memory_strength != 0``.
    """
    m = float(np.clip(memory_strength, -1.0, 1.0))
    p0 = 0.5 * (1.0 + np.cos(theta))
    p1 = 1.0 - p0
    # Conditional second-time probabilities retain the first-time record.
    base = 0.5 * (1.0 + np.cos(phi))
    c0 = float(np.clip(base + 0.25 * m * np.sin(theta), 0.0, 1.0))
    c1 = float(np.clip(base - 0.25 * m * np.sin(theta), 0.0, 1.0))
    out = np.array([p0 * c0, p0 * (1.0 - c0), p1 * c1, p1 * (1.0 - c1)])
    return out / out.sum()


def same_process_lock(theta: float, phi: float, memory_strength: float, kernel: np.ndarray) -> dict:
    """Audit equality and TV contraction for a shared non-Markovian process."""
    p_qm = memory_process_distribution(theta, phi, memory_strength)
    # Under the theorem hypothesis PDT uses the identical microscopic process
    # and identical interventions; hence the pre-resource distribution is same.
    p_pdt = memory_process_distribution(theta, phi, memory_strength)
    q_qm = apply_stochastic_kernel(kernel, p_qm)
    q_pdt = apply_stochastic_kernel(kernel, p_pdt)
    return {
        "tv_micro": total_variation(p_qm, p_pdt),
        "tv_resource": total_variation(q_qm, q_pdt),
        "equal_micro": bool(np.allclose(p_qm, p_pdt, atol=1e-12)),
        "equal_resource": bool(np.allclose(q_qm, q_pdt, atol=1e-12)),
    }


def contraction_audit(kernel: np.ndarray, p: np.ndarray, q: np.ndarray) -> tuple[float, float]:
    """Return TV before/after common classical resource post-processing."""
    before = total_variation(p, q)
    after = total_variation(apply_stochastic_kernel(kernel, p), apply_stochastic_kernel(kernel, q))
    return before, after
