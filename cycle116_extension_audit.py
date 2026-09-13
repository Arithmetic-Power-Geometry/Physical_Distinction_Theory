from __future__ import annotations

import json
import random
from pathlib import Path

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]


def zero(n):
    return (0,) * n


def had(a, b):
    return tuple(x * y for x, y in zip(a, b))


def mul(x, y, lam=1):
    a, m = x
    b, n = y
    return had(a, b), tuple(ai * ni + mi * bi + lam * ai * bi
                            for ai, mi, bi, ni in zip(a, m, b, n))


def audit(seed=1160913):
    rng = random.Random(seed)
    rows = []
    total = assoc = proj = extra = 0
    for dim in DIMS:
        trials = 200 if dim <= 12 else 80
        af = pf = ef = 0
        for _ in range(trials):
            a = tuple(rng.randint(-2, 2) for _ in range(dim))
            b = tuple(rng.randint(-2, 2) for _ in range(dim))
            c = tuple(rng.randint(-2, 2) for _ in range(dim))
            x, y, z = (a, zero(dim)), (b, zero(dim)), (c, zero(dim))
            xy = mul(x, y)
            af += mul(xy, z) != mul(x, mul(y, z))
            pf += xy[0] != had(a, b)
            ef += any(v != 0 for v in xy[1])
        rows.append({"n": dim, "trials": trials, "associativity_failures": af,
                     "projection_failures": pf, "extra_sector_nonzero": ef})
        total += trials; assoc += af; proj += pf; extra += ef
    return {"cycle": 116, "rows": rows,
            "totals": {"trials": total, "associativity_failures": assoc,
                       "projection_failures": proj, "extra_sector_nonzero": extra},
            "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY SUPPORTED", "OPEN"],
            "breakthrough_candidate": False}


if __name__ == "__main__":
    result = audit()
    path = Path("results/cycle116_extension_audit.json")
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["totals"], indent=2))
