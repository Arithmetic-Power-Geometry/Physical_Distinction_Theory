"""Cycle 121: visible-quotient underdetermination no-go.

Any identity formulated only through a quotient projection pi and functions of
that projected state is inherited unchanged by any microscopic extension having
the same quotient dynamics. Therefore visible-only conservation/refinement laws
cannot, by themselves, imply same-sector microscopic closure.
"""
from __future__ import annotations

import json
import random

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def base_mul(a, b):
    return [x * y for x, y in zip(a, b)]


def zero(n):
    return [0] * n


def lift(a):
    return (a, zero(len(a)))


def project(x):
    return x[0]


def extension_mul(x, y):
    """Associative leaking extension of coordinatewise multiplication."""
    a, m = x
    b, r = y
    v = base_mul(a, b)
    h = [a[i] * r[i] + m[i] * b[i] + v[i] for i in range(len(a))]
    return v, h


def visible_resources(v):
    return {
        "sum": sum(v),
        "l1": sum(abs(x) for x in v),
        "sq": sum(x * x for x in v),
        "support": sum(x != 0 for x in v),
        "maxabs": max((abs(x) for x in v), default=0),
    }


def run(seed=121):
    rng = random.Random(seed)
    checks = mismatches = leaks = assoc_failures = 0

    for n in DIMS:
        for _ in range(80):
            a = [rng.randint(-2, 2) for _ in range(n)]
            b = [rng.randint(-2, 2) for _ in range(n)]
            c = [rng.randint(-2, 2) for _ in range(n)]
            x, y, z = lift(a), lift(b), lift(c)

            left = extension_mul(extension_mul(x, y), z)
            right = extension_mul(x, extension_mul(y, z))
            assoc_failures += int(left != right)

            base_three = base_mul(base_mul(a, b), c)
            ext_three = project(left)
            mismatches += int(base_three != ext_three)
            checks += 1

            base_two = base_mul(a, b)
            ext_two_full = extension_mul(x, y)
            ext_two = project(ext_two_full)
            mismatches += int(visible_resources(base_two) != visible_resources(ext_two))
            checks += 1
            leaks += int(any(ext_two_full[1]))

    # Smallest exact witness: visible quotient is unchanged but hidden output is generated.
    witness = extension_mul(lift([1]), lift([1]))
    assert witness == ([1], [1])
    assert project(witness) == base_mul([1], [1])
    assert assoc_failures == 0
    assert mismatches == 0

    return {
        "cycle": 121,
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "stress_dimensions": DIMS,
        "visible_transcript_checks": checks,
        "visible_transcript_mismatches": mismatches,
        "associativity_failures": assoc_failures,
        "trials_with_hidden_leakage": leaks,
        "smallest_leak_dimension": 1,
        "smallest_leak_witness": {"x": [1, 0], "y": [1, 0], "output": [1, 1]},
        "theorem": "Any law expressible solely through a quotient homomorphism pi and functions of pi is inherited unchanged by an associative extension with the same quotient, so such visible-only laws cannot imply microscopic same-sector closure.",
        "open_target": "Find a PDT-native law with microscopic/sector-sensitive content not factorizable through the visible quotient.",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
