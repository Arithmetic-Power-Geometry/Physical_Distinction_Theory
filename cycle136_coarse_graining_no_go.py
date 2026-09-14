"""Cycle 136: universal coarse-graining no-go for scalar probability reweighting.

Hypotheses
----------
Let raw mutually exclusive event weights add under coarse-graining. Let a scalar
rule f:[0,inf)->[0,inf) satisfy f(0)=0 and f(x)>0 for x>0, and define contextwise
probabilities by

    P_f(i | q) = f(q_i) / sum_j f(q_j).

Require exact event consistency when outcomes of weights a,b are merged while an
outside outcome c>0 remains. Then

    [f(a)+f(b)]/[f(a)+f(b)+f(c)]
      = f(a+b)/[f(a+b)+f(c)]

for all a,b>=0,c>0. Cross multiplication and f(c)>0 imply
f(a+b)=f(a)+f(b). Nonnegative additivity makes f monotone, hence linear on the
nonnegative reals. Thus f(x)=C x; calibration f(1)=1 gives f(x)=x.

Therefore genuinely nonlinear scalar escort/reweighting rules cannot produce a
same-input deviation while preserving these standard coarse-graining semantics.
The result is conditional on additive raw merged weights and contextwise scalar
normalization. It does not exclude nonseparable/context-dependent/resource-
dependent structural probability laws or altered event composition.

This strengthens Cycle 064 from explicit contextuality witnesses to an exact
functional characterization. The additive-function mathematics is classical;
no novelty claim is made for that ingredient.
"""
from __future__ import annotations

import json
import random
from dataclasses import asdict, dataclass
from fractions import Fraction

OUTCOME_COUNTS = list(range(3, 13)) + [16, 24, 32, 48, 64, 96, 128]
ALPHAS = [0.5, 1.0, 2.0, 3.0]
SEED = 136
TOL = 1e-12


def merged_event_probabilities(weights: list[float], alpha: float, i: int = 0, j: int = 1) -> tuple[float, float]:
    if len(weights) < 3:
        raise ValueError("at least three outcomes are needed for a nontrivial merge with an outside event")
    if i == j:
        raise ValueError("merged outcomes must be distinct")
    if any(x < 0 for x in weights) or not any(x > 0 for x in weights):
        raise ValueError("weights must be nonnegative with positive total")
    transformed = [x ** alpha for x in weights]
    fine = (transformed[i] + transformed[j]) / sum(transformed)
    merged_weight = weights[i] + weights[j]
    outside = sum(transformed[k] for k in range(len(weights)) if k not in (i, j))
    coarse = merged_weight ** alpha / (merged_weight ** alpha + outside)
    return fine, coarse


def exact_quadratic_witness() -> dict[str, str]:
    a, b, c = Fraction(1), Fraction(2), Fraction(3)
    fine = (a*a + b*b) / (a*a + b*b + c*c)
    coarse = (a+b)*(a+b) / ((a+b)*(a+b) + c*c)
    gap = coarse - fine
    assert fine == Fraction(5, 14)
    assert coarse == Fraction(1, 2)
    assert gap == Fraction(1, 7)
    return {"weights": "(1,2,3)", "rule": "f(q)=q^2", "fine_merged": str(fine), "coarse_merged": str(coarse), "gap": str(gap)}


@dataclass
class Audit:
    outcome_counts: list[int]
    total_cases_per_alpha: int
    linear_failures: int
    nonlinear_cases: int
    nonlinear_violations: int
    alpha_half_violations: int
    alpha_two_violations: int
    alpha_three_violations: int
    max_linear_residual: float
    smallest_observed_nonlinear_gap: float
    largest_observed_nonlinear_gap: float
    exact_witness: dict[str, str]
    theorem_status: str
    nonlinear_scalar_route_status: str


def run_audit() -> Audit:
    rng = random.Random(SEED)
    per_alpha = {a: {"cases": 0, "violations": 0, "max_gap": 0.0, "min_positive_gap": float("inf")} for a in ALPHAS}
    for m in OUTCOME_COUNTS:
        trials = 100 if m <= 12 else 40
        for _ in range(trials):
            # Keep weights bounded away from zero to stress the genuine, nondegenerate regime.
            weights = [0.1 + rng.random() for _ in range(m)]
            for alpha in ALPHAS:
                fine, coarse = merged_event_probabilities(weights, alpha)
                gap = abs(fine - coarse)
                s = per_alpha[alpha]
                s["cases"] += 1
                s["violations"] += int(gap > TOL)
                s["max_gap"] = max(s["max_gap"], gap)
                if gap > 0:
                    s["min_positive_gap"] = min(s["min_positive_gap"], gap)

    nonlinear = [0.5, 2.0, 3.0]
    return Audit(
        outcome_counts=OUTCOME_COUNTS,
        total_cases_per_alpha=per_alpha[1.0]["cases"],
        linear_failures=per_alpha[1.0]["violations"],
        nonlinear_cases=sum(per_alpha[a]["cases"] for a in nonlinear),
        nonlinear_violations=sum(per_alpha[a]["violations"] for a in nonlinear),
        alpha_half_violations=per_alpha[0.5]["violations"],
        alpha_two_violations=per_alpha[2.0]["violations"],
        alpha_three_violations=per_alpha[3.0]["violations"],
        max_linear_residual=per_alpha[1.0]["max_gap"],
        smallest_observed_nonlinear_gap=min(per_alpha[a]["min_positive_gap"] for a in nonlinear),
        largest_observed_nonlinear_gap=max(per_alpha[a]["max_gap"] for a in nonlinear),
        exact_witness=exact_quadratic_witness(),
        theorem_status="CONDITIONAL/PROVED",
        nonlinear_scalar_route_status="FALSIFIED",
    )


def main() -> None:
    print(json.dumps(asdict(run_audit()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
