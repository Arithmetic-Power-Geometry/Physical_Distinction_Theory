import streamlit as st

from pdt_record_capacity_welch import revelation_average_ceiling, welch_average_floor

st.title("Cycle 018 — Finite Record-Capacity Bound")
st.caption("Welch-bound audit for multibranch pure environment records")

d = st.number_input("Environment dimension d", min_value=1, value=3, step=1)
k = st.number_input("Number of branch records k", min_value=1, value=6, step=1)
floor = welch_average_floor(int(k), int(d))
ceiling = revelation_average_ceiling(int(k), int(d))

st.metric("Minimum average squared overlap", f"{floor:.6f}")
st.metric("Maximum average revelation proxy", f"{ceiling:.6f}")
st.latex(r"\frac{1}{k(k-1)}\sum_{i\ne j}|\langle e_i|e_j\rangle|^2\ge \max\{0,\frac{k-d}{d(k-1)}\}")

if k > d:
    st.warning("Perfect pairwise revelation of all pure records is impossible in this dimension.")
else:
    st.success("An orthonormal pure-record family is dimensionally possible.")

st.info("Status: PROVED under stated assumptions; IMPORTED/KNOWN Welch-bound mathematics; conditional PDT operational corollary; not a breakthrough claim.")
