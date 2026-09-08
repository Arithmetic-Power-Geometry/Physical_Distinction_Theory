import numpy as np
import streamlit as st

from pdt_revelation_coherence_budget import budget_terms

st.title("Controlled-record revelation/coherence budget")
st.caption("PROVED operational corollary; underlying duality/fidelity mathematics is imported/known.")

st.latex(r"D^2+|\chi|^2\le 1")
st.markdown(
    "For a controlled relative unitary $V$ acting on an environment state $\\eta$, "
    "$D=\\tfrac12\\|\\eta-V\\eta V^\\dagger\\|_1$ and "
    "$\\chi=\\mathrm{Tr}(\\eta V)$. The unit disk is a kill-test boundary, not a PDT-vs-QM deviation."
)

theta = st.slider("Qubit rotation angle", 0.0, float(np.pi), 0.7, 0.01)
purity_bias = st.slider("Qubit population p", 0.0, 1.0, 0.8, 0.01)
eta = np.diag([purity_bias, 1.0 - purity_bias]).astype(complex)
v = np.array(
    [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]],
    dtype=complex,
)
terms = budget_terms(eta, v)

c1, c2, c3 = st.columns(3)
c1.metric("D", f"{terms['trace_distance']:.6f}")
c2.metric("|chi|", f"{terms['abs_chi']:.6f}")
c3.metric("D^2+|chi|^2", f"{terms['trace_distance']**2 + terms['abs_chi']**2:.6f}")

st.write("Root fidelity:", f"{terms['root_fidelity']:.6f}")
st.write("Budget margin:", f"{terms['revelation_coherence_margin']:.6e}")
st.info("Pure records saturate the boundary. Mixed records generally lie inside it.")
