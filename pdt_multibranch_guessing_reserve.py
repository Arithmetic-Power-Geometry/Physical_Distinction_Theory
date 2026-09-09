"""Cycle 026: multi-branch guessing-reserve balance.

For a classical label X encoded in quantum records on S E, define
G_SE = P_guess(X|SE), G_S = P_guess(X|S), and R_G = G_SE-G_S >= 0.

Under one common CPTP map Lambda on SE followed by access to S,
L_G = G_SE(s)-G_SE(t) >= 0 and the exact accounting identity is

    G_S(t)-G_S(s) = R_G(s)-R_G(t)-L_G.

This is a direct consequence of data processing for optimal guessing
probability. The numerical audit below exercises the commuting/classical
special case exactly, where P_guess has a closed form.
"""
from __future__ import annotations
import numpy as np


def classical_guess_probability(priors: np.ndarray, conditional: np.ndarray) -> float:
    """Exact P_guess(X|Z) for classical conditional P(z|x)."""
    p = np.asarray(priors, dtype=float)
    q = np.asarray(conditional, dtype=float)
    if q.ndim != 2 or len(p) != q.shape[0]:
        raise ValueError("shape mismatch")
    if np.any(p < 0) or not np.isclose(p.sum(), 1.0):
        raise ValueError("priors must be a probability vector")
    if np.any(q < -1e-15) or not np.allclose(q.sum(axis=1), 1.0, atol=1e-12):
        raise ValueError("conditional rows must be probabilities")
    return float(np.max(p[:, None] * q, axis=0).sum())


def coarse_grain_environment(conditional_se: np.ndarray, d_s: int, d_e: int) -> np.ndarray:
    """Marginalize a flat joint alphabet z=(s,e) down to s."""
    q = np.asarray(conditional_se, dtype=float)
    if q.shape[1] != d_s * d_e:
        raise ValueError("joint alphabet dimension mismatch")
    return q.reshape(q.shape[0], d_s, d_e).sum(axis=2)


def apply_common_channel(conditional: np.ndarray, channel: np.ndarray) -> np.ndarray:
    """Apply same row-stochastic channel K(z'|z) to every hypothesis."""
    q = np.asarray(conditional, dtype=float)
    k = np.asarray(channel, dtype=float)
    if q.shape[1] != k.shape[0]:
        raise ValueError("channel input mismatch")
    if np.any(k < -1e-15) or not np.allclose(k.sum(axis=1), 1.0, atol=1e-12):
        raise ValueError("channel must be row stochastic")
    return q @ k


def reserve_balance(priors, q_se_s, q_se_t, d_s: int, d_e: int) -> dict:
    g_joint_s = classical_guess_probability(priors, q_se_s)
    g_local_s = classical_guess_probability(priors, coarse_grain_environment(q_se_s, d_s, d_e))
    g_joint_t = classical_guess_probability(priors, q_se_t)
    g_local_t = classical_guess_probability(priors, coarse_grain_environment(q_se_t, d_s, d_e))
    r_s = g_joint_s - g_local_s
    r_t = g_joint_t - g_local_t
    loss = g_joint_s - g_joint_t
    delta_local = g_local_t - g_local_s
    rhs = r_s - r_t - loss
    return {"G_joint_s": g_joint_s, "G_local_s": g_local_s, "G_joint_t": g_joint_t,
            "G_local_t": g_local_t, "R_s": r_s, "R_t": r_t, "L": loss,
            "delta_local": delta_local, "rhs": rhs, "residual": delta_local-rhs}


def random_probability_vector(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.dirichlet(np.ones(n))


def random_conditional(rng: np.random.Generator, k: int, alphabet: int) -> np.ndarray:
    return rng.dirichlet(np.ones(alphabet), size=k)


def random_channel(rng: np.random.Generator, n: int) -> np.ndarray:
    return rng.dirichlet(np.ones(n), size=n)


def random_permutation_channel(rng: np.random.Generator, n: int) -> np.ndarray:
    perm = rng.permutation(n)
    k = np.zeros((n, n))
    k[np.arange(n), perm] = 1.0
    return k


def run_dimension_audit(seed: int = 260926, trials: int = 200, dims=range(1, 13)):
    rng = np.random.default_rng(seed)
    rows = []
    for d_s in dims:
        d_e = 2 if d_s > 1 else 3
        k_labels = max(3, min(7, d_s + 2))
        max_resid = max_bound_excess = max_loss_negative = max_unitary_loss = 0.0
        for _ in range(trials):
            p = random_probability_vector(rng, k_labels)
            q0 = random_conditional(rng, k_labels, d_s*d_e)
            K = random_channel(rng, d_s*d_e)
            q1 = apply_common_channel(q0, K)
            b = reserve_balance(p, q0, q1, d_s, d_e)
            max_resid = max(max_resid, abs(b["residual"]))
            max_bound_excess = max(max_bound_excess, b["delta_local"] - b["R_s"])
            max_loss_negative = max(max_loss_negative, -b["L"])
            P = random_permutation_channel(rng, d_s*d_e)
            qp = apply_common_channel(q0, P)
            bp = reserve_balance(p, q0, qp, d_s, d_e)
            max_unitary_loss = max(max_unitary_loss, abs(bp["L"]))
        rows.append({"d_s": d_s, "d_e": d_e, "labels": k_labels, "trials": trials,
                     "max_abs_balance_residual": max_resid,
                     "max_delta_minus_initial_reserve": max_bound_excess,
                     "max_negative_global_loss": max_loss_negative,
                     "max_abs_reversible_global_loss": max_unitary_loss})
    return rows
