# Physical Distinction Theory — Computational Laboratory

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

Licensed under the Apache License 2.0.

This repository is a direct, reproducible testing and comparison implementation of Physical Distinction Theory (PDT) and the **Akhtar Distinction Dynamics Equation (ADDE)**. It contains no manuscript-production material.

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

When \(\Gamma_A=0\), the equation reduces exactly to von Neumann/Schrödinger evolution.

## Implemented coverage

The software implements and tests finite-resource distinction primitives; codebook capacity; decision values and Bregman regret; BQDC and polarization; finite-group invariant geometry; erasure/radial reconstruction checks; Bloch states; Born probabilities; CHSH/Tsirelson; restricted operational norms; resource kernels; ellipsoid tensors; Stinespring dilation; complementary channels; global trace-distinction conservation; local contraction; microscopic environment-record overlap; record bits; pure-record distinguishability; deterministic, weak-record and Poisson rates; ADDE; multi-constraint ADDE; distinction generators; directional contraction; non-Markovian backflow; distinction entropy; conditional Landauer cost; entropy-production defect; operational hypothesis-testing divergence; measured distinction free energy; hidden free-energy gap; conditional small-causal-diamond calculations; horizon-capacity calculator; and four-model dynamical comparison.

## Install and verify

```bash
python -m pip install -r requirements.txt
pytest -q
python pdt_lab.py
```

## Baselines

Every dynamical comparison uses four roles:

1. Schrödinger/von Neumann — closed-system null baseline.
2. GKLS/Lindblad — Markovian open-system baseline.
3. Time-dependent-rate non-Markovian baseline.
4. PDT/ADDE — environmental-record-based dynamics.

In the controlled-record benchmark PDT/ADDE receives \(\nu\) and \(D_E\) independently and therefore has zero fitted decay parameters.

## Public benchmark registry

The source includes download metadata for NPL 2023 (*Modelling non-Markovian noise in driven superconducting qubits*, DOI `10.5281/zenodo.8363718`) and KIT 2026 (*Probing the memory of a superconducting qubit environment*, associated DOI `10.48550/arXiv.2603.11889`).

A decisive PDT experiment requires independent measurement of environment-record variables rather than estimating \(\Gamma_A\) from the same system coherence curve being predicted.
