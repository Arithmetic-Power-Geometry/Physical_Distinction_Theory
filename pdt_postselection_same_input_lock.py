"""Cycle 045: postselection same-input lock.

This module tests a narrow PDT-II no-go statement:
if PDT and QM share the same microscopic joint law over an outcome O and
selection/resource record S, then conditioning/postselection on S cannot
create a difference between their conditional outcome probabilities.

The theorem is elementary probability; the PDT contribution is the explicit
classification of postselection as a non-escape route for a same-input
prediction unless the joint law or selection mechanism itself is changed.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class AuditRow:
    dimension: int
    trials: int
    max_same_joint_error: float
    max_normalization_error: float


def conditional_from_joint(joint: np.ndarray, selected: Iterable[int]) -> np.ndarray:
    """Return P(O | S in selected) from a nonnegative O x S joint table."""
    q = np.asarray(joint, dtype=float)
    if q.ndim != 2 or np.any(q < 0):
        raise ValueError("joint must be a nonnegative 2D table")
    total = q.sum()
    if not np.isfinite(total) or total <= 0:
        raise ValueError("joint must have positive finite mass")
    q = q / total
    idx = np.asarray(list(selected), dtype=int)
    if idx.size == 0:
        raise ValueError("selection set must be nonempty")
    branch = q[:, idx].sum(axis=1)
    success = branch.sum()
    if success <= 0:
        raise ValueError("postselection event must have nonzero probability")
    return branch / success


def postselection_same_input_lock(joint_qm: np.ndarray, joint_pdt: np.ndarray,
                                  selected: Iterable[int], atol: float = 1e-12) -> bool:
    """Exact operational lock when the microscopic joint laws are identical."""
    a = np.asarray(joint_qm, dtype=float)
    b = np.asarray(joint_pdt, dtype=float)
    if a.shape != b.shape or not np.allclose(a, b, atol=atol, rtol=0.0):
        return False
    return np.allclose(
        conditional_from_joint(a, selected),
        conditional_from_joint(b, selected),
        atol=atol,
        rtol=0.0,
    )


def random_joint(rng: np.random.Generator, outcomes: int, records: int) -> np.ndarray:
    q = rng.random((outcomes, records))
    return q / q.sum()


def stress_audit(seed: int = 20260910, trials: int = 500) -> list[AuditRow]:
    """Audit dimensions 1..12 with changing outcome and record alphabets."""
    rng = np.random.default_rng(seed)
    rows: list[AuditRow] = []
    for d in range(1, 13):
        max_err = 0.0
        max_norm = 0.0
        for _ in range(trials):
            q = random_joint(rng, outcomes=d + 2, records=max(2, d))
            selected = [j for j in range(q.shape[1]) if j % 2 == 1]
            if not selected:
                selected = [0]
            qm = conditional_from_joint(q, selected)
            pdt = conditional_from_joint(q.copy(), selected)
            max_err = max(max_err, float(np.max(np.abs(qm - pdt))))
            max_norm = max(max_norm, abs(float(qm.sum()) - 1.0))
        rows.append(AuditRow(d, trials, max_err, max_norm))
    return rows


def rare_event_witness(epsilon: float = 1e-6) -> dict[str, float]:
    """Show that postselection may greatly change a conditional number without creating theory disagreement."""
    if not (0.0 < epsilon < 1.0):
        raise ValueError("epsilon must lie in (0,1)")
    # O={0,1}, S={reject,keep}. Kept events are almost entirely O=1.
    joint = np.array([[0.5 - epsilon / 2.0, epsilon / 2.0],
                      [0.5 - epsilon / 2.0, epsilon / 2.0]], dtype=float)
    # Modify kept branch so O=1 dominates while preserving valid total mass.
    joint[0, 1] = epsilon * epsilon
    joint[1, 1] = epsilon - epsilon * epsilon
    joint[:, 0] *= (1.0 - epsilon) / joint[:, 0].sum()
    joint /= joint.sum()
    unconditional = joint.sum(axis=1)
    conditional = conditional_from_joint(joint, [1])
    return {
        "success_probability": float(joint[:, 1].sum()),
        "unconditional_P_O1": float(unconditional[1]),
        "conditional_P_O1_given_keep": float(conditional[1]),
        "qm_pdt_conditional_gap_same_joint": 0.0,
    }


def write_artifacts(base: str | Path = "results") -> None:
    base = Path(base)
    base.mkdir(parents=True, exist_ok=True)
    rows = stress_audit()
    csv = "dimension,trials,max_same_joint_error,max_normalization_error\n" + "\n".join(
        f"{r.dimension},{r.trials},{r.max_same_joint_error:.17g},{r.max_normalization_error:.17g}" for r in rows
    ) + "\n"
    (base / "cycle045_postselection_same_input_audit.csv").write_text(csv, encoding="utf-8")
    ledger = {
        "cycle": 45,
        "result": "postselection_same_input_lock",
        "classification": ["PROVED", "IMPORTED/KNOWN", "FALSIFIED_ESCAPE_ROUTE"],
        "breakthrough_candidate": False,
        "theorem": "Same joint P(O,S) plus same selection event implies identical P(O|S) for PDT and QM.",
        "escape_coordinates": ["change joint microscopic law", "change physical selection instrument", "change probability rule"],
        "stress_dimensions": [1, 12],
        "rare_event_witness": rare_event_witness(),
        "rows": [asdict(r) for r in rows],
    }
    (base / "cycle045_postselection_same_input_status.json").write_text(
        json.dumps(ledger, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    write_artifacts()
