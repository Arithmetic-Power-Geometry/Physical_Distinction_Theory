"""PDT-II Cycle 150: recoverable refinement bridge.

The analytic theorem is conditional and deliberately modest.

Let M be a scalar operational resource monotone for every admissible/free map T:
    M(Tx) <= M(x).
If E and C are both admissible/free and C(E(x)) = x exactly, then
    M(E(x)) = M(x).
Proof: monotonicity under E gives M(E(x)) <= M(x), while monotonicity under C
applied to E(x) gives M(x)=M(C(E(x))) <= M(E(x)).

For resolved nonnegative shares q, replacing one component q_i by daughters
q_i w_j with w_j >= 0 and sum_j w_j = 1 has an exact deterministic merge
left-inverse. Thus the Cycle-149 local equal-subdivision premise follows as a
special case IF PDT independently establishes that both the refinement encoding
and its merge are admissible/free for the same operational ledger.

Crucially, recoverability alone does not imply scalar-ledger invariance.  The
Cycle-146 functional Phi(q)=(sum q_i^2)^2/(sum q_i^3) supplies a counterexample:
it changes under a recoverable local split.  This prevents a circular promotion
of the bridge to PDT-native status.
"""

from fractions import Fraction
import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 150


def normalize_weights(weights):
    ws = [Fraction(w) for w in weights]
    if any(w < 0 for w in ws):
        raise ValueError("weights must be nonnegative")
    s = sum(ws, Fraction(0))
    if s <= 0:
        raise ValueError("weights must have positive total")
    return [w / s for w in ws]


def refine_component(q, idx, weights):
    if not 0 <= idx < len(q):
        raise IndexError("component index out of range")
    ws = normalize_weights(weights)
    x = q[idx]
    return q[:idx] + [x * w for w in ws] + q[idx + 1 :]


def merge_daughters(q, idx, k):
    if k < 1 or idx < 0 or idx + k > len(q):
        raise ValueError("invalid daughter block")
    return q[:idx] + [sum(q[idx : idx + k], Fraction(0))] + q[idx + k :]


def additive_ledger(q):
    return sum(q, Fraction(0))


def cycle146_phi(q):
    s2 = sum((x * x for x in q), Fraction(0))
    s3 = sum((x * x * x for x in q), Fraction(0))
    return Fraction(0) if s3 == 0 else s2 * s2 / s3


def run_audit():
    rng = random.Random(SEED)
    cases = 0
    exact_recovery_failures = 0
    additive_invariance_failures = 0
    phi_changed_cases = 0

    for n in DIMS:
        trials = 50 if n <= 12 else 20
        for _ in range(trials):
            q = [Fraction(rng.randint(0, 20), rng.randint(1, 20)) for _ in range(n)]
            if all(x == 0 for x in q):
                q[0] = Fraction(1)
            idx = rng.randrange(n)
            k = rng.randint(2, 7)
            raw_weights = [Fraction(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(k)]
            refined = refine_component(q, idx, raw_weights)
            recovered = merge_daughters(refined, idx, k)

            exact_recovery_failures += int(recovered != q)
            additive_invariance_failures += int(additive_ledger(refined) != additive_ledger(q))
            if q[idx] != 0 and cycle146_phi(refined) != cycle146_phi(q):
                phi_changed_cases += 1
            cases += 1

    witness = [Fraction(1), Fraction(3)]
    witness_refined = refine_component(witness, 1, [Fraction(1, 4), Fraction(3, 4)])

    return {
        "cycle": 150,
        "classification": {
            "recoverable_monotone_invariance_theorem": "PROVED",
            "application_to_PDT_composition": "CONDITIONAL",
            "recoverability_alone_implies_ledger_invariance": "FALSIFIED",
            "resource_theory_monotonicity_mechanism": "IMPORTED/KNOWN",
            "exact_regression": "NUMERICALLY_SUPPORTED",
            "pdt_native_free_realization_of_both_maps": "OPEN",
            "breakthrough_candidate": False,
        },
        "dimensions": DIMS,
        "exact_random_cases": cases,
        "exact_recovery_failures": exact_recovery_failures,
        "additive_invariance_failures": additive_invariance_failures,
        "cycle146_phi_changed_cases": phi_changed_cases,
        "witness": {
            "q": [str(x) for x in witness],
            "refined": [str(x) for x in witness_refined],
            "recovered": [str(x) for x in merge_daughters(witness_refined, 1, 2)],
            "phi_before": str(cycle146_phi(witness)),
            "phi_after": str(cycle146_phi(witness_refined)),
            "phi_difference": str(cycle146_phi(witness_refined) - cycle146_phi(witness)),
        },
        "surviving_obligation": (
            "derive from PDT primitives that the local refinement encoding and its exact "
            "merge are both admissible/free for the same operational resource monotone"
        ),
    }


def main(path="results/cycle150_recoverable_refinement_bridge.json"):
    result = run_audit()
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
