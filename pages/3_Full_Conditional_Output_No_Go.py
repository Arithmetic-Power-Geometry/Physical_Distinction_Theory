import numpy as np
import pandas as pd
import streamlit as st

from conditional_output_no_go import full_output_pair_witness, phase_family

st.set_page_config(page_title="PDT Full Conditional-Output No-Go", layout="wide")
st.title("Full Conditional-Output Identifiability No-Go")
st.caption("Status: PROVED / NO-GO. This page does not claim a novel quantum-mechanical law.")

st.markdown(
    r"""
For controlled dephasing, the conditional environment states are
\(\rho_E^{(0)}=U_0\eta U_0^\dagger\) and
\(\rho_E^{(1)}=U_1\eta U_1^\dagger\), while the system coherence factor is
\(\chi=\mathrm{Tr}(U_0\eta U_1^\dagger)\).

Take \(\eta=I_d/d\). Then both conditional states are always \(I_d/d\),
independent of the relative unitary, whereas \(\chi=\mathrm{Tr}(V^\dagger)/d\).
Therefore even the **complete pair of conditional density operators** does not,
in general, identify the coherence factor.
"""
)

d = st.slider("Environment dimension d", 2, 12, 2)
w = full_output_pair_witness(d)

c1, c2, c3 = st.columns(3)
c1.metric("Conditional-pair residual", f"{w['conditional_pair_residual']:.3e}")
c2.metric("|chi| model A", f"{w['abs_chi_model_A']:.6f}")
c3.metric("|chi| model B", f"{w['abs_chi_model_B']:.6f}")

st.success(
    f"Exact witness at d={d}: identical complete conditional outputs = "
    f"{w['same_complete_conditional_outputs']}, different coherence = {w['different_coherence']}."
)

alphas = np.linspace(0.0, 2.0 * np.pi, 257)
df = pd.DataFrame(phase_family(d, alphas))
st.subheader("Continuous family")
st.line_chart(df.set_index("alpha")[["abs_chi"]])
st.dataframe(df.iloc[::32].reset_index(drop=True), use_container_width=True)

st.subheader("Interpretation")
st.markdown(
    "The no-go is stronger than a failure of trace distance alone: any statistic "
    "computed only from the two conditional output states is identical for these "
    "witness models, yet their system coherence differs. Recovering chi therefore "
    "requires additional process-level information (for example the controlled "
    "relative unitary or an interferometrically equivalent statistic)."
)
