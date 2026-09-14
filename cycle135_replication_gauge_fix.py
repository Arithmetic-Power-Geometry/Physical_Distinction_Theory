"""Cycle 135: two-and-three-copy replication fixes the scalar resource gauge.

Conditional theorem. Suppose a surviving composite resource has the form R=f(Q),
where Q>=0 is the already-selected quadratic revelation ledger, f:[0,inf)->[0,inf)
is continuous, and f(1)=1. If identical independent replication is extensive for
both two and three copies,

    f(2q)=2f(q),   f(3q)=3f(q)   for all q>=0,

then f(q)=q for all q>=0.

Proof: for q=e^t define h(t)=f(e^t)/e^t. Then ln 2 and ln 3 are periods of h.
Their ratio is irrational (otherwise 2^m=3^n for nonzero integers m,n), so the
period subgroup is dense. Continuity forces h to be constant; f(1)=1 fixes that
constant to one.

Decisive no-go for doubling alone: for sufficiently small epsilon>0,

    f_eps(q)=q[1+eps sin(2*pi*log_2 q)], q>0; f_eps(0)=0,

is positive, continuous, strictly increasing and obeys f_eps(2q)=2f_eps(q), but
violates three-copy extensivity. Hence two-copy replication alone does not fix
the gauge.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass

import numpy as np

DIMS = list(range(1, 13)) + [16, 24, 32, 48, 64, 96, 128]
SEED = 135
TRIALS_PER_DIM = 20
EPS = 0.05
TOL = 1e-10


def quadratic_ledger(a: np.ndarray) -> float:
    return float(np.sum(a * a))


def linear_gauge(q: float) -> float:
    return float(q)


def doubling_periodic_gauge(q: float, eps: float = EPS) -> float:
    if q <= 0.0:
        return 0.0
    return float(q * (1.0 + eps * math.sin(2.0 * math.pi * math.log2(q))))


def monotonicity_lower_bound(eps: float = EPS) -> float:
    k = 2.0 * math.pi / math.log(2.0)
    return 1.0 - eps * math.sqrt(1.0 + k * k)


@dataclass
class Audit:
    dimensions: list[int]
    cases: int
    linear_two_copy_failures: int
    linear_three_copy_failures: int
    periodic_two_copy_failures: int
    periodic_three_copy_violations: int
    max_periodic_two_copy_relative_residual: float
    max_periodic_three_copy_relative_residual: float
    monotonicity_derivative_lower_bound: float
    theorem_status: str
    doubling_only_status: str


def relative_residual(lhs: float, rhs: float) -> float:
    return abs(lhs - rhs) / max(1.0, abs(rhs))


def run_audit() -> Audit:
    rng = np.random.default_rng(SEED)
    cases = 0
    l2 = l3 = p2 = p3v = 0
    max_p2 = max_p3 = 0.0

    for n in DIMS:
        for _ in range(TRIALS_PER_DIM):
            a = rng.normal(size=(n, n))
            q = quadratic_ledger(a)

            r = linear_gauge(q)
            l2 += int(relative_residual(linear_gauge(2*q), 2*r) > TOL)
            l3 += int(relative_residual(linear_gauge(3*q), 3*r) > TOL)

            rp = doubling_periodic_gauge(q)
            e2 = relative_residual(doubling_periodic_gauge(2*q), 2*rp)
            e3 = relative_residual(doubling_periodic_gauge(3*q), 3*rp)
            p2 += int(e2 > TOL)
            p3v += int(e3 > TOL)
            max_p2 = max(max_p2, e2)
            max_p3 = max(max_p3, e3)
            cases += 1

    return Audit(
        dimensions=DIMS,
        cases=cases,
        linear_two_copy_failures=l2,
        linear_three_copy_failures=l3,
        periodic_two_copy_failures=p2,
        periodic_three_copy_violations=p3v,
        max_periodic_two_copy_relative_residual=max_p2,
        max_periodic_three_copy_relative_residual=max_p3,
        monotonicity_derivative_lower_bound=monotonicity_lower_bound(),
        theorem_status="CONDITIONAL/PROVED",
        doubling_only_status="FALSIFIED",
    )


def main() -> None:
    print(json.dumps(asdict(run_audit()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
