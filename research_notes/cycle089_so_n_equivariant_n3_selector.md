# Cycle 089 — Conditional SO(n)-equivariant selector for n=3

## Status

- **CONDITIONAL**: exact theorem under stated hypotheses.
- **IMPORTED/KNOWN**: mathematical mechanism belongs to classical invariant theory / vector-product representation theory.
- **NUMERICALLY SUPPORTED**: SO(3) covariance regression and dimension sweep.
- **OPEN**: PDT-native derivation of the selecting hypotheses.
- **NOT BREAKTHROUGH CANDIDATE**.

## Candidate principle

Let the elementary distinction space be a real Euclidean vector space `V = R^n`. Assume:

1. **Full reversible isotropy.** Every orientation-preserving orthogonal change of distinction coordinates, `R in SO(n)`, is an allowed reversible symmetry.
2. **Alternating binary closure.** There exists a nonzero bilinear alternating operation `B: V x V -> V` that composes two elementary distinction directions into an elementary distinction direction.
3. **Covariance.** `B(Rx,Ry)=R B(x,y)` for all `R in SO(n)`.

Then `n=3`.

## Proof

Use the Euclidean inner product to associate to `B` the alternating 3-form

`T(x,y,z)=<B(x,y),z>`.

Covariance of `B` and orthogonality of `R` imply that `T` is `SO(n)`-invariant.

For `n>3`, take any coefficient `T(e_i,e_j,e_k)` with distinct indices. Choose an unused index `l`. The rotation by pi in the `(k,l)` plane belongs to `SO(n)`, fixes `e_i,e_j`, and sends `e_k` to `-e_k`. Invariance therefore gives

`T(e_i,e_j,e_k) = -T(e_i,e_j,e_k)`,

so every coefficient vanishes. Hence `T=0` and therefore `B=0`, contradicting nonzero closure.

For `n=2`, `Lambda^2 V` is one-dimensional and is fixed by every `SO(2)` rotation, whereas the standard two-dimensional representation has no nonzero vector fixed by all rotations. Hence every equivariant map `Lambda^2 V -> V` is zero. For `n=1`, alternation is zero trivially.

For `n=3`, the oriented volume form is `SO(3)`-invariant and induces the usual cross product via the metric, giving a nonzero equivariant alternating bilinear operation. Thus `n=3` is the unique positive dimension satisfying the three assumptions.

## Counterexample / boundary search

The theorem does **not** survive weakening the symmetry assumption from full `SO(n)` to an arbitrary proper reversible subgroup. In dimension 7, the octonionic cross product is preserved by `G2`, a proper subgroup of `SO(7)`. Thus `n=7` is an immediate boundary witness against any claim based only on 'some transitive/reversible symmetry group plus cross-product-like closure'.

Accordingly, PDT cannot claim a native derivation of 3 unless it independently derives why the elementary reversible group is the full `SO(n)` (or an equivalently strong symmetry condition), rather than selecting that condition because it yields 3.

## Stress audit

Exact component-killing logic was applied for `n=1..12` and `n=16,24,32,48,64,96,128`. Only `n=3` has a nonzero equivariant-map dimension. For `n>3`, all `C(n,3)` candidate 3-form coefficients are killed by explicit determinant-+1 pi rotations. A 500-trial random SO(3) covariance regression for the ordinary cross product gave maximum floating residual `4.3059624662327e-15`.

## Prior-art boundary

This is not new mathematics. Brown–Gray-type vector cross-product classification is established prior art: metric two-fold vector cross products can exist in dimensions 3 and 7. The stronger full-`SO(n)` covariance used here removes the 7-dimensional case because the 7D cross product is preserved by `G2`, not all of `SO(7)`. In three dimensions, the Hodge dual maps bivectors to vectors, producing the ordinary cross product.

## PDT consequence

Cycle 088 showed tensor composition alone cannot select elementary dimension 3. Cycle 089 supplies an exact non-circular **conditional selector**: if PDT independently derives full reversible isotropy and a nonzero alternating binary elementary closure, then 3 follows rather than being assumed. The missing step is therefore sharply localized: derive those hypotheses from PDT's primitive operational/resource postulates without importing three-dimensional geometry.
