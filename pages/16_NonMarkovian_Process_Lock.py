import numpy as np
import streamlit as st
from pdt_process_lock import same_process_lock

st.title('Non-Markovian Same-Process Lock')
st.caption('PROVED no-go; established process-tensor mathematics')

theta = st.slider('theta', 0.0, float(np.pi), 0.73)
phi = st.slider('phi', 0.0, float(np.pi), 1.19)
memory = st.slider('memory strength', -1.0, 1.0, 0.8)
kernel = np.array([[1.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0]])
out = same_process_lock(theta, phi, memory, kernel)
st.metric('TV before resource processing', f"{out['tv_micro']:.3e}")
st.metric('TV after resource processing', f"{out['tv_resource']:.3e}")
st.write(out)
st.markdown('Under identical multi-time process, interventions, and resource processing, memory alone does not create a prediction difference.')
