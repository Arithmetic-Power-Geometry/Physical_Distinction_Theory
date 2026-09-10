"""PDT-II cycle: local tomography does not determine composite physics.

Exact dependency-free audit for n-input hypercube bits.  For every n>=2,
the minimal and maximal no-signalling composites share the same locally
tomographic ambient vector-space dimension (n+1)^2, but differ operationally:
the maximal composite contains an embedded PR-box witness with CHSH=4, whereas
all product-mixture (minimal) composites obey CHSH<=2.

This is established GPT/boxworld mathematics.  The PDT-specific result is a
no-go boundary: multiplicative scalar/vector dimension plus local tomography
cannot by itself define a unique PDT composition law.
"""

from fractions import Fraction
import csv
import json
from pathlib import Path


def pr_probability(n: int, x: int, y: int, a: int, b: int) -> Fraction:
    """Embedded PR box for first two settings; uniform elsewhere."""
    if n < 1:
        raise ValueError("n must be >=1")
    if not (0 <= x < n and 0 <= y < n and a in (0, 1) and b in (0, 1)):
        raise ValueError("invalid setting/outcome")
    if x < 2 and y < 2:
        return Fraction(1, 2) if (a ^ b) == (x & y) else Fraction(0)
    return Fraction(1, 4)


def correlator(n: int, x: int, y: int) -> Fraction:
    return sum(
        (1 if (a ^ b) == 0 else -1) * pr_probability(n, x, y, a, b)
        for a in (0, 1) for b in (0, 1)
    )


def chsh_pr(n: int):
    if n < 2:
        return None
    return correlator(n, 0, 0) + correlator(n, 0, 1) + correlator(n, 1, 0) - correlator(n, 1, 1)


def deterministic_local_chsh_max() -> int:
    """Exhaust all deterministic assignments for two binary settings."""
    best = -10
    for A0 in (-1, 1):
        for A1 in (-1, 1):
            for B0 in (-1, 1):
                for B1 in (-1, 1):
                    s = A0 * B0 + A0 * B1 + A1 * B0 - A1 * B1
                    best = max(best, s)
    return best


def normalization_ok(n: int) -> bool:
    for x in range(n):
        for y in range(n):
            if sum(pr_probability(n, x, y, a, b) for a in (0, 1) for b in (0, 1)) != 1:
                return False
    return True


def nonsignalling_ok(n: int) -> bool:
    for x in range(n):
        marginals = []
        for y in range(n):
            marginals.append(tuple(sum(pr_probability(n, x, y, a, b) for b in (0, 1)) for a in (0, 1)))
        if len(set(marginals)) != 1:
            return False
    for y in range(n):
        marginals = []
        for x in range(n):
            marginals.append(tuple(sum(pr_probability(n, x, y, a, b) for a in (0, 1)) for b in (0, 1)))
        if len(set(marginals)) != 1:
            return False
    return True


def audit_row(n: int) -> dict:
    local_vector_dim = n + 1
    composite_vector_dim = local_vector_dim ** 2
    s = chsh_pr(n)
    return {
        "n_fiducial_binary_settings": n,
        "local_vector_dim": local_vector_dim,
        "locally_tomographic_composite_dim": composite_vector_dim,
        "normalization_exact": normalization_ok(n),
        "nonsignalling_exact": nonsignalling_ok(n),
        "minimal_local_CHSH_bound": 2 if n >= 2 else "NA",
        "maximal_embedded_PR_CHSH": int(s) if s is not None else "NA",
        "minimal_maximal_separated": bool(n >= 2 and s == 4),
    }


def run_audit(nmax: int = 12):
    return [audit_row(n) for n in range(1, nmax + 1)]


def write_artifacts(outdir: str = "results"):
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    rows = run_audit(12)
    csv_path = out / "cycle041_local_tomography_composite_no_go.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    status = {
        "result": "Local tomography plus multiplicative vector dimension does not determine a unique composite cone/state space.",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN"],
        "breakthrough_candidate": False,
        "smallest_decisive_witness_n": 2,
        "minimal_CHSH_bound": deterministic_local_chsh_max(),
        "maximal_PR_CHSH": 4,
        "dimensions_audited": [1, 12],
        "novelty_note": "Underlying minimal/maximal GPT tensor-product and PR-box mathematics is prior art; only the PDT-specific no-go interpretation is new to this project ledger."
    }
    json_path = out / "cycle041_local_tomography_composite_no_go.json"
    json_path.write_text(json.dumps(status, indent=2), encoding="utf-8")
    return csv_path, json_path


if __name__ == "__main__":
    assert deterministic_local_chsh_max() == 2
    for row in run_audit(12):
        assert row["normalization_exact"] and row["nonsignalling_exact"]
        if row["n_fiducial_binary_settings"] >= 2:
            assert row["minimal_maximal_separated"]
    write_artifacts()
