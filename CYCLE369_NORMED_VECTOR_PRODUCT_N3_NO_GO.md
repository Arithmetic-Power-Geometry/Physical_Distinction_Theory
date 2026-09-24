# Cycle 369 — Normed vector-product selector: decisive n=3 no-go

## Target attacked
PDT-II targets (1) PDT-native composition and (2) a non-circular derivation of n=3.

## Candidate principle
Let V=R^n carry a positive-definite inner product and suppose physical distinctions admit a bilinear alternating internal product x×y in V satisfying

1. <x×y,x>=<x×y,y>=0;
2. ||x×y||^2=||x||^2||y||^2-<x,y>^2;
3. x×y is nonzero for linearly independent x,y.

This is a tempting PDT selector because in ordinary R^3 it turns two directional distinctions into a third orthogonal distinction without leaving the distinction space.

## Prove-or-falsify result
**FALSIFIED as an n=3 selector.** The classical classification of vector product algebras / normed binary vector cross products permits the nontrivial positive-definite binary product in dimensions 3 and 7 (with trivial dimensions 0 and 1 also appearing in the full classification). Therefore the stated hypotheses do not imply n=3. The smallest higher-dimensional decisive countermodel is n=7, realized by the imaginary octonions.

The n=7 product preserves the same bilinearity, orthogonality and norm/area identity. Hence adding only these metric product axioms cannot remove n=7 without an extra hypothesis.

## Stronger surviving statement
If one additionally requires the product bracket to satisfy the Jacobi identity, n=7 is excluded: the ordinary R^3 cross product is a Lie bracket whereas the octonionic 7D cross product fails Jacobi. This does **not** constitute a PDT-native derivation of n=3: Jacobi is an additional algebraic assumption and importing it merely to eliminate n=7 would be circular unless PDT independently derives why physical distinctions must form such a Lie algebra.

Status of the strengthened route: **CONDITIONAL / OPEN as PDT**, not promoted.

## Dimension audit n=1..12
Under the candidate's nontrivial normed binary vector-product axioms, among n=1..12 only n=3 and n=7 are admissible nontrivially. Thus the audit has two surviving dimensions, not a unique n=3. See `results/cycle369_normed_vector_product_dimension_audit.csv`.

## Composition and prediction consequences
This candidate is an internal binary product on one real vector space; it is not a tensor/composite-system rule. Therefore it does not solve PDT-II target (1). It also supplies no outcome-probability functional and hence cannot yield a same-input numerical P_PDT(O|I,R) != P_QM(O|I,R). Any such inference is unsupported.

## Prior-art boundary
The dimension restriction is classical mathematics, tied to vector product algebras and normed division algebras; it is not PDT novelty. Erik Darpo, *Vector product algebras* (arXiv:0810.5464, 2008) gives an elementary treatment and states dimensions 0,1,3,7. The 7D countermodel is standard octonionic structure.

## Classification
- normed binary vector-product classification: **IMPORTED/KNOWN**
- candidate axioms => n=3: **FALSIFIED** (n=7 countermodel)
- candidate axioms => {3,7} among nontrivial finite positive-definite cases: **IMPORTED/KNOWN**
- + Jacobi eliminates the standard 7D cross product: **IMPORTED/KNOWN / CONDITIONAL as a PDT selector**
- candidate => PDT composition law: **FALSIFIED as an inference**
- candidate => same-input PDT/QM probability deviation: **FALSIFIED as an inference**
- BREAKTHROUGH CANDIDATE: **NO**

## Research consequence
Do not use a cross-product/normed-division-algebra argument as a non-circular PDT derivation of three dimensions. A future selector must independently derive an operational PDT axiom that excludes the n=7 octonionic countermodel rather than stipulating a 3D-specific identity.
