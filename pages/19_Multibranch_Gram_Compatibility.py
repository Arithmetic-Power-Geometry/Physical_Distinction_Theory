import numpy as np
import streamlit as st

from pdt_multibranch_gram_compatibility import (
    equal_visibility_bound,
    phase_frustrated_counterexample,
    triple_minor,
)

st.title("Multi-branch Gram compatibility")
st.caption("Composite controlled-record kill test: pairwise-valid coherences need not be jointly realizable.")

r = st.slider("Equal pairwise coherence magnitude r", 0.0, 1.0, 0.9, 0.01)
phi = st.slider("Loop phase Φ", 0.0, float(np.pi), float(np.pi), 0.01)
minor = 1.0 - 3.0 * r**2 + 2.0 * r**3 * np.cos(phi)

st.metric("3×3 Gram determinant", f"{minor:.6f}")
st.write("Compatible" if minor >= -1e-12 else "Globally impossible despite pairwise-valid magnitudes")
st.write(f"Largest equal r at this loop phase: approximately {equal_visibility_bound(phi):.5f}")

st.subheader("Canonical phase-frustrated counterexample")
st.json(phase_frustrated_counterexample(0.9))

st.latex(r"1-a^2-b^2-c^2+2abc\cos\Phi\ge 0")
st.info("Status: PROVED / IMPORTED-KNOWN Gram mathematics / falsification tool. Not a PDT breakthrough claim.")
