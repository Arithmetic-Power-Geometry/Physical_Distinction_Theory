import math
import numpy as np
import streamlit as st

from pdt_prior_weighted_record_bound import (
    postmeasurement_min_entropy_floor,
    uniform_copy_bound,
)

st.set_page_config(page_title="PDT prior-weighted record capacity", layout="centered")
st.title("Prior-weighted composite record capacity")
st.caption("Cycle 022 — arbitrary priors + tensor-product record dimension")

st.markdown(r"""
For branch priors \(p_i\) and a record of total Hilbert-space dimension \(D\),

\[
P_{\rm success}\le \min(1,Dp_{\max}).
\]

For a tensor product with dimensions \(d_1,\ldots,d_m\),
\(D=\prod_j d_j\). Equivalently,

\[
H_{\min}(X|\mathrm{measurement})\ge
\max(0,H_{\min}(X)-\log_2 D).
\]

This is standard quantum discrimination / one-shot information mathematics,
used here as a PDT finite-resource composition audit.
""")

d = int(st.number_input("Single-record dimension d", min_value=1, max_value=1000, value=2, step=1))
copies = int(st.number_input("Number of copies m", min_value=1, max_value=20, value=2, step=1))
k = int(st.number_input("Number of labels k", min_value=1, max_value=100000, value=10, step=1))
pmax = float(st.number_input("Largest prior p_max", min_value=1.0/k, max_value=1.0, value=max(1.0/k, 0.2), step=0.01))

D = d ** copies
generic = min(1.0, D * pmax)
uniform = uniform_copy_bound(d, copies, k)

c1, c2, c3 = st.columns(3)
c1.metric("Total dimension D", str(D))
c2.metric("Prior-weighted success ceiling", f"{generic:.6f}")
c3.metric("Uniform-label ceiling", f"{uniform:.6f}")

priors_demo = np.array([pmax] + [(1-pmax)/(k-1)]*(k-1)) if k > 1 else np.array([1.0])
if np.max(priors_demo) <= pmax + 1e-12:
    floor = postmeasurement_min_entropy_floor(priors_demo, (D,))
    st.metric("Min-entropy floor (demo source)", f"{floor:.6f} bits")

if uniform < 1:
    st.warning("For uniform labels, perfect exact identification is forbidden by dimension alone.")
else:
    st.info("Dimension alone does not forbid perfect identification; state geometry may still do so.")

st.markdown("### PDT kill test")
st.write(
    "A same-input PDT exact-label success above D·p_max requires an explicit changed physical resource or law; "
    "ordinary prior imbalance and standard tensor-product composition cannot produce it."
)
