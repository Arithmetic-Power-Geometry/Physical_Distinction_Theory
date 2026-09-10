"""Cycle 058: exact audit of augmented likelihood-ratio profile canonicalization.

Classification target: PROVED + IMPORTED/KNOWN boundary.
No PDT novelty is claimed.
"""
from fractions import Fraction
from collections import defaultdict
from random import Random


def normalize(xs):
    s = sum(xs, Fraction(0))
    return tuple(x / s for x in xs)


def augmented_profile(p, q):
    """Return singular P-mass and Q-weighted finite likelihood-ratio profile."""
    s = sum((pi for pi, qi in zip(p, q) if qi == 0), Fraction(0))
    mu = defaultdict(Fraction)
    for pi, qi in zip(p, q):
        if qi > 0:
            mu[pi / qi] += qi
    return s, tuple(sorted(mu.items(), key=lambda z: z[0]))


def canonical_experiment(p, q):
    """Collapse outcomes with equal likelihood ratio, plus one singular symbol."""
    s, mu = augmented_profile(p, q)
    pc = [lam * w for lam, w in mu]
    qc = [w for _, w in mu]
    if s:
        pc.append(s)
        qc.append(Fraction(0))
    return tuple(pc), tuple(qc)


def tv(p, q):
    return sum((abs(a-b) for a, b in zip(p, q)), Fraction(0)) / 2


def split_experiment(p, q, rng):
    """Split each outcome identically under both hypotheses; Blackwell-equivalent refinement."""
    ps, qs = [], []
    for pi, qi in zip(p, q):
        a = Fraction(rng.randint(1, 9), 10)
        ps.extend((a*pi, (1-a)*pi))
        qs.extend((a*qi, (1-a)*qi))
    return tuple(ps), tuple(qs)


def random_pair(n, rng, allow_zeros=True):
    def draw():
        vals = [rng.randint(0 if allow_zeros else 1, 9) for _ in range(n)]
        if not any(vals):
            vals[rng.randrange(n)] = 1
        return normalize(tuple(Fraction(v) for v in vals))
    return draw(), draw()


def audit(seed=58058, trials_per_n=200):
    rng = Random(seed)
    rows = []
    for n in range(1, 13):
        failures = 0
        for _ in range(trials_per_n):
            p, q = random_pair(n, rng, allow_zeros=True)
            pc, qc = canonical_experiment(p, q)
            p2, q2 = split_experiment(p, q, rng)
            # Canonical profile is unchanged by likelihood-preserving splitting.
            if augmented_profile(p, q) != augmented_profile(pc, qc):
                failures += 1
            if augmented_profile(p, q) != augmented_profile(p2, q2):
                failures += 1
            # All decision-relevant TV distinction is preserved by canonicalization/splitting.
            if tv(p, q) != tv(pc, qc) or tv(p, q) != tv(p2, q2):
                failures += 1
        rows.append((n, trials_per_n, failures))
    return rows


if __name__ == "__main__":
    print("n,trials,failures")
    for row in audit():
        print(",".join(map(str, row)))
