import pandas as pd
import streamlit as st

from pdt_transitive_norm_euclideanization import audit

st.title("Cycle 017 — Transitive Norm Euclideanization")
st.caption("PROVED / CONDITIONAL PDT interpretation / IMPORTED-KNOWN mathematics")

st.markdown(
    "If a compact linear isometry group acts transitively on a finite-dimensional norm unit sphere, "
    "Haar averaging yields an invariant inner product whose radius is constant on that sphere. "
    "Therefore the norm is Euclidean up to scale. This does not select n=3."
)

max_n = st.slider("Maximum audited dimension", 2, 100, 12)
p_values = st.multiselect("l_p families", [1.0, 1.5, 2.0, 3.0, 4.0, 10.0], default=[1.0, 1.5, 2.0, 3.0, 4.0, 10.0])
rows = audit(max_n, tuple(p_values)) if p_values else []
if rows:
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True)
    st.markdown("**Kill-test:** among the displayed l_p families, only p=2 has zero radius gap in every n>=2.")
else:
    st.info("Select at least one p value.")

st.warning("This theorem Euclideanizes the local norm but does not derive Two-Point Isotropy or n=3.")
