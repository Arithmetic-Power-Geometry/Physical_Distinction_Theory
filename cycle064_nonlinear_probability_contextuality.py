"""Cycle 064: nonlinear probability-deformation contextuality witness.

Purpose
-------
Test a common same-input PDT escape route: keep the quantum microscopic state
and effects, but replace Born weights b_i = Tr(rho E_i) by a completion-normalized
nonlinear transform

    p_i = g(b_i) / sum_j g(b_j).

For g(x)=x**alpha with alpha != 1 this generally assigns a different probability
to the same effect when that effect is embedded in different POVM completions.
That is measurement contextuality, not a same-operational-primitives deformation
that preserves effect noncontextuality.

The explicit qubit witness for alpha=2 is exact:
  rho = |0><0|,
  E = diag(1/2,0).
  M2 = {E, I-E} has Born weights (1/2,1/2), hence p(E)=1/2.
  M3 = {E,F,G}, F=G=diag(1/4,1/2), has weights (1/2,1/4,1/4),
  hence p(E)=(1/2)^2 / [(1/2)^2+2(1/4)^2] = 2/3.

Classification: FALSIFIED route + IMPORTED/KNOWN foundational boundary.
No novelty claim is made for Gleason/Busch/Caves-Fuchs-Manne-Renes results.
"""

from fractions import Fraction
import math
import random


def power_rule(weights, alpha=2.0):
    vals = [float(w) ** alpha for w in weights]
    z = sum(vals)
    if z <= 0:
        raise ValueError("normalization denominator must be positive")
    return [v / z for v in vals]


def exact_qubit_witness():
    # Only Born weights are needed because all displayed effects are diagonal in rho.
    m2 = [Fraction(1, 2), Fraction(1, 2)]
    m3 = [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)]
    p2 = m2[0] ** 2 / sum(w ** 2 for w in m2)
    p3 = m3[0] ** 2 / sum(w ** 2 for w in m3)
    assert p2 == Fraction(1, 2)
    assert p3 == Fraction(2, 3)
    return {"p_same_effect_M2": p2, "p_same_effect_M3": p3, "gap": p3 - p2}


def split_context_witness(x, remainder_parts, alpha):
    """Compare {x,1-x} with {x,*remainder_parts}, sum parts=1-x."""
    assert 0 < x < 1
    assert all(r >= 0 for r in remainder_parts)
    assert abs(sum(remainder_parts) - (1.0 - x)) < 1e-12
    p_coarse = power_rule([x, 1.0 - x], alpha)[0]
    p_split = power_rule([x] + list(remainder_parts), alpha)[0]
    return p_coarse, p_split


def randomized_split_audit(seed=64064):
    rng = random.Random(seed)
    dimensions = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    alphas = [0.5, 1.5, 2.0, 3.0]
    rows = []
    for n in dimensions:
        trials = 200 if n <= 12 else 50
        contextual = 0
        tested = 0
        max_gap = 0.0
        for _ in range(trials):
            # n labels the ambient stress-test scale; the witness itself needs only
            # one retained outcome and a split remainder, so it embeds in every n.
            x = rng.uniform(0.05, 0.95)
            t = rng.uniform(0.05, 0.95)
            parts = [t * (1 - x), (1 - t) * (1 - x)]
            for alpha in alphas:
                a, b = split_context_witness(x, parts, alpha)
                gap = abs(a - b)
                tested += 1
                max_gap = max(max_gap, gap)
                if gap > 1e-12:
                    contextual += 1
        rows.append({
            "dimension": n,
            "tests": tested,
            "contextual_cases": contextual,
            "max_gap": max_gap,
        })
    return rows


if __name__ == "__main__":
    w = exact_qubit_witness()
    print("exact witness:", {k: str(v) for k, v in w.items()})
    rows = randomized_split_audit()
    total = sum(r["tests"] for r in rows)
    contextual = sum(r["contextual_cases"] for r in rows)
    print("randomized tests:", total)
    print("contextual cases:", contextual)
    print("noncontextual exceptions:", total - contextual)
    print("max observed gap:", max(r["max_gap"] for r in rows))
