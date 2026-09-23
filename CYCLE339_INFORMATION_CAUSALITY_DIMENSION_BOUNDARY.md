# Cycle 339 — Information-Causality Dimension/Prediction Boundary

Date: 2026-09-23
Branch: `pdt-breakthrough-lab-24x7`

## Targets attacked

PDT-II obligations (1) composition, (2) non-circular `n=3`, and (3) same-input PDT/QM probability gap.

## Candidate principle

**Information Causality (IC).** In the standard random-access-code formulation, if Alice sends `m` classical bits, Bob's total accessible information about Alice's otherwise unknown data is bounded by `m`, even with preshared nonsignalling resources.

## Exact hypotheses

Assume only the operational IC bound in its standard Shannon-information formulation. Do not assume a preferred dimension, PDT tensor product, Born rule, or a PDT-specific information functional.

## Prove-or-falsify result

### 1. IC does not select n=3

Classical finite-dimensional probability theory obeys IC for every finite alphabet size. Complex quantum theory also obeys IC for every finite Hilbert-space dimension. Therefore IC is compatible with systems of dimensions `n=1,2,...,12` and arbitrary finite `n`; in particular, `n=2` is already a decisive counterexample to the implication `IC => n=3`.

This is an exact all-finite-dimension counterfamily, not a numerical failure.

### 2. IC cannot by itself force a PDT/QM same-input probability gap

Ordinary complex quantum theory satisfies IC. Hence IC alone cannot entail

`P_PDT(O|I,R) != P_QM(O|I,R)`

under identical microscopic input `I` and resource window `R`. A discriminator requires an additional PDT-native operational law that excludes at least one ordinary quantum probability assignment.

### 3. Composition claim must be stated narrowly

IC is **not** dismissed as composition-irrelevant. Patra et al., *Phys. Rev. Lett.* 130, 110202 (2023), showed that, assuming quantum local systems, IC rules out both minimal and maximal tensor-product extremes and provides a rationale toward self-dual quantum composite cones. Thus IC genuinely constrains composition.

But this is established prior art and does not supply a PDT-native derivation. More importantly, the fact that both classical and quantum theories obey IC means the principle, without additional local-system hypotheses, does not uniquely determine a universal physical theory or a preferred finite dimension.

## Dimension stress n=1..12

For every `n=1,...,12`:

- finite classical `n`-level theory: IC = satisfied;
- finite complex quantum `n`-level theory: IC = satisfied;
- `n=3` selected by IC: no.

The constructions extend to arbitrary finite `n`, so randomized higher-dimensional tests cannot overturn this counterfamily.

## Information-functional robustness warning

The standard IC success depends on the chosen information measure. Minagawa, Arai and Buscemi, *Entropy* 26, 562 (2024), show that replacing Shannon information by a Renyi measure need not reproduce the Tsirelson bound. Therefore importing an information measure into PDT and then treating the resulting bound as PDT-native would require an independent PDT derivation of that measure.

## Fresh prior-art check

A September 2026 preprint by Gachechiladze and Miklin reports that generalized IC characterizes the quantum correlation set in the simplest two-input/two-output bipartite Bell scenario. This strengthens, rather than weakens, the present boundary: IC is active modern quantum-foundations machinery and cannot be claimed as a PDT-native principle without a genuinely new derivation or consequence.

Relevant prior art:

- M. Pawlowski et al., *Information causality as a physical principle*, Nature 461, 1101–1104 (2009), doi:10.1038/nature08400.
- R. K. Patra et al., *Principle of Information Causality Rationalizes Quantum Composition*, Phys. Rev. Lett. 130, 110202 (2023), doi:10.1103/PhysRevLett.130.110202.
- Y. Minagawa, S. Arai, F. Buscemi, *Bounding Quantum Correlations: The Role of the Shannon Information in the Information Causality Principle*, Entropy 26, 562 (2024), doi:10.3390/e26070562.
- M. Gachechiladze, N. Miklin, *Information Causality Characterizes the Set of Quantum Correlations in the Simplest Bell Scenario*, arXiv:2609.10508 (2026 preprint).

## Surviving theorem

**Theorem (IC dimension/prediction underdetermination).** Standard information causality, without an independently specified PDT-native local state space, correlated-composition rule and probability functional, cannot select `n=3` and cannot imply a same-input deviation from finite-dimensional complex quantum theory.

**Proof.** Complex quantum theory satisfies IC for every finite Hilbert-space dimension, including `n=2` and every `n=1,...,12`. Hence IC cannot imply `n=3`. Since the quantum model itself satisfies the hypothesis, IC cannot logically entail a probability assignment unequal to quantum theory on the same input/resource specification. QED.

## Status ledger

| Claim | Status |
|---|---|
| Standard information causality | IMPORTED/KNOWN |
| IC constrains some candidate quantum composites | IMPORTED/KNOWN |
| IC implies `n=3` | FALSIFIED |
| IC alone implies same-input PDT/QM probability gap | FALSIFIED |
| IC uniquely determines a universal composition without local hypotheses | FALSIFIED by classical/quantum underdetermination |
| IC dimension/prediction underdetermination theorem | PROVED |
| Shannon choice uniquely PDT-native | OPEN |
| PDT-native correlated-composite selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Next attack

Do not recycle information causality as PDT novelty. The next viable route must define a genuinely PDT-native correlated-distinction quantity or resource-refinement law, derive its composition behavior without importing the quantum tensor product, and then test whether it excludes the all-finite-dimensional classical/quantum counterfamilies.