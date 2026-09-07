# Physical Distinction Theory (PDT) — Theorem-Audit Reproducibility Package

**Copyright (C) 2026 Mohammad Amir Khusru Akhtar**  
Licensed under the **Apache License 2.0**.

Companion repository for **“Physical Distinction Theory: Quadratic Distinction Conservation, Quantum Bounds, Resource-Bounded Capacity, and the Route to Causal Geometry.”**

## What is implemented

- resource-bounded finite-code distinction capacity;
- Helstrom discrimination, trace distance, entropy and depolarizing channels;
- explicit classical-local and PR-box foil models showing that broad A1–A6 operational axioms do not isolate quantum correlations;
- Balanced Quadratic Distinction Conservation / parallelogram-law audits across non-Hilbertian p-norm foils;
- conditional Hilbertian CHSH/Tsirelson bound checks;
- equal-orthogonal-refinement audit selecting Born exponent q=2 within the continuous power-law family;
- compatible complex-structure J audit;
- homogeneous capacity–volume, screen-capacity and Planck localization/collapse scaling pipelines;
- 14 automated tests, heavy deterministic reproduction, manuscript table export and GitHub Actions CI.

## Scientific-status firewall

The software distinguishes analytic/conditional results from open claims. The Tsirelson theorem is conditional on the quadratic distinction law plus bounded bilinear correlations; the Born result is conditional on the stated refinement assumptions. Capacity–volume is a conditional measure theorem. The exact horizon coefficient `1/(4 ln 2)` is **not** claimed as derived from PDT first principles.

## One-command verification

```bash
python -m pip install -r requirements.txt
python scripts/verify_all.py
```

The verification gate runs pytest, regenerates results/figures, exports LaTeX tables, and checks the headline numerical invariants.

## Audited reference run

- 14/14 tests passed.
- 5,000 random depolarizing-channel pairs: 0 data-processing violations.
- 2,000,000 planar standard-quantum CHSH samples: best `2.8281077683` versus `2√2 = 2.8284271247`.
- exact classical deterministic CHSH maximum: `2`.
- canonical PR-box CHSH: `4`.
- sampled ℓ2 parallelogram maximum defect: `2.13e-14` (roundoff scale).
- numerical Born-refinement minimizer: `q = 2.0000000029`; objective at q=2 ≈ `5.88e-32`.
- canonical complex-structure residuals: zero to floating-point precision.

Generated outputs are written to `results/`, `figures/`, and `generated_latex/`.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
