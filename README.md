# Physical Distinction Theory — Computational Laboratory

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License 2.0.

This repository contains the final reproducible software package for Physical Distinction Theory (PDT) and the **Akhtar Distinction Dynamics Equation (ADDE)**. The package implements the complete computational chain used for testing and comparison: finite-resource distinction primitives, BQDC and polarization, elementary reconstruction checks, Born weighting, CHSH/Tsirelson tests, resource-restricted norms and canonical geometry, Stinespring global distinction conservation, complementary-channel records, microscopic record overlap, deterministic and Poisson record dynamics, ADDE and multi-constraint ADDE, dynamical distinction geometry, non-Markovian backflow, distinction entropy, Landauer bounds, hypothesis-testing distinction divergence, operational distinction free energy, conditional causal-geometry calculations, and model benchmarking.

## Canonical Akhtar Distinction Dynamics Equation

\[
\dot\rho=-\frac{i}{\hbar}[H,\rho]+\Gamma_A(t)(\mathcal E_R-I)[\rho],
\qquad
\Gamma_A(t)=-\frac{d}{dt}\ln|\kappa_{\rm tot}(t)|.
\]

For deterministic independent pure environment records,

\[
\Gamma_A=-\nu\ln|\kappa|=-\frac{\nu}{2}\ln(1-D_E^2).
\]

The zero-record limit \(\Gamma_A=0\) reduces exactly to von Neumann/Schrödinger evolution.

## Included package

`Physical_Distinction_Theory_Software.zip` contains the full Python package, equation registry, tests, reproduction scripts, benchmark outputs, public-dataset registry, and GitHub Actions workflow.

## Reproduce

```bash
unzip Physical_Distinction_Theory_Software.zip -d pdt_software
cd pdt_software
python -m pip install -e . pytest
python scripts/verify_all.py
```

## Comparison models

The benchmark suite compares:

- Schrödinger/von Neumann evolution — closed-system null baseline;
- GKLS/Lindblad — Markovian open-system baseline;
- time-dependent-rate non-Markovian baseline;
- PDT/ADDE — environmental-record-based dynamics.

In the built-in controlled-record benchmark PDT/ADDE uses independently specified \(\nu\) and \(D_E\) and therefore uses **zero fitted decay parameters**.

## Public benchmark registry

The package includes download metadata for:

- NPL 2023, *Modelling non-Markovian noise in driven superconducting qubits*, DOI `10.5281/zenodo.8363718`;
- KIT 2026, *Probing the memory of a superconducting qubit environment*, associated DOI `10.48550/arXiv.2603.11889`.

The decisive PDT test requires independent measurement of environment-record quantities rather than inferring the decay rate from the same system curve being predicted.
