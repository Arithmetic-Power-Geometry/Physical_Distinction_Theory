"""Streamlit audit for the conditional-output non-identifiability no-go."""
import numpy as np
import pandas as pd
import streamlit as st

from conditional_output_no_go import full_output_pair_witness, phase_family

st.set_page_config(page_title="PDT Conditional-Output No-Go", layout="wide")
st.title("Conditional Environment Outputs Do Not Identify Dephasing Coherence")
st.caption("Status: PROVED / NO-GO. This is a constraint on PDT record-based prediction, not a breakthrough claim.")

st.markdown(
    r"""
For controlled dephasing, let

\[
\rho_E^{(0)}=U_0\eta U_0^\dagger,\qquad
\rho_E^{(1)}=U_1\eta U_1^\dagger,
\]

while the system coherence multiplier is

\[
\chi=\operatorname{Tr}(U_0\eta U_1^\dagger).
\]

A tempting hypothesis is that complete knowledge of the pair
\((\rho_E^{(0)},\rho_E^{(1)})\) should determine \(\chi\). The construction below
shows that this is false for mixed environments.
"""
)

d = st.slider("Environment dimension", 2, 12, 2)
w = full_output_pair_witness(d)
cols = st.columns(4)
cols[0].metric("dimension", d)
cols[1].metric("conditional-output residual", f"{w['conditional_pair_residual']:.3e}")
cols[2].metric("|chi| model A", f"{w['abs_chi_model_A']:.6f}")
cols[3].metric("|chi| model B", f"{w['abs_chi_model_B']:.3e}")

st.success(
    "The conditional output pair is the same (up to floating-point precision), yet the coherence factors differ maximally."
)

alphas = np.linspace(0.0, 2.0 * np.pi, 181)
df = pd.DataFrame(phase_family(d, alphas))
st.subheader("Continuous hidden-relative-unitary family")
st.line_chart(df.set_index("alpha")["abs_chi"])
st.dataframe(df.iloc[::30], use_container_width=True)

st.markdown(
    r"""
### Exact witness
Take \(\eta=I_d/d\) and \(U_0=I_d\). Then for every unitary \(V\),

\[
\rho_E^{(0)}=\rho_E^{(1)}=I_d/d,
\]

but

\[
\chi=\frac{1}{d}\operatorname{Tr}(V^\dagger).
\]

Choosing \(V=I_d\) gives \(|\chi|=1\), while choosing diagonal \(V\) with the
\(d\)-th roots of unity gives \(\operatorname{Tr}V=0\), hence \(|\chi|=0\).
Therefore no function of the two conditional density operators alone can recover
\(\chi\) for all mixed-environment controlled-dephasing models.

### Consequence for the breakthrough search
A PDT law that predicts dephasing only from conditional environment states, their
trace distance, fidelity, or any statistic determined solely by that pair is not
universally identifiable. A successful same-input PDT prediction must contain
additional operational information sensitive to the relative dilation/unitary
structure, or it must explicitly restrict the physical model class enough to restore
identifiability.
"""
)

st.warning(
    "Novelty boundary: mixed-state dephasing and environment-information limitations have substantial prior literature. This explicit no-go is being treated as a rigorous PDT design constraint until a dedicated prior-art review establishes whether its exact formulation is new."
)
