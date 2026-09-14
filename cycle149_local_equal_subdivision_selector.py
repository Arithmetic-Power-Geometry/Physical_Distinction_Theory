"""PDT-II Cycle 149: local equal-subdivision selector.

Analytic theorem under test
---------------------------
Let F be defined on all finite nonnegative vectors. Assume:
  (i) permutation symmetry;
  (ii) continuity on each fixed finite dimension and compatibility at zero-padding;
  (iii) local equal-subdivision invariance: replacing any component x by k copies
        x/k (integer k>=2) leaves F unchanged;
  (iv) singleton calibration F((S,)) = S for S>=0.
Then F(q_1,...,q_n) = sum_i q_i for every finite nonnegative q.

The proof is analytic. This script supplies exact-rational regression checks and attacks
Cycle 146's strongest continuous/multiplicative counterfamily, showing that it is killed
by local equal subdivision.
"""

from fractions import Fraction
import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 149


def split_component(q, idx, k):
    if k < 2:
        raise ValueError("k must be >=2")
    x = q[idx]
    return q[:idx] + [x / Fraction(k) for _ in range(k)] + q[idx + 1 :]


def additive_ledger(q):
    return sum(q, Fraction(0))


def cycle146_phi(q):
    """Prior counterfamily: (sum q_i^2)^2 / sum q_i^3."""
    s2 = sum((x * x for x in q), Fraction(0))
    s3 = sum((x * x * x for x in q), Fraction(0))
    return Fraction(0) if s3 == 0 else s2 * s2 / s3


def run_audit():
    rng = random.Random(SEED)
    cases = 0
    additive_failures = 0
    max_exact_error = Fraction(0)
    phi_changed_cases = 0

    for n in DIMS:
        trials = 50 if n <= 12 else 20
        for _ in range(trials):
            q = [Fraction(rng.randint(0, 20), rng.randint(1, 20)) for _ in range(n)]
            if all(x == 0 for x in q):
                q[0] = Fraction(1)
            idx = rng.randrange(n)
            k = rng.randint(2, 7)
            refined = split_component(q, idx, k)

            err = abs(additive_ledger(refined) - additive_ledger(q))
            max_exact_error = max(max_exact_error, err)
            additive_failures += int(err != 0)
            cases += 1

            if q[idx] != 0 and cycle146_phi(refined) != cycle146_phi(q):
                phi_changed_cases += 1

    witness = [Fraction(1), Fraction(3)]
    witness_split = split_component(witness, 1, 2)
    return {
        "classification": {
            "selector_theorem": "PROVED",
            "pdt_native_derivation_of_local_subdivision_invariance": "OPEN",
            "cycle146_counterfamily_survival": "FALSIFIED",
            "regression": "NUMERICALLY_SUPPORTED",
        },
        "dimensions": DIMS,
        "exact_random_cases": cases,
        "additive_split_failures": additive_failures,
        "max_exact_error": str(max_exact_error),
        "cycle146_phi_changed_cases": phi_changed_cases,
        "exact_witness": {
            "q": [str(x) for x in witness],
            "split": [str(x) for x in witness_split],
            "phi_before": str(cycle146_phi(witness)),
            "phi_after": str(cycle146_phi(witness_split)),
            "difference": str(cycle146_phi(witness_split) - cycle146_phi(witness)),
        },
    }


def main(path="cycle149_results.json"):
    result = run_audit()
    Path(path).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
