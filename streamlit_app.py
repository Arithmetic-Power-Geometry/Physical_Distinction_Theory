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

st.set_page_config(page_title="PDT Breakthrough Lab", layout="wide")
st.title("Physical Distinction Theory — Breakthrough Laboratory")
st.caption("Proofs, counterexamples, simulations, falsification tests, and same-input audits")

st.sidebar.header("Research controls")
page = st.sidebar.radio(
    "Module",
    [
        "Research dashboard",
        "Geometry no-go",
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

elif page == "Geometry no-go":
    st.subheader("CEU + CER does not force Euclidean geometry")
    ps = st.multiselect("p values", [1.1, 1.25, 1.5, 2.0, 3.0, 4.0, 6.0], default=[1.25, 1.5, 2.0, 3.0, 4.0])
    df = ceu_cer_counterfamily(ps)
    st.dataframe(df, use_container_width=True)
    st.write("Euclidean structure is detected by a zero parallelogram defect; among the tested lp balls this occurs only at p=2.")

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
            ["PDT-native n=3", "OPEN"],
            ["Born weighting", "CONDITIONAL"],
            ["Tsirelson bound in bilinear Euclidean sector", "CONDITIONAL"],
            ["Total distinction tensor identity", "EXACT IDENTITY"],
            ["Controlled-record same-input deviation from QM", "NOT ESTABLISHED"],
            ["Gravity derivation", "OPEN FRONTIER"],
        ],
        columns=["Claim", "Status"],
    )
    st.dataframe(ledger, use_container_width=True)
