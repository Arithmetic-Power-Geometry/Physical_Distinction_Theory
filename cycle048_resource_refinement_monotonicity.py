"""PDT-II Cycle 048: resource-refinement monotonicity and conservation kill test.

This module uses exact rational arithmetic only.

For probability distributions p,q and a stochastic coarse-graining kernel K,
TV(Kp,Kq) <= TV(p,q).  A refinement can therefore reveal previously hidden
operational distinction, but cannot reduce the finest available distinction.

The naive conservation claim TV(Kp,Kq) == TV(p,q) is false.  The smallest
counterexample has two fine outcomes merged into one coarse outcome:
p=(1,0), q=(0,1), giving fine TV=1 and coarse TV=0.
"""

from fractions import Fraction
import csv
from pathlib import Path


def tv(p, q):
    if len(p) != len(q):
        raise ValueError("p and q must have equal length")
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def pushforward(p, kernel):
    if not kernel or len(kernel) != len(p):
        raise ValueError("kernel must have one row per input state")
    width = len(kernel[0])
    if width == 0 or any(len(row) != width for row in kernel):
        raise ValueError("kernel rows must have common nonzero width")
    for row in kernel:
        if any(x < 0 for x in row) or sum(row) != 1:
            raise ValueError("each kernel row must be a probability distribution")
    return [sum(p[i] * kernel[i][j] for i in range(len(p))) for j in range(width)]


def deterministic_merge_first_two(n):
    """Merge outcomes 0 and 1; leave all later outcomes individually visible."""
    if n < 2:
        return [[Fraction(1)]]
    width = max(1, n - 1)
    K = [[Fraction(0) for _ in range(width)] for _ in range(n)]
    K[0][0] = 1
    K[1][0] = 1
    for i in range(2, n):
        K[i][i - 1] = 1
    return K


def lcg(seed):
    while True:
        seed = (1664525 * seed + 1013904223) % (2**32)
        yield seed


def random_rational_distribution(n, gen):
    vals = [next(gen) % 17 + 1 for _ in range(n)]
    total = sum(vals)
    return [Fraction(v, total) for v in vals]


def random_rational_kernel(n, m, gen):
    rows = []
    for _ in range(n):
        vals = [next(gen) % 13 + 1 for _ in range(m)]
        total = sum(vals)
        rows.append([Fraction(v, total) for v in vals])
    return rows


def exact_random_audit(n, trials=200):
    gen = lcg(1000 + n)
    max_violation = Fraction(0)
    max_ratio = Fraction(0)
    for _ in range(trials):
        p = random_rational_distribution(n, gen)
        q = random_rational_distribution(n, gen)
        m = max(1, (n + 1) // 2)
        K = random_rational_kernel(n, m, gen)
        d_fine = tv(p, q)
        d_coarse = tv(pushforward(p, K), pushforward(q, K))
        max_violation = max(max_violation, d_coarse - d_fine)
        if d_fine:
            max_ratio = max(max_ratio, d_coarse / d_fine)
    return max_violation, max_ratio


def witness(n):
    if n == 1:
        return Fraction(0), Fraction(0)
    p = [Fraction(0) for _ in range(n)]
    q = [Fraction(0) for _ in range(n)]
    p[0] = 1
    q[1] = 1
    K = deterministic_merge_first_two(n)
    return tv(p, q), tv(pushforward(p, K), pushforward(q, K))


def generate_csv(path="results/cycle048_resource_refinement_audit.csv"):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "trials", "max_exact_dpi_violation", "max_contraction_ratio", "witness_fine_tv", "witness_coarse_tv", "witness_revelation"])
        for n in range(1, 13):
            violation, ratio = exact_random_audit(n)
            fine, coarse = witness(n)
            w.writerow([n, 200, str(violation), str(ratio), str(fine), str(coarse), str(fine - coarse)])


if __name__ == "__main__":
    generate_csv()
