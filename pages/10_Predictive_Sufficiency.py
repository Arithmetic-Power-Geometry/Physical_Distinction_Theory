"""Streamlit audit for PDT operational predictive sufficiency."""

import pandas as pd
import streamlit as st

from pdt_predictive_sufficiency import audit_predictive_sufficiency

st.set_page_config(page_title="PDT Predictive Sufficiency", layout="wide")
st.title("Operational Predictive Sufficiency Audit")
st.caption(
    "Status: PROVED PDT formulation / mathematical factorization logic known. "
    "Use this page as a same-input kill test for candidate resource statistics."
)

st.markdown(
    r"""
Let a resource window retain only a statistic \(S_R(I)\) of the complete microscopic
input \(I\), while a reference theory predicts an outcome distribution \(Q(I)\).
An exact resource-only predictor exists iff

\[
S_R(I_1)=S_R(I_2)\;\Longrightarrow\;Q(I_1)=Q(I_2).
\]

For approximate prediction, if one fibre contains predictions separated by total-
variation diameter \(\Delta\), every predictor depending only on the statistic has
worst-case error at least \(\Delta/2\) somewhere on that fibre.
"""
)

mode = st.selectbox(
    "Audit example",
    ["Sufficient repeated fibre", "Maximally insufficient binary fibre"],
)

if mode == "Sufficient repeated fibre":
    labels = ["same", "same", "other"]
    predictions = [[0.7, 0.3], [0.7, 0.3], [0.2, 0.8]]
else:
    labels = ["same-output", "same-output"]
    predictions = [[1.0, 0.0], [0.0, 1.0]]

rows, sufficient, lower = audit_predictive_sufficiency(labels, predictions)
df = pd.DataFrame(
    [
        {
            "fibre": row.label,
            "count": row.count,
            "TV diameter": row.tv_diameter,
            "minimax lower bound": row.minimax_error_lower_bound,
        }
        for row in rows
    ]
)

c1, c2 = st.columns(2)
c1.metric("Exact factorization possible?", "YES" if sufficient else "NO")
c2.metric("Universal worst-case error lower bound", f"{lower:.3f}")
st.dataframe(df, use_container_width=True)

if sufficient:
    st.success("The sampled prediction map is constant on every resource-statistic fibre.")
else:
    st.error(
        "The resource statistic collapses prediction-distinct microscopic inputs. "
        "No exact predictor based only on that statistic can reproduce all sampled same-input predictions."
    )

st.markdown(
    r"""
### PDT research use
This criterion generalizes the controlled-environment non-identifiability examples.
Before promoting any candidate PDT statistic to a predictive law, group microscopic
models by the accessible statistic and measure the prediction diameter inside every
fibre. A nonzero diameter is an immediate no-go for universal exact prediction from
that statistic alone.

A true same-input departure from quantum mechanics therefore cannot be created by
mere relabeling or post-processing of an insufficient statistic. It must either use
a predictively sufficient operational quotient or explicitly modify some physical
ingredient such as state space, composition, dynamics, or measurement law.
"""
)

st.warning(
    "Novelty boundary: factorization through fibres/quotients and sufficient-statistic logic are established mathematics. "
    "This page is a PDT research diagnostic, not a claim of new mathematical or quantum physics."
)
