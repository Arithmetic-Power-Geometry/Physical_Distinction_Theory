# Cycle 316 — Associative/functorial composition still does not select a PDT composite law

## Target
Strengthen Cycle 315 by testing whether the ambiguity between product-compatible composite distinction laws disappears after adding the most natural coherence axioms: associativity, permutation symmetry, and functorial contraction under local maps.

## Hypotheses tested
Let each finite-dimensional real normed distinction space X be assigned a norm on algebraic composites X⊗Y such that:

1. **Crossnorm/product exactness:** α(x⊗y)=||x|| ||y|| for all simple tensors.
2. **Associative coherence:** iterated composition is canonically isometric under (X⊗Y)⊗Z ≅ X⊗(Y⊗Z).
3. **Permutation symmetry:** swapping factors is an isometry.
4. **Local contraction functoriality:** if ||A||≤1 and ||B||≤1 then ||A⊗B||≤1.

Question: do these conditions uniquely determine α, and hence provide a PDT-native composition law?

## Decisive counterfamily
They do not. The classical injective tensor norm ε and projective tensor norm π are distinct standard uniform crossnorm constructions. Both satisfy product exactness and the local-map metric mapping property; their standard tensor-product constructions are associative and symmetric up to the canonical tensor identifications.

Take X=Y=R^d with Euclidean norm and identify X⊗Y with d×d matrices. Then:

- ε is the spectral/operator norm;
- π is the nuclear/trace norm.

For every simple tensor xy^T both equal ||x||_2||y||_2, so all product distinctions agree exactly. For the correlated tensor

Z_d = Σ_{i=1}^d e_i⊗e_i = I_d,

we have exactly

ε(Z_d)=1,    π(Z_d)=d.

Thus the stronger coherent axioms still permit two different composite predictions. The smallest decisive witness is d=2: 1 versus 2. The separation is d-fold and therefore grows with dimension.

## Exact/numerical stress
For d=1,...,12, singular-value evaluation of I_d gives operator norm 1 and nuclear norm d. Edge case d=1 agrees, as it must; every nontrivial d≥2 separates. The formula proves the result for arbitrary finite d, while the numerical suite is only a regression check.

## Consequences for PDT-II
The following implication is false:

> product exactness + associativity + symmetry + local contraction functoriality ⇒ unique composite distinction law.

Therefore these coherence principles cannot by themselves derive n=3, a same-input PDT/QM deviation, or a distinctive experimental inequality. A surviving PDT-native selector must constrain genuinely correlated tensors beyond the standard uniform-crossnorm axioms, or derive a state/effect/cone structure that does so independently.

## Prior-art audit
This mechanism is not claimed as PDT novelty. Injective/projective tensor norms, reasonable/uniform crossnorms, their extremal relation ε≤α≤π, and applications of projective/cross norms in quantum information are established tensor-norm literature. This cycle is a no-go result for a PDT derivation route.

## Status ledger
- Product exactness uniquely determines composite distinction: **FALSIFIED** (Cycle 315).
- Product exactness + associativity + symmetry + local contraction functoriality uniquely determines composite distinction: **FALSIFIED**.
- d=2 smallest correlated witness within this family: **PROVED**.
- d=1,...,12 stress: **NUMERICALLY SUPPORTED**, with exact formula **PROVED** for all finite d.
- Injective/projective tensor-norm machinery: **IMPORTED/KNOWN**.
- PDT-native correlated-tensor selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input parameter-free PDT/QM deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Search for a PDT-native correlated-composite axiom that is not merely a known tensor-norm/GPT selector. Every candidate must first be checked against ε/π and other admissible tensor norms before promotion.
