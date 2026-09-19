# Cycle 258 — Purification selector audit

## Candidate
Use the purification principle as the missing PDT-native composition principle and/or as a non-circular selector of `n=3`.

## Exact hypotheses tested
For each finite-dimensional system, every mixed state admits a pure extension whose marginal is that state, with purifications equivalent under reversible transformations on the purifying system. Candidate claim: this property uniquely selects `n=3` or uniquely fixes PDT composition.

## Result
**FALSIFIED as an n=3 selector.** Standard complex quantum theory supplies an analytic counterfamily in every finite Hilbert dimension. For any `n>=1` and any spectrum `lambda_i`, the vector

`|Psi> = sum_i sqrt(lambda_i) |i>_A |i>_B`

purifies `rho_A = sum_i lambda_i |i><i|`. Hence the principle holds at n=2 as well as n=3 and embeds in every higher n. The accompanying exact rational harness checks full-rank spectra for n=1..12; the analytic construction covers arbitrary finite n.

**FALSIFIED as a unique composition principle when used alone.** Purification is a constraint on an already-defined operational composite: it refers to a bipartite state, marginalisation, and reversible transformations on the purifying system. By itself it does not define the tensor/composition rule. Treating those notions as the desired PDT composition would be circular.

## Prior-art boundary
Chiribella, D'Ariano and Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), DOI 10.1103/PhysRevA.81.062348, develops purification directly in GPTs and derives reversible dilations and a state-transformation isomorphism. Their *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311 (2011), obtains finite-dimensional quantum theory from purification only together with five additional informational axioms. Therefore purification/reversible-environment structure is IMPORTED/KNOWN, not PDT-native novelty; and even the reconstructed quantum theory contains systems of arbitrary finite dimension rather than selecting n=3.

## Status ledger
- Arbitrary-finite-n purification counterfamily: **PROVED**.
- Exact n=1..12 rational regression: **PROVED** (algebraic harness; no floating-point inference).
- Purification as unique n=3 selector: **FALSIFIED**; smallest nontrivial competitor n=2.
- Purification alone as unique PDT composition law: **FALSIFIED as stated**.
- Purification/reversible-dilation principle: **IMPORTED/KNOWN**.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input `P_PDT(O|I,R) != P_QM(O|I,R)`: **OPEN**.
- PDT-native experimentally distinctive inequality: **OPEN**.
- Gravity/capacity law: **OPEN; not promoted**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Do not recycle purification, dilation, or environment-record conservation under new terminology. Next cycles should prioritize a genuinely PDT-defined binary operation on distinction resources and test associativity, unit, monotonicity, quotient compatibility, and whether competing tensor rules satisfy the same axioms before attempting any n=3 claim.
