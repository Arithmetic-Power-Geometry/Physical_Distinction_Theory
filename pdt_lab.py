"""Physical Distinction Theory computational core.

This module mirrors the submission-ready PDT manuscript and keeps logical status
explicit: PDT-native/no-go results, conditional theorems, imported standard
quantum-information identities, and open frontier statements are not conflated.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Sequence
import math

import numpy as np
import pandas as pd
from scipy.linalg import expm, sqrtm

KB = 1.380649e-23
HBAR = 1.054571817e-34


@dataclass(frozen=True)
class ResourceWindow:
    energy: float
    time: float
    actions: tuple[str, ...] = ()
    region: str = ""
    epsilon: float = 0.0


@dataclass(frozen=True)
class PhysicalDistinction:
    A: str
    B: str
    resource: ResourceWindow


# ---------------------------------------------------------------------------
# Resource-bounded distinction and scalar-capacity / geometry separation
# ---------------------------------------------------------------------------
def codebook_capacity_bits(n: int) -> float:
    if n < 1:
        raise ValueError("n must be >= 1")
    return float(np.log2(n))


def max_admissible_capacity_bits(codebook_sizes: Iterable[int]) -> float:
    vals = [int(v) for v in codebook_sizes]
    if not vals:
        raise ValueError("empty codebook family")
    return max(codebook_capacity_bits(v) for v in vals)


def p_norm(x: Sequence[float], p: float) -> float:
    return float(np.linalg.norm(np.asarray(x, dtype=float), ord=p))


def parallelogram_defect(x, y, p: float = 2.0) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    return float(
        p_norm(x + y, p) ** 2 + p_norm(x - y, p) ** 2
        - 2 * p_norm(x, p) ** 2 - 2 * p_norm(y, p) ** 2
    )


def ceu_cer_counterfamily(ps=(1.25, 1.5, 2.0, 3.0, 4.0)) -> pd.DataFrame:
    e1, e2 = np.array([1.0, 0.0]), np.array([0.0, 1.0])
    rows = []
    for p in ps:
        defect = parallelogram_defect(e1, e2, p)
        rows.append({
            "p": float(p),
            "CEU_antipodal_midpoint": True,
            "CER_radial_representation": True,
            "parallelogram_defect": defect,
            "euclidean": bool(abs(defect) < 1e-12),
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# State-resolved distinction and conditional Euclidean structure
# ---------------------------------------------------------------------------
def q_distinction(x, G=None) -> float:
    x = np.asarray(x, float)
    G = np.eye(len(x)) if G is None else np.asarray(G, float)
    return float(x @ G @ x)


def polarization(x, y, norm_sq: Callable | None = None) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    norm_sq = (lambda z: float(np.asarray(z) @ np.asarray(z))) if norm_sq is None else norm_sq
    return float(0.25 * (norm_sq(x + y) - norm_sq(x - y)))


def bqdc_residual(x, y, G=None) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    return float(
        q_distinction(x + y, G) + q_distinction(x - y, G)
        - 2 * q_distinction(x, G) - 2 * q_distinction(y, G)
    )


def finite_group_invariant_metric(group, auxiliary=None) -> np.ndarray:
    mats = [np.asarray(g, float) for g in group]
    if not mats:
        raise ValueError("group must be nonempty")
    G0 = np.eye(mats[0].shape[0]) if auxiliary is None else np.asarray(auxiliary, float)
    G = sum(g.T @ G0 @ g for g in mats) / len(mats)
    return 0.5 * (G + G.T)


def pair_erasure(alpha, beta) -> np.ndarray:
    return 0.5 * (np.asarray(alpha, float) + np.asarray(beta, float))


def radial_state(mu, alpha, p: float) -> np.ndarray:
    return np.asarray(mu, float) + (2 * float(p) - 1) * (
        np.asarray(alpha, float) - np.asarray(mu, float)
    )


def ellipsoid_quadratic_form(axis_lengths) -> np.ndarray:
    a = np.asarray(axis_lengths, float)
    if np.any(a <= 0):
        raise ValueError("axis lengths must be positive")
    return np.diag(1.0 / (a * a))


def reversible_covariance_residual(U, G) -> float:
    U, G = np.asarray(U, float), np.asarray(G, float)
    return float(np.linalg.norm(U.T @ G @ U - G))


# ---------------------------------------------------------------------------
# Imported Bloch representation and conditional probability/correlations
# ---------------------------------------------------------------------------
def bloch_density(x) -> np.ndarray:
    x = np.asarray(x, float)
    if x.shape != (3,):
        raise ValueError("Bloch vector must have dimension 3")
    if np.linalg.norm(x) > 1 + 1e-12:
        raise ValueError("outside Bloch ball")
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    return 0.5 * (np.eye(2) + x[0] * sx + x[1] * sy + x[2] * sz)


def born_probabilities(amplitudes) -> np.ndarray:
    a = np.asarray(amplitudes, complex)
    w = np.abs(a) ** 2
    if w.sum() <= 0:
        raise ValueError("zero amplitude vector")
    return w / w.sum()


def orthogonal_additivity_residual(s, t, F: Callable[[float], float] = lambda q: q) -> float:
    return float(F(float(s) + float(t)) - F(float(s)) - F(float(t)))


def bilinear_correlation(a, b, T) -> float:
    return float(np.asarray(a, float) @ np.asarray(T, float) @ np.asarray(b, float))


def operator_norm(T) -> float:
    return float(np.linalg.svd(np.asarray(T, float), compute_uv=False)[0])


def chsh_bilinear(a0, a1, b0, b1, T) -> float:
    return abs(
        bilinear_correlation(a0, b0, T) + bilinear_correlation(a0, b1, T)
        + bilinear_correlation(a1, b0, T) - bilinear_correlation(a1, b1, T)
    )


def tsirelson_bound() -> float:
    return float(2 * np.sqrt(2))


# ---------------------------------------------------------------------------
# Restricted geometry and standard channel identities
# ---------------------------------------------------------------------------
def restricted_effect_norm(X, effects) -> float:
    X = np.asarray(X, complex)
    return float(max(abs(np.trace(np.asarray(E, complex) @ X)) for E in effects))


def null_kernel(basis_ops, effects, tol=1e-12):
    return [i for i, X in enumerate(basis_ops) if restricted_effect_norm(X, effects) <= tol]


def trace_distance(rho, sigma) -> float:
    d = np.asarray(rho, complex) - np.asarray(sigma, complex)
    return float(0.5 * np.sum(np.linalg.svd(d, compute_uv=False)))


def apply_kraus(rho, kraus):
    rho = np.asarray(rho, complex)
    return sum(np.asarray(K) @ rho @ np.asarray(K).conj().T for K in kraus)


def stinespring_from_kraus(kraus) -> np.ndarray:
    ks = [np.asarray(K, complex) for K in kraus]
    dout, din = ks[0].shape
    V = np.zeros((dout * len(ks), din), complex)
    for i, K in enumerate(ks):
        V[i * dout:(i + 1) * dout] = K
    return V


def global_dilated_state(rho, kraus) -> np.ndarray:
    V = stinespring_from_kraus(kraus)
    rho = np.asarray(rho, complex)
    return V @ rho @ V.conj().T


def complementary_output(rho, kraus) -> np.ndarray:
    ks, rho = [np.asarray(K, complex) for K in kraus], np.asarray(rho, complex)
    out = np.zeros((len(ks), len(ks)), complex)
    for i, Ki in enumerate(ks):
        for j, Kj in enumerate(ks):
            out[i, j] = np.trace(Ki @ rho @ Kj.conj().T)
    return out


def amplitude_damping_kraus(gamma: float):
    g = float(gamma)
    if not 0 <= g <= 1:
        raise ValueError("gamma must lie in [0,1]")
    return [
        np.array([[1, 0], [0, np.sqrt(1 - g)]], complex),
        np.array([[0, np.sqrt(g)], [0, 0]], complex),
    ]


def global_distinction_residual(rho, sigma, kraus) -> float:
    return abs(
        trace_distance(global_dilated_state(rho, kraus), global_dilated_state(sigma, kraus))
        - trace_distance(rho, sigma)
    )


def local_contraction_gap(rho, sigma, kraus) -> float:
    return trace_distance(rho, sigma) - trace_distance(
        apply_kraus(rho, kraus), apply_kraus(sigma, kraus)
    )


# ---------------------------------------------------------------------------
# Pure and mixed environmental records
# ---------------------------------------------------------------------------
def record_overlap(e0, e1) -> complex:
    return complex(np.vdot(np.asarray(e1, complex), np.asarray(e0, complex)))


def coherence_record_bit(kappa) -> float:
    a = abs(kappa)
    return np.inf if a <= 0 else float(-np.log2(a))


def pure_record_distinguishability(kappa) -> float:
    return float(np.sqrt(max(0.0, 1 - abs(kappa) ** 2)))


def overlap_from_pure_distinguishability(D) -> float:
    D = float(D)
    if not 0 <= D <= 1:
        raise ValueError("D must lie in [0,1]")
    return float(np.sqrt(max(0.0, 1 - D * D)))


def root_fidelity(rho, sigma) -> float:
    rho, sigma = np.asarray(rho, complex), np.asarray(sigma, complex)
    sr = sqrtm(rho)
    return float(np.real(np.trace(sqrtm(sr @ sigma @ sr))))


def controlled_environment_outputs(eta, U0, U1):
    eta, U0, U1 = np.asarray(eta, complex), np.asarray(U0, complex), np.asarray(U1, complex)
    rho0, rho1 = U0 @ eta @ U0.conj().T, U1 @ eta @ U1.conj().T
    chi = complex(np.trace(U0 @ eta @ U1.conj().T))
    return chi, rho0, rho1


def mixed_record_envelope(eta, U0, U1) -> dict:
    chi, rho0, rho1 = controlled_environment_outputs(eta, U0, U1)
    D = trace_distance(rho0, rho1)
    f = root_fidelity(rho0, rho1)
    upper = float(np.sqrt(max(0.0, 1 - D * D)))
    return {
        "abs_chi": abs(chi),
        "root_fidelity": f,
        "trace_distinguishability": D,
        "fuchs_van_de_graaf_upper": upper,
        "left_residual": f - abs(chi),
        "right_residual": upper - f,
    }


# ---------------------------------------------------------------------------
# ADDE: exact controlled-dephasing scope
# ---------------------------------------------------------------------------
def deterministic_rate(nu, kappa) -> float:
    return np.inf if abs(kappa) <= 0 else float(-float(nu) * np.log(abs(kappa)))


def deterministic_rate_from_D(nu, D) -> float:
    D = float(D)
    if not 0 <= D <= 1:
        raise ValueError("D must lie in [0,1]")
    if D == 1:
        return np.inf
    return float(-0.5 * float(nu) * np.log(1 - D * D))


def weak_record_rate(nu, D) -> float:
    return float(0.5 * float(nu) * float(D) ** 2)


def poisson_rate(nu, kappa) -> float:
    return float(float(nu) * (1 - float(np.real(kappa))))


def phase_complete_generator(chi, chi_dot) -> tuple[float, float]:
    chi, chi_dot = complex(chi), complex(chi_dot)
    if abs(chi) == 0:
        raise ValueError("logarithmic generator is singular at chi=0")
    z = chi_dot / chi
    return float(-np.real(z)), float(np.imag(z))


def conditional_expectation_dephase(rho):
    rho = np.asarray(rho, complex)
    return np.diag(np.diag(rho))


def akhtar_rhs(rho, H, gamma, expectation=conditional_expectation_dephase, hbar=1.0):
    rho, H = np.asarray(rho, complex), np.asarray(H, complex)
    return -1j / hbar * (H @ rho - rho @ H) + float(gamma) * (expectation(rho) - rho)


def akhtar_dephasing_solution(t, c0, omega, gamma):
    return complex(c0) * np.exp(-(float(gamma) + 1j * float(omega)) * np.asarray(t, float))


# ---------------------------------------------------------------------------
# Total dynamical distinction tensor - manuscript Theorem 13.1
# ---------------------------------------------------------------------------
def total_distinction_tensor(G, G_dot, L) -> np.ndarray:
    G, G_dot, L = np.asarray(G, float), np.asarray(G_dot, float), np.asarray(L, float)
    A = -0.5 * (G_dot + L.T @ G + G @ L)
    return 0.5 * (A + A.T)


def metric_motion_component(G_dot) -> np.ndarray:
    return -0.5 * np.asarray(G_dot, float)


def state_flow_component(G, L) -> np.ndarray:
    G, L = np.asarray(G, float), np.asarray(L, float)
    return -0.5 * (L.T @ G + G @ L)


def q_dot_from_flow(X, G, G_dot, L) -> float:
    X, G, G_dot, L = map(lambda z: np.asarray(z, float), (X, G, G_dot, L))
    return float(X @ (G_dot + L.T @ G + G @ L) @ X)


def total_tensor_identity_residual(X, G, G_dot, L) -> float:
    X = np.asarray(X, float)
    A = total_distinction_tensor(G, G_dot, L)
    return float(-0.5 * q_dot_from_flow(X, G, G_dot, L) - X @ A @ X)


def distinction_backflow_witness(X, A_tot) -> float:
    X, A_tot = np.asarray(X, float), np.asarray(A_tot, float)
    return float(X @ A_tot @ X)


# ---------------------------------------------------------------------------
# Resource-relative thermodynamic / hypothesis-testing quantities
# ---------------------------------------------------------------------------
def shannon_bits(p) -> float:
    p = np.asarray(p, float)
    if np.any(p < 0) or p.sum() <= 0:
        raise ValueError("invalid probability vector")
    p = p / p.sum()
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def conditional_entropy_bits(joint) -> float:
    j = np.asarray(joint, float)
    j = j / j.sum()
    return shannon_bits(j.ravel()) - shannon_bits(j.sum(axis=0))


def landauer_min_heat(H_bits, T, kb=KB) -> float:
    return float(kb * float(T) * np.log(2) * float(H_bits))


def gibbs_state(H, T, kb=KB):
    H = np.asarray(H, complex)
    X = expm(-H / (kb * float(T)))
    return X / np.trace(X)


def equilibrium_free_energy(H, T, kb=KB) -> float:
    H = np.asarray(H, complex)
    Z = float(np.real(np.trace(expm(-H / (kb * float(T))))))
    return float(-kb * float(T) * np.log(Z))


def hypothesis_testing_beta(rho, sigma, effects, epsilon) -> float:
    rho, sigma = np.asarray(rho, complex), np.asarray(sigma, complex)
    vals = [float(np.real(np.trace(T @ sigma))) for T in effects
            if np.real(np.trace(T @ rho)) >= 1 - float(epsilon) - 1e-12]
    return min(vals) if vals else np.inf


def hypothesis_testing_divergence_bits(rho, sigma, effects, epsilon) -> float:
    beta = hypothesis_testing_beta(rho, sigma, effects, epsilon)
    if beta == 0:
        return np.inf
    return -np.inf if not np.isfinite(beta) else float(-np.log2(beta))


def hypothesis_testing_distinction_free_energy(rho, H, T, effects, epsilon, kb=KB) -> float:
    gamma = gibbs_state(H, T, kb)
    D = hypothesis_testing_divergence_bits(rho, gamma, effects, epsilon)
    return float(equilibrium_free_energy(H, T, kb) + kb * float(T) * np.log(2) * D)


# ---------------------------------------------------------------------------
# Deterministic synthetic benchmark used for manuscript Table 2 / Figure 2
# ---------------------------------------------------------------------------
def rmse(y, yhat) -> float:
    return float(np.sqrt(np.mean((np.asarray(y) - np.asarray(yhat)) ** 2)))


def mae(y, yhat) -> float:
    return float(np.mean(np.abs(np.asarray(y) - np.asarray(yhat))))


def aic_from_sse(y, yhat, k) -> float:
    n = len(y)
    sse = max(float(np.sum((np.asarray(y) - np.asarray(yhat)) ** 2)), 1e-300)
    return float(n * np.log(sse / n) + 2 * int(k))


def bic_from_sse(y, yhat, k) -> float:
    n = len(y)
    sse = max(float(np.sum((np.asarray(y) - np.asarray(yhat)) ** 2)), 1e-300)
    return float(n * np.log(sse / n) + int(k) * np.log(n))


def synthetic_record_dataset(seed=7, n=240, nu=1.3, D=0.55, omega=1.7, noise=0.012, poisson=False):
    rng = np.random.default_rng(seed)
    t = np.linspace(0, 6, int(n))
    kappa = overlap_from_pure_distinguishability(D)
    gamma = poisson_rate(nu, kappa) if poisson else deterministic_rate_from_D(nu, D)
    truth = np.exp(-gamma * t) * np.cos(omega * t)
    signal = truth + rng.normal(0, noise, len(t))
    return pd.DataFrame({"t": t, "signal": signal, "truth": truth}), {
        "nu": float(nu), "D_E": float(D), "omega": float(omega),
        "gamma": float(gamma), "kappa": float(kappa), "poisson": bool(poisson),
    }


def compare_models(df, meta) -> pd.DataFrame:
    t, y, w = df.t.to_numpy(float), df.signal.to_numpy(float), float(meta["omega"])
    sch = np.cos(w * t)
    grid = np.linspace(0, 1.5, 601)
    gfit = min(grid, key=lambda g: np.sum((y - np.exp(-g * t) * np.cos(w * t)) ** 2))
    gkls = np.exp(-gfit * t) * np.cos(w * t)
    best = (np.inf, None)
    for g0 in np.linspace(0, 1, 31):
        for amp in np.linspace(-0.25, 0.25, 21):
            for freq in np.linspace(0.5, 4, 18):
                integ = g0 * t + amp * (1 - np.cos(freq * t)) / freq
                pred = np.exp(-integ) * np.cos(w * t)
                sse = float(np.sum((y - pred) ** 2))
                if sse < best[0]:
                    best = (sse, pred)
    pdt = np.exp(-float(meta["gamma"]) * t) * np.cos(w * t)
    rows = []
    for name, pred, k in [
        ("Non-Markovian", best[1], 3), ("PDT/ADDE", pdt, 0),
        ("GKLS", gkls, 1), ("Schrodinger", sch, 0),
    ]:
        rows.append({"Model": name, "RMSE": rmse(y, pred), "MAE": mae(y, pred),
                     "AIC": aic_from_sse(y, pred, k), "BIC": bic_from_sse(y, pred, k),
                     "k_dyn": int(k)})
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Manuscript-facing tables / evidence registry
# ---------------------------------------------------------------------------
def core_numerical_audit(seed=42, samples=100_000) -> pd.DataFrame:
    rng, maxS, T = np.random.default_rng(seed), 0.0, np.eye(2)
    for _ in range(int(samples)):
        vecs = []
        for _ in range(4):
            x = rng.normal(size=2); vecs.append(x / np.linalg.norm(x))
        maxS = max(maxS, chsh_bilinear(*vecs, T))
    r, s, ks = np.diag([1, 0]).astype(complex), np.diag([0, 1]).astype(complex), amplitude_damping_kraus(0.37)
    nu, D = 1.3, 0.55
    kap = overlap_from_pure_distinguishability(D)
    rows = [
        ("Maximum random planar CHSH value (100,000 samples)", f"{maxS:.10f}"),
        ("Tsirelson bound", f"{tsirelson_bound():.10f}"),
        ("Stinespring global-distinction residual", f"{global_distinction_residual(r, s, ks):.1f}"),
        ("Local contraction gap in amplitude-damping audit", f"{local_contraction_gap(r, s, ks):.10f}"),
        ("Biased-bit entropy H2(0.01)", f"{shannon_bits([.99, .01]):.10f} bits"),
        ("Controlled-record example (nu, D_E)", f"({nu:.1f}, {D:.2f})"),
        ("Derived kappa", f"{kap:.10f}"),
        ("Exact Gamma_A", f"{deterministic_rate_from_D(nu, D):.10f}"),
        ("Weak-record approximation", f"{weak_record_rate(nu, D):.10f}"),
    ]
    return pd.DataFrame(rows, columns=["Quantity", "Result"])


def theorem_status_matrix() -> pd.DataFrame:
    rows = [
        ["PDT no-go theorem", "Scalar capacity does not determine geometry", "Non-isometric equal-capacity models", "Scalar capacity alone uniquely fixes local geometry"],
        ["PDT no-go theorem", "CEU+CER do not imply BQDC", "Radial l_p counterfamily", "Counterfamily invalid under stated CEU/CER definitions"],
        ["Conditional PDT theorem", "CEU+CER+RDE => B^n", "Finite dimension; closed reversible group; maximal-pair coverage; RDE", "All assumptions hold but body is non-ellipsoidal"],
        ["Imported theorem", "B^n => B^3 under composite conditions", "External local-tomographic reversible-interaction classification", "No claim outside imported theorem hypotheses"],
        ["PDT no-go theorem", "Local data do not fix unique composite", "Inequivalent composites with same locals", "Unique-composition theorem from strictly local data"],
        ["Conditional theorem", "Quadratic weight => Born form", "Noncontextual F(Q_D); positivity; normalized orthogonal additivity", "Counterexample inside assumptions"],
        ["Conditional theorem", "Euclidean bilinear correlations => 2sqrt(2)", "Separate affinity; centering; ||T||_op<=1", "Violation of bounded bilinear representation"],
        ["Exact PDT identity", "Total distinction tensor", "Differentiable G_R, X_t; Xdot=LX", "Product-rule failure"],
        ["Exact controlled-sector identity", "c'=c chi", "Controlled unitary; initial product structure", "Persistent violation inside domain"],
        ["Imported inequality + PDT use", "|chi|<=f_E<=sqrt(1-D_E^2)", "Uhlmann/Fuchs-van de Graaf hypotheses", "Counterexample to standard fidelity inequalities"],
        ["Exact sector representation", "ADDE time-local form", "Nonzero differentiable overlap; phase in H_eff", "Finite-time map mismatch in domain"],
        ["Identifiability theorem", "Same-input microscopic QM gives same chi", "Same environment state and controlled unitaries", "Different result under same microscopic model"],
        ["Computational evidence", "Numerical audits", "Correct implementation and tolerance", "Test/CI failure"],
        ["Real-data stress test", "Three public sources; no decisive case", "Published public data as processed", "Qualifying fully blind same-input dataset found"],
        ["Open frontier", "PDT-specific composition/prediction/gravity", "Not yet proved", "Remains open until proof/experiment"],
    ]
    return pd.DataFrame(rows, columns=["Status", "Statement", "Required assumptions", "Failure condition"])


def real_data_audit_table() -> pd.DataFrame:
    rows = [
        ["Photonic qubit + quantum which-path detector", "Independent system coherence and detector distinguishability", "Pure-record zero-fit RMSE 0.338286; MAE 0.268612", "Not decisive: records mixed/imperfect; pure equality inapplicable; mixed same-input baseline required."],
        ["NPL driven superconducting qubits", "1728 raw rows; 558 reconstructed X/Y coherence traces", "Median RMSE: Schrodinger 0.561710; GKLS 0.216393; non-Markovian 0.183937", "Not decisive: no independent environment record in public file."],
        ["Ramsey experimental archive", "11 visibility-delay points", "Schrodinger RMSE 0.221700; fitted GKLS 0.165523; fitted gamma=0.00558546", "Not decisive: no independent environment record."],
    ]
    return pd.DataFrame(rows, columns=["Dataset", "Observable audit", "Main result", "Status"])


def evidence_count_summary() -> dict:
    return {"N_real": 3, "N_independent_record": 1, "N_time_decay": 2, "N_decisive": 0}


if __name__ == "__main__":
    print(core_numerical_audit().to_string(index=False))
