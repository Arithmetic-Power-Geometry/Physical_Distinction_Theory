"""Resource-filtration ambiguity utilities for Physical Distinction Theory.

These functions quantify how much microscopic predictive ambiguity remains after
coarse-graining inputs through a resource statistic.  The mathematics is elementary
partition/factorization theory; PDT uses it as a disciplined kill-test for resource-only
predictors.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Hashable, Iterable, Sequence

import numpy as np


def tv(p: Sequence[float], q: Sequence[float]) -> float:
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    return 0.5 * float(np.abs(p - q).sum())


def fibre_diameter(labels: Iterable[Hashable], predictions: Sequence[Sequence[float]]) -> float:
    labels = list(labels)
    preds = [np.asarray(x, dtype=float) for x in predictions]
    if len(labels) != len(preds):
        raise ValueError("labels and predictions must have the same length")
    groups: dict[Hashable, list[int]] = defaultdict(list)
    for i, lab in enumerate(labels):
        groups[lab].append(i)
    diameter = 0.0
    for idxs in groups.values():
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                diameter = max(diameter, tv(preds[idxs[a]], preds[idxs[b]]))
    return diameter


def is_refinement(coarse: Iterable[Hashable], fine: Iterable[Hashable]) -> bool:
    """Return True iff equality under fine labels implies equality under coarse labels."""
    coarse = list(coarse)
    fine = list(fine)
    if len(coarse) != len(fine):
        return False
    seen: dict[Hashable, Hashable] = {}
    for c, f in zip(coarse, fine):
        if f in seen and seen[f] != c:
            return False
        seen[f] = c
    return True


def revelation_increment(coarse: Iterable[Hashable], fine: Iterable[Hashable], predictions: Sequence[Sequence[float]]) -> float:
    """Decrease in worst-case within-fibre predictive ambiguity under refinement."""
    coarse = list(coarse)
    fine = list(fine)
    if not is_refinement(coarse, fine):
        raise ValueError("fine statistic must refine coarse statistic")
    return fibre_diameter(coarse, predictions) - fibre_diameter(fine, predictions)


def chain_revelation(label_chain: Sequence[Sequence[Hashable]], predictions: Sequence[Sequence[float]]) -> tuple[list[float], float]:
    """Return successive ambiguity drops and their telescoping total."""
    if len(label_chain) < 2:
        return [], 0.0
    drops: list[float] = []
    for a, b in zip(label_chain[:-1], label_chain[1:]):
        drops.append(revelation_increment(a, b, predictions))
    total = fibre_diameter(label_chain[0], predictions) - fibre_diameter(label_chain[-1], predictions)
    return drops, total
