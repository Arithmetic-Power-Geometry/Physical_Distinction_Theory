import math
import streamlit as st

from pdt_revelation_reset_tradeoff import (
    K_B,
    dimension_information_ceiling_bits,
    landauer_heat_for_bits,
    revelation_reset_ceiling_bits,
)

st.title("Cycle 020 — Revelation / Reset Thermodynamic Tradeoff")
st.caption("PROVED conditional PDT corollary · IMPORTED/KNOWN Holevo + Landauer mathematics · not a breakthrough")

d = st.slider("Quantum record dimension d", 1, 128, 4)
t = st.number_input("Bath temperature T (K)", min_value=0.001, value=300.0)
q_zj = st.number_input("Available reset heat budget (zeptojoule)", min_value=0.0, value=10.0)
q = q_zj * 1e-21

info_dim = dimension_information_ceiling_bits(d)
info_thermo = q / (K_B * t * math.log(2.0))
info_joint = revelation_reset_ceiling_bits(d, q, t)

c1, c2, c3 = st.columns(3)
c1.metric("Dimension ceiling", f"{info_dim:.4f} bits")
c2.metric("Thermal-reset ceiling", f"{info_thermo:.4f} bits")
c3.metric("Joint revelation ceiling", f"{info_joint:.4f} bits")

st.latex(r"I(X:Y)\leq \min\left\{\log_2d,\frac{Q_{reset}}{k_BT\ln2}\right\}")

r = st.slider("Claimed operational revelation r (bits)", 0.0, 10.0, 2.0, 0.1)
q_floor = landauer_heat_for_bits(r, t)
st.write({
    "claimed_revelation_bits": r,
    "minimum_standard_reset_heat_J": q_floor,
    "minimum_standard_reset_heat_zJ": q_floor / 1e-21,
    "passes_dimension_ceiling": r <= info_dim + 1e-12,
    "passes_declared_heat_budget": q + 1e-30 >= q_floor,
})

st.warning("This audit is conditional on standard isothermal Landauer reset of an energetically degenerate classical record with no useful side information retained. Side information, nonthermal reservoirs, nondegenerate memories, or consumed nonequilibrium resources require expanded bookkeeping rather than being counted as violations.")
