import pandas as pd
import streamlit as st

from pdt_resource_coarse_graining import audit

st.set_page_config(page_title="PDT Resource Coarse-Graining No-Go", layout="wide")
st.title("Resource Coarse-Graining Same-Input No-Go")
st.markdown(
    r"""
If the declared resource window only post-processes a fixed microscopic
outcome distribution through the same stochastic kernel $K_R$, then

$$p_{\rm PDT,R}=K_R p_{\rm micro}=p_{\rm QM,R}.$$

Therefore resource-relative bookkeeping alone cannot generate a genuine
same-input PDT-vs-QM prediction difference. A nonzero difference requires a
changed physical/probability law, not merely inaccessible distinctions.
"""
)

alpha = st.slider("Nonlinear deformation exponent (diagnostic only)", 0.2, 3.0, 1.3, 0.1)
rows = audit(max_dimension=12, alpha=alpha)
df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)

st.metric(
    "Largest identical-coarse-graining error",
    f"{df['same_coarse_graining_max_abs_error'].max():.3e}",
)
st.metric(
    "Smallest nonlinear response-law TV gap",
    f"{df['nonlinear_deformation_tv_gap'].min():.6f}",
)

st.caption(
    "Classification: PROVED / IMPORTED-KNOWN / decisive falsification of the "
    "resource-quotient-only same-input breakthrough route."
)
