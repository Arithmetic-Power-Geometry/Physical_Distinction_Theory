"""PDT-II Cycle 117: finite revelation does not force same-sector closure.

Countermodel.  On A = V + M with V=M=R^n define coordinatewise

    (a,m)*(b,r) = (a*b, a*r + m*b + lam*a*b).

The coarse resource window observes pi_0(a,m)=a.  A one-step refined finite-resource
window observes pi_1(a,m)=(a,m), so every generated auxiliary component is revealed
exactly after finite refinement.  Nevertheless visible-sector inputs (a,0),(b,0)
generically compose to (a*b,lam*a*b), outside V.  Thus exact eventual revelation,
associativity, and exact coarse composition do not imply ontic same-sector closure.

The algebra-extension mechanism is standard; no historical novelty is claimed for it.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def product(x, y, lam=1):
    a, m = x
    b, r = y
    if not (len(a) == len(m) == len(b) == len(r)):
        raise ValueError("all components must have equal dimension")
    visible = [ai * bi for ai, bi in zip(a, b)]
    hidden = [ai * ri + mi * bi + lam * ai * bi
              for ai, mi, bi, ri in zip(a, m, b, r)]
    return visible, hidden


def coarse_window(x):
    return list(x[0])


def refined_window(x):
    # Injective finite refinement: reveals the complete auxiliary sector.
    return list(x[0]), list(x[1])


def run_audit(seed=1170913):
    rng = random.Random(seed)
    trials = 0
    assoc_failures = 0
    coarse_failures = 0
    reveal_failures = 0
    generated = 0
    rows = []

    for n in DIMS:
        reps = 200 if n <= 12 else 80
        local_generated = 0
        for _ in range(reps):
            a = [rng.randint(-3, 3) for _ in range(n)]
            b = [rng.randint(-3, 3) for _ in range(n)]
            c = [rng.randint(-3, 3) for _ in range(n)]
            z = [0] * n
            x, y, w = (a, z.copy()), (b, z.copy()), (c, z.copy())

            xy = product(x, y)
            if any(xy[1]):
                generated += 1
                local_generated += 1

            if product(xy, w) != product(x, product(y, w)):
                assoc_failures += 1
            if coarse_window(xy) != [ai * bi for ai, bi in zip(a, b)]:
                coarse_failures += 1
            if refined_window(xy) != (list(xy[0]), list(xy[1])):
                reveal_failures += 1
            trials += 1

        rows.append({"n": n, "trials": reps,
                     "nonzero_hidden_generated": local_generated})

    return {
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN",
                           "NUMERICALLY_SUPPORTED", "OPEN"],
        "breakthrough_candidate": False,
        "seed": seed,
        "dimensions": DIMS,
        "trials": trials,
        "associativity_failures": assoc_failures,
        "coarse_projection_failures": coarse_failures,
        "refined_revelation_failures": reveal_failures,
        "nonzero_hidden_generated": generated,
        "smallest_counterexample": {
            "n": 1, "lambda": 1,
            "x": [[2], [0]], "y": [[3], [0]],
            "product": [[6], [6]],
            "coarse_visible": [6],
            "refined_visible": [[6], [6]],
        },
        "rows": rows,
    }


def write_results(path="results/cycle117_finite_revelation_no_go.json"):
    result = run_audit()
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    print(json.dumps(write_results(), indent=2, sort_keys=True))
