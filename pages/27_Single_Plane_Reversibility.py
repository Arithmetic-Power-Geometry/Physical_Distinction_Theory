import pandas as pd
import streamlit as st
import numpy as np
from pdt_single_plane_reversibility import rank4_counterexample, stress_dimensions

st.title("Cycle 027 — Single-Plane Reversibility")
st.caption("Conditional dimension filter; underlying linear/Lie algebra mathematics is imported/known.")
st.latex(r"\mathrm{SPR}:\; \operatorname{rank}(A)\le 2\ \forall A\in\mathfrak{so}(n)")
st.latex(r"\max_{A\in\mathfrak{so}(n)}\operatorname{rank}(A)=2\lfloor n/2\rfloor")
st.latex(r"\mathrm{SPR}+\mathrm{NCR}\iff n=3")
trials = st.slider("Random skew-generator trials per dimension", 10, 1000, 200, 10)
rows = stress_dimensions(range(1, 13), trials=trials, seed=2701)
st.dataframe(pd.DataFrame(rows), use_container_width=True)
n = st.number_input("Explicit rank-4 witness dimension", min_value=4, max_value=128, value=4)
st.write("rank(J12 + J34) =", int(np.linalg.matrix_rank(rank4_counterexample(int(n)))))
st.warning("SPR is an additional candidate PDT axiom. This page does not claim a PDT-native derivation or historical novelty.")
