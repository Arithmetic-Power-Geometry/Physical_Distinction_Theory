import streamlit as st

from pdt_scalar_isotropy_no_go import audit, verify_witness

st.title("Scalar Isotropy ≠ Two-Point Isotropy")
st.caption("PDT dimension-selection kill test")

st.markdown(
    r"""
The natural action of $SU(m)$ on $\mathbb C^m\simeq\mathbb R^{2m}$ preserves
all scalar Euclidean distances and is sphere-transitive, but it need not be
two-point isotropic with respect to the real Euclidean angle.

Fix $x=e_1$, $y=e_2$, and
$z=i a e_1+\sqrt{1-a^2}e_2$.  Then $y,z$ have the same real angle and distance
from $x$, but the stabilizer of $x$ preserves the full complex inner product,
so it cannot map $y$ to $z$.
"""
)

a = st.slider("Witness parameter a", 0.05, 0.95, 0.60, 0.05)
m = st.slider("Complex dimension m", 2, 12, 2)
row = verify_witness(m, a)
st.json(row)

st.subheader("Audit: real dimensions 4–12")
st.dataframe(audit(range(2, 7), a), use_container_width=True)

st.warning(
    "Classification: PROVED / FALSIFIED ROUTE / IMPORTED-KNOWN mathematics. "
    "This does not establish a PDT breakthrough; it blocks a circular/insufficient derivation of TPI."
)
