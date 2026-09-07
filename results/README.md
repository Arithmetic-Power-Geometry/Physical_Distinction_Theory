# Generated manuscript results

Run `python scripts/generate_results.py` from the repository root.

The committed CSV/SVG files are deterministic manuscript-facing outputs. The public-data refresh is produced by `scripts/real_experimental_benchmark.py` and is used by the table generator when available.

- Table 1: `table1_core_numerical_audit.csv`
- Table 2: `table2_synthetic_model_comparison.csv`
- Table 3: `table3_real_data_audit.csv`
- Table 4: `table4_proof_status_matrix.csv`
- Figure 1: `figure1_pdt_logical_architecture.svg`
- Figure 2: `figure2_synthetic_rmse.svg`
- CEU/CER counterfamily: `geometry_audit.csv`
- Total-tensor verification: `total_tensor_verification.csv`
- Mixed-record envelope example: `mixed_record_envelope_example.csv`
- Machine-readable summary: `summary.json`

Current public-data evidence count: `N_real=3`, `N_independent_record=1`, `N_time_decay=2`, `N_decisive=0`.
