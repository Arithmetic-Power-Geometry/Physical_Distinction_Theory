"""Cycle 061: exact chi-square revelation/conservation law under resource channels.

Finite full-support binary experiments. Classification:
PROVED + IMPORTED/KNOWN mathematics + PDT resource-accounting theorem.
"""
from fractions import Fraction
from typing import Sequence


def pushforward(kernel: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]):
    return [sum(kernel[j][i] * vector[i] for i in range(len(vector))) for j in range(len(kernel))]


def compose_channels(h, k):
    """Return H o K for column-stochastic kernels K:X->J and H:J->Y."""
    return [[sum(h[a][j] * k[j][i] for j in range(len(k))) for i in range(len(k[0]))] for a in range(len(h))]


def chi2_divergence(p, q):
    if len(p) != len(q) or any(qi <= 0 for qi in q):
        raise ValueError("p,q must have equal length and q full support")
    return sum((pi - qi) ** 2 / qi for pi, qi in zip(p, q))


def revelation_loss(p, q, kernel):
    """Exact distinction hidden by K: chi2(P||Q)-chi2(PK||QK)."""
    kp, kq = pushforward(kernel, p), pushforward(kernel, q)
    if any(x <= 0 for x in kq):
        raise ValueError("remove zero-Q output cells before applying theorem")
    return chi2_divergence(p, q) - chi2_divergence(kp, kq)


def conditional_variance_loss(p, q, kernel):
    """E_Q Var_Q[L|J], L=P/Q; exactly equals revelation_loss."""
    l = [pi / qi for pi, qi in zip(p, q)]
    kq = pushforward(kernel, q)
    total = Fraction(0)
    for j, qj in enumerate(kq):
        if qj <= 0:
            raise ValueError("remove zero-Q output cells before applying theorem")
        mean = sum(kernel[j][i] * q[i] * l[i] for i in range(len(q))) / qj
        total += sum(kernel[j][i] * q[i] * (l[i] - mean) ** 2 for i in range(len(q)))
    return total


def nested_conservation(p, q, k, h):
    """Return losses (X->J, J->Y, X->Y); theorem says third=first+second."""
    kp, kq = pushforward(k, p), pushforward(k, q)
    hk = compose_channels(h, k)
    first = revelation_loss(p, q, k)
    second = revelation_loss(kp, kq, h)
    total = revelation_loss(p, q, hk)
    return first, second, total


def verify_exact(p, q, k, h):
    first, second, total = nested_conservation(p, q, k, h)
    return (
        first == conditional_variance_loss(p, q, k)
        and first >= 0 and second >= 0
        and total == first + second
    )
