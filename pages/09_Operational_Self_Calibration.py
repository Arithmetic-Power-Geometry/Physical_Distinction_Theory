import pandas as pd
import streamlit as st

from pdt_self_calibration import audit_dimensions

st.title("Operational Self-Calibration Dimension Filter")
st.caption("Conditional PDT axiom candidate — not a breakthrough claim")

max_n = st.slider("Maximum dimension", min_value=3, max_value=50, value=12)
rows = audit_dimensions(1, max_n)
df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

selected = df.loc[df["selected"], "n"].tolist()
st.metric("OSC + noncommuting dimensions", ", ".join(map(str, selected)) or "none")

st.latex(r"\dim SO(n)=\frac{n(n-1)}{2}")
st.latex(r"\mathrm{OSC}:\quad \dim SO(n)\le n")
st.latex(r"\mathrm{OSC}+\mathrm{NCR}\Longrightarrow n=3")

st.warning(
    "OSC is an operational self-calibration hypothesis, not an established physical law. "
    "The dimension conclusion is conditional on Euclidean B^n geometry, full SO(n) isotropy, "
    "regular control metrics, and genuinely noncommuting connected reversibility."
)
