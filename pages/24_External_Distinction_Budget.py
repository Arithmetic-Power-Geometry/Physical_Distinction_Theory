import streamlit as st

st.title("Cycle 024 — External Distinction Budget")
st.caption("PROVED + CONDITIONAL PDT COROLLARY + IMPORTED/KNOWN")

st.latex(r"D_S(t)-D_S(s)\le D_E(s)+C_1(s)+C_2(s)")
st.write(
    "A revival of locally accessible distinction is not free under standard joint "
    "unitary dynamics. It must be paid for by distinguishability already present "
    "in the environment and/or by system–environment correlations."
)
st.latex(r"C_i=D(\rho_{SE}^{(i)},\rho_S^{(i)}\otimes\rho_E^{(i)})")
st.info(
    "Kill test: if the two preparations share the same environment marginal and "
    "both are initially product with that environment, then the external budget is "
    "zero and local trace distance cannot increase."
)
st.warning(
    "This is established quantum information-flow mathematics, not a PDT-native breakthrough."
)
