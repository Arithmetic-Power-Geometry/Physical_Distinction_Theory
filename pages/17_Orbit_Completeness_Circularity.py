import streamlit as st

from pdt_orbit_completeness import dimension_audit, su_scalar_isotropy_witness

st.title("Orbit Completeness ⇔ TPI")
st.caption("PDT circularity / independence kill test")

st.markdown(
    r"""
Fix a pure distinction $x$ and let $H=G_x$ be its reversible stabilizer.  If
$s_x(y)$ is the declared scalar distinction from $x$, then saying that
$s_x$ is a **complete invariant** of $H$-orbits means that each scalar level
set is exactly one $H$-orbit.  That is precisely Two-Point Isotropy (TPI)
relative to the scalar.  So scalar operational completeness cannot be used as
an independent derivation of TPI.

The $SU(m)$ family gives an explicit failure of scalar completeness: equal
real Euclidean angle/distance can hide a distinct complex invariant preserved
by the stabilizer.
"""
)

a = st.slider("SU(m) witness parameter a", 0.05, 0.95, 0.50, 0.05)
m = st.slider("Complex dimension m", 2, 12, 2)
st.json(su_scalar_isotropy_witness(m, a))

st.subheader("Counterfamily audit: real dimensions 4–12")
st.dataframe(dimension_audit(12), use_container_width=True)

st.error(
    "Classification: PROVED EQUIVALENCE / FALSIFIED DERIVATION ROUTE / IMPORTED-KNOWN mathematics. "
    "Declaring the current scalar 'complete' assumes TPI in equivalent language; richer invariants evade the scalar-only dimension proof."
)
