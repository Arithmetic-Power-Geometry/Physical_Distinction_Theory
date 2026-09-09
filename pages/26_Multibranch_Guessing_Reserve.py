import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Cycle 026 — Multi-branch Guessing Reserve")
st.latex(r"G_{SE}=P_{\rm guess}(X|SE),\quad G_S=P_{\rm guess}(X|S),\quad R_G=G_{SE}-G_S")
st.latex(r"\Delta G_S=R_G(s)-R_G(t)-L_G,\qquad L_G=G_{SE}(s)-G_{SE}(t)\ge 0")
st.latex(r"\Delta G_S\le R_G(s)")
st.markdown("For common reversible evolution, **L_G=0**, so local guessing revival is exactly paid by depletion of inaccessible guessing reserve.")
st.info("Classification: PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN. Not a breakthrough candidate.")
p=Path("results/cycle026_multibranch_guessing_reserve_audit.csv")
if p.exists():
    st.dataframe(pd.read_csv(p), use_container_width=True)
