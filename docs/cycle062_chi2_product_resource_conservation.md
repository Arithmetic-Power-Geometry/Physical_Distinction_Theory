# Cycle 062 — exact chi-square composition/resource ledger

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT STRUCTURAL BRIDGE.**  Not a breakthrough candidate.

## Hypotheses

Let `(P_A,Q_A)` and `(P_B,Q_B)` be independent finite binary experiments with full-support reference distributions `Q_A,Q_B`. Define

`C(P,Q)=chi^2(P||Q)=E_Q[(P/Q-1)^2]`.

Local resource restrictions are arbitrary stochastic kernels applied separately to A and B.

## Exact composition theorem

Writing `C_A=C(P_A,Q_A)` and `C_B=C(P_B,Q_B)`, independence gives

`1+C_AB=(1+C_A)(1+C_B)`,

or equivalently

`C_AB=C_A+C_B+C_A C_B`.

Proof: if `L_A=P_A/Q_A` and `L_B=P_B/Q_B`, then under `Q_A x Q_B`, `L_AB=L_A L_B`, `E[L_A]=E[L_B]=1`, and `1+C=E[L^2]`. Independence factorizes the second moment.

## Exact local resource-loss theorem

After local stochastic restrictions let the surviving capacities be `C_A'` and `C_B'`, with losses `Delta_A=C_A-C_A'` and `Delta_B=C_B-C_B'`. Then

`Delta_AB = Delta_A(1+C_B') + Delta_B(1+C_A') + Delta_A Delta_B >= 0`.

This follows by subtracting the product identities before and after restriction. The nonnegativity uses chi-square data processing under stochastic maps.

## Additive log budget

Define

`K(P,Q)=log(1+C(P,Q))`.

Then

`K_AB=K_A+K_B`,

and local resource losses telescope additively:

`(K_AB-K_AB')=(K_A-K_A')+(K_B-K_B')`.

This is a clean composition-compatible refinement of Cycle 061's single-system revelation ledger.

## Novelty boundary

`K=log(1+chi^2)` is exactly the order-2 Renyi divergence. Product additivity and data processing are established information-theoretic facts. Therefore this result must not be presented as new mathematics or as a PDT breakthrough. Its value here is structural: it identifies an exact scalar ledger that simultaneously respects independent composition and local resource degradation, and it supplies a regression target that any richer PDT-native composition law should recover in the classical independent limit.

## Audit

The executable audit uses exact `Fraction` arithmetic. It checks 200 randomized cases for every dimension `n=1..12`, plus 50 cases for `n=16,24,32,48,64,96,128`. Total: 2,750 cases; recorded failures: 0. Identity-map and explicit rational regression cases are included in the test suite.
