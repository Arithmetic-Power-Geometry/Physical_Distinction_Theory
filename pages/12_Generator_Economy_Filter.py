import pandas as pd
import streamlit as st

from pdt_generator_economy import audit_range

st.set_page_config(page_title="PDT Generator Economy Filter", layout="wide")
st.title("Generator Economy + Noncommuting Reversibility")
st.caption("Conditional PDT dimension filter; standard Lie mathematics; not a breakthrough claim.")

n_max = st.slider("Maximum dimension", min_value=3, max_value=100, value=12, step=1)
rows = audit_range(1, n_max)
df = pd.DataFrame([row.__dict__ for row in rows])

selected = df.loc[df["selected"], "n"].tolist()
col1, col2, col3 = st.columns(3)
col1.metric("Dimensions scanned", len(df))
col2.metric("GE+NCR solutions", len(selected))
col3.metric("Selected n", ", ".join(map(str, selected)) if selected else "none")

st.dataframe(df, use_container_width=True, hide_index=True)

st.latex(r"\dim\mathfrak{so}(n)=\frac{n(n-1)}{2}")
st.markdown(
    "**Generator Economy (GE):** $\dim\mathfrak{so}(n)\le n$, hence positive $n\le3$.  "
    "**Noncommuting Reversibility (NCR):** $\mathfrak{so}(n)$ is non-abelian, hence $n\ge3$.  "
    "Together, under the stated full-isotropy assumptions, they select **$n=3$**."
)

st.warning(
    "GE and NCR are candidate operational axioms, not yet derived from the existing PDT axioms. "
    "The result is conditional and does not constitute a same-input deviation from quantum mechanics."
)
