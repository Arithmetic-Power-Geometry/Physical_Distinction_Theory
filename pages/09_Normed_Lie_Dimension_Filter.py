import streamlit as st

from pdt_dimension_filter import dimension_filter_table, randomized_audit

st.set_page_config(page_title="PDT Dimension Filter", layout="wide")
st.title("Conditional Normed–Lie Dimension Filter")
st.warning(
    "This page does not claim a PDT-native derivation of n=3. The 3/7 cross-product "
    "classification and the 7D Jacobi failure are established mathematics. PDT still "
    "needs an independent physical reason for the candidate interaction axioms."
)

st.markdown(r"""
After Euclidean rigidity, consider an additional bilinear antisymmetric interaction product
\(x\times y\in\mathbb R^n\) satisfying

\[
x\times y\perp x,y,\qquad
\|x\times y\|^2=\|x\|^2\|y\|^2-\langle x,y\rangle^2,
\]

and the Jacobi identity. Known normed-cross-product classification leaves nontrivial
products only in dimensions 3 and 7; Jacobi rejects the standard octonionic 7D product.
Thus this *conditional algebraic filter* leaves dimension 3.
""")

st.subheader("Dimensions 1–12")
st.dataframe(dimension_filter_table(12), use_container_width=True, hide_index=True)

st.subheader("Explicit numerical stress test")
trials = st.slider("Random trials per explicit model", 100, 10000, 2000, step=100)
for n in (3, 7):
    audit = randomized_audit(n, trials=trials)
    st.markdown(f"**n = {n}**")
    st.json(audit)

st.caption(
    "Research kill-test: a genuine PDT derivation must justify the normed bilinear "
    "antisymmetric Lie interaction physically, without circularly importing SO(3), "
    "qubits, Pauli matrices, or ordinary three-dimensional rotations."
)
