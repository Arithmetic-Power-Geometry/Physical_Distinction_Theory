"""Resource-coarse-graining kill test for PDT same-input prediction claims.

A resource restriction that is only classical post-processing of a fixed
microscopic outcome distribution cannot create a PDT-vs-QM discrepancy.
"""
from __future__ import annotations

import numpy as np


def normalize_probability(p):
    p = np.asarray(p, dtype=float)
    if p.ndim != 1 or np.any(p < 0):
        raise ValueError("p must be a nonnegative vector")
    s = p.sum()
    if s <= 0:
        raise ValueError("p must have positive mass")
    return p / s


def normalize_kernel_columns(kernel):
    k = np.asarray(kernel, dtype=float)
    if k.ndim != 2 or np.any(k < 0):
        raise ValueError("kernel must be a nonnegative matrix")
    sums = k.sum(axis=0, keepdims=True)
    if np.any(sums <= 0):
        raise ValueError("every input column must have positive mass")
    return k / sums


def coarse_grain(p, kernel):
    p = normalize_probability(p)
    k = normalize_kernel_columns(kernel)
    if k.shape[1] != p.size:
        raise ValueError("kernel input dimension must match p")
    return k @ p


def total_variation(p, q):
    p = normalize_probability(p)
    q = normalize_probability(q)
    if p.size != q.size:
        raise ValueError("probability vectors must have equal length")
    return 0.5 * np.abs(p - q).sum()


def power_reweight(p, alpha=1.3):
    """A deliberately nonlinear response-law deformation for kill testing."""
    p = normalize_probability(p)
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    q = p ** alpha
    return q / q.sum()


def audit(seed=20260908, max_dimension=12, alpha=1.3):
    rng = np.random.default_rng(seed)
    rows = []
    for d in range(1, max_dimension + 1):
        microscopic_outcomes = max(2, d + 1)
        accessible_outcomes = max(2, d // 2 + 2)
        p = normalize_probability(rng.random(microscopic_outcomes))
        kernel = normalize_kernel_columns(
            rng.random((accessible_outcomes, microscopic_outcomes))
        )
        resource_qm = coarse_grain(p, kernel)
        resource_pdt_if_only_coarse = coarse_grain(p, kernel)
        nonlinear = power_reweight(resource_qm, alpha=alpha)
        rows.append(
            {
                "dimension": d,
                "microscopic_outcomes": microscopic_outcomes,
                "accessible_outcomes": accessible_outcomes,
                "same_coarse_graining_max_abs_error": float(
                    np.max(np.abs(resource_qm - resource_pdt_if_only_coarse))
                ),
                "nonlinear_deformation_tv_gap": float(
                    total_variation(resource_qm, nonlinear)
                ),
            }
        )
    return rows
