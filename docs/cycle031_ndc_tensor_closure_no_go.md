# Cycle 031 — Tensor-Closure No-Go for Universal Normed Distinction Composition

## Decisive falsification

Cycle 030 introduced **Normed Distinction Composition (NDC)** on a real Euclidean distinction space `V = R^n`: a nontrivial bilinear alternating vector-valued product that is orthogonal to both inputs and obeys the area/norm identity

`||x × y||^2 = ||x||^2 ||y||^2 - <x,y>^2`.

Classical vector-cross-product theory restricts such nontrivial binary products to dimensions `n = 3` and `n = 7`.

This cycle asks whether the same NDC axiom can be imposed **universally on composites** under the ordinary tensor-product rule

`dim(V ⊗ W) = dim(V) dim(W)`.

It cannot.

If a nontrivial NDC system has dimension `n`, then `n` is either 3 or 7. Its tensor square has dimension `n^2`. But

- `3 × 3 = 9`,
- `3 × 7 = 21`,
- `7 × 7 = 49`,

and none of `9, 21, 49` belongs to the nontrivial NDC dimension set `{3,7}`.

Therefore no nontrivial finite-dimensional family satisfying NDC can be closed under ordinary tensor composition while requiring the composite distinction space itself to satisfy the same binary NDC axiom.

Formally, if `A = {3,7}` is the nontrivial admissible dimension set, then for every `n in A`, `n^2 notin A`. Hence there is no nonempty multiplicatively closed subset of `A`.

## What is falsified

The statement

> Every physical distinction space, including every standard tensor-product composite, carries the same nontrivial NDC product.

is **FALSIFIED**.

This does **not** falsify the classical single-system implication `NDC + JSC -> n=3`. It changes its interpretation: Cycle 030 can only be an irreducible/single-system conditional dimension filter unless PDT provides a different composite rule or a factor-relative/graded product that does not require the whole composite vector space to be another NDC space of the same type.

## Why this matters for a PDT-native n=3 derivation

A physically credible dimension-selection principle should coexist with composition. A principle that selects `n=3` locally but becomes mathematically impossible on the tensor square of the selected system cannot serve as a universal compositional axiom without additional structure.

So the current NDC route has a sharper research fork:

1. **Irreducible-only NDC:** define NDC only on primitive distinction sectors and provide an independently motivated composition law for composites; or
2. **Alternative composition:** derive a PDT-native composite construction whose operational dimension need not be the ordinary vector-space product; or
3. **Abandon universal NDC:** if neither repair is independently justified, universal NDC must remain rejected.

A repair must not be chosen merely to preserve `n=3`; it must have an operational derivation and survive same-input comparison with quantum/GPT composition.

## Edge and higher-dimensional checks

The exact self-tensor audit is recorded for `n=1..12`. The only local nontrivial NDC dimensions in this range are 3 and 7, and both fail universal NDC on their self-tensor dimensions 9 and 49. The same obstruction is analytic and therefore does not weaken at higher dimension.

The accompanying tests also check all tensor dimension products for `1..12`, explicit witnesses `(3,3)->9`, `(3,7)->21`, `(7,7)->49`, and representative higher dimensions.

## Prior art / novelty

The ingredients are standard mathematics:

- the nontrivial Euclidean binary vector-cross-product dimensions are 3 and 7 (Brown–Gray classification and equivalent composition-algebra results);
- finite-dimensional tensor products multiply vector-space dimensions.

Accordingly, this cycle makes **no novelty claim** for those ingredients. The contribution here is a PDT audit conclusion: universal NDC is incompatible with standard tensor closure and therefore cannot presently be used as a universal PDT composition principle.

## Status

- Tensor-closure no-go under stated assumptions: **PROVED**.
- Universal-NDC interpretation of Cycle 030: **FALSIFIED**.
- Mathematical ingredients: **IMPORTED/KNOWN**.
- Irreducible-only NDC: **CONDITIONAL / OPEN as a PDT principle**.
- PDT-native replacement composition law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.
