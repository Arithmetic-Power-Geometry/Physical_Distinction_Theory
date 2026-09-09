import streamlit as st
st.title("Cycle 025 — Exact Distinction-Reserve Balance")
st.caption("PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN")
st.latex(r"R_S=D(\rho_{SE}^{(1)},\rho_{SE}^{(2)})-D(\rho_S^{(1)},\rho_S^{(2)})\ge 0")
st.latex(r"\Delta D_S=R_S(s)-R_S(t)-L,\quad L=D_{SE}(s)-D_{SE}(t)\ge0")
st.write("For common unitary joint evolution, L=0 and local distinction gain is exactly paid by depletion of inaccessible distinction reserve.")
st.info("Kill test: local gain cannot exceed the initial reserve under identical standard-quantum microscopic inputs and common CPTP dynamics.")
st.warning("The information-flow mathematics is established prior art; this page is PDT bookkeeping, not a breakthrough claim.")
