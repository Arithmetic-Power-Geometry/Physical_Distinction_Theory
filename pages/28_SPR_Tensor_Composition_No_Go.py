import streamlit as st

st.set_page_config(page_title="PDT Cycle 028 — SPR Tensor No-Go", layout="wide")
st.title("Cycle 028 — Tensor-composition no-go for universal SPR")
st.caption("Status: PROVED + FALSIFIED + IMPORTED/KNOWN; not a breakthrough candidate")

st.markdown(r"""
Cycle 027 proposed **Single-Plane Reversibility (SPR)**: an elementary infinitesimal reversible generator has rank at most 2.

Under standard tensor composition, a local generator lifts as

\[
A \mapsto A\otimes I_B.
\]

The matrix-rank identity gives

\[
\operatorname{rank}(A\otimes I_B)=\operatorname{rank}(A)\,d_B.
\]

Thus a rank-2 single-plane generator becomes rank \(2d_B\). Universal SPR therefore fails on every nontrivial composite with \(d_B\ge 2\).
""")

d = st.slider("Spectator dimension d_B", 1, 64, 2)
lifted_rank = 2 * d
st.metric("Composite lifted rank", lifted_rank)
st.metric("Universal SPR holds?", "YES" if lifted_rank <= 2 else "NO")
st.metric("Factor-local normalized rank", lifted_rank / d)

st.markdown(r"""
### Interpretation

The isolated-space filter SPR + noncommuting reversibility may still select \(n=3\) conditionally, but SPR cannot be imposed unchanged on ordinary tensor-product composites.

A composition-compatible repair candidate is **factor-local SPR**,

\[
\frac{\operatorname{rank}(A\otimes I_B)}{d_B}\le 2,
\]

which removes spectator multiplicity. This repair is currently **OPEN** as a PDT-native physical principle and does not yet constitute a derivation of three dimensions.
""")
