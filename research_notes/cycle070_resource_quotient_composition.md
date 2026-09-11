# Cycle 070 — Resource-Quotient Composition Boundary

## Status

**PROVED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED**  
**Not a BREAKTHROUGH CANDIDATE.**

## Hypotheses

Let `H_d` be the real vector space of Hermitian `d x d` matrices with Hilbert–Schmidt pairing `<X,A>=Tr(XA)`. A resource window `R` declares an accessible real operator subspace `S_R subset H_d` containing the identity. A microscopic state `rho` is operationally represented at resource `R` only through its expectation-value functional

`q_R(rho): A in S_R -> Tr(rho A)`.

## Theorem 1 — exact resource quotient

Two states are indistinguishable under all observables in `S_R` iff

`rho - sigma in S_R^perp`.

Hence the exact resource state is the quotient class

`[rho]_R in H_d / S_R^perp`,

or equivalently the restricted functional `q_R(rho) in S_R^*`.

This is stronger than any single scalar distinction summary: it retains exactly all linear prediction data available in the declared window and no data orthogonal to that window.

## Theorem 2 — exact refinement/revelation map

For nested resource windows `S_R subset S_R'`, the coarse state is exactly the restriction of the fine state:

`q_R(rho) = q_R'(rho)|_{S_R}`.

The newly revealed linear degrees of freedom are the quotient directions in `S_R'/S_R`; no ad hoc revelation rule is required.

## Theorem 3 — exact product composition

For independent systems with product-accessible resource space `S_AB = span{A tensor B: A in S_A, B in S_B}` and product state `rho_A tensor rho_B`,

`q_AB(rho_A tensor rho_B)(A tensor B) = q_A(rho_A)(A) q_B(rho_B)(B)`.

Thus the restricted state functional composes exactly by tensor product:

`q_AB(rho_A tensor rho_B) = q_A(rho_A) tensor q_B(rho_B)`

on the product-accessible span.

This gives an exact composition object, unlike the scalar/spectral candidates killed in earlier cycles. It does **not** by itself solve interacting/correlated composition, choose a unique tensor product for arbitrary GPTs/operator systems, derive `n=3`, or produce a PDT-vs-QM same-input deviation.

## Counterexample/search discipline

The theorem is linear-algebraic, so numerical tests are regression evidence rather than proof. The audit tests random mixed noncommuting states and random accessible Hermitian subspaces over dimensions `1..12` and `16,24,32,48,64`, including identity-only/low-rank resource windows where applicable. Product factorization is tested for all dimension pairs `1..6` with random product states and random local accessible spaces.

Recorded audit:

- refinement/resource cases: `265`
- product cases: `288`
- maximum restriction error: `0.0`
- maximum annihilator orthogonality error: `1.2490009027033011e-15`
- maximum product-coordinate error: `1.1102230246251565e-16`

No numerical contradiction was found.

## Prior-art boundary

The mathematical core is established finite-dimensional dual-space/operator-system mathematics. State restriction to accessible observables, measurement-restricted distinguishability, operator-system quotients, and tensor products are well-developed topics. Relevant prior art includes restricted-observable quantum information, measurement-restricted distinguishability norms, and operator-system quotient/tensor-product theory. Therefore the present result is a **PDT structural bridge**, not a historical novelty claim.

## PDT consequence

The surviving native-composition target is sharpened:

1. A scalar distinction is generally too compressed to be composition-complete.
2. The exact resource object is naturally a resource-indexed functional/quotient state.
3. A genuinely new PDT law would have to derive a physically privileged resource subspace/operator system and a nontrivial composition/refinement rule from PDT principles, or produce a falsifiable consequence that standard operator-system/statistical theory does not already supply.

This cycle therefore advances target (1) and target (4) structurally, but does not close either as a PDT-native breakthrough.
