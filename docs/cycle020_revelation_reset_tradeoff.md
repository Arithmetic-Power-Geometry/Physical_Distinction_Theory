# Cycle 020 — Distinction Revelation–Reset Tradeoff

## Status

**PROVED (conditional corollary) + IMPORTED/KNOWN mathematics. Not a BREAKTHROUGH CANDIDATE.**

## Statement

Let a classical branch label `X` be read into a classical memory record `Y` through a `d`-dimensional quantum record system. Under unchanged standard quantum mechanics and under the standard Landauer reset model in which the logical memory states are energetically degenerate, the reset is isothermal at bath temperature `T>0`, and there is no useful side information retained during reset,

`I(X:Y) <= min(log2 d, Q_reset / (k_B T ln 2)).`

Equivalently, obtaining `r` operational bits of branch revelation and then closing the cycle by erasing the classical record requires

`Q_reset >= k_B T ln(2) r`.

For perfect revelation of `k` equiprobable branches, `r=log2 k`, so

`Q_reset >= k_B T ln k`,

and the quantum record dimension must satisfy `d>=k`.

## Proof

1. Holevo's bound gives `I(X:Y) <= chi <= log2 d` for any measurement on a `d`-dimensional quantum record.
2. For an ordinary classical measurement memory, `I(X:Y) <= H(Y)`.
3. Under the stated Landauer assumptions, resetting that memory to a standard state dissipates at least `Q_reset >= k_B T ln(2) H(Y)`.
4. Therefore `Q_reset >= k_B T ln(2) I(X:Y)`, giving the joint resource ceiling.

No specifically PDT-native premise is needed for the inequality itself; PDT contributes only the interpretation of `I(X:Y)` as operationally revealed distinction information.

## Kill-test use

A proposed PDT experiment that claims `r` revealed bits from the same `d`-dimensional quantum record while also claiming a closed-cycle reset heat below `k_B T ln(2) r` violates at least one declared assumption. The candidate must explicitly identify which physical ingredient changes: nondegenerate memory energetics/free-energy bookkeeping, retained side information/correlations, nonthermal reservoir, noncyclic resource consumption, modified measurement/state space, or modified thermodynamics.

This is especially important because apparent sub-Landauer protocols can consume correlations, ancillas, nonequilibrium free energy, or other resources. Those are not same-resource violations.

## Edge cases

- `d=1` gives zero accessible record information.
- `k=1` gives zero full-revelation reset floor.
- `T=0` is excluded from the simple thermal formula; zero-temperature quantum thermodynamics requires separate treatment.
- With side information the relevant erasure cost is conditional and can differ from the no-side-information expression.
- Nondegenerate logical memories require full free-energy accounting rather than the simple entropy-only form.

## Audit

`results/cycle020_revelation_reset_tradeoff.csv` evaluates dimensions `d=1..12` at `T=300 K` with `k=d+3`. The test suite verifies the analytic formulas through `d=1000` and `k=100`.

## Prior-art boundary

The ingredients are established: Holevo's accessible-information bound and Landauer's information-erasure principle. Finite-time and quantum-memory refinements are also known. Therefore historical novelty is not claimed for the mathematical inequality. Its value here is as a PDT thermodynamic consistency law and falsification gate.
