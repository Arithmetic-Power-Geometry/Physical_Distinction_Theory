"""Cycle 152: exact no-go audit for complete-record-neutral nontrivial refinement.

A parent share x is split into >=2 positive daughters.  The coarse record keeps only
total mass; the fine record keeps the resolved positive daughter multiset.  Exact
rational arithmetic verifies that coarse records agree while fine records differ.
"""
from fractions import Fraction
import json, random

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
RNG = random.Random(152)

def split(q, i, weights):
    return q[:i] + [q[i] * w for w in weights] + q[i+1:]

def coarse_record(q):
    return sum(q, Fraction(0))

def fine_record(q):
    # A daughter-resolving window can distinguish the positive resolved shares.
    return tuple(sorted((x for x in q if x > 0), reverse=True))

def run():
    cases = coarse_fail = fine_neutral = recovery_fail = 0
    for n in DIMS:
        for _ in range(30):
            q = [Fraction(RNG.randint(0, 9), RNG.randint(1, 9)) for _ in range(n)]
            if not any(q): q[0] = Fraction(1)
            positive = [j for j, x in enumerate(q) if x > 0]
            i = RNG.choice(positive)
            k = RNG.randint(2, 5)
            raw = [RNG.randint(1, 9) for _ in range(k)]
            s = sum(raw)
            w = [Fraction(a, s) for a in raw]
            qp = split(q, i, w)
            cases += 1
            coarse_fail += coarse_record(qp) != coarse_record(q)
            fine_neutral += fine_record(qp) == fine_record(q)
            # merge the inserted daughters exactly
            qm = qp[:i] + [sum(qp[i:i+k], Fraction(0))] + qp[i+k:]
            recovery_fail += qm != q
    return {
        "cycle": 152, "dimensions": DIMS, "cases": cases,
        "coarse_record_failures": coarse_fail,
        "fine_record_neutral_cases": fine_neutral,
        "exact_recovery_failures": recovery_fail,
        "classification": {
            "nontrivial_refinement_neutral_for_all_resolving_windows": "FALSIFIED",
            "coarse_window_neutrality": "NUMERICALLY_SUPPORTED",
            "complete_record_bridge_without_window_restriction": "OPEN/BLOCKED"
        }
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
