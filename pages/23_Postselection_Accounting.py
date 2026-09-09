import numpy as np
import streamlit as st

from pdt_postselection_accounting import (
    postselected_conditional_accuracy_bound,
    postselected_joint_correct_bound,
    uniform_postselection_bound,
)

st.set_page_config(page_title="PDT postselection accounting", layout="centered")
st.title("Postselection-accounted distinction yield")
st.caption("Cycle 023 — conditional accuracy must be charged by retention probability")

st.markdown(r"""
For label priors \(p_i\), a \(D\)-dimensional quantum record, and conclusive effects whose sum is at most the identity,

\[
P(\mathrm{retain\ and\ correct})\le \min(1,Dp_{\max}).
\]

If \(s=P(\mathrm{retain})\), then

\[
P(\mathrm{correct}\mid\mathrm{retain})\le
\min\!\left(1,\frac{Dp_{\max}}{s}\right).
\]

A high conditional score after rare-event filtering is therefore not, by itself, a same-input PDT-vs-QM anomaly.
""")

D = int(st.number_input("Record dimension D", min_value=1, max_value=1000, value=2, step=1))
k = int(st.number_input("Number of labels k", min_value=2, max_value=100000, value=20, step=1))
s = float(st.slider("Retention probability s", min_value=0.001, max_value=1.0, value=0.10, step=0.001))
uniform = bool(st.checkbox("Use uniform priors", value=True))

if uniform:
    priors = np.full(k, 1.0 / k)
else:
    pmax = float(st.number_input("Largest prior p_max", min_value=1.0/k, max_value=1.0, value=max(1.0/k, 0.2), step=0.01))
    priors = np.array([pmax] + [(1.0-pmax)/(k-1)]*(k-1))

joint = postselected_joint_correct_bound(priors, D)
cond = postselected_conditional_accuracy_bound(priors, D, s)

c1, c2, c3 = st.columns(3)
c1.metric("Joint correct-yield ceiling", f"{joint:.6f}")
c2.metric("Conditional-accuracy ceiling", f"{cond:.6f}")
c3.metric("Retention", f"{s:.6f}")

if uniform:
    st.write("Uniform closed form:", f"C <= {uniform_postselection_bound(D, k, s):.6f}")

st.markdown("### PDT kill test")
st.write(
    "Report retention and conditional correctness together. Under identical microscopic states and allowed effects, "
    "a decisive anomaly requires the retention-weighted joint yield s*C to exceed D*p_max; conditional accuracy alone can be inflated by postselection."
)
