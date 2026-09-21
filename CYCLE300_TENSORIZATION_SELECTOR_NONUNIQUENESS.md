# Cycle 300 — Tensorization selector nonuniqueness

## Target
PDT-II target (1): test whether the exact tensorizing affinity found in Cycle 299 can be selected from generic composition principles, rather than imported by choice.

## Candidate selector and hypotheses
Suppose a scalar overlap/distinction functional is required to be continuous on finite probability simplices, invariant under relabelling, normalized on identical distributions, monotone under stochastic coarse-graining in the appropriate direction, and exactly multiplicative (or logarithmically additive) on conditionally independent products.

A tempting inference would be that these requirements select the Cycle-299 Bhattacharyya/Hellinger affinity.

## Counterfamily
For every alpha in (0,1), define the alpha-affinity

`A_alpha(P,Q) = sum_i P_i^alpha Q_i^(1-alpha)`.

Direct factorization gives

`A_alpha(P⊗R,Q⊗S) = A_alpha(P,Q) A_alpha(R,S)`.

The associated Rényi divergence

`D_alpha(P||Q) = log(A_alpha(P,Q))/(alpha-1)`

is therefore additive on products. These functionals are continuous (with the usual boundary interpretation), relabelling invariant, normalized at P=Q, and belong to the established Rényi/Chernoff family. For alpha != 1/2 they are generally distinct from the symmetric Bhattacharyya coefficient. If symmetry under exchange P<->Q is additionally demanded, one may form

`S_alpha(P,Q) = sqrt(A_alpha(P,Q) A_(1-alpha)(P,Q))`,

which is symmetric and still multiplicative on products. Thus even adding symmetry does not select alpha=1/2.

## Small decisive witness
Take `P=(0.9,0.1)` and `Q=(0.6,0.4)`. Then `A_1/2(P,Q)` and `S_1/4(P,Q)` are unequal, while both are symmetric normalized multiplicative overlaps satisfying the same generic product-composition form. Hence generic tensorization + symmetry + continuity + normalization cannot uniquely select the Cycle-299 invariant.

## Consequence for PDT-II
The Cycle-299 exact composition law is a useful imported boundary but cannot become PDT-native merely by axiomatizing product tensorization. PDT still needs an independently physical selector tied to what a distinction operation means operationally. Choosing alpha=1/2 because it gives a convenient geometry would be circular/model selection, not a derivation.

This also blocks a premature same-input PDT-vs-QM prediction: different admissible tensorizing invariants assign different numerical distinctions to the same microscopic pair, so the invariant must be physically fixed before a quantitative deviation is meaningful.

## Prior-art boundary
Rényi divergences are established product-additive/data-processing quantities; alpha-skewed Bhattacharyya/Chernoff affinities are established. Prior work on additive data-processing divergences explicitly characterizes broad Rényi-based families. No novelty is claimed for this counterfamily or its tensorization.

## Classification
- `A_alpha` product tensorization: **PROVED / IMPORTED-KNOWN**.
- symmetric `S_alpha` product tensorization: **PROVED / IMPORTED-KNOWN**.
- generic tensorization + continuity + normalization selecting alpha=1/2: **FALSIFIED**.
- same claim with exchange symmetry added: **FALSIFIED**.
- smallest displayed nondegenerate witness: binary (`n=2`): **PROVED**.
- embeddings through n=2..12 and arbitrary higher finite dimension: **PROVED** by zero-padding; randomized positive-support stress tests are supplied separately.
- PDT-native selector for a fundamental compositional invariant: **OPEN**.
- PDT-native composition law: **OPEN**.
- non-circular PDT-native n=3 derivation: **OPEN**.
- fully specified same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Guardrail
Do not cite the Rényi/Chernoff family or its tensorization as a PDT novelty. The result of this cycle is a no-go boundary: generic scalar tensorization principles are underdetermining.