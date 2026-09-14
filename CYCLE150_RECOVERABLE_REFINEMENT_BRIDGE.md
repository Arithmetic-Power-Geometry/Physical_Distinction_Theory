# PDT-II Cycle 150 — Recoverable Refinement Bridge

## Result

This cycle attacks the open bridge left by Cycle 149: whether local equal-subdivision invariance can be obtained from a more operational PDT principle rather than assumed directly.

### Theorem — recoverable free refinement invariance

Let `M` be a scalar operational resource on objects `x`. Assume every admissible/free transformation `T` obeys

`M(Tx) <= M(x)`.

Let `E` be a refinement encoding and `C` a coarse-graining/merge map such that both `E` and `C` are admissible/free and

`C(E(x)) = x`

exactly. Then

`M(E(x)) = M(x)`.

**Proof.** Monotonicity under `E` gives `M(E(x)) <= M(x)`. Monotonicity under `C`, applied to `E(x)`, gives `M(x)=M(C(E(x))) <= M(E(x))`. Therefore equality holds. QED.

Classification: **PROVED**, with the general reversible-free-operation mechanism **IMPORTED/KNOWN** from resource-theory/data-processing mathematics.

## Resolved-share realization

For a nonnegative resolved-share vector `q`, choose component `q_i` and daughter weights `w_j >= 0`, `sum_j w_j=1`. Define the refinement

`q_i -> (q_i w_1, ..., q_i w_k)`.

The deterministic merge that sums those daughters is an exact left inverse. Hence **arbitrary weighted local subdivision**, not merely equal subdivision, is recoverable at the share-vector level.

If PDT independently licenses both maps as admissible/free for the same operational ledger, the theorem gives local subdivision invariance. Cycle 149 then yields additive resolved composition (its equal-subdivision premise is a special case).

Classification of this application: **CONDITIONAL**.

## Why this is not yet a PDT-native proof

Recoverability by itself is insufficient. It would be circular to infer scalar-ledger invariance merely from the existence of a merge map unless the ledger has already been shown to be monotone/invariant under the relevant admissible transformations.

The Cycle-146 counterfunctional

`Phi(q) = (sum_i q_i^2)^2 / (sum_i q_i^3)`

provides an exact witness. For

`q=(1,3)`

and the recoverable weighted split of the second channel with weights `(1/4,3/4)`, one obtains

`q'=(1,3/4,9/4)`

and merging the last two components recovers `(1,3)` exactly. Nevertheless,

`Phi(q)=25/7`,

`Phi(q')=2809/820`,

so

`Phi(q')-Phi(q)=-837/5740 != 0`.

Therefore

**recoverability alone => ledger invariance**

is **FALSIFIED**.

## Exact stress audit

The executable audit covers dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`

with exact rational arithmetic and arbitrary positive rational daughter weights.

- exact random cases: **740**
- exact split/merge recovery failures: **0**
- additive-ledger invariance failures: **0**
- cases in which the Cycle-146 functional changes: **705**
- dedicated regression assertions: **5/5 passed locally**

The numerical/exact audit supports the implementation only; the theorem itself is analytic.

## Prior-art boundary

The abstract mechanism is standard: resource monotones do not increase under free operations, so two objects freely interconvertible in both directions have equal values for every such monotone. This belongs to established quantum/general resource-theory methodology; see Chitambar and Gour, *Quantum resource theories*, Rev. Mod. Phys. 91, 025001 (2019), DOI 10.1103/RevModPhys.91.025001. Distinguishability resource theories likewise treat channels as free transformations and derive monotonicity/conversion structure; see Wang and Wilde, *Resource theory of asymmetric distinguishability*, Phys. Rev. Research 1, 033170 (2019), DOI 10.1103/PhysRevResearch.1.033170.

No novelty is claimed for that mathematical principle.

## Surviving PDT-II obligation

The composition target has been narrowed to one non-circular physical question:

> Can PDT primitives independently establish that the local refinement encoding and its exact merge are both admissible/free transformations for the **same operational resource ledger**?

If yes, Cycle 150 supplies local subdivision invariance and Cycle 149 then fixes additive resolved composition. Until that admissibility/free-operation bridge is derived rather than assumed, the PDT-native composition law remains **OPEN**.

## Status ledger

- Recoverable-monotone invariance theorem: **PROVED**
- Application to PDT resolved composition: **CONDITIONAL**
- Recoverability alone implies ledger invariance: **FALSIFIED**
- Resource-theory/data-processing mechanism: **IMPORTED/KNOWN**
- Exact implementation stress audit: **NUMERICALLY SUPPORTED**
- PDT-native admissibility of both split and merge for the same ledger: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
