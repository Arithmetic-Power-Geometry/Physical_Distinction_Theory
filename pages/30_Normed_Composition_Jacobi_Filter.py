import numpy as np
import pandas as pd
import streamlit as st

from pdt_normed_composition_filter import (
    classification_row,
    explicit_7d_jacobi_witness,
    randomized_audit,
)

st.title("Cycle 030 — Normed Composition + Jacobi Dimension Filter")
st.caption("Conditional PDT filter; classical cross-product mathematics is not claimed as new.")

st.markdown(r"""
Assume a nontrivial bilinear alternating binary distinction product that is orthogonal to both inputs and obeys

$$\|x\times y\|^2=\|x\|^2\|y\|^2-\langle x,y\rangle^2.$$

The known Euclidean vector-cross-product classification leaves only $n=3,7$. If sequential composition must also obey Jacobi,

$$x\times(y\times z)+y\times(z\times x)+z\times(x\times y)=0,$$

then the standard 7D octonionic product is excluded, leaving $n=3$.
""")

rows=[classification_row(n) for n in range(1,13)]
st.dataframe(pd.DataFrame(rows), use_container_width=True)

_,_,_,j=explicit_7d_jacobi_witness()
st.subheader("Exact seven-dimensional kill witness")
st.code(f"(e1,e2,e4) Jacobiator = {j.tolist()}")

trials=st.slider("Random audit trials per explicit dimension",100,2000,500,100)
if st.button("Run 3D/7D stress audit"):
    st.json({"n3":randomized_audit(3,trials), "n7":randomized_audit(7,trials)})

st.warning("Status: PROVED + CONDITIONAL + IMPORTED/KNOWN. Not a BREAKTHROUGH CANDIDATE. The unresolved task is to derive Jacobi sequential consistency from PDT rather than assume it.")
