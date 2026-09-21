# Cycle 299 — Tensorizing affinity composition boundary

## Target
PDT-II target (1): search for a nontrivial scalar compositional invariant after Cycle 298 proved that total-variation distinction itself has no universal scalar product law `D_AB = F(D_A,D_B)`.

## Candidate and exact hypotheses
For finite classical experiments with hypotheses represented by probability vectors `P,Q`, define the Bhattacharyya/Hellinger affinity

`A(P,Q) = sum_i sqrt(P_i Q_i)`.

For conditionally independent composites use the ordinary product rule `(P,Q) -> (P⊗R,Q⊗S)`.

## Proof
Direct factorization gives

`A(P⊗R,Q⊗S) = sum_{i,j} sqrt(P_i R_j Q_i S_j)`
`= (sum_i sqrt(P_i Q_i))(sum_j sqrt(R_j S_j))`
`= A(P,Q) A(R,S)`.

Hence the complementary quantity `H2 = 1-A` obeys the exact scalar composition law

`H2_AB = H2_A + H2_B - H2_A H2_B = 1-(1-H2_A)(1-H2_B)`.

This remains exact for degenerate probabilities and arbitrary finite dimensions, including n=1 through n=12 and higher dimensions.

## Interpretation
This is a useful boundary, not a PDT breakthrough. Cycle 298 showed that operational total-variation distinguishability does not tensorize from its two local scalar values. The present result shows that scalar tensorization can be recovered by changing the invariant to Hellinger/Bhattacharyya affinity. But that invariant and its product factorization are established statistics/information theory; choosing it is not a PDT-native derivation and does not by itself produce a same-input deviation from QM.

The key surviving PDT obligation is therefore stronger: derive, from PDT-native physical assumptions, which operational invariant is fundamental and why. Selecting a convenient tensorizing divergence after the fact would be imported structure.

## Prior-art check
Established Hellinger/Bhattacharyya theory defines the affinity/integral and its associated distance. Contemporary product-distribution literature explicitly contrasts total variation with Hellinger/KL/chi-square measures that tensorize over independent marginals. Therefore neither the affinity nor this product law is claimed as novel.

## Classification
- `A(P⊗R,Q⊗S)=A(P,Q)A(R,S)`: **PROVED / IMPORTED-KNOWN**.
- `H2_AB = 1-(1-H2_A)(1-H2_B)`: **PROVED / IMPORTED-KNOWN**.
- universal scalar product law for total variation: remains **FALSIFIED** (Cycle 298).
- PDT-native reason to privilege affinity/Hellinger over competing divergences: **OPEN**.
- PDT-native composition law: **OPEN**.
- non-circular PDT-native n=3 derivation: **OPEN**.
- fully specified same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Guardrail
This cycle must not be cited as a novel PDT composition theorem. It is a prior-art-controlled boundary result identifying an exact compositional invariant and, more importantly, exposing the still-missing PDT-native selector.
