import streamlit as st

from pdt_tensor_dimension_closure import (
    finite_tensor_selector_no_go,
    tensor_power_ladder,
    universal_single_dimension_survives,
)

st.set_page_config(page_title="PDT Tensor Dimension Closure", layout="wide")
st.title("Cycle 032 — Tensor-Dimension Closure No-Go")
st.caption("Exact structural audit; no novelty claim for tensor-product dimension mathematics.")

d = st.number_input("Candidate universal dimension", min_value=1, max_value=256, value=3, step=1)
copies = st.slider("Repeated copies", min_value=1, max_value=12, value=6)

ladder = tensor_power_ladder(int(d), int(copies))
st.write("Repeated tensor dimensions:", ladder)

if universal_single_dimension_survives(int(d)):
    st.success("This singleton dimension is closed under self-tensoring.")
else:
    st.error(f"{{{int(d)}}} is not tensor closed because {int(d)} x {int(d)} = {int(d)**2} != {int(d)}.")

st.subheader("Finite selector audit")
selector_text = st.text_input("Comma-separated admissible dimensions", value="3,7")
try:
    selector = {int(x.strip()) for x in selector_text.split(",") if x.strip()}
    if finite_tensor_selector_no_go(selector):
        st.warning("Finite selector contains a nontrivial dimension and is not tensor closed.")
    else:
        st.info("No finite-selector no-go triggered by this exact check.")
except ValueError:
    st.error("Use positive integer dimensions only.")

st.markdown(
    r"""
### Exact theorem
If a system class is closed under ordinary tensor composition and contains a dimension $d>1$, then it contains

$$d,d^2,d^3,\ldots$$

and therefore has infinitely many admissible dimensions. Hence a universal rule that every system, including composites, has exactly dimension 3 is inconsistent with ordinary tensor composition.

### Scope
This does **not** rule out dimension 3 for irreducible/primitive sectors, nor effective dimensions after a non-faithful resource quotient, nor an independently derived nonstandard composition law.

**Classification:** PROVED + CONDITIONAL + IMPORTED/KNOWN. Not a BREAKTHROUGH CANDIDATE.
"""
)
