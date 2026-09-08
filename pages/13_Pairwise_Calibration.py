import streamlit as st

from pdt_pairwise_calibration import audit_table, stabilizer_witness

st.set_page_config(page_title="PDT Pairwise Calibration", page_icon="🧭", layout="wide")
st.title("Pairwise Calibration Closure")
st.caption("Conditional PDT dimension-selection theorem; group-base mathematics is established prior art.")

st.markdown(
    r"""
For a Euclidean distinction body $B^n$ with full connected isotropy $SO(n)$,
ask whether **one ordered pair of reference states** can identify every connected
reversible control.  Two independent references leave pointwise stabilizer
$SO(n-2)$.  Thus pairwise calibration is injective only through $n\le 3$;
requiring genuinely noncommuting connected reversibility then leaves exactly
$n=3$.
"""
)

max_n = st.slider("Maximum dimension", min_value=3, max_value=30, value=12)
df = audit_table(max_n)
st.dataframe(df, use_container_width=True, hide_index=True)

passing = df.loc[df["passes_PCC_plus_noncommuting"], "n"].tolist()
st.metric("Dimensions passing PCC + noncommutativity", str(passing))

st.subheader("Adversarial stabilizer witness")
n = st.slider("Witness dimension", min_value=3, max_value=max(4, max_n), value=min(4, max_n))
Q = stabilizer_witness(n, 2)
if n >= 4:
    st.write("A nonidentity rotation can fix both reference directions while rotating their orthogonal complement:")
else:
    st.write("In n=3 the connected pointwise stabilizer of two independent references is trivial.")
st.dataframe(Q)

st.warning(
    "PCC is not yet a fundamental law. The theorem becomes a breakthrough route only if the requirement that one primitive distinction pair calibrates all elementary reversible controls is independently derived or experimentally justified."
)
