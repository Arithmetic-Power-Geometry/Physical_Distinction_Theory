# Cycle 337 — Purity-Preservation Selector Boundary

Date: 2026-09-23
Branch: `pdt-breakthrough-lab-24x7`

## Target attacked

Strongest unresolved PDT-II obligations: (1) PDT-native composition law; (2) non-circular PDT-native `n=3` derivation; (3) same-input PDT/QM prediction gap.

## Candidate principle

**Purity Preservation (PP).** Sequential and parallel compositions of pure transformations are pure.

Question: can PP, interpreted as a distinction-conservation principle, select a unique PDT composition rule, select `n=3`, or force a same-input deviation from ordinary complex quantum theory?

## Exact hypotheses

For each finite system size `n`, consider a convex operational theory with a notion of pure transformation. Assume only:

1. identities are pure;
2. sequential composition of pure transformations is pure;
3. parallel composition of pure transformations is pure.

No tensor rule, state cone, effect cone, Born rule, or dimension is inserted as a hidden hypothesis.

## Counterfamilies

### Classical family

For an `n`-level classical system, deterministic maps are extremal/pure transformations. Composition of deterministic maps is deterministic. The parallel product of deterministic maps is deterministic. Therefore PP holds for every finite `n >= 1`.

### Complex-quantum family

For an `n`-dimensional complex quantum system, take pure channels to include isometric channels `rho -> V rho V^†`. Sequential composition of isometries is an isometry, and the tensor product of isometries is an isometry. Hence this pure subtheory satisfies PP for every finite `n >= 1`. Standard operational reconstructions formulate the stronger general axiom that sequential and parallel compositions of pure transformations remain pure.

These two families have inequivalent state spaces and composite structures but satisfy the same PP statement. Therefore PP cannot determine a unique composition law.

## Smallest decisive counterexample

`n=2` already suffices. A classical bit and a complex qubit both admit purity-preserving sequential and parallel composition, yet their normalized state spaces are respectively a line segment/simplex and a Bloch ball, and their correlated composites are operationally inequivalent.

Thus the implication

`Purity Preservation => unique physical composition`

is false.

Since both counterfamilies exist for every finite `n`, the implication

`Purity Preservation => n=3`

is also false. There is no singularity at `n=3`.

## Dimension stress: n=1..12 and beyond

The constructions above are algebraic and hold for each `n=1,...,12`; no numerical approximation is involved. They extend to arbitrary finite `n`. Higher-dimensional random search is unnecessary for the falsification because an exact all-finite-n counterfamily is stronger.

## Same-input QM discriminator

Complex quantum theory itself satisfies PP. Therefore PP alone cannot logically imply

`P_PDT(O | I,R) != P_QM(O | I,R)`

for identical microscopic input `I` and declared resource window `R`. Any such inequality requires an additional PDT-native axiom that excludes the quantum PP model and independently fixes operational probabilities.

## Prior-art rejection

This principle is not PDT-native novelty. Chiribella and Scandolo explicitly formulate Purity Preservation as the axiom that sequential and parallel compositions of pure transformations yield pure transformations in their operational work on diagonalization and sharp theories with purification (2015/2016). Their framework also shows that purity principles support structures broader than a unique quantum composition. Later work on higher-order interference uses Causality + Purity Preservation + Pure Sharpness + Purification and explicitly notes that these principles do not restrict one to the entire quantum formalism.

Relevant prior art:

- G. Chiribella and C. M. Scandolo, *Operational axioms for diagonalizing states*, EPTCS 195 (2015), arXiv:1506.00380.
- G. Chiribella and C. M. Scandolo, *Entanglement as an axiomatic foundation for statistical mechanics*, arXiv:1608.04459.
- H. Barnum, C. M. Lee, C. M. Scandolo, J. H. Selby, *Ruling out Higher-Order Interference from Purity Principles*, Entropy 19, 253 (2017).

## Surviving strengthened statement

**Theorem (PP underdetermination boundary).** Closure of pure transformations under sequential and parallel composition, without an independently specified PDT-native rule fixing which transformations are pure and how correlated composites are formed, is insufficient to determine a unique finite-dimensional operational theory, a unique tensor/composition law, or a preferred finite dimension.

**Proof.** The classical and complex-quantum all-finite-dimension counterfamilies above satisfy PP but are operationally inequivalent. Existence of two inequivalent models satisfying the same hypotheses refutes uniqueness. Since each family exists for every finite `n`, PP cannot select `n=3`. QED.

## Status ledger

| Claim | Status |
|---|---|
| Purity Preservation as an operational axiom | IMPORTED/KNOWN |
| Classical all-finite-`n` PP counterfamily | PROVED |
| Complex-quantum all-finite-`n` PP counterfamily | PROVED |
| PP implies unique PDT composition | FALSIFIED |
| PP implies `n=3` | FALSIFIED |
| PP implies same-input PDT/QM probability gap | FALSIFIED as an inference |
| PP-underdetermination boundary theorem | PROVED |
| PDT-native selector excluding both counterfamilies | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Consequence for next cycle

Do not spend further cycles trying to derive PDT-II from purity closure alone. A viable selector must constrain **correlated composite distinctions beyond closure of pure processes**, and it must exclude ordinary complex QM if it is to generate a same-input experimental discriminator.