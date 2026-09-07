# Physical Distinction Theory - Reproducibility Laboratory

Copyright (C) 2026 Mohammad Amir Khusru Akhtar  
Licensed under the Apache License 2.0.

This repository is synchronized with the submission-ready manuscript **Physical Distinction Theory: From Resource-Bounded Discrimination to Quantum Geometry, Open-System Dynamics, and Thermodynamic Monotones**.

The implementation keeps PDT-native/no-go results, conditional theorems, established quantum-information identities, and open frontier statements explicitly separated.

## Reproduce and test

```bash
python -m pip install -r requirements.txt
PYTHONPATH=. pytest -q
python scripts/real_experimental_benchmark.py
python scripts/generate_results.py
python pdt_lab.py
```

## Canonical manuscript-synchronized dynamics

The total distinction tensor is

\[
\mathfrak A_R^{\rm tot}
=-\frac12\left(\dot G_R+L^T G_R+G_RL\right).
\]

The older expression `-0.5*dot(G_R)` is retained only as the **resource/metric-motion component**; it is not the total dynamical tensor.

For the controlled-record sector,

\[
\dot\rho=-\frac{i}{\hbar}[H_{\rm eff},\rho]
+\Gamma_A(t)(\mathcal E_R-I)[\rho],
\qquad
\Gamma_A=-\frac{d}{dt}\ln|\chi_{\rm tot}|.
\]

The phase of `chi` is handled by `H_eff`. A same-input comparison is mandatory: when PDT bookkeeping and standard microscopic quantum mechanics receive the same environment state and controlled unitaries, they predict the same controlled-dephasing coherence factor.

## Generated manuscript outputs

`python scripts/generate_results.py` writes manuscript-facing outputs into `results/`:

- `table1_core_numerical_audit.csv`
- `table2_synthetic_model_comparison.csv`
- `table3_real_data_audit.csv`
- `table4_proof_status_matrix.csv`
- `figure1_pdt_logical_architecture.svg`
- `figure2_synthetic_rmse.svg`
- `geometry_audit.csv`
- `total_tensor_verification.csv`
- `mixed_record_envelope_example.csv`
- `summary.json`

The real-data audit remains deliberately conservative:

`N_real=3`, `N_independent_record=1`, `N_time_decay=2`, `N_decisive=0`.

## Scientific status

This repository supports a resource-relative foundations framework with proved no-go statements, conditional rigidity/probability/correlation results, exact record and dynamical identities, resource-relative monotones, and explicit falsification rules. It does **not** claim a completed replacement for quantum mechanics or gravity, and currently available public datasets are **not** treated as decisive PDT-specific experimental confirmation.
