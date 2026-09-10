"""Cycle 056: distinction-profile martingale/resource law.

Finite full-support binary experiments only.  This module verifies the exact
identity that a stochastic resource map sends the likelihood-ratio variable
L=P/Q to its conditional expectation given the accessible output J.

Classification: PROVED + IMPORTED/KNOWN mathematics + PDT structural bridge.
"""

from fractions import Fraction
from typing import Callable, Iterable, Sequence


def pushforward(kernel: Sequence[Sequence[Fraction]], vector: Sequence[Fraction]):
    return [
        sum(kernel[j][i] * vector[i] for i in range(len(vector)))
        for j in range(len(kernel))
    ]


def likelihood_ratio(p: Sequence[Fraction], q: Sequence[Fraction]):
    if len(p) != len(q):
        raise ValueError("p and q must have equal length")
    if any(x <= 0 for x in q):
        raise ValueError("cycle056 finite theorem assumes full support q_i>0")
    return [p_i / q_i for p_i, q_i in zip(p, q)]


def coarse_likelihood_ratio(
    p: Sequence[Fraction],
    q: Sequence[Fraction],
    kernel: Sequence[Sequence[Fraction]],
):
    kp = pushforward(kernel, p)
    kq = pushforward(kernel, q)
    if any(x <= 0 for x in kq):
        raise ValueError("remove inaccessible zero-probability outputs first")
    return likelihood_ratio(kp, kq)


def conditional_expectation_ratio(
    p: Sequence[Fraction],
    q: Sequence[Fraction],
    kernel: Sequence[Sequence[Fraction]],
):
    """Return E_Q[L|J=j], where I~Q and J~K(.|I)."""
    l = likelihood_ratio(p, q)
    kq = pushforward(kernel, q)
    out = []
    for j in range(len(kernel)):
        if kq[j] <= 0:
            raise ValueError("remove inaccessible zero-probability outputs first")
        numerator = sum(kernel[j][i] * q[i] * l[i] for i in range(len(q)))
        out.append(numerator / kq[j])
    return out


def convex_functional(
    p: Sequence[Fraction],
    q: Sequence[Fraction],
    phi: Callable[[Fraction], Fraction],
):
    l = likelihood_ratio(p, q)
    return sum(q_i * phi(l_i) for q_i, l_i in zip(q, l))


def tv_from_profile(p: Sequence[Fraction], q: Sequence[Fraction]):
    return Fraction(1, 2) * convex_functional(p, q, lambda x: abs(x - 1))


def tensor(a: Sequence[Fraction], b: Sequence[Fraction]):
    return [x * y for x in a for y in b]


def tensor_kernel(
    ka: Sequence[Sequence[Fraction]], kb: Sequence[Sequence[Fraction]]
):
    """Kronecker product of two column-stochastic kernels."""
    ma, na = len(ka), len(ka[0])
    mb, nb = len(kb), len(kb[0])
    out = [[Fraction(0) for _ in range(na * nb)] for _ in range(ma * mb)]
    for ja in range(ma):
        for jb in range(mb):
            j = ja * mb + jb
            for ia in range(na):
                for ib in range(nb):
                    i = ia * nb + ib
                    out[j][i] = ka[ja][ia] * kb[jb][ib]
    return out


def composition_resource_commutes(pa, qa, pb, qb, ka, kb):
    """Exact check: local degradation then product equals product then K_AxK_B."""
    lhs_p = tensor(pushforward(ka, pa), pushforward(kb, pb))
    lhs_q = tensor(pushforward(ka, qa), pushforward(kb, qb))
    kab = tensor_kernel(ka, kb)
    rhs_p = pushforward(kab, tensor(pa, pb))
    rhs_q = pushforward(kab, tensor(qa, qb))
    return lhs_p == rhs_p and lhs_q == rhs_q
