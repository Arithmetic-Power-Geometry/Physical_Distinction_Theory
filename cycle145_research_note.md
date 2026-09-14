# Cycle 145 — Tensor/uniform composition counterexample

## Status

**DECISIVE FALSIFICATION; not a breakthrough candidate.**

The following candidate implication is false:

> permutation symmetry + zero-padding stability + singleton calibration + conservation under every uniform resolved refinement + positive homogeneity + tensor-product multiplicativity => ordinary additive composition.

For nonnegative shares `q=(q_i)`, let `k(q)` be the number of positive coordinates and define

`F(q)=k(q) sum_i q_i^2 / sum_i q_i` for `q != 0`, with `F(0)=0`.

## Exact identities

For every positive scalar `c`, permutation `pi`, and zero padding,

`F(cq)=cF(q)`, `F(pi q)=F(q)`, and `F(q,0)=F(q)`.

If a total share `S` is refined uniformly into `m` positive daughters, `q_i=S/m`, then `F(S/m,...,S/m)=S`.

For product shares `(q tensor r)_ij=q_i r_j`,

`F(q tensor r)=F(q)F(r)`

because positive support sizes, first moments, and second moments all multiply.

## Decisive unequal witness

For `q=(1,3)`, `F(1,3)=2(1^2+3^2)/(1+3)=5`, whereas ordinary additive composition gives `1+3=4`.

Thus the audited axiom package does not force ordinary composition.

## Boundary diagnosis

For epsilon > 0,

`F(1,epsilon)=2(1+epsilon^2)/(1+epsilon) -> 2`

as epsilon decreases to zero, while `F(1,0)=1`. Hence the counterfamily is discontinuous when a positive channel disappears. A physically justified vanishing-channel continuity principle excludes this counterfamily, but it has NOT been proved here that continuity plus the remaining axioms uniquely forces additive composition. That stronger statement remains OPEN.

## Prior-art boundary

Writing `S=sum_i q_i` and `p_i=q_i/S` gives `F(q)=S k(p) sum_i p_i^2`. The factor `sum_i p_i^2` is the order-2 collision probability, equivalently the exponential of minus Renyi-2 entropy. Its product multiplicativity is standard. Therefore the mathematical mechanism is IMPORTED/KNOWN and is not claimed as a new PDT theorem. Here it is used adversarially as a counterexample to a tempting PDT-II composition axiom package.

## Frozen stress audit

Dimensions: 1–12, 16, 24, 32, 48, 64, 96, 128. Seed: 145. The audit includes dense and sparse/zero-containing inputs, permutations, zero padding, scalings over many orders of magnitude, uniform refinements, product tensors, and the vanishing-channel edge. See `cycle145_composition_counterexample.json`.

Local regression result before commit: **7/7 tests passed**.

## Classification

- Counterfamily identities: **PROVED**
- Candidate implication: **FALSIFIED**
- Frozen randomized/dimension audit: **NUMERICALLY SUPPORTED**
- Renyi-2/collision-probability mechanism: **IMPORTED/KNOWN**
- PDT-native complete composition law: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
