"""Cycle 047: exact three-axis kill test for the CHSH-matching capped composite.

Candidate correlation bodies in R^{n x n}:
  C_op  = {T: ||T||_op <= 1}
  C_cap = {T: ||T||_op <= 1 and ||T||_* <= 2}

For the rank-r diagonal functional M_r(T)=sum_{i=1}^r T_ii,
  sup_{C_op} |M_r|  = r,
  sup_{C_cap}|M_r| = min(r,2).
The r=3 witness therefore separates the bodies: 3 versus 2.
For an ordinary two-qubit singlet T=-I_3, |M_3|=3 and ||T||_*=3,
so C_cap excludes a standard quantum state despite reproducing CHSH 2 sqrt(2).
"""

from __future__ import annotations

import csv
import json
from pathlib import Path


def op_body_bound(rank: int) -> int:
    if rank < 0:
        raise ValueError("rank must be nonnegative")
    return rank


def capped_body_bound(rank: int, cap: int = 2) -> int:
    if rank < 0 or cap < 0:
        raise ValueError("rank and cap must be nonnegative")
    return min(rank, cap)


def singlet_triad() -> dict[str, int | bool]:
    nuclear_norm = 3
    op_norm = 1
    m3_abs = 3
    return {
        "dimension": 3,
        "operator_norm": op_norm,
        "nuclear_norm": nuclear_norm,
        "abs_M3": m3_abs,
        "in_C_op": op_norm <= 1,
        "in_C_cap": op_norm <= 1 and nuclear_norm <= 2,
    }


def audit(max_n: int = 12) -> list[dict[str, int | bool]]:
    rows = []
    for n in range(1, max_n + 1):
        r = min(3, n)
        op = op_body_bound(r)
        cap = capped_body_bound(r)
        rows.append({
            "n": n,
            "rank_probed": r,
            "C_op_bound": op,
            "C_cap_bound": cap,
            "separated": op != cap,
        })
    return rows


def write_results(root: str | Path = ".") -> None:
    root = Path(root)
    results = root / "results"
    results.mkdir(exist_ok=True)
    rows = audit(12)
    with (results / "cycle047_triad_correlation_audit.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    status = {
        "cycle": 47,
        "result": "DECISIVE FALSIFICATION",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN"],
        "claim": "The nuclear-norm-capped CHSH-matching composite is not a viable full qubit composite because it excludes the two-qubit singlet correlation tensor T=-I_3.",
        "smallest_decisive_dimension": 3,
        "C_op_M3_max": 3,
        "C_cap_M3_max": 2,
        "singlet_abs_M3": 3,
        "breakthrough_candidate": False,
    }
    (results / "cycle047_status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_results()
