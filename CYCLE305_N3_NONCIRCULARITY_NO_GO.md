# PDT Cycle 305 — Non-circular n=3 selection no-go

## Target
Attack PDT-II target (2): a non-circular PDT-native derivation of `n=3`, while respecting the prove-or-falsify rule.

## Candidate principle tested
Can `n=3` be selected from the presently available generic distinction architecture using only:

1. a finite normalized convex state space;
2. pure states that are mutually permutable by reversible transformations;
3. a distinction functional invariant under those reversible relabellings;
4. closure under independent composition;
5. ordinary coarse-graining/data processing; and
6. no dimension-specific constant, three-outcome postulate, qutrit/Hilbert-space assumption, or experimentally inserted value?

## Result
**FALSIFIED as a derivation of n=3.**

For every integer `n >= 2`, the classical `n`-level simplex

`Delta_(n-1) = { p in R^n : p_i >= 0, sum_i p_i = 1 }`

satisfies all six generic requirements.

### Proof family
For arbitrary `n >= 2`:

- `Delta_(n-1)` is finite-dimensional, normalized and convex.
- Its pure states are the vertices `e_1,...,e_n`.
- The permutation group `S_n` acts reversibly and transitively on those pure states by permutation matrices.
- Any relabelling-invariant classical distinction such as total variation, Hellinger, or a symmetric function of the likelihood-ratio data is invariant under this reversible action.
- Independent systems compose as `p tensor q`, producing the simplex on the Cartesian-product outcome set; associativity is inherited from the ordinary tensor/product distribution construction.
- Stochastic coarse-graining obeys data processing for standard operational distinguishability measures.

Hence the same dimension-free structural assumptions admit `n=2,3,4,...` simultaneously. They therefore cannot logically entail `n=3`.

This is stronger than merely exhibiting `n=4`: there is an infinite model family satisfying the hypotheses. A purported proof of `n=3` from only these assumptions must contain a hidden dimension-selecting premise or an invalid inference.

## Exact n=1..12 stress
`n=1` is the degenerate one-state simplex. For every `n=2..12`, the construction has exactly `n` pure vertices, reversible group `S_n`, affine dimension `n-1`, and product with an `m`-level member gives `nm` pure product vertices. Nothing singular occurs at `n=3` under these hypotheses.

| n | affine dimension | pure vertices | reversible vertex permutations |
|---:|---:|---:|---:|
|1|0|1|1|
|2|1|2|2|
|3|2|3|6|
|4|3|4|24|
|5|4|5|120|
|6|5|6|720|
|7|6|7|5040|
|8|7|8|40320|
|9|8|9|362880|
|10|9|10|3628800|
|11|10|11|39916800|
|12|11|12|479001600|

Higher dimensions continue identically; no randomized test is needed for this counterfamily because it is exact for every finite `n`.

## Composition check
The family is closed under independent composition in the operational sense: `Delta_(n-1) x_tensor Delta_(m-1)` has `nm` deterministic product vertices and is represented by `Delta_(nm-1)` when arbitrary classical joint distributions are admitted. Thus adding ordinary compositional closure does not isolate `n=3` either.

## Edge and degenerate cases
- `n=1`: vacuous distinction; does not select 3.
- `n=2`: fully nondegenerate countermodel to any claim that the axioms require at least 3.
- `n=4`: smallest countermodel above 3 and enough by itself to refute uniqueness.
- arbitrary `n`: exact infinite counterfamily.
- mixed states: already included as convex combinations of vertices.
- restricted resources: restricting stochastic measurements may reduce operational distinction but does not change the existence of the `n`-simplex models unless a new dimension-dependent restriction is separately postulated.

## Prior-art boundary
This construction is standard classical probability/GPT structure, not PDT novelty. Classical finite systems are represented by simplices in generalized probabilistic theories, and GPT frameworks explicitly encompass classical, quantum and more general state spaces. Therefore the simplex family and its permutation symmetries are **IMPORTED/KNOWN**. The result here is a PDT-II no-go audit: the current dimension-free premises do not derive 3.

Relevant prior-art anchors: Barrett, Phys. Rev. A 75, 032304 (2007), on generalized probabilistic theories; Plavala, arXiv:1608.05614 / Phys. Rev. A, on simplex state spaces and compatible measurements; Schmid et al., PRX Quantum 2, 010331 (2021), on simplex structure/embeddability as classicality.

## Consequence for PDT-II
A defensible non-circular `n=3` theorem now requires at least one additional PDT-native premise `H` for which:

1. `H` is independently physically motivated rather than chosen because 3 is desired;
2. `H` holds for the intended PDT `n=3` model;
3. `H` provably fails for every competing `n != 3` model in the admissible class, or combines with other independently justified premises to do so;
4. `H` survives composition/resource/degeneracy checks; and
5. `H` is not merely a disguised statement of three-dimensionality, three outcomes, SU(2)/SO(3), the Bloch sphere, or another imported dimension selector.

Until such an `H` exists, `n=3` must remain an input/model choice rather than a PDT prediction.

## Status ledger
- Generic convexity + reversible pure-state transitivity + relabelling-invariant distinction + ordinary composition/coarse-graining uniquely imply `n=3`: **FALSIFIED**.
- Infinite simplex counterfamily for every finite `n>=2`: **PROVED**.
- Exact stress through `n=1..12`: **PROVED**.
- Extension to arbitrary finite `n`: **PROVED**.
- Classical simplex/GPT machinery: **IMPORTED/KNOWN**.
- Non-circular PDT-native dimension selector: **OPEN**.
- PDT-native composition selector: **OPEN**.
- Fully specified same-input `P_PDT != P_QM`: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Search for an independently motivated PDT-native premise capable of excluding the exact simplex counterfamily without importing `n=3`. In parallel, test whether any proposed capacity/revelation invariant has a dimension-specific extremum at 3 for physical reasons rather than by normalization. If no such premise survives, retain the no-go and move priority to the same-input quantitative-prediction target.