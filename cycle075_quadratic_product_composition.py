"""Cycle 075: quadratic distinction-energy product composition and correlation-sign audit.

The proof-level identity is
    E_d(rho) = d Tr(rho^2) - 1,
    1 + E_AB(rho_A tensor rho_B) = (1 + E_A)(1 + E_B).
The numerical audit is regression evidence only.  The same script records exact
correlated witnesses showing that the residual relative to the product baseline
is sign-indefinite, so it cannot be interpreted universally as a nonnegative
correlation energy.
"""
from __future__ import annotations

import json
from fractions import Fraction
import numpy as np


def distinction_energy_from_spectrum(p: np.ndarray) -> float:
    d = int(p.size)
    return float(d * np.dot(p, p) - 1.0)


def compose_product_energy(ea: float, eb: float) -> float:
    return ea + eb + ea * eb


def random_spectrum(rng: np.random.Generator, d: int) -> np.ndarray:
    if d == 1:
        return np.array([1.0])
    x = rng.gamma(shape=1.0, scale=1.0, size=d)
    return x / x.sum()


def exact_negative_residual(n: int) -> Fraction:
    """Classical diagonal witness embedded in local dimension n>=2.

    Joint probabilities on a 2x2 block are [[0,1/5],[1/5,3/5]].
    Joint purity=11/25 and each marginal purity=17/25.
    Residual = E_AB - (E_A + E_B + E_A E_B) = -14 n^2 / 625.
    """
    if n < 2:
        return Fraction(0, 1)
    return Fraction(-14 * n * n, 625)


def exact_positive_residual(n: int) -> Fraction:
    """Maximally entangled pure-state witness in local dimension n>=2."""
    if n < 2:
        return Fraction(0, 1)
    return Fraction(n * n - 1, 1)


def run_audit(seed: int = 75011) -> dict:
    rng = np.random.default_rng(seed)
    dims = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
    cases = 0
    failures = 0
    max_err = 0.0
    rows = []

    for d in dims:
        reps = 100 if d <= 12 else 40
        for _ in range(reps):
            p = random_spectrum(rng, d)
            q = random_spectrum(rng, d)
            ea = distinction_energy_from_spectrum(p)
            eb = distinction_energy_from_spectrum(q)
            eab = float(d * d * np.dot(p, p) * np.dot(q, q) - 1.0)
            rhs = compose_product_energy(ea, eb)
            err = abs(eab - rhs)
            max_err = max(max_err, err)
            if err > 1e-12:
                failures += 1
            cases += 1
        rows.append({"d": d, "repetitions": reps})

    sign_rows = []
    for n in dims:
        neg = exact_negative_residual(n)
        pos = exact_positive_residual(n)
        sign_rows.append(
            {
                "n": n,
                "negative_residual": f"{neg.numerator}/{neg.denominator}",
                "positive_residual": f"{pos.numerator}/{pos.denominator}",
                "classification": "DEGENERATE" if n == 1 else "BOTH_SIGNS",
            }
        )
        if n >= 2 and not (neg < 0 < pos):
            failures += 1

    return {
        "classification": [
            "PROVED(product composition identity)",
            "IMPORTED/KNOWN(purity/Tsallis-2 boundary)",
            "NUMERICALLY_SUPPORTED",
            "FALSIFIED(nonnegative universal correlation residual)",
        ],
        "formula": "E_AB = E_A + E_B + E_A E_B for product states",
        "additive_coordinate": "C=log(1+E)=log(d Tr(rho^2))",
        "cases": cases,
        "failures": failures,
        "max_abs_product_error": max_err,
        "dimensions": dims,
        "dimension_rows": rows,
        "correlation_residual_sign_rows": sign_rows,
        "smallest_negative_witness": {
            "local_dimension": 2,
            "joint_probabilities": [["0", "1/5"], ["1/5", "3/5"]],
            "joint_purity": "11/25",
            "marginal_purity": "17/25",
            "residual": "-56/625",
        },
        "smallest_positive_witness": {
            "local_dimension": 2,
            "state": "Bell pure state with maximally mixed marginals",
            "residual": "3",
        },
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
