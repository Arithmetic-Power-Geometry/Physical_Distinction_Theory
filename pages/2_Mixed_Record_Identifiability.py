import numpy as np
import pandas as pd
import streamlit as st

from mixed_record_no_go import controlled_record_quantities, scalar_record_nonidentifiability_witness

st.set_page_config(page_title="PDT Mixed-Record Identifiability", layout="wide")
st.title("Mixed-Record Identifiability No-Go")
st.caption("Scientific status: PROVED / NO-GO. This is a PDT identifiability result, not a claim of new quantum mechanics.")

st.markdown(r"""
For mixed environmental records, the scalar trace distinguishability
\(D_E=\frac12\|\rho_E^{(0)}-\rho_E^{(1)}\|_1\) does not uniquely determine the
controlled-dephasing coherence factor \(|\chi|\).

The explicit family used here fixes \(\eta_E=I/2\), \(U_0=I\), and varies
\(U_1(\theta)=e^{-i\theta\sigma_z/2}\). The two conditional environment states
remain identical for all \(\theta\), so \(D_E=0\), while \(|\chi|=|\cos(\theta/2)|\).
""")

theta_deg = st.slider("Relative unitary angle θ (degrees)", 0, 180, 90, 1)
q = controlled_record_quantities(np.deg2rad(theta_deg))

c1, c2, c3 = st.columns(3)
c1.metric("D_E", f"{q['D_E']:.12f}")
c2.metric("|χ|", f"{q['abs_chi']:.12f}")
c3.metric("analytic |cos(θ/2)|", f"{q['analytic_abs_chi']:.12f}")

angles = np.linspace(0.0, 180.0, 181)
rows = []
for deg in angles:
    r = controlled_record_quantities(np.deg2rad(deg))
    rows.append({"theta_deg": deg, "D_E": r["D_E"], "abs_chi": r["abs_chi"]})
df = pd.DataFrame(rows)
st.line_chart(df.set_index("theta_deg")[["D_E", "abs_chi"]])

st.subheader("Explicit same-D witness")
w = scalar_record_nonidentifiability_witness()
st.json(w)

st.warning("Kill test: any proposed exact mixed-record PDT law of the form |χ| = f(D_E) alone fails on this family. A richer operational statistic or genuinely new dynamical principle is required.")
