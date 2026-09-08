import pandas as pd
import streamlit as st

from pdt_generator_duality import audit_range

st.set_page_config(page_title="PDT Generator–Distinction Duality", layout="wide")
st.title("Generator–Distinction Self-Duality")
st.caption("Conditional PDT dimension filter; representation mathematics is established prior art.")

n_max = st.slider("Maximum dimension", min_value=3, max_value=50, value=12)
rows = audit_range(1, n_max)
df = pd.DataFrame([r.__dict__ for r in rows])

st.dataframe(df, use_container_width=True)

matches = df.loc[df["dimension_match"], "n"].tolist()
st.metric("Positive dimensions satisfying dim(V)=dim(so(V))", str(matches))

st.latex(r"\dim V=n,\qquad \dim\mathfrak{so}(n)=\frac{n(n-1)}2")
st.latex(r"n=\frac{n(n-1)}2\ \Longrightarrow\ n=3\quad(n>0)")

st.info(
    "Interpretation: if PDT independently justifies an equivariant one-to-one identification "
    "between elementary distinction directions and elementary reversible generators at the "
    "same resource scale, then a positive-dimensional Euclidean elementary space must have n=3."
)
st.warning(
    "This is not yet a breakthrough: the vector/adjoint representation coincidence in 3D is "
    "known mathematics. The unresolved task is a non-circular physical derivation of the GDSD axiom."
)
