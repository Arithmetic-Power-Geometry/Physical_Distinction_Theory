"""Cycle 062: exact pair-faithfulness dimension filter.

This audit does NOT claim a PDT-native derivation of n=3.  It proves the
conditional group-theoretic statement used in docs/cycle062_....md.

Hypotheses for the Euclidean reversible family G_n = SO(n):
  NCR: the connected reversible group is non-abelian.
  PIF: the pointwise stabilizer of two independent calibrated directions
       contains no nontrivial continuous reversible transformation.

For SO(n), Stab(e1,e2) ~= SO(n-2), so PIF holds iff n <= 3 (for n>=2),
while NCR holds iff n >= 3. Hence NCR + PIF selects n=3.
"""
from __future__ import annotations

import json
from pathlib import Path


def so_dimension(n: int) -> int:
    return n * (n - 1) // 2


def pair_stabilizer_dimension(n: int) -> int:
    if n < 2:
        raise ValueError("two independent calibrated directions require n >= 2")
    m = n - 2
    return m * (m - 1) // 2


def ncr(n: int) -> bool:
    # SO(1) trivial, SO(2) abelian, SO(n) non-abelian for n>=3.
    return n >= 3


def pif(n: int) -> bool:
    # No nontrivial *continuous* pointwise stabilizer of a 2-frame.
    return pair_stabilizer_dimension(n) == 0


def selected(n: int) -> bool:
    return n >= 2 and ncr(n) and pif(n)


def audit_dimensions(dimensions: list[int]) -> dict:
    rows = []
    for n in dimensions:
        if n < 2:
            rows.append({
                "n": n,
                "applicable": False,
                "reason": "two independent directions unavailable",
            })
            continue
        rows.append({
            "n": n,
            "applicable": True,
            "dim_SO_n": so_dimension(n),
            "dim_pair_stabilizer_SO_n_minus_2": pair_stabilizer_dimension(n),
            "NCR": ncr(n),
            "PIF": pif(n),
            "NCR_and_PIF": selected(n),
        })
    winners = [r["n"] for r in rows if r.get("NCR_and_PIF")]
    return {"rows": rows, "winners": winners, "pass": winners == [3]}


def main() -> None:
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128, 256]
    result = audit_dimensions(dims)
    out = Path("results") / "cycle062_pair_faithfulness_dimension_filter.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not result["pass"]:
        raise SystemExit("dimension-filter audit failed")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
