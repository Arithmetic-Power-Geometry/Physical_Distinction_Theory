# Cycle 036 — Pairwise cross-product dimension-selection no-go

**Status:** PROVED as a no-go for the stated axiom package; underlying cross-product mathematics IMPORTED/KNOWN; PDT consequence only.

## Question
Can the current Normed Distinction Composition (NDC) route be strengthened using only repeated-input / pairwise cross-product identities so that it selects `n=3` without invoking the Jacobi identity or another genuinely three-input condition?

## Result
No, not for the natural package audited here.

Let `V` be a Euclidean space with a nontrivial bilinear alternating product `x × y` satisfying

1. `<x, x×y>=<y, x×y>=0`,
2. `||x×y||^2 = ||x||^2||y||^2 - <x,y>^2`,
3. `x × (x × y) = <x,y>x - ||x||^2 y`.

The standard cross products in both `R^3` and the imaginary-octonion `R^7` satisfy all three identities. Therefore this pairwise package leaves both dimensions alive and cannot by itself derive `n=3`.

The established vector-cross-product classification already restricts nontrivial Euclidean binary normed cross products to dimensions 3 and 7. The 7D product differs from the 3D product only when additional higher-order structure is probed: in particular the 7D octonionic product fails the Jacobi identity because of nonassociativity, while the 3D product satisfies Jacobi.

Hence the current conditional route has a sharp structural boundary:

`NDC + pairwise repeated-input identities  ==>  n in {3,7}`, not `n=3`.

To remove `n=7`, PDT must derive an independent principle that is sensitive to three independent distinction directions (such as sequential-consistency/Jacobi), or derive a stronger symmetry/composition principle that excludes the octonionic case. Merely adding identities that the 7D normed cross product already shares with the 3D one is circularly ineffective.

## Adversarial checks

- Exact basis-vector audit in `R^3` and `R^7`.
- Random integer-vector tests for alternation, orthogonality, norm identity, and double-cross identity.
- Dimension ledger for `n=1..12`, using the known Brown-Gray/Hurwitz classification only as imported prior art.
- The test does not assume that Jacobi is PDT-native; it records Jacobi only as the known discriminator between the current 3D and 7D models.

## Prior-art boundary

The existence of the 7D cross product, the 3/7 classification, the repeated-input identity, and the failure of Jacobi in the octonionic case are established mathematics. This cycle therefore does **not** claim a new mathematical theorem. Its contribution is a PDT-specific falsification of an entire class of attempted dimension-selection repairs that remain within the same pairwise normed-product structure.

## Classification

- `PROVED`: the stated pairwise package cannot uniquely select `n=3` because an explicit `n=7` model satisfies it.
- `IMPORTED/KNOWN`: cross-product classification and octonionic identities.
- `FALSIFIED`: any claim that NDC plus these pairwise/repeated-input identities alone derives `n=3`.
- `OPEN`: derive a genuinely PDT-native three-input/sequential/composition law that excludes `n=7` without importing Lie/Jacobi structure by assumption.
