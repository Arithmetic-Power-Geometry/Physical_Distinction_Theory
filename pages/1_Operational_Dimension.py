"""Operational dimension audit for the PDT breakthrough laboratory."""
import pandas as pd
import streamlit as st

from pdt_breakthrough import dimension_identifiability_audit, dimension_theorem_status

st.set_page_config(page_title="PDT Operational Dimension Audit", layout="wide")
st.title("Operational Dimension Audit")
st.caption("Known metric-entropy mathematics used as a conservative PDT identifiability audit")

max_n = st.slider("Maximum Euclidean dimension", 3, 12, 6)
eps = st.multiselect(
    "Resolution epsilon",
    [0.25, 0.1, 0.03, 0.01, 0.003, 0.001, 1e-4, 1e-6, 1e-8],
    default=[0.1, 0.03, 0.01, 0.003],
)

if not eps:
    st.warning("Select at least one epsilon value.")
    st.stop()

df = dimension_identifiability_audit(dimensions=range(2, max_n + 1), epsilons=eps)
st.dataframe(df, use_container_width=True)

plot_df = df[["epsilon", "target_dimension", "slope_upper"]].copy()
plot_df["log10_inverse_epsilon"] = -plot_df["epsilon"].map(lambda x: __import__("math").log10(x))
st.line_chart(plot_df, x="log10_inverse_epsilon", y="slope_upper", color="target_dimension")

status = dimension_theorem_status()
st.subheader("Scientific status")
st.json(status)
st.success(
    "Boundary result: under Euclidean codebook assumptions the fine-resolution capacity slope converges to n. "
    "This makes n operationally estimable; it does not select n=3 and is not claimed as new mathematics."
)
st.info(
    "Breakthrough consequence: a genuine PDT n=3 result must introduce a dimension-sensitive physical principle, "
    "most plausibly at the composite/interventional level, rather than another purely local symmetry axiom."
)
