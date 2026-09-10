"""Cycle 050: exact distinction-loss accounting for arbitrary stochastic resource maps.

For probability vectors p,q and a column-stochastic kernel K,
D(p,q)-D(Kp,Kq) = 1/2 sum_j [sum_i K[j,i]|d_i| - |sum_i K[j,i]d_i|], d=p-q.
The identity is exact; equality in data processing holds iff every output row j receives
positive K-weight from at most one sign class of d (zeros irrelevant).
"""
from fractions import Fraction


def tv_from_delta(delta):
    return sum(abs(x) for x in delta) / 2


def apply_kernel(K, delta):
    return [sum(row[i] * delta[i] for i in range(len(delta))) for row in K]


def stochastic_loss_rhs(K, delta):
    total = Fraction(0, 1)
    for row in K:
        incoming_abs = sum(row[i] * abs(delta[i]) for i in range(len(delta)))
        net = abs(sum(row[i] * delta[i] for i in range(len(delta))))
        total += incoming_abs - net
    return total / 2


def exact_loss(K, p, q):
    delta = [a-b for a,b in zip(p,q)]
    return tv_from_delta(delta) - tv_from_delta(apply_kernel(K, delta))


def equality_condition(K, p, q):
    delta = [a-b for a,b in zip(p,q)]
    for row in K:
        has_pos = any(row[i] > 0 and delta[i] > 0 for i in range(len(delta)))
        has_neg = any(row[i] > 0 and delta[i] < 0 for i in range(len(delta)))
        if has_pos and has_neg:
            return False
    return True


def is_column_stochastic(K):
    if not K or not K[0]:
        return False
    n = len(K[0])
    if any(len(r) != n for r in K):
        return False
    return all(all(x >= 0 for x in r) for r in K) and all(sum(K[j][i] for j in range(len(K))) == 1 for i in range(n))
