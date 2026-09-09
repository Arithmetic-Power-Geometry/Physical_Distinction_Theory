# Cycle 030 — Normed Distinction Composition + Jacobi Sequential Consistency

## Result

This cycle tests a composition-native route to a dimension filter rather than another generator-counting rule.

Let the irreducible distinction space be a real Euclidean vector space `V = R^n`. Postulate a binary distinction-composition map `x × y` with:

1. **Bilinearity**.
2. **Alternation**: `x × x = 0` (equivalently antisymmetry in characteristic zero).
3. **Orthogonality**: `<x×y,x>=<x×y,y>=0`.
4. **Norm composition**: `||x×y||^2 = ||x||^2 ||y||^2 - <x,y>^2`.
5. **Nontriviality**.

Call these conditions **Normed Distinction Composition (NDC)**.

A classical theorem on Euclidean vector cross products restricts nontrivial binary products with these properties to dimensions 3 and 7 (trivial products occur in 0 and 1 dimensions). Thus NDC alone does **not** derive three dimensions: seven survives.

Now add **Jacobi Sequential Consistency (JSC)**:

`x × (y × z) + y × (z × x) + z × (x × y) = 0`.

The ordinary three-dimensional cross product satisfies Jacobi. The octonionic seven-dimensional cross product does not. With the convention implemented in `pdt_normed_composition_filter.py`, the exact basis witness

`(x,y,z) = (e1,e2,e4)`

gives Jacobiator

`(0,0,0,0,0,0,-3)`.

Therefore, under NDC + JSC,

**n = 3 is the only nontrivial Euclidean dimension.**

## Status

- Mathematical implication NDC -> n in {3,7}: **PROVED / IMPORTED-KNOWN** (classical vector-cross-product classification).
- Explicit 7D Jacobi failure: **PROVED / IMPORTED-KNOWN**.
- PDT statement NDC + JSC -> n=3: **CONDITIONAL**.
- PDT-native derivation of NDC: **OPEN**.
- PDT-native derivation of JSC: **OPEN and decisive**.
- BREAKTHROUGH CANDIDATE: **NO**.

The result must not be advertised as a new mathematical classification. Its possible PDT value is only in deriving the assumptions physically from distinction composition.

## Adversarial checks

The branch implements explicit 3D and 7D products and fixed-seed random stress tests. For 500 trials per explicit dimension:

- n=3 maximum norm-identity residual: `1.4210854715202004e-14`.
- n=3 maximum orthogonality residual: `2.1187942970986815e-15`.
- n=3 maximum Jacobiator norm: `2.6645352591003757e-15`.
- n=7 maximum norm-identity residual: `1.1368683772161603e-13`.
- n=7 maximum orthogonality residual: `9.805605636208159e-15`.
- n=7 maximum Jacobiator norm: `115.5452688752578`.

The n=7 nonzero Jacobi behavior is not inferred from numerics alone: the exact basis witness above already falsifies JSC.

The dimension table n=1..12 records n=3 as the only dimension passing NDC+JSC; n=7 fails JSC and the remaining dimensions fail the known binary normed-cross-product classification. Higher-dimensional checks in unit tests include 16, 24, 32, 64, 128 and 256, but those checks encode the known classification rather than rediscover it numerically.

## Prior art / novelty rejection

Brown and Gray, *Vector Cross Products* (Commentarii Mathematici Helvetici 42, 1967, 222–236) is classical prior art for vector cross-product classification. Darpö (2009), *Vector product algebras*, gives the dimension set 0,1,3,7. The relation of the seven-dimensional product to octonions and its Jacobi failure is also established mathematics.

Accordingly, this cycle rejects any claim that the algebraic theorem itself is PDT novelty.

## Critical next attack

The next cycle should not add another independent axiom merely to retain n=3. It should attempt one of two things:

1. derive JSC from a pre-existing PDT operational principle such as path-independent sequential revelation or closure of infinitesimal distinction updates; or
2. construct a physically coherent PDT model with NDC but non-Jacobi sequential composition, demonstrating that JSC is optional and thereby killing this dimension-selection route.

Until one of these succeeds, the result remains a conditional filter rather than a PDT derivation of physical three-dimensionality.
