"""Cycle 118: multiplicative-resource conservation does not force same-sector closure.

The construction transports ordinary complex multiplication to pairs (a,m) via
phi(a,m)=a+i(m+a).  It is therefore associative.  The positive quadratic
resource q(a,m)=|phi(a,m)|^2 obeys q(x*y)=q(x)q(y) exactly, yet products of
states in the visible sector m=0 generally generate a nonzero auxiliary sector.
"""

from __future__ import annotations

import json
import random
from pathlib import Path


DIMENSIONS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 1180913


def product_scalar(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    """Transport complex multiplication through phi(a,m)=a+i(m+a)."""
    a, m = x
    b, r = y
    imag_x = m + a
    imag_y = r + b
    visible = a * b - imag_x * imag_y
    imag = a * imag_y + b * imag_x
    hidden = imag - visible
    return visible, hidden


def resource_scalar(x: tuple[int, int]) -> int:
    """Squared complex modulus after phi; nonnegative and exact over integers."""
    a, m = x
    return a * a + (m + a) * (m + a)


def product(x, y):
    if len(x) != len(y):
        raise ValueError("dimension mismatch")
    return [product_scalar(xi, yi) for xi, yi in zip(x, y)]


def resource_vector(x):
    return [resource_scalar(xi) for xi in x]


def visible_state(values):
    return [(int(a), 0) for a in values]


def run_audit(seed: int = SEED) -> dict:
    rng = random.Random(seed)
    associativity_failures = 0
    resource_failures = 0
    hidden_generation_trials = 0
    trials = 0

    # Exact scalar grid for the algebraic identities.
    scalar_resource_failures = 0
    scalar_associativity_failures = 0
    scalar_associativity_cases = 0
    vals = range(-3, 4)
    for a in vals:
        for m in vals:
            for b in vals:
                for r in vals:
                    x = (a, m)
                    y = (b, r)
                    if resource_scalar(product_scalar(x, y)) != resource_scalar(x) * resource_scalar(y):
                        scalar_resource_failures += 1
                    for c in (-1, 0, 1):
                        for s in (-1, 0, 1):
                            z = (c, s)
                            scalar_associativity_cases += 1
                            if product_scalar(product_scalar(x, y), z) != product_scalar(x, product_scalar(y, z)):
                                scalar_associativity_failures += 1

    for n in DIMENSIONS:
        reps = 100 if n <= 12 else 40
        for _ in range(reps):
            x = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(n)]
            y = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(n)]
            z = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(n)]
            xy = product(x, y)
            if product(xy, z) != product(x, product(y, z)):
                associativity_failures += 1
            qx = resource_vector(x)
            qy = resource_vector(y)
            qxy = resource_vector(xy)
            if any(qxy[i] != qx[i] * qy[i] for i in range(n)):
                resource_failures += 1

            a = [rng.randint(-3, 3) for _ in range(n)]
            b = [rng.randint(-3, 3) for _ in range(n)]
            out = product(visible_state(a), visible_state(b))
            if any(hidden != 0 for _, hidden in out):
                hidden_generation_trials += 1
            trials += 1

    witness_x = (2, 0)
    witness_y = (3, 0)
    witness_out = product_scalar(witness_x, witness_y)

    return {
        "seed": seed,
        "dimensions": DIMENSIONS,
        "trials": trials,
        "scalar_associativity_cases": scalar_associativity_cases,
        "scalar_associativity_failures": scalar_associativity_failures,
        "scalar_resource_failures": scalar_resource_failures,
        "vector_associativity_failures": associativity_failures,
        "vector_resource_failures": resource_failures,
        "hidden_generation_trials": hidden_generation_trials,
        "smallest_explicit_witness": {
            "n": 1,
            "x": list(witness_x),
            "y": list(witness_y),
            "product": list(witness_out),
            "q_x": resource_scalar(witness_x),
            "q_y": resource_scalar(witness_y),
            "q_product": resource_scalar(witness_out),
        },
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
    }


if __name__ == "__main__":
    result = run_audit()
    print(json.dumps(result, indent=2))
