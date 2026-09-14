# Cycle 149 — Local Equal-Subdivision Selects the Additive Ledger

## Status

- **PROVED:** under the exact hypotheses below, local equal subdivision of any single resolved channel forces the full additive ledger.
- **FALSIFIED:** Cycle 146's continuous, symmetric, homogeneous, zero-padding-stable, uniform-refinement and tensor-multiplicative counterfamily can survive local equal subdivision. It cannot.
- **IMPORTED/KNOWN:** the proof mechanism uses standard density of rational points plus continuity; branching/refinement axioms have a substantial prior literature in information theory.
- **NUMERICALLY SUPPORTED:** exact-rational regression tests through dimension 128 support the implementation.
- **OPEN:** derive local equal-subdivision invariance from PDT-native physical primitives without importing additive accounting.
- **BREAKTHROUGH CANDIDATE:** **NO**. The selector theorem is strong, but its PDT-native physical premise is not yet derived.

## Theorem

Let `F` be a real-valued resource functional on all finite nonnegative vectors. Assume:

1. **Permutation symmetry:** reordering resolved channels leaves `F` unchanged.
2. **Zero-padding compatibility and continuity:** `F(q,0)=F(q)`, and `F` is continuous on every fixed finite-dimensional nonnegative orthant.
3. **Local equal-subdivision invariance:** for every component `x>=0` and integer `k>=2`, replacing that one component by `k` copies of `x/k` leaves `F` unchanged.
4. **Singleton calibration:** `F((S))=S` for every `S>=0`.

Then for every finite nonnegative vector `q=(q_1,...,q_n)`,

```text
F(q) = q_1 + ... + q_n.
```

No global Schur-monotonicity, arbitrary unequal split axiom, tensor multiplicativity, differentiability, or entropy assumption is required.

## Proof

Fix `q` with total `S=sum_i q_i`.

### Rational proportions

Suppose first that every `q_i/S` is rational (the `S=0` case is immediate). Choose a common denominator `M` and nonnegative integers `m_i` with

```text
q_i = (m_i/M) S,     sum_i m_i = M.
```

For each nonzero component `q_i`, apply local equal-subdivision invariance with multiplicity `m_i`. This replaces `q_i` by `m_i` copies of

```text
q_i/m_i = S/M.
```

After performing this operation for all components, the resulting vector consists of exactly `M` equal entries `S/M`, up to zero entries and ordering. By symmetry and zero-padding compatibility,

```text
F(q) = F(S/M,...,S/M).
```

But applying local equal subdivision once to the calibrated singleton `(S)` with multiplicity `M` gives

```text
F((S)) = F(S/M,...,S/M).
```

Therefore `F(q)=F((S))=S` for every rational-proportion vector.

### Arbitrary proportions

Rational points are dense in each fixed-total simplex. Approximate an arbitrary `q` by nonnegative rational-proportion vectors `q^(r)` with the same total `S`. The rational case gives `F(q^(r))=S` for all `r`. Continuity then yields

```text
F(q)=S=sum_i q_i.
```

This proves the theorem.

## Why this is stronger than Cycles 142–148

The earlier routes either assumed conservation for selected global equal splits, arbitrary unequal splits, or global majorization monotonicity. The present selector needs only a **local operation**: any one already-resolved channel may be replaced by equally weighted subchannels without changing the total resource. Repeating this local rule rationally refines an arbitrary composition to a common atom size; continuity closes the irrational boundary.

## Decisive attack on the Cycle 146 counterfamily

Cycle 146 used

```text
Phi(q) = (sum_i q_i^2)^2 / (sum_i q_i^3).
```

It survives continuity, symmetry, positive homogeneity, zero-padding, all global uniform refinements, and tensor-product multiplicativity. But it fails the new local rule already for

```text
q = (1,3).
```

Before refinement,

```text
Phi(1,3) = 25/7.
```

Split only the second channel equally into two daughters:

```text
(1,3) -> (1,3/2,3/2).
```

Then

```text
Phi(1,3/2,3/2) = 121/31,
```

and the exact change is

```text
121/31 - 25/7 = 72/217 != 0.
```

So this strongest previous counterfamily is decisively excluded.

## Frozen exact audit

`cycle149_results.json` records exact-rational tests across

```text
n = 1..12, 16, 24, 32, 48, 64, 96, 128.
```

Results:

- exact local-split cases: **740**;
- additive-ledger split failures: **0**;
- maximum exact arithmetic error: **0**;
- Cycle-146 counterfamily changed under the tested nonzero local splits in **648** cases.

The analytic proof, not the random audit, establishes the theorem.

## Prior-art boundary

The mathematical ingredients are not claimed as novel. Density/continuity arguments are elementary analysis, while branching and refinement axioms are well established in axiomatic information theory. In particular, entropy characterization literature studies continuity together with branching or recursive decomposition rules. The PDT-specific research question is narrower: whether the physical meaning of a resolved distinction makes **local equal subdivision operationally neutral** without silently presupposing additive resource accounting.

## Surviving PDT-II obligation

The strongest target for the next cycle is now:

> Derive or falsify local equal-subdivision invariance directly from PDT-native distinction/refinement/revelation primitives.

If this premise is physically derived, the resolved composition law follows from the theorem above. Until that bridge exists, the result remains a conditional selector rather than a PDT breakthrough.
