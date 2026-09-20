# Cycle 274 — Composition-selector non-uniqueness

## Target attacked
PDT-II target (1): derive a PDT-native composition law rather than import or guess one.

## Candidate claim tested
A tempting strengthening after the Hellinger/Bhattacharyya product law is that requiring a scalar distinction `d` to have identity 0, symmetry under exchange of independent factors, monotonicity, continuity, associativity, and the probabilistic-sum product rule

`d_AB = d_A + d_B - d_A d_B`

might select the physical distinction functional.

## Exact counterfamily
For strictly positive finite probability vectors p,q define the order-2 Rényi likelihood moment

`S2(p||q) = sum_i p_i^2/q_i >= 1`

and bounded distinction

`d2(p,q) = 1 - 1/S2(p||q)`.

For independent products,

`S2(p⊗r || q⊗s) = [sum_i p_i^2/q_i][sum_j r_j^2/s_j] = S2(p||q) S2(r||s)`.

Therefore

`1-d2_AB = (1-d2_A)(1-d2_B)`

and hence exactly

`d2_AB = d2_A + d2_B - d2_A d2_B`.

This is the same scalar composition operation obtained in Cycle 273 from squared Hellinger/Bhattacharyya affinity, but d2 is a different state-pair functional. Thus even fixing the binary composition operation does not select the underlying distinction measure.

More generally, whenever an additive nonnegative divergence A obeys `A(P⊗R,Q⊗S)=A(P,Q)+A(R,S)`, every fixed c>0 gives `d_c=1-exp(-c A)` and the same probabilistic-sum law. This general observation is mathematically known additive-generator structure; it is not claimed as PDT novelty.

## Small decisive example
Take p=(1/2,1/2), q=(3/4,1/4). Then

`S2 = (1/4)/(3/4) + (1/4)/(1/4) = 1/3 + 1 = 4/3`,
so `d2=1/4`.
For two identical independent copies, `S2_AB=16/9`, hence `d2_AB=7/16`, exactly equal to `1/4+1/4-1/16=7/16`.

This already works in dimension n=2 and zero-padding/positive-tail approximations extend the obstruction to arbitrary larger finite ambient dimensions. Direct strictly-positive constructions exist in every n>=2 as well.

## Consequence for PDT-II
The following route is decisively closed:

`nice scalar composition axioms + probabilistic-sum law => unique PDT distinction functional`.

A PDT-native composition theorem must contain additional operational content that selects BOTH (i) the state-pair statistic and (ii) the admissible joint experiments/resources. Algebraic properties of the scalar binary operation alone are insufficient.

This also cannot select n=3: the construction is dimension-independent.

## Prior-art boundary
Rényi divergences and their tensor-product additivity are established information-theoretic structure. Continuous associative monotone operations and t-conorm/additive-generator representations are also established mathematics. The PDT contribution of this cycle is therefore a falsification/boundary result for a proposed PDT-II derivation route, not a claim to have discovered Rényi additivity or t-conorm theory.

## Status
- Product factorization of S2: **PROVED**.
- Bounded d2 probabilistic-sum composition: **PROVED**.
- Same scalar composition operation uniquely selects the distinction functional: **FALSIFIED**.
- Composition axioms above select n=3: **FALSIFIED**.
- Rényi/additive-generator mathematics: **IMPORTED/KNOWN**.
- PDT-native selector coupling resource-admissible joint experiments to a unique distinction functional: **OPEN**.
- PDT-native composition law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
