"""Cycle 133: resolved-channel mixing selects quadratic composite resource.

This module supplies deterministic numerical stress tests and exact rational witnesses.
The rigorous theorem proof is recorded in cycle133_resolved_channel_mixing_note.md.
"""
from __future__ import annotations

import json
import math
import random
from fractions import Fraction
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 133
TRIALS_PER_DIMENSION = 50


def resolved_lp_resource(values, p: int):
    return sum(abs(x) ** p for x in values)


def rotate_pair(values, i: int, j: int, theta: float):
    out = list(values)
    c, s = math.cos(theta), math.sin(theta)
    a, b = values[i], values[j]
    out[i] = c * a - s * b
    out[j] = s * a + c * b
    return out


def signed_permutation(values, rng: random.Random):
    out = list(values)
    rng.shuffle(out)
    return [(-x if rng.randrange(2) else x) for x in out]


def exact_345_witness():
    result = {}
    for p in (1, 2, 4):
        value = abs(Fraction(3, 5)) ** p + abs(Fraction(4, 5)) ** p
        delta = value - 1
        result[str(p)] = {
            "mixed_resource": f"{value.numerator}/{value.denominator}",
            "difference_from_1": f"{delta.numerator}/{delta.denominator}",
        }
    return result


def run_stress():
    rng = random.Random(SEED)
    quadratic_checks = quadratic_failures = 0
    discrete_checks = discrete_failures = 0
    max_relative_quadratic_residual = 0.0

    for n in DIMS:
        if n < 2:
            continue
        for _ in range(TRIALS_PER_DIMENSION):
            values = [rng.gauss(0.0, 1.0) for _ in range(n)]
            i, j = rng.sample(range(n), 2)
            theta = rng.uniform(-math.pi, math.pi)
            mixed = rotate_pair(values, i, j, theta)
            before = resolved_lp_resource(values, 2)
            after = resolved_lp_resource(mixed, 2)
            residual = abs(after - before) / max(1.0, before)
            quadratic_checks += 1
            max_relative_quadratic_residual = max(
                max_relative_quadratic_residual, residual
            )
            if residual > 1e-12:
                quadratic_failures += 1

            for p in (1, 2, 4):
                transformed = signed_permutation(values, rng)
                before_p = resolved_lp_resource(values, p)
                after_p = resolved_lp_resource(transformed, p)
                discrete_checks += 1
                if abs(after_p - before_p) > 1e-12 * max(1.0, before_p):
                    discrete_failures += 1

    return {
        "cycle": 133,
        "theorem": (
            "resolved-channel additivity + SO(n)xSO(n) two-plane mixing + "
            "unit calibration => Frobenius-squared resource for n>=2"
        ),
        "dimensions_tested": DIMS,
        "seed": SEED,
        "trials_per_dimension_n_ge_2": TRIALS_PER_DIMENSION,
        "quadratic_rotation_checks": quadratic_checks,
        "quadratic_rotation_failures": quadratic_failures,
        "max_relative_quadratic_residual": max_relative_quadratic_residual,
        "discrete_signed_permutation_checks": discrete_checks,
        "discrete_signed_permutation_failures": discrete_failures,
        "exact_3_4_5_witness": exact_345_witness(),
        "edge_n1": (
            "non-unique: |t| and |t|^4 both satisfy single-channel "
            "additivity/calibration because SO(1) has no two-plane mixing"
        ),
        "classification": {
            "resolved_channel_mixing_theorem": [
                "PROVED",
                "CONDITIONAL",
                "IMPORTED/KNOWN",
                "NUMERICALLY SUPPORTED",
            ],
            "discrete_symmetry_suffices": "FALSIFIED",
            "n1_extension": "FALSIFIED",
            "pdt_native_derivation_of_resolved_composite_additivity": "OPEN",
        },
        "breakthrough_candidate": False,
    }


def main():
    result = run_stress()
    target = Path(__file__).with_name("cycle133_resolved_channel_mixing_results.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
