# Real Experimental PDT/ADDE Audit

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Result

Three real experimental sources were executed. **Zero** currently satisfy all requirements for a decisive PDT-specific blind ADDE test simultaneously. This is an important identifiability result, not a positive experimental confirmation.

### Independent record/coherence experiment

The QWPD photonic-qubit data provide separately measured detector distinguishability and system coherence with zero fitted parameters in the pure-record predictor. The raw-count reconstruction gives RMSE **0.338286** and MAE **0.268612**. However, the source explicitly reports imperfect entanglement/mixed detector states, so the exact pure-record equality is outside its stated applicability domain.

### Superconducting-qubit data

The NPL public CSV contains **1728** experimental rows and yields **558** usable X/Y transverse-coherence traces. Median RMSE: Schrodinger **0.561710**, constant-rate GKLS/ADDE-fit **0.216393**, non-Markovian baseline **0.183937**. Because the public file does not independently measure the environment record, an ADDE rate fitted from the same system trace is not counted as PDT validation.

### Ramsey cross-platform data

The Ramsey archive provides **11** delay points in the selected 0+1 sequence. Schrodinger RMSE **0.221700** and fitted exponential/GKLS RMSE **0.165523**. Again, no independent environment record is present, so this is a compatibility/diagnostic test only.

## Required decisive experiment

Measure the conditional environment record pair (or a sufficient pure-record distinguishability D_E) independently, determine event statistics/rate, freeze

Gamma_A = -nu/2 ln(1-D_E^2)

before the system coherence curve is revealed, and then compare the blind ADDE prediction against GKLS and non-Markovian baselines.
