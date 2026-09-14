# Cycle 148 — Maximal Uniformization Does Not Imply Schur Monotonicity

## Status

- **PROVED:** the explicit counterfamily below has the stated algebraic properties.
- **FALSIFIED:** endpoint/equal-split calibration plus monotonicity under complete uniformization is enough to imply global Schur monotonicity.
- **IMPORTED/KNOWN:** majorization, Schur monotonicity, doubly stochastic maps, and T-transform characterizations are classical Hardy–Littlewood–Pólya / majorization theory.
- **NUMERICALLY SUPPORTED:** seeded stress tests through dimension 128; numerical checks are regression evidence, not the proof.
- **OPEN:** derive monotonicity under arbitrary *partial* T-transforms from PDT-native refinement/revelation operations.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Candidate bridge under attack

Cycle 147 proved that if a fixed-total PDT resource is globally Schur-monotone and calibrated equally on the maximally concentrated and maximally uniform vectors, the resource is squeezed to the additive ledger. A tempting weakening is:

> perhaps it is enough that the resource never increase under the single maximal coarse-graining that sends a vector to the uniform vector of the same total.

That weakening is false.

## Counterfamily

For a nonnegative finite vector `q`, write

- `S = sum_i q_i`,
- `p_i = q_i / S` when `S>0`,
- `c = sum_i p_i^2`.

For fixed `epsilon>0`, define

```text
F_epsilon(q)
  = S [1 + epsilon c(1-c) sin^2(pi/c)]       (S>0),
  = 0                                         (S=0).
```

### Properties

1. **Permutation symmetry.** `c` depends only on the multiset of shares.
2. **Positive homogeneity.** Scaling `q` by `a>=0` preserves `p,c` and scales `S` by `a`.
3. **Zero-padding stability.** Appending zero coordinates does not change `S` or `c`.
4. **Continuity.** For `S>0` it is elementary continuous; as `S->0`, the bracket is bounded, so `F->0`.
5. **Every equal-support uniform split is calibrated.** If exactly `k` entries are equal and positive, then `c=1/k`, so `sin^2(pi/c)=sin^2(k pi)=0` and `F=S`.
6. **Complete uniformization never increases the resource.** For any `q`, `F(q)>=S`, while its equalized vector has value exactly `S`.

Thus the family survives much more than a single binary/ternary split: it survives all equal-support uniform refinements, continuity, symmetry, homogeneity, and zero-padding stability.

## Smallest decisive majorization chain

In dimension 2,

```text
(1,0)  majorizes  (3/4,1/4)  majorizes  (1/2,1/2).
```

At both endpoints, `F=1`. At the interior point,

```text
c = (3/4)^2 + (1/4)^2 = 5/8,
F = 1 + epsilon (5/8)(3/8) sin^2(8 pi / 5) > 1.
```

Therefore:

- Schur-convexity fails because the more concentrated endpoint `(1,0)` has **smaller** value than `(3/4,1/4)`;
- Schur-concavity fails because `(3/4,1/4)` has **larger** value than the more uniform `(1/2,1/2)`.

So maximal uniformization monotonicity is strictly weaker than global Schur monotonicity.

## Frozen numerical audit

`cycle148_results.json` records the seeded regression run over

```text
n = 1..12, 16, 24, 32, 48, 64, 96, 128.
```

There were 1,320 random cases and zero observed failures of complete-uniformization nonincrease, permutation symmetry, positive homogeneity, or zero-padding stability. Maximum relative floating residual among the equality checks was approximately `6.96e-16`.

These numbers are not evidence for novelty and are not substituted for the analytic counterexample.

## Prior-art boundary

The implication `x majorizes y iff y is obtainable from x by a doubly stochastic transformation` and the associated Schur-convex/Schur-concave framework are classical majorization theory. The PDT question is not whether these mathematical facts are new. The open PDT obligation is whether the physical primitives of distinction/refinement/revelation justify monotonicity under the **full family of partial mixing/T-transform operations**, rather than only under the terminal map to complete uniformity.

## Surviving theorem target

The composition route should now be formulated as:

> If PDT-native operations imply monotonicity under every physically realizable elementary partial mixing that generates the majorization preorder, then Cycle 147's squeeze theorem fixes the additive resolved-resource ledger.

The unresolved part is the physical derivation of that premise without importing entropy, Born/Hilbert structure, or additive accounting itself.
