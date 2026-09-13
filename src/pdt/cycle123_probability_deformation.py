"""Cycle 123: exact/numerical guards for scalar Born-probability deformations."""
from fractions import Fraction
import math
import random


def power_deform(q: float, alpha: float) -> float:
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must lie in [0,1]")
    if alpha <= 0.0:
        raise ValueError("alpha must be positive")
    if q == 0.0 or q == 1.0:
        return q
    a = q ** alpha
    b = (1.0 - q) ** alpha
    return a / (a + b)


def exact_alpha2_witness():
    q1 = Fraction(0, 1)
    q2 = Fraction(1, 2)
    t = Fraction(1, 2)
    qmix = t*q1 + (1-t)*q2
    # alpha=2, exact rational form
    f = lambda q: q*q / (q*q + (1-q)*(1-q)) if q not in (0,1) else q
    lhs = f(qmix)
    rhs = t*f(q1) + (1-t)*f(q2)
    return {"qmix": qmix, "lhs": lhs, "rhs": rhs, "residual": lhs-rhs}


def randomized_affinity_audit(alpha: float, trials: int = 2000, seed: int = 123):
    rng = random.Random(seed)
    violations = 0
    max_abs = 0.0
    for _ in range(trials):
        q1, q2, t = rng.random(), rng.random(), rng.random()
        lhs = power_deform(t*q1+(1-t)*q2, alpha)
        rhs = t*power_deform(q1,alpha)+(1-t)*power_deform(q2,alpha)
        r = abs(lhs-rhs)
        max_abs = max(max_abs,r)
        if r > 1e-12:
            violations += 1
    return {"alpha":alpha,"trials":trials,"violations":violations,"max_abs_residual":max_abs}


if __name__ == "__main__":
    print(exact_alpha2_witness())
    for a in (0.5, 1.0, 2.0, 3.0):
        print(randomized_affinity_audit(a))
