import pandas as pd
import streamlit as st

from pdt_ndc_tensor_no_go import (
    nontrivial_tensor_closure_witnesses,
    self_tensor_row,
    theorem_holds,
)

st.title("Cycle 031 — NDC Tensor-Closure No-Go")
st.caption("Exact composition audit; classical cross-product classification is imported/known mathematics.")

st.markdown(r"""
Cycle 030's nontrivial Normed Distinction Composition (NDC) is available only in dimensions

$$n\in\{3,7\}.$$

If composites use the ordinary tensor rule

$$\dim(V\otimes W)=\dim(V)\dim(W),$$

then requiring the *same* nontrivial NDC structure on every composite fails immediately:

$$3\otimes3\to 9,\qquad 3\otimes7\to21,\qquad 7\otimes7\to49,$$

and none of $9,21,49$ admits such a binary normed vector cross product.
""")

st.subheader("Exact nontrivial witnesses")
st.dataframe(pd.DataFrame(nontrivial_tensor_closure_witnesses()), use_container_width=True)

st.subheader("Self-tensor audit, n=1..12")
st.dataframe(pd.DataFrame([self_tensor_row(n) for n in range(1, 13)]), use_container_width=True)

st.metric("No-go theorem evaluates to", str(theorem_holds()))

st.error("Universal NDC under ordinary tensor-product closure: FALSIFIED.")
st.warning("Cycle 030 remains only a conditional irreducible/single-system n=3 filter unless PDT derives a different, independently justified composition rule.")
