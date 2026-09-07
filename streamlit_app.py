"""Interactive Physical Distinction Theory breakthrough laboratory.

This app is deliberately conservative: it visualizes proved identities,
conditional results, no-go tests, and open research hypotheses separately.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import streamlit as st

from pdt_lab import (
    ceu_cer_counterfamily,
    deterministic_rate_from_D,
    mixed_record_envelope,
    total_distinction_tensor,
    total_tensor_identity_residual,
    tsirelson_bound,
)
from pdt_dimension import dimension_audit

st.set_page_config(page_title="PDT Breakthrough Lab", layout="wide")
st.title("Physical Distinction Theory — Breakthrough Laboratory")
st.caption("Proofs, counterexamples, simulations, falsification tests, and same-input audits")

st.sidebar.header("Research controls")
page = st.sidebar.radio(
    "Module",
    [
        "Research dashboard",
        "Geometry no-go",
        "Dimension selection audit",
        "Operational dimension",
        "Total distinction tensor",
        "Environmental records",
        "Same-input test design",
        "Proof-status ledger",
    ],
)

if page == "Research dashboard":
    st.subheader("Current research frontier")
    st.markdown(
        """
        **Priority breakthrough routes**
        1. PDT-native composition principle strong enough to constrain the elementary dimension.
        2. Same-input physical prediction that differs quantitatively from standard quantum mechanics.
        3. New resource-relative monotone or dynamical theorem not reducible to known GPT/QI results.

        A result is promoted only after: mathematical proof or numerical stress test, counterexample search,
        prior-art check, and explicit falsification conditions.
        """
    )
    st.metric("Current decisive PDT-specific experiments", 0)
    st.metric("Current real-data audits", 3)
    st.warning("Local CEU+CER+RDE structure cannot select n=3: every Euclidean ball B^n passes. Resolution-scaled codebook growth can identify an existing n, but that is standard metric-entropy mathematics and does not explain why n=3.")

elif page == "Geometry no-go":
    st.subheader("CEU + CER does not force Euclidean geometry")
    ps = st.multiselect("p values", [1.1, 1.25, 1.5, 2.0, 3.0, 4.0, 6.0], default=[1.25, 1.5, 2.0, 3.0, 4.0])
    df = ceu_cer_counterfamily(ps)
    st.dataframe(df, use_container_width=True)
    st.write("Euclidean structure is detected by a zero parallelogram defect; among the tested lp balls this occurs only at p=2.")

elif page == "Dimension selection audit":
    st.subheader("Local dimension-selection no-go")
    st.write("CEU, CER and RDE hold on every Euclidean unit ball B^n. Therefore these local assumptions alone cannot uniquely select n=3.")
    n_max = st.slider("Maximum dimension to test", 3, 20, 10)
    samples = st.slider("Random pairs per dimension", 10, 500, 100, 10)
    rows = []
    for n in range(2, n_max + 1):
        rng = np.random.default_rng(20260907 + n)
        ceu = cer = rde = 0.0
        for _ in range(samples):
            a = rng.normal(size=n)
            a /= np.linalg.norm(a)
            ceu = max(ceu, float(np.linalg.norm(0.5 * (a - a))))
            r = float(rng.random())
            q = 0.5 * (1.0 + r)
            cer = max(cer, float(np.linalg.norm(r * a - (q * a + (1.0 - q) * (-a)))))
            b = rng.normal(size=n)
            b /= np.linalg.norm(b)
            if np.linalg.norm(a - b) < 1e-14:
                H = np.eye(n)
            else:
                v = a - b
                v /= np.linalg.norm(v)
                H = np.eye(n) - 2.0 * np.outer(v, v)
            rde = max(rde, float(np.linalg.norm(H @ a - b)), float(np.linalg.norm(H.T @ H - np.eye(n))))
        rows.append([n, ceu, cer, rde, max(ceu, cer, rde) < 1e-10])
    audit = pd.DataFrame(rows, columns=["n", "CEU residual", "CER residual", "RDE residual", "PASS"])
    st.dataframe(audit, use_container_width=True)
    st.success("PROVED / NO-GO: all n>=2 satisfy the same local structure. A PDT-native n=3 theorem must add a dimension-sensitive composite or interventional principle.")
    st.caption("The random audit checks the constructive proof numerically; it is not a substitute for the proof.")

elif page == "Operational dimension":
    st.subheader("Resolution-scaled distinction capacity")
    st.write("A single capacity value does not determine geometry, but the asymptotic growth of distinguishable codebooks with improving resolution can identify an already-existing finite metric dimension.")
    n = st.slider("Candidate metric dimension n", 2, 12, 3)
    eps_values = st.multiselect("Resolution values epsilon", [0.25, 0.1, 0.03, 0.01, 0.003, 0.001], default=[0.25, 0.1, 0.03, 0.01, 0.003])
    audit = dimension_audit(ns=(n,), epsilons=eps_values)
    st.dataframe(audit, use_container_width=True)
    if not audit.empty:
        st.line_chart(audit.set_index("epsilon")[["dimension_ratio_lower", "dimension_ratio_upper"]])
    st.info("STATUS: IMPORTED/KNOWN metric-entropy mathematics + PDT operational corollary. The ratio tends to n as epsilon→0, but this does not select n=3 or constitute new quantum mechanics.")

elif page == "Total distinction tensor":
    st.subheader("Exact total distinction tensor identity")
    g1 = st.number_input("G11", value=1.0)
    g2 = st.number_input("G22", value=1.4)
    gd1 = st.number_input("Gdot11", value=0.2)
    gd2 = st.number_input("Gdot22", value=-0.1)
    l11 = st.number_input("L11", value=-0.3)
    l22 = st.number_input("L22", value=-0.1)
    G = np.diag([g1, g2])
    Gd = np.diag([gd1, gd2])
    L = np.diag([l11, l22])
    A = total_distinction_tensor(G, Gd, L)
    X = np.array([1.0, 0.7])
    residual = total_tensor_identity_residual(X, G, Gd, L)
    st.write("A_tot =")
    st.dataframe(pd.DataFrame(A), use_container_width=True)
    st.metric("Identity residual", f"{residual:.3e}")
    st.write("Numerical zero (up to floating-point precision) confirms the implemented identity for this parameter choice.")

elif page == "Environmental records":
    st.subheader("Pure-record rate and mixed-record envelope")
    D = st.slider("Pure-record distinguishability D", 0.0, 0.999, 0.5, 0.001)
    nu = st.number_input("Interaction rate nu", min_value=0.0, value=1.0)
    st.metric("Exact deterministic pure-record rate", f"{deterministic_rate_from_D(nu, D):.6f}")

    theta = st.slider("Mixed qubit environment rotation", 0.0, 3.14159, 0.7, 0.01)
    eta = np.diag([0.7, 0.3]).astype(complex)
    U0 = np.eye(2, dtype=complex)
    U1 = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], complex)
    env = mixed_record_envelope(eta, U0, U1)
    st.json({k: float(v) for k, v in env.items()})
    st.write("Required envelope: |chi| <= fidelity <= sqrt(1-D^2).")

elif page == "Same-input test design":
    st.subheader("Breakthrough gate: same inputs, different prediction")
    st.markdown(
        """
        A candidate PDT modification counts as new physics only if it specifies an observable and predicts
        a value different from standard quantum mechanics **under exactly the same microscopic inputs**.

        **Protocol**
        - Freeze the microscopic state, Hamiltonian/control unitaries, resource window, and observable.
        - Compute the standard-QM prediction before looking at the target data.
        - Compute the PDT prediction from its independent law, not by reusing the QM output.
        - Predefine an effect-size threshold and uncertainty model.
        - Run blind or preregistered comparison.
        - Reject the PDT candidate if the prediction is algebraically identical or empirically unsupported.
        """
    )
    st.info(f"Reference conditional CHSH ceiling in the current bilinear Euclidean sector: {tsirelson_bound():.6f}")

else:
    st.subheader("Proof-status ledger")
    ledger = pd.DataFrame(
        [
            ["Capacity does not determine geometry", "PROVED / no-go"],
            ["CEU+CER do not force Euclidean geometry", "PROVED / counterfamily"],
            ["CEU+CER+RDE => Euclidean ball", "CONDITIONAL"],
            ["CEU+CER+RDE uniquely select n=3", "FALSIFIED / all B^n pass"],
            ["Resolution-scaled capacity identifies existing metric dimension", "IMPORTED/KNOWN + PDT corollary"],
            ["PDT-native n=3 with an additional composite principle", "OPEN"],
            ["Born weighting", "CONDITIONAL"],
            ["Tsirelson bound in bilinear Euclidean sector", "CONDITIONAL"],
            ["Total distinction tensor identity", "EXACT IDENTITY"],
            ["Controlled-record same-input deviation from QM", "NOT ESTABLISHED"],
            ["Gravity derivation", "OPEN FRONTIER"],
        ],
        columns=["Claim", "Status"],
    )
    st.dataframe(ledger, use_container_width=True)
