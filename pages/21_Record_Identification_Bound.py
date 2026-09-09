import streamlit as st

from pdt_record_identification_bound import error_lower_bound, success_upper_bound

st.set_page_config(page_title="PDT exact record identification", layout="centered")
st.title("Exact record-identification capacity")
st.caption("Cycle 021 — one-shot dimension-limited branch identification")

st.markdown(r"""
For **k equiprobable labels** encoded into arbitrary quantum record states on a
**d-dimensional** Hilbert space, every POVM obeys

\[
P_{\rm success}\le \min(1,d/k),\qquad
P_{\rm error}\ge \max(0,1-d/k).
\]

This is standard quantum-state-discrimination mathematics and is used here as
a PDT resource kill test, not as a novelty claim.
""")

d = st.number_input("Record dimension d", min_value=1, max_value=10000, value=3, step=1)
k = st.number_input("Number of equiprobable labels k", min_value=1, max_value=100000, value=6, step=1)

ps = success_upper_bound(int(d), int(k))
pe = error_lower_bound(int(d), int(k))

c1, c2 = st.columns(2)
c1.metric("Maximum exact success", f"{ps:.6f}")
c2.metric("Minimum exact error", f"{pe:.6f}")

if k > d:
    st.warning("Label overload: perfect one-shot identification is impossible in the unchanged record space.")
else:
    st.success("The dimension-only bound does not forbid perfect identification; geometry of the states may still do so.")

st.markdown("### PDT same-input kill test")
st.write(
    "A PDT proposal predicting exact-label success above d/k for the same record states and measurement class must identify an explicit changed physical resource or law."
)
