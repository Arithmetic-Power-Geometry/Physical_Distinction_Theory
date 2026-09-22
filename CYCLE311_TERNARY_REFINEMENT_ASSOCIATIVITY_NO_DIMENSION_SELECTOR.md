# PDT Cycle 311 — Ternary refinement/associativity does not select physical n=3

## Target
Attack the strongest open composition route left by Cycle 310: whether introducing a genuinely ternary/sequential distinction object, together with coarse-graining/refinement consistency and associativity, can non-circularly force a three-way physical structure or uniquely supply PDT-II's composition law.

## Hypotheses
Let `D_n(p_1,...,p_n)` be a permutation-invariant scalar distinction/information assigned to a finite probability vector. Require:

1. continuity on each finite simplex;
2. expansibility: adjoining a zero-probability branch changes nothing;
3. refinement/grouping consistency: splitting branch `p_k` into conditional subbranches `p_k q_1,...,p_k q_m` obeys
   `D(...,p_k q_1,...,p_k q_m,...)=D(...,p_k,...)+p_k D(q_1,...,q_m)`;
4. associativity/coherence: successive refinements give the same value independent of bracketing/order of refinement.

These are deliberately stronger than binary pairwise distinction and directly test the higher-order route proposed after Cycle 310.

## Candidate principle A
`ternary refinement + associativity/coherence` provides a non-circular selector of physical `n=3`.

## Result A
**FALSIFIED.** The axioms are arity-generic. Shannon entropy

`H_n(p) = - sum_i p_i log p_i`

satisfies the refinement identity for every finite `n`, not specifically `n=3`. For a refinement `p_k -> (p_k q_j)_j`, direct algebra gives

`-sum_{i != k} p_i log p_i - sum_j p_k q_j log(p_k q_j)`
`= H_n(p) + p_k H_m(q)`.

Repeated refinement is coherent because multiplication of conditional probabilities and ordinary addition are associative. Thus exactly the same law exists for `n=1,2,3,...`; ternary consistency is merely one instance of an all-arity law.

Therefore ternary refinement cannot be used as a non-circular physical dimension selector unless an additional independently physical premise excludes all other arities.

## Candidate principle B
`ternary refinement + associativity` is by itself a novel PDT-native composition law.

## Result B
**FALSIFIED as a novelty route / IMPORTED-KNOWN in substance.** The grouping/refinement equation is classical information theory. Faddeev-type characterizations use continuity/symmetry plus grouping to characterize Shannon entropy (up to scale under standard regularity assumptions). Modern operadic formulations encode the same all-arity substitution law. General composability/associativity also has a substantial generalized-entropy/formal-group literature. Therefore adopting this law without an independently PDT-derived physical reason would import known information-theoretic composition rather than derive PDT composition.

## Exact dimension stress
- `n=1`: `H_1(1)=0`; degenerate but consistent.
- `n=2`: grouping law holds exactly.
- `n=3`: grouping law holds exactly; nothing singular occurs.
- `n=4,...,12`: same algebra proves exact consistency.
- arbitrary finite `n`: same proof.
- higher dimensions/asymptotics: no numerical search can create an `n=3` selector because an exact all-finite-`n` counterfamily already exists.

## Edge/degenerate cases
Using the standard convention `0 log 0 = 0`, zero branches obey expansibility. Deterministic distributions have zero entropy. Refinements by deterministic conditionals add zero. Hence boundary points do not rescue an `n=3` exception.

## Composite/sequential interpretation
For a joint classical distribution `p(x,y)=p(x) p(y|x)`, the same refinement law becomes the Shannon chain rule

`H(X,Y)=H(X)+sum_x p(x) H(Y|X=x)`.

For three sequential variables, iterating the rule is bracket-independent. This demonstrates composition, but it is ordinary classical conditional composition and therefore cannot be promoted as PDT-native.

## Relation to earlier cycles
- Cycles 300–304 showed that generic additivity/DPI and symmetric scalar repairs do not uniquely select a PDT distinction law.
- Cycle 305 showed generic PDT premises do not select `n=3`.
- Cycles 306–310 showed that affine/binary distinction and even simulation closure do not reconstruct a unique response/measurement theory.
- This cycle closes the immediate higher-order escape hatch: **moving from binary to ternary refinement plus associativity still does not select `n=3`, and its canonical exact realization is already known information theory.**

## Prior-art disposition
**IMPORTED/KNOWN.** Faddeev's grouping axiom and Shannon/Khinchin-style characterizations predate PDT. Operadic formulations make the all-arity substitution/refinement structure explicit. Generalized entropy work also studies symmetric associative composability beyond ordinary addition. Hence neither refinement coherence nor abstract associative composability should be claimed as PDT novelty.

## Status ledger
- ternary refinement + associativity => physical `n=3`: **FALSIFIED**.
- exact all-finite-`n` Shannon counterfamily: **PROVED / IMPORTED-KNOWN**.
- refinement identity for `n=1..12`: **PROVED** algebraically.
- arbitrary finite-`n` persistence: **PROVED**.
- ternary grouping as PDT novelty: **FALSIFIED / IMPORTED-KNOWN**.
- PDT-native reason for a particular refinement weight or non-Shannon higher-order object: **OPEN**.
- PDT-native composition law: **OPEN**.
- non-circular PDT-native `n=3` derivation: **OPEN**.
- parameter-free same-input `P_PDT != P_QM`: **OPEN**.
- experimentally distinctive PDT inequality: **OPEN**.
- gravity/capacity law: **OPEN; DO NOT IMPORT**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Do not add further arity-only axioms. The next useful attack is a resource-sensitive refinement law: define distinction relative to an explicitly declared admissible resource set `R`, then prove-or-falsify whether refinement `R subseteq R'` gives a monotone revelation law with a quantitatively constrained increment. Immediately compare any surviving law against standard statistical experiments, Blackwell order, resource theories, accessible information and data-processing results. Only a residual statement not reducible to those frameworks can count as PDT-native.