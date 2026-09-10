"""PDT-II Cycle 049: exact revelation accounting under deterministic resource coarse-graining.

Let p,q be two finite probability distributions and let a deterministic resource map
partition fine outcomes into coarse cells C_j.  Put delta_i=p_i-q_i.  Then

TV(p,q)-TV(Kp,Kq)
 = 1/2 sum_j [sum_{i in C_j}|delta_i|-|sum_{i in C_j}delta_i|]
 = sum_j min(P_j,N_j),

where P_j=sum_{i in C_j, delta_i>0} delta_i and
N_j=sum_{i in C_j, delta_i<0} -delta_i.

Thus the exact distinction hidden by coarse-graining is the within-cell cancellation
between positive and negative likelihood contrast.  Equality TV(Kp,Kq)=TV(p,q)
holds iff every coarse cell is sign-pure (ignoring zero entries).

This is an operational accounting identity built from standard total-variation/Jordan
signed-measure mathematics; no historical novelty is claimed for the underlying math.
"""

from fractions import Fraction
import csv
from pathlib import Path


def tv(p, q):
    if len(p) != len(q):
        raise ValueError("p and q must have equal length")
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def coarse_pushforward(p, partition):
    if len(p) != len(partition):
        raise ValueError("partition must label every fine outcome")
    labels = sorted(set(partition))
    return [sum((p[i] for i, c in enumerate(partition) if c == label), Fraction(0))
            for label in labels]


def cancellation_loss(p, q, partition):
    if len(p) != len(q) or len(p) != len(partition):
        raise ValueError("p, q and partition must have equal length")
    delta = [a - b for a, b in zip(p, q)]
    loss = Fraction(0)
    for label in sorted(set(partition)):
        positive = sum((d for i, d in enumerate(delta)
                        if partition[i] == label and d > 0), Fraction(0))
        negative = sum((-d for i, d in enumerate(delta)
                        if partition[i] == label and d < 0), Fraction(0))
        loss += min(positive, negative)
    return loss


def is_sign_pure(p, q, partition):
    delta = [a - b for a, b in zip(p, q)]
    for label in set(partition):
        signs = {1 if d > 0 else -1 for i, d in enumerate(delta)
                 if partition[i] == label and d != 0}
        if len(signs) > 1:
            return False
    return True


def exact_identity(p, q, partition):
    fine = tv(p, q)
    kp = coarse_pushforward(p, partition)
    kq = coarse_pushforward(q, partition)
    coarse = tv(kp, kq)
    loss = cancellation_loss(p, q, partition)
    return fine, coarse, loss, fine - coarse == loss


def lcg(seed):
    while True:
        seed = (1664525 * seed + 1013904223) % (2**32)
        yield seed


def random_rational_distribution(n, gen):
    vals = [next(gen) % 17 + 1 for _ in range(n)]
    total = sum(vals)
    return [Fraction(v, total) for v in vals]


def random_partition(n, gen):
    cells = max(1, (n + 1) // 2)
    return [next(gen) % cells for _ in range(n)]


def exact_random_audit(n, trials=200):
    gen = lcg(49000 + n)
    max_identity_error = Fraction(0)
    max_loss = Fraction(0)
    equality_condition_failures = 0
    zero_loss_cases = 0
    for _ in range(trials):
        p = random_rational_distribution(n, gen)
        q = random_rational_distribution(n, gen)
        part = random_partition(n, gen)
        fine, coarse, loss, identity_ok = exact_identity(p, q, part)
        err = abs((fine - coarse) - loss)
        max_identity_error = max(max_identity_error, err)
        max_loss = max(max_loss, loss)
        if loss == 0:
            zero_loss_cases += 1
        if (fine == coarse) != is_sign_pure(p, q, part):
            equality_condition_failures += 1
        if not identity_ok:
            raise AssertionError("exact revelation identity failed")
    return max_identity_error, max_loss, zero_loss_cases, equality_condition_failures


def generate_csv(path="results/cycle049_exact_revelation_accounting.csv"):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "trials", "max_exact_identity_error", "max_observed_loss",
                    "zero_loss_cases", "equality_condition_failures"])
        for n in range(1, 13):
            err, loss, zeros, failures = exact_random_audit(n)
            w.writerow([n, 200, str(err), str(loss), zeros, failures])


if __name__ == "__main__":
    generate_csv()
