# Cycle 182 — Local distinction data do not fix a unique composite

## Status

- Claim that subsystem distinction structures plus independent product tests uniquely determine a PDT composite: **FALSIFIED**.
- Surviving product-cardinality law for explicitly independent elementary alternatives: **PROVED (finite sets), IMPORTED/KNOWN**.
- Claim that this product law uniquely determines the full composite event/test structure: **FALSIFIED**.
- PDT-native composition law beyond the product substructure: **OPEN**.
- Breakthrough candidate: **NO**.

## Exact hypotheses attacked

Let A and B be finite operational distinction systems. Assume only:

1. every local test of A and B remains available in the composite;
2. independently performed local tests have joint elementary records `(a,b)`;
3. relabelings of A and B induce relabelings of those product records;
4. for a fixed pair of independent finite tests, elementary record count multiplies.

The tempting inference is that these requirements uniquely determine the full PDT composite.

## Theorem 182.1 — product record count

For finite independent elementary record sets A and B, the Cartesian product has

`|A x B| = |A||B|`.

Consequently Hartley capacity satisfies

`H0(A x B)=H0(A)+H0(B)`

when `H0(X)=log |X|`.

This is elementary finite-set/information theory and is not claimed as PDT novelty.

## Proposition 182.2 — local product data underdetermine the full composite

The hypotheses above specify a product **substructure**, not a unique full composite.

### Smallest explicit construction

Take two binary local tests

`A={a0,a1}`, `B={b0,b1}`.

Their independent product test has four records

`P={(a0,b0),(a0,b1),(a1,b0),(a1,b1)}`.

Define composite C_min to contain only the local/product test structure required by the hypotheses.

Define C_plus to contain exactly the same required local/product structure and additionally admit a genuinely global test/effect G that is not identified with any required product test/effect (for example, an extra global binary test `{g0,g1}` with its own operational outcomes, subject to whatever consistency axioms a future PDT composite definition imposes).

The local restrictions and the independent product records are identical in C_min and C_plus, while the full composite structures differ. Therefore local distinction data and product-cardinality constraints alone cannot select a unique full composite.

This is a logical underdetermination result: any uniqueness theorem must add a closure/maximality/minimality/no-signalling/tomographic/dynamical principle strong enough to decide which global tests/effects exist.

## Adversarial checks

### n=1 through n=12

For local record counts m,n in 1..12, product cardinality is exactly `mn`; associativity of record sets holds up to canonical bijection:

`(A x B) x C ~= A x (B x C)`.

These checks establish only the elementary independent-record layer. They do not constrain additional global tests/effects.

### Degenerate cases

If one factor is a singleton, `|A x {e}|=|A|`. This still does not imply that a full composite with an operationally trivial ancilla has no additional global structure unless an explicit ancilla-invariance axiom is imposed.

### Reversible groups

Local permutation groups act componentwise on product records. Covariance under this action does not forbid adding global tests in whole group orbits, so covariance does not restore uniqueness.

### Alternative composition rules

Minimal closure under required product tests and larger closures containing additional global tests agree on all stipulated local/product observations. Hence the hypotheses cannot distinguish them.

### Pure/mixed and dynamical cases

No state-space, convex, Markovian, non-Markovian, thermodynamic, or environment-record assumption was used. Therefore those structures cannot be inferred from this theorem; importing one may select a composite but must be declared as an additional physical axiom.

## Prior-art boundary

Operational/test-space and quantum-logical literature already treats composition as nontrivial. Foulis–Randall style products encode product/sequential tests and no-signalling constraints; broader composite test spaces can contain non-product measurements. Quantum theory likewise uses tensor-product state spaces and permits entangled/non-product states. Therefore the general observation that local systems do not by themselves fix all global composite structure is **IMPORTED/KNOWN**, not PDT novelty.

Relevant prior art to cite in PDT-II before any novelty claim:

- D. J. Foulis and C. H. Randall, empirical logic / tensor-product work.
- A. Acin, T. Fritz, A. Leverrier, A. B. Sainz, combinatorial approaches to nonlocality/contextuality and multipartite composition.
- General operational/GPT literature on minimal/maximal composites and local tomography.

## Consequence for PDT-II targets

### (1) PDT-native composition law

**OPEN.** Cartesian product is justified for explicitly independent elementary records, but it is not a derivation of the full composite. PDT must independently specify which global distinctions/tests/states/dynamics are admitted.

### (2) non-circular n=3 derivation

No advance. A ternary product/counting construction supplies combinatorics, not a preparation-dependent probability law.

### (3) same-input PDT != QM prediction

No advance. Choosing a different composite closure by hand would be an imported model choice, not a PDT prediction.

### (4) refinement/revelation/conservation

The result sharpens the boundary: additive disjoint refinement and multiplicative independent composition are different operations. Neither determines the allowed global composite closure.

### (5) experimentally distinctive inequalities

Premature until PDT fixes the admissible composite state/effect/test set. Bell/contextual inequalities depend precisely on those structural choices.

### (6) gravity/capacity

No derivation. Product-cardinality/Hartley additivity alone does not imply a gravitational law.

## Smallest decisive counterexample catalogue entry

**ID:** PDT-COMP-UNDERDET-2x2

**Local systems:** two binary tests.

**Shared data:** identical local tests and identical four product records.

**Model 1:** minimal composite closure.

**Model 2:** same closure plus at least one additional globally defined test/effect consistent with the eventual declared operational axioms.

**Decision:** local/product distinction data do not uniquely fix the full composite.

## Next prove-or-falsify target

Test candidate PDT closure principles one at a time: minimal closure, maximal consistency closure, no-signalling closure, local tomography, purification-like closure, and resource-bounded closure. For each, determine whether it is (a) derivable from PDT primitives, (b) known/imported, (c) inconsistent, or (d) still leaves multiple composites. Do not use a chosen closure to manufacture a PDT-vs-QM prediction.
