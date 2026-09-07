# Physical Distinction Theory (PDT) — Reproducibility Package

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the **Apache License 2.0**.

This repository accompanies the manuscript **“Physical Distinction Theory: Resource-Bounded Distinction Capacity as a Common Operational Substrate for Quantum Structure, Classical Records, Causal Geometry, and Gravitational Thermodynamics.”**

## What this software does

The package implements reproducible numerical stress tests for the operational quantities used in the manuscript. It includes:

- finite-code resource-bounded distinction-capacity calculations;
- binary Helstrom discrimination and trace-distance utilities;
- data-processing audits under depolarizing channels;
- CHSH numerical search in the standard qubit/singlet realization;
- a redundant-record/decoherence toy model;
- a causal-diamond curvature/capacity scaling toy model;
- entropy-versus-distinction comparisons;
- automated tests and a one-command reproduction workflow.

## What the numerical results mean

The software does **not** numerically prove a new theory of quantum gravity. In particular, the CHSH computation verifies consistency with the standard quantum Tsirelson value; it is not a derivation of that bound from PDT axioms. The causal-diamond calculation is a falsifiable scaling-model pipeline check, not experimental evidence. These distinctions match the manuscript's novelty audit.

## One-click reproduction

```bash
python -m pip install -r requirements.txt
pytest -q
python scripts/reproduce_all.py
```

or run the full verification gate:

```bash
PYTHONPATH=. python scripts/verify_all.py
```

Outputs are written to `results/` and `figures/`.

## Audited local results

- 6/6 automated tests passed.
- 500 random depolarizing-channel data-processing trials: 0 violations.
- 120,000 random planar CHSH settings: best value 2.8278349577; quantum Tsirelson value 2.8284271247; sampling gap 0.0005921670.
- 36 capacity/noise configurations generated.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
