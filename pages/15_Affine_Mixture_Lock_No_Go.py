import numpy as np
import pandas as pd
import streamlit as st

from pdt_affine_mixture_lock import audit_dimensions, mixture_deviation

st.title("Affine-Mixture Lock No-Go")
st.caption("Same-input PDT kill test: classical preparation mixing cannot create a mixed-state-only deviation if pure states already agree with QM.")

st.latex(r"P_{PDT}(E|\sum_i p_i\rho_i,R)=\sum_i p_i P_{PDT}(E|\rho_i,R)")
st.latex(r"P_{PDT}(E|\psi,R)=P_{QM}(E|\psi)\ \forall\psi\ \Rightarrow\ P_{PDT}(E|\rho,R)=P_{QM}(E|\rho)\ \forall\rho")

st.markdown("**Classification:** PROVED / IMPORTED-KNOWN convex mathematics / FALSIFIED candidate route. No novelty claim for convex linearity.")

eps = st.slider("Uniform pure-state deviation bound ε", 0.0, 0.10, 0.01, 0.005)
d = st.slider("Mixture size", 1, 20, 5)
rng = np.random.default_rng(20260908)
w = rng.random(d); w /= w.sum()
delta = rng.uniform(-eps, eps, size=d) if eps > 0 else np.zeros(d)
mixed = mixture_deviation(w, delta)
st.metric("Resulting affine mixed-state deviation", f"{mixed:.6f}")
st.write(f"Guaranteed bound: |δ_mixed| ≤ ε = {eps:.6f}")

if st.button("Run d=1..12 numerical audit"):
    st.dataframe(pd.DataFrame(audit_dimensions(max_d=12, trials=100, eps=max(eps, 1e-12))), use_container_width=True)

st.info("A PDT deviation that survives this no-go must change pure-state predictions, preparation-mixture affinity, microscopic state/effect assignment, dynamics, or the measurement law itself.")
