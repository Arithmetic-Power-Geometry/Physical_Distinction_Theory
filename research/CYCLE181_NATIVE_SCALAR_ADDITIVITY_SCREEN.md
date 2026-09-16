# Cycle 181 — PDT-native scalar additivity screen

## Question
Can a non-probabilistic scalar already native to finite distinction structure satisfy the additive splitting law needed in Cycle 180, thereby fixing the response exponent alpha=1 without importing a measure?

## Classification
- Finite quotient cardinality under genuine disjoint union: **PROVED / IMPORTED-KNOWN**.
- Log-cardinality (Hartley capacity) under disjoint refinement: **FALSIFIED**.
- Orbit size under disjoint refinement: **FALSIFIED**.
- Linear-algebraic rank: **CONDITIONAL / REPRESENTATION-DEPENDENT**, hence not native to a bare quotient.
- Generic distinguishability radius: **FALSIFIED** as an exact additive refinement scalar.
- Unique PDT-native probability selector from these candidates: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## 1. Cardinality survives, but only as counting measure
Let Q=A ⊔ B be a genuine disjoint union of finite distinction classes. Then

|Q| = |A| + |B|.

This is exact for every finite size, hence in particular n=1,...,12. If Cycle 180 uses s(A)=|A|, normalization gives

P(A)=|A|/|Q|.

This is the ordinary normalized counting measure (uniform measure on elementary classes). It is rigorous but not a new PDT probability principle: cardinality on finite sets is the standard counting measure. It therefore cannot by itself provide a preparation-dependent n=3 law or a same-input deviation from QM.

## 2. Hartley/log-cardinality fails the required disjoint additivity
For H0(A)=log |A|, disjoint union requires, if it were additive,

log(|A|+|B|) = log|A| + log|B|.

Smallest nondegenerate witness: |A|=|B|=1. Then H0(A⊔B)=log 2 while H0(A)+H0(B)=0. Thus exact disjoint-refinement additivity is false.

Important distinction: log-cardinality is additive for Cartesian products, because log|A×B|=log|A|+log|B|. That is a composition law for independent product alternatives, not the splitting law required by Cycle 180.

## 3. Orbit size fails under disjoint union
Take two singleton components A={a}, B={b} with no retained tag distinguishing their origin after union. Each singleton has automorphism-orbit size 1. The unlabeled two-point union has automorphism group S2, so the orbit of a has size 2. Hence orbit-size(A⊔B)=2 while orbit-size(A)+orbit-size(B)=2 only accidentally at the whole-set level; per-class orbit weights change from 1 to 2 and do not define a refinement-consistent additive set function. With tagged components the orbit remains 1, showing dependence on extra structure. Therefore orbit size is not a canonical additive scalar of the bare quotient/refinement operation.

## 4. Rank is additive only after importing linear representation
For vector spaces V,W, dim(V⊕W)=dim V+dim W. But a finite distinction quotient has no canonical vector-space structure, field, or embedding. The same finite quotient can be represented in different ambient dimensions. Therefore rank/dimension can be useful only after explicit representation hypotheses; it cannot close the non-circular PDT-native probability derivation from bare distinctions.

## 5. Metric radius is not disjoint additive
For a diameter/radius-based distinguishability scalar, disjoint union depends on the cross-component metric. Two singleton components each have diameter 0, while their union can have any positive diameter d allowed by the chosen metric. Thus no exact additive law follows from the components alone. This is a smallest two-point counterexample.

## 6. Theorem boundary
Among the screened bare finite-quotient candidates, cardinality is the only canonical scalar here that obeys genuine disjoint-union additivity without extra geometric/algebraic data. But this survivor is exactly counting measure. Consequently the Cycle-180 route does not yet yield a new physical probability law:

bare finite distinctions + disjoint additivity -> counting weights -> uniform distribution on elementary classes.

Any nonuniform preparation-dependent prediction still requires additional independently physical structure plus a justified map from that structure to additive weights.

## 7. Implications for PDT-II targets
1. Composition: distinguish two operations sharply — disjoint refinement uses + on cardinalities, independent Cartesian composition uses × on cardinalities and + on log-cardinality.
2. n=3 derivation: bare three-class counting gives only (1/3,1/3,1/3); generic qutrit statistics remain underived.
3. Same-input PDT != QM: not obtained. Choosing non-counting weights would add a new law that must itself be derived/tested.
4. Refinement/revelation: cardinality has exact finite additivity for disjoint alternatives; log-cardinality does not.
5. Experimental inequality: none promoted from this cycle.
6. Gravity/capacity: no dimensional physical bridge is derived; do not infer gravity from counting/log-counting alone.

## 8. Stress-test scope
The companion test enumerates n=1,...,12 for cardinality disjoint-additivity and Cartesian multiplicativity, and checks explicit counterexamples for log-cardinality. The proofs above cover all finite n; numerical checks are regression guards, not evidence replacing proof.

## Prior-art boundary
Counting cardinality is the standard counting measure; finite/countable additivity is measure-theoretic prior art. Hartley information is log-cardinality and is standard information theory. Linear dimension additivity under direct sum is standard linear algebra. No novelty claim is made for these facts.
