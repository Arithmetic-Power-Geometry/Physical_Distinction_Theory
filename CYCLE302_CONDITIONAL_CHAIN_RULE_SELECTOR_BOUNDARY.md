# Cycle 302 — Conditional chain-rule selector boundary

## Target
PDT-II target (1): test whether strengthening product additivity and stochastic data processing by an exact sequential/conditional decomposition can supply a defensible composition selector.

## Hypotheses tested
For a divergence-like distinction functional `D(P||Q)` on finite distributions, require the exact conditional chain rule

`D(P_XY||Q_XY) = D(P_X||Q_X) + sum_x P_X(x) D(P_{Y|x}||Q_{Y|x})`.

This is stronger than independent-product additivity because it covers correlated/sequential records and fixes the weighting of branchwise distinction by the first distribution's actual branch probabilities.

## Exact result
Kullback–Leibler divergence satisfies this identity by direct logarithmic factorization:

`log(P_XY/Q_XY)=log(P_X/Q_X)+log(P_{Y|X}/Q_{Y|X})`,

followed by expectation under `P_XY`.

However, the Renyi-1/2 divergence that survived the weaker Cycle-301 additivity+DPI requirements fails this exact conditional rule. A rational 2x2 witness is

`P_XY=(5,1,6,8)/20`, `Q_XY=(1,17,1,1)/20`.

Numerically,

- `D_1/2(P_XY||Q_XY) = 1.083069644124446`
- conditional-chain RHS = `0.7845063136443375`
- absolute defect = `0.2985633304801085`.

Thus exact conditional decomposition is a genuine additional selector, not a consequence of product additivity+DPI.

## What this does NOT prove
This does **not** make KL a PDT-native law. The KL chain rule and its characterizing role are established information theory. PDT presently has no independent physical axiom forcing the asymmetric `P`-weighted conditional accounting above. Calling it “distinction conservation” would import the desired selector unless that weighting is operationally derived from PDT.

It also does not yield a same-input PDT-vs-QM deviation: adopting KL would be a model choice until PDT derives why physical distinction must obey this exact sequential accounting.

## Dimension and edge coverage
The 2x2 witness embeds into all larger finite alphabets by adding common zero coordinates; strict-interior epsilon embeddings preserve failure by continuity. Hence the counterexample persists for dimensions 2 through 12 and arbitrarily high finite dimension. Product cases remain a special case of the chain rule. Degenerate zero-probability cases require the usual absolute-continuity conventions and are not used in the decisive witness.

## Prior-art audit
The exact KL conditional chain rule is standard. Renyi divergences generally use different composition/chain rules; alpha=1 is distinguished by the ordinary expectation-form chain rule. Therefore the selector mechanism is IMPORTED/KNOWN, not a PDT novelty claim.

## Status
- KL exact conditional chain rule: **PROVED / IMPORTED-KNOWN**.
- Additivity + DPI => exact conditional chain rule: **FALSIFIED** (Renyi-1/2 witness).
- Exact ordinary conditional chain rule as a PDT-native axiom: **OPEN**.
- PDT-native derivation of the branch weighting: **OPEN**.
- PDT-native composition law: **OPEN**.
- Same-input quantitative PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Consequence for the search
The next composition attack should not add generic information-theoretic axioms blindly. It must derive, from PDT operational primitives, either (i) a sequential accounting rule strong enough to select a functional, or (ii) a counterexample showing that no scalar functional can carry the required controlled-record/composite information. Until then, KL/Renyi/Hellinger choices remain imported selectors.
