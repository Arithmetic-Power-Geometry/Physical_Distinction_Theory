"""Cycle 122: resource-saturation closure theorem and counterexample audit.

Theorem (conditional, exact): Let A=V⊕M and Q(v,m)=Q_V(v)+H(m), where
H>=0 and H(m)=0 iff m=0. For visible inputs x,y∈V, suppose a declared
composition budget B(x,y) satisfies both

    Q(C(x,y)) = B(x,y)                 (total-budget conservation)
    Q_V(pi C(x,y)) = B(x,y)            (visible-budget saturation).

Then H(hidden(C(x,y)))=0 and therefore C(x,y)∈V.

This is not claimed as a PDT-native derivation: the open physical burden is to
derive the visible-saturation law independently from PDT primitives. Total
conservation alone is insufficient; the audit constructs leaking budget splits.
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def hidden_resource(total_budget: int, visible_budget: int) -> int:
    """Exact sector resource implied by an additive resource ledger."""
    return total_budget - visible_budget


def saturation_forces_closure(total_budget: int, visible_budget: int) -> bool:
    """Return theorem conclusion under exact visible saturation."""
    if total_budget < 0 or visible_budget < 0:
        raise ValueError("resources must be nonnegative")
    if total_budget != visible_budget:
        return False
    return hidden_resource(total_budget, visible_budget) == 0


def leaking_split(total_budget: int, delta: int) -> tuple[int, int]:
    """Countermodel to total conservation alone: Qvis=B-delta, H=delta."""
    if total_budget <= 0:
        raise ValueError("positive budget required")
    if not (1 <= delta <= total_budget):
        raise ValueError("delta must lie in [1,total_budget]")
    return total_budget - delta, delta


@dataclass
class Audit:
    dimensions: list[int]
    randomized_trials: int
    saturation_failures: int
    leaking_total_conservation_witnesses: int
    smallest_leak_budget: int
    smallest_leak_visible: int
    smallest_leak_hidden: int


def run_audit(seed: int = 122, trials_per_dimension: int = 50) -> Audit:
    rng = random.Random(seed)
    trials = 0
    saturation_failures = 0
    leaking = 0
    smallest = None

    for n in DIMS:
        for _ in range(trials_per_dimension):
            # Microscopic inputs are represented only to produce a nonnegative,
            # dimension-dependent exact integer budget. The theorem itself is
            # independent of this particular budget function.
            x = [rng.randint(-3, 3) for _ in range(n)]
            y = [rng.randint(-3, 3) for _ in range(n)]
            qx = sum(a * a for a in x)
            qy = sum(b * b for b in y)
            B = qx * qy

            # Exact theorem check: Qtotal=B and Qvisible=B imply H=0.
            if not saturation_forces_closure(B, B):
                saturation_failures += 1

            # Adversarial check: whenever B>0, exact total conservation permits
            # a nonzero hidden allocation unless visible saturation is imposed.
            if B > 0:
                delta = rng.randint(1, B)
                qvis, h = leaking_split(B, delta)
                assert qvis + h == B
                if h > 0:
                    leaking += 1
                    candidate = (B, qvis, h)
                    if smallest is None or candidate < smallest:
                        smallest = candidate
            trials += 1

    if smallest is None:
        smallest = (1, 0, 1)
    return Audit(DIMS, trials, saturation_failures, leaking, *smallest)


def main() -> None:
    audit = run_audit()
    payload = asdict(audit)
    payload["classification"] = {
        "saturation_closure_theorem": "PROVED / CONDITIONAL",
        "total_conservation_implies_closure": "FALSIFIED",
        "pdt_native_visible_saturation_derivation": "OPEN",
        "breakthrough_candidate": False,
    }
    out = Path("results") / "cycle122_resource_saturation_closure.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
