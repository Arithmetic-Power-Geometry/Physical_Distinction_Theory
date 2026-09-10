# Cycle 051 — independent-product distinction composition law

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT operational composition corollary.**  
**DECISIVE FALSIFICATION** of naive scalar additivity and multiplicativity.  
**Not a BREAKTHROUGH CANDIDATE.**

## Hypotheses

Let `(p,q)` be two probability distributions on a finite record alphabet `X`, and `(r,s)` two probability distributions on `Y`. Assume the two records compose independently, so the competing joint laws are `p⊗r` and `q⊗s`. Let

`D(P,Q) = (1/2) sum |P-Q|`

be operational distinction measured by total variation.

## Theorem

Writing `d1=D(p,q)` and `d2=D(r,s)`, the independent composite obeys

`max(d1,d2) <= D(p⊗r,q⊗s) <= d1+d2-d1*d2 = 1-(1-d1)(1-d2)`.

More generally, for independent factors `(P_i,Q_i)`,

`D(⊗_i P_i, ⊗_i Q_i) <= 1 - product_i (1-D(P_i,Q_i))`.

### Proof of the lower bound

Marginalization is a stochastic map. Marginalizing the product pair to either subsystem and applying total-variation data processing gives

`D(p,q) <= D(p⊗r,q⊗s)` and `D(r,s) <= D(p⊗r,q⊗s)`.

Taking the maximum proves the lower bound.

### Proof of the upper bound

For finite probability laws, define overlap `O(P,Q)=sum_z min(P_z,Q_z)=1-D(P,Q)`. For nonnegative `a,b,c,d`,

`min(ab,cd) >= min(a,c) min(b,d)`.

Therefore

`O(p⊗r,q⊗s) >= O(p,q) O(r,s) = (1-d1)(1-d2)`.

Since `D=1-O`,

`D(p⊗r,q⊗s) <= 1-(1-d1)(1-d2)`.

Iteration proves the k-factor result.

## Sharpness

The upper bound is globally sharp. For any `d1,d2 in [0,1]`, choose

`p=(1,0)`, `q=(1-d1,d1)`, `r=(1,0)`, `s=(1-d2,d2)`.

Then the product overlap is exactly `(1-d1)(1-d2)`, hence

`D(p⊗r,q⊗s)=d1+d2-d1*d2`.

The lower bound is also sharp in allowed cases, e.g. when the second factor is identical (`d2=0`), for which the composite distance is exactly `d1`.

## Decisive falsifications

### Naive additivity

The rule `D_AB=D_A+D_B` is false even for independent binary records. With `d1=1/2` and `d2=1/4`, the saturating witness gives

`D_AB = 1/2+1/4-(1/2)(1/4)=5/8`,

not `3/4`.

### Naive multiplicativity

The rule `D_AB=D_A D_B` is also false. If the second factor is identical, `D_B=0`, but tensoring it onto a nonzero first distinction leaves the first distinction unchanged: `D_AB=D_A>0`, not zero.

## PDT consequence

This supplies a defensible operational composition constraint that is native to PDT's distinction quantity once **independent record composition** is declared. It does **not** determine the full physical tensor product, state cone, effect cone, entangled sector, or Hilbert/GPT composite. Those remain open.

A useful complement variable is unresolved overlap `U=1-D`. Under independent composition it satisfies

`U_AB >= U_A U_B`.

Thus independent composition cannot destroy joint overlap faster than the product of local overlaps. Equality is attainable but is not universal.

## Stress tests

The branch audit uses exact rational arithmetic for random finite distributions with local alphabet dimensions `n=1..12`, 200 cases per dimension. It records zero violations of either theorem bound. Additional randomized exact checks at alphabet dimensions 16, 24, 32, 48, 64 and 96 found zero violations in 50 cases per dimension. Degenerate one-point distributions, zero distinction, perfect distinction and upper-bound saturating binary families are covered explicitly by unit tests.

## Prior-art boundary

The mathematics is not claimed novel. Total variation, overlap identities, coupling/data-processing arguments, and product-distribution TV bounds belong to established probability/statistics. Recent work also studies total variation of product measures and emphasizes that TV does not generally tensorize as a simple equality. The PDT contribution here is only the operational interpretation and its use as a kill test for proposed PDT scalar composition laws.

## Surviving obligation

A genuine PDT-native composition breakthrough would have to derive more than these universal independent-record bounds: it must select the physical composite structure or establish a new equality/inequality from specifically PDT hypotheses that survives known GPT/QM alternatives and prior-art review.
