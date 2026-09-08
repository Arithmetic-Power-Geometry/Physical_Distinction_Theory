"""Operational predictive-sufficiency audits for PDT resource statistics.

A resource statistic S is exactly sufficient for a prediction map Q iff Q is
constant on every fibre of S.  The utilities below test this condition on
finite/sampled families and quantify an unavoidable minimax error lower bound
from fibre diameters in total-variation distance.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Hashable, Iterable, Sequence

import numpy as np


@dataclass(frozen=True)
class FibreAudit:
    label: Hashable
    count: int
    tv_diameter: float
    minimax_error_lower_bound: float


def total_variation(p: Sequence[float], q: Sequence[float]) -> float:
    """Total-variation distance between two finite outcome distributions."""
    pa = np.asarray(p, dtype=float)
    qa = np.asarray(q, dtype=float)
    if pa.shape != qa.shape:
        raise ValueError("prediction vectors must have identical shapes")
    if np.any(pa < -1e-12) or np.any(qa < -1e-12):
        raise ValueError("probabilities must be non-negative")
    if not np.isclose(pa.sum(), 1.0, atol=1e-10) or not np.isclose(qa.sum(), 1.0, atol=1e-10):
        raise ValueError("each prediction vector must sum to one")
    return float(0.5 * np.abs(pa - qa).sum())


def audit_predictive_sufficiency(
    labels: Iterable[Hashable],
    predictions: Iterable[Sequence[float]],
    tol: float = 1e-12,
) -> tuple[list[FibreAudit], bool, float]:
    """Audit whether predictions are constant on fibres of a resource statistic.

    Returns (per_fibre_audits, exactly_sufficient, universal_error_lower_bound).
    The last quantity is one half of the largest within-fibre TV diameter. Any
    predictor that depends only on the supplied label has worst-case TV error at
    least this value on the sampled family.
    """
    labels = list(labels)
    predictions = [np.asarray(p, dtype=float) for p in predictions]
    if len(labels) != len(predictions):
        raise ValueError("labels and predictions must have equal length")
    if not labels:
        return [], True, 0.0

    groups: dict[Hashable, list[np.ndarray]] = defaultdict(list)
    for label, pred in zip(labels, predictions):
        # validation through self-distance
        total_variation(pred, pred)
        groups[label].append(pred)

    audits: list[FibreAudit] = []
    max_diameter = 0.0
    for label, group in groups.items():
        diameter = 0.0
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                diameter = max(diameter, total_variation(group[i], group[j]))
        max_diameter = max(max_diameter, diameter)
        audits.append(
            FibreAudit(
                label=label,
                count=len(group),
                tv_diameter=diameter,
                minimax_error_lower_bound=0.5 * diameter,
            )
        )

    audits.sort(key=lambda row: str(row.label))
    return audits, bool(max_diameter <= tol), 0.5 * max_diameter


def exact_factorization_criterion(
    labels: Iterable[Hashable],
    predictions: Iterable[Sequence[float]],
    tol: float = 1e-12,
) -> bool:
    """Finite-family version of Q = g o S iff Q is constant on fibres of S."""
    _, sufficient, _ = audit_predictive_sufficiency(labels, predictions, tol=tol)
    return sufficient
