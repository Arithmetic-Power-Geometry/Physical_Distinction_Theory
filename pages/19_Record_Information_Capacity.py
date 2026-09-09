import math
import numpy as np
import streamlit as st

from pdt_record_information_capacity import (
    accessible_information_ceiling_bits,
    random_pure_ensemble,
    residual_label_uncertainty_floor_bits,
    uniform_pure_holevo,
)

st.title("Cycle 019 — Record Information Capacity")
st.caption("PROVED conditional PDT corollary · IMPORTED/KNOWN Holevo mathematics · not a breakthrough")

k = st.slider("Number of equiprobable branch labels k", 1, 128, 8)
d = st.slider("Quantum record dimension d", 1, 64, 3)

cap = accessible_information_ceiling_bits(k, d)
floor = residual_label_uncertainty_floor_bits(k, d)

c1, c2, c3 = st.columns(3)
c1.metric("H(X)", f"{math.log2(k):.4f} bits")
c2.metric("Accessible-info ceiling", f"{cap:.4f} bits")
c3.metric("Residual uncertainty floor", f"{floor:.4f} bits")

if k > d:
    st.warning("Perfect branch revelation is impossible for every measurement under the unchanged d-dimensional quantum record model.")
else:
    st.info("The dimension ceiling alone does not forbid perfect revelation; orthogonality and the actual ensemble still matter.")

st.latex(r"I(X:Y)\leq \chi \leq \min\{H(X),\log_2 d\}")
st.latex(r"H(X|Y)\geq \max\{0,\log_2(k/d)\}\quad\text{for uniform labels}")

st.subheader("Fixed-seed random ensemble audit")
seed = st.number_input("Seed", min_value=0, value=1909, step=1)
trials = st.slider("Trials", 1, 500, 100)
rng = np.random.default_rng(int(seed))
chis = []
for _ in range(trials):
    vecs = random_pure_ensemble(k, d, rng)
    chis.append(uniform_pure_holevo(vecs))

st.write({
    "max_random_Holevo_chi_bits": float(max(chis)),
    "log2_d_bits": float(math.log2(d)),
    "max_minus_log2d": float(max(chis) - math.log2(d)),
})

st.markdown("""
**Interpretation.** Any PDT variable advertised as *operationally recoverable branch information* from the same finite-dimensional quantum record must respect this ceiling unless PDT explicitly changes the physical state space, measurement/probability law, or interaction. Merely renaming hidden distinctions cannot evade it.

The core bound is standard quantum-information theory (Holevo), so this page is a **kill test**, not a novelty claim.
""")
