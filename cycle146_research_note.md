# Cycle 146 — Continuity does not rescue the composition selector

## Status

**DECISIVE FALSIFICATION; not a breakthrough candidate.**

Cycle 145 left open whether adding vanishing-channel continuity to its structural package would force ordinary additive composition. It does not.

For nonnegative resource shares q=(q_i), define

F(q)=((sum_i q_i^2)^2)/(sum_i q_i^3) for q != 0, with F(0)=0.

## Exact identities

The counterfamily is permutation invariant, zero-padding stable, singleton calibrated and positively homogeneous: F(cq)=cF(q) for c>=0.

For a uniform k-way resolved vector q=(a,...,a),

F(q)=(ka^2)^2/(ka^3)=ka=sum_i q_i,

so every uniform refinement is conserved.

For product shares (q tensor r)_ij=q_i r_j, every power sum factors, hence F(q tensor r)=F(q)F(r).

The map is continuous when nonzero because it is a quotient of polynomials with positive denominator. At the origin, Cauchy-Schwarz gives

(sum_i q_i^2)^2 <= (sum_i q_i)(sum_i q_i^3),

hence 0<=F(q)<=sum_i q_i -> 0. This also supplies a global bound.

## Decisive unequal witness

For q=(1,3), F(1,3)=100/28=25/7, whereas ordinary additive composition gives 4. The exact gap is -3/7.

Therefore permutation symmetry + zero-padding stability + singleton calibration + positive homogeneity + conservation under every uniform resolved refinement + tensor-product multiplicativity + vanishing-channel continuity does NOT imply ordinary additive composition.

## Equality boundary

The Cauchy-Schwarz equality condition shows F(q)=sum_i q_i exactly when all positive components of q are equal (zeros are irrelevant). Thus the counterexample agrees on every uniform split while separating generic unequal refinements.

## Prior-art boundary

Writing S=sum_i q_i and p_i=q_i/S gives

F(q)/S=(sum_i p_i^2)^2/(sum_i p_i^3)=exp(2(H_3(p)-H_2(p))).

Rényi entropies and their additivity on product states/distributions are established information-theoretic structures. That machinery is **IMPORTED/KNOWN** and is not claimed as PDT novelty. Here it is used adversarially to reject a tempting PDT-II axiom package.

## Frozen audit

Seed 146. Dimensions: 1–12, 16, 24, 32, 48, 64, 96, 128. The audit spans dense and sparse inputs over 24 orders of magnitude, permutations, zero padding, positive scaling, uniform refinements, tensor products, the origin, and vanishing-channel probes.

Local regression before commit: **7/7 tests passed**.

## Classification

- Counterfamily identities and continuity proof: **PROVED**
- Continuity-rescues-Cycle-145 implication: **FALSIFIED**
- Frozen randomized/dimension audit: **NUMERICALLY SUPPORTED**
- Rényi/power-sum product structure: **IMPORTED/KNOWN**
- PDT-native full composition law: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**

## Surviving obligation

Continuity plus product structure is still too weak. A successful PDT-native composition law must constrain **unequal resolved refinements** directly, for example through a physically derived arbitrary unequal refinement/recombination law, rather than only uniform splitting, continuity and independent-product behavior.
