"""Cycle 069: kill test for a dimension-independent finite trace-word cutoff.

The exact theorem is algebraic.  For d=L+1 choose a probability spectrum
lambda with d distinct positive entries and monic polynomial
p(t)=prod_i (t-lambda_i).  Perturb only the constant coefficient.  For a
sufficiently small nonzero perturbation the new polynomial retains d positive
real roots mu.  All elementary symmetric polynomials e_1,...,e_{d-1} are
unchanged, hence Newton identities give equal power sums through order d-1=L,
while the determinant/product changes.

With sigma=I/d, every trace word in (rho,sigma) of total length <=L reduces
to d^{-#sigma} Tr(rho^{#rho}), so the two pairs agree on every such word but
rho and rho' have different spectra and are not unitarily equivalent.

The numerical routines below only instantiate/stress-test the exact proof.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np


def witness(d: int) -> Tuple[np.ndarray, np.ndarray, float]:
    if d < 2:
        raise ValueError("d must be >=2; d=1 is degenerate")
    lam = np.arange(1, d + 1, dtype=float)
    lam /= lam.sum()
    coeff = np.poly(lam)
    base = abs(coeff[-1])
    for factor in (1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12):
        for sign in (1.0, -1.0):
            c = coeff.copy()
            c[-1] += sign * factor * base
            roots = np.roots(c)
            if np.max(np.abs(roots.imag)) > 1e-8:
                continue
            mu = np.sort(roots.real)
            if np.min(mu) <= 1e-12:
                continue
            if abs(mu.sum() - 1.0) > 1e-8:
                continue
            return np.sort(lam), mu, sign * factor
    raise RuntimeError(f"failed to instantiate witness for d={d}")


def moment_errors(lam: np.ndarray, mu: np.ndarray, cutoff: int) -> List[float]:
    return [abs(float(np.sum(lam**k) - np.sum(mu**k))) for k in range(1, cutoff + 1)]


def operational_separator(lam: np.ndarray, mu: np.ndarray) -> Dict[str, float]:
    j = int(np.argmax(np.abs(lam - mu)))
    return {
        "coordinate": j,
        "p": float(lam[j]),
        "q": float(mu[j]),
        "gap": float(abs(lam[j] - mu[j])),
    }


def embedded_witness(n: int, cutoff: int = 6) -> Tuple[np.ndarray, np.ndarray]:
    """Embed a (cutoff+1)-dimensional witness into any n>=cutoff+1.

    Appending the same positive tail and applying the same scale preserves all
    moment equalities through the cutoff while keeping a nonzero separator.
    """
    d = cutoff + 1
    if n < d:
        raise ValueError("n must be >= cutoff+1")
    lam, mu, _ = witness(d)
    if n == d:
        return lam, mu
    tail_count = n - d
    tail_total = 0.2
    scale = 1.0 - tail_total
    tail = np.full(tail_count, tail_total / tail_count)
    return np.concatenate([scale * lam, tail]), np.concatenate([scale * mu, tail])


def run_audit() -> Dict[str, object]:
    finite = []
    for d in range(1, 13):
        if d == 1:
            finite.append({"dimension": 1, "status": "DEGENERATE", "reason": "single-state spectrum fixed by trace"})
            continue
        lam, mu, factor = witness(d)
        cutoff = d - 1
        errs = moment_errors(lam, mu, cutoff)
        sep = operational_separator(lam, mu)
        finite.append(
            {
                "dimension": d,
                "cutoff": cutoff,
                "perturbation_relative_factor": factor,
                "max_moment_error": max(errs),
                "determinant_gap": float(abs(np.prod(lam) - np.prod(mu))),
                "max_coordinate_probability_gap": sep["gap"],
                "status": "NUMERIC_WITNESS",
            }
        )

    high = []
    for n in (16, 24, 32, 48, 64, 96, 128):
        lam, mu = embedded_witness(n, cutoff=6)
        errs = moment_errors(lam, mu, 6)
        high.append(
            {
                "dimension": n,
                "cutoff": 6,
                "max_moment_error": max(errs),
                "max_coordinate_probability_gap": operational_separator(lam, mu)["gap"],
                "status": "NUMERIC_EMBEDDED_WITNESS",
            }
        )

    return {
        "cycle": 69,
        "claim": "No dimension-independent finite trace-word cutoff can be operator-complete across all finite dimensions.",
        "classification": ["PROVED", "FALSIFIED", "IMPORTED/KNOWN", "NUMERICALLY_SUPPORTED"],
        "finite_dimension_audit": finite,
        "higher_dimension_embedding_audit": high,
    }


def main() -> None:
    result = run_audit()
    out = Path("results/cycle069_no_universal_traceword_cutoff.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
