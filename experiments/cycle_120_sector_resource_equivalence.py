"""Cycle 120: sector-resource circularity guard.

This module tests the exact equivalence, on zero-hidden-resource inputs, between
same-sector closure and the proposed zero-resource monotonicity condition.
No novelty is claimed for generic resource-theory/free-operation logic.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def hidden_resource(m):
    return sum(x * x for x in m)


def compose_preserving(a, m, b, r):
    n = len(a)
    return ([a[i] * b[i] for i in range(n)],
            [a[i] * r[i] + m[i] * b[i] for i in range(n)])


def compose_leaking(a, m, b, r):
    n = len(a)
    return ([a[i] * b[i] for i in range(n)],
            [a[i] * r[i] + m[i] * b[i] + a[i] * b[i] for i in range(n)])


def visible_pair_equivalence(op, a, b):
    n = len(a)
    z = [0] * n
    _, out_m = op(a, z, b, z)
    closure = hidden_resource(out_m) == 0
    zero_resource_monotonicity = hidden_resource(out_m) <= 0
    return closure, zero_resource_monotonicity, hidden_resource(out_m)


def run(seed=120):
    rng = random.Random(seed)
    pair_checks = mismatches = leak_nonzero = preserve_nonzero = 0
    for n in DIMS:
        k = min(n, 12)
        for i in range(k):
            for j in range(k):
                a = [0] * n; b = [0] * n
                a[i] = 1; b[j] = 1
                for op in (compose_preserving, compose_leaking):
                    c, q, h = visible_pair_equivalence(op, a, b)
                    mismatches += int(c != q)
                    pair_checks += 1
                    if op is compose_leaking:
                        leak_nonzero += int(h > 0)
                    else:
                        preserve_nonzero += int(h > 0)
        for _ in range(50):
            a = [rng.randint(-3, 3) for _ in range(n)]
            b = [rng.randint(-3, 3) for _ in range(n)]
            for op in (compose_preserving, compose_leaking):
                c, q, h = visible_pair_equivalence(op, a, b)
                mismatches += int(c != q)
                pair_checks += 1
                if op is compose_leaking:
                    leak_nonzero += int(h > 0)
                else:
                    preserve_nonzero += int(h > 0)

    # Smallest exact witness: V=M=R, H(m)=m^2.
    c, q, h = visible_pair_equivalence(compose_leaking, [1], [1])
    assert not c and not q and h == 1
    assert mismatches == 0

    return {
        "cycle": 120,
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "stress_dimensions": DIMS,
        "pair_checks": pair_checks,
        "equivalence_mismatches": mismatches,
        "leaking_nonzero_hidden_outputs": leak_nonzero,
        "preserving_nonzero_hidden_outputs": preserve_nonzero,
        "smallest_leak_dimension": 1,
        "smallest_leak_witness": {"x": [1, 0], "y": [1, 0], "output": [1, 1], "H_inputs": [0, 0], "H_output": 1},
    }


if __name__ == "__main__":
    out = run()
    print(json.dumps(out, indent=2))
