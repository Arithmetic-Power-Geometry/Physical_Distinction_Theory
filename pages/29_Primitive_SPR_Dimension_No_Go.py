import streamlit as st

from primitive_spr_no_go import audit_dimensions

st.set_page_config(page_title="PDT Cycle 029 — Primitive SPR No-Go", layout="wide")
st.title("Cycle 029 — Primitive SPR does not select n=3")
st.caption("Status: PROVED + FALSIFIED + IMPORTED/KNOWN; not a breakthrough candidate")

st.markdown(r"""
The natural control-theoretic reading of **Single-Plane Reversibility (SPR)** is that the *primitive generating controls* each act in one plane. For

\[
J_{ij}=E_{ij}-E_{ji},
\]

every primitive coordinate-plane generator has rank 2 in every dimension \(n\ge2\). Moreover, for every \(n\ge3\),

\[
[J_{12},J_{23}]\ne0.
\]

Therefore

\[
\boxed{\text{primitive SPR}+\text{NCR holds for every }n\ge3,}
\]

so this physically natural interpretation cannot uniquely select three dimensions.
""")

rows = audit_dimensions(12)
st.dataframe(rows, use_container_width=True)

selected = [row["n"] for row in rows if row["primitive_spr_plus_ncr"]]
st.metric("Dimensions selected in n=1..12", ", ".join(map(str, selected)))
st.metric("Unique n=3?", "NO")

st.markdown(r"""
### Why this matters

Cycle 027's uniqueness depended on requiring **every** element of \(\mathfrak{so}(n)\) to have rank at most 2. In \(n\ge4\), sums such as \(J_{12}+J_{34}\) have rank 4. But those sums need not be primitive controls.

The factor-local repair from Cycle 028 also cannot restore uniqueness by itself because

\[
\frac{\operatorname{rank}(A\otimes I_m)}{m}=\operatorname{rank}(A),
\]

which simply returns the same local rank-2 condition in every dimension.

A genuine PDT derivation of \(n=3\) therefore needs an additional physical/compositional principle that is not automatically satisfied by plane-rotation generating bases of all \(SO(n)\).
""")
