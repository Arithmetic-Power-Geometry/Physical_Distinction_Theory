# Cycle 125 — Hurwitz norm-composition no-go for an n=3 route

## Target attacked

PDT-II target (2): a non-circular PDT-native derivation of `n=3`, with direct consequences for target (1), the PDT-native composition law.

## Candidate principle

A tempting strengthening of the Cycle 124 same-sector bilinear route is to require a finite-dimensional real vector space `V` with:

1. a bilinear same-sector product `*: V x V -> V`;
2. a two-sided identity `1`;
3. a positive-definite Euclidean norm;
4. exact norm composition

   `||x*y|| = ||x|| ||y||` for all `x,y`.

This looks physically attractive if the norm is interpreted as an exactly multiplicative distinction/resource magnitude.

## Decisive result

**FALSIFIED as an n=3 selector.**

By the classical Hurwitz theorem on real composition algebras, a finite-dimensional real unital algebra with a nondegenerate positive-definite multiplicative quadratic norm can only have dimension

`1, 2, 4, 8`.

Thus the candidate does not merely fail to select `n=3`; under these hypotheses it excludes `n=3`.

The standard witnesses are the real numbers, complex numbers, quaternions and octonions. The smallest counterdirection is already dimension 1: `R` satisfies all candidate axioms.

## Why this matters for PDT

Cycle 124 found the known conditional selector

`nonzero SO(n)-equivariant bilinear map V x V -> V  =>  n=3` for nontrivial `n>=2`.

Cycle 125 shows that adding a unit and exact multiplicativity of the Euclidean norm is the wrong strengthening. It changes the structural problem from the three-dimensional cross-product/intertwiner setting into the Hurwitz composition-algebra setting, whose distinguished dimensions are `1,2,4,8`.

Therefore a viable PDT-native `n=3` derivation should not quietly import the axioms of a positive-definite unital normed composition algebra. If PDT retains the Cycle 124 route, the relevant product must instead be non-unital/area-like (as the 3D cross product is), or PDT must derive a genuinely different physical composition principle.

## Exact and numerical audit

The executable audit records the exact Hurwitz dimension filter over

`n=1..12,16,24,32,48,64,96,128`.

It also constructs the standard Cayley-Dickson products in dimensions `1,2,4,8` and checks:

- basis products and the two-sided identity;
- zero edge cases;
- squared-norm multiplicativity;
- 500 deterministic random product tests in each allowed dimension.

Frozen run: 2,000 random product tests total, zero failures at relative tolerance `1e-12`; maximum observed floating relative error was below `6e-16`. These numerical checks are regression evidence only; the dimension restriction itself is imported classical mathematics.

## Prior-art boundary

This is not claimed as a new mathematical theorem. Relevant prior art includes:

- Bruce W. Westbury, *Hurwitz' theorem on composition algebras*, arXiv:1011.6197. The paper explicitly presents Hurwitz's theorem that composition-algebra dimension is among `0,1,2,4,8`.
- Z. Li, Y. Nakatsukasa, T. Soma, and A. Uschmajew, *On orthogonal tensors and best rank-one approximation ratio*, arXiv:1707.02569, which relates real orthogonal tensors to the Hurwitz composition problem and notes the `1,2,4,8` restriction.
- Standard real division-algebra classifications (R, C, H, O) provide the familiar positive-definite examples.

The PDT contribution of this cycle is only the **no-go boundary**: exact positive-definite unital norm composition must not be advertised as a route to PDT-native three-dimensionality.

## Status

- Hurwitz dimension restriction: **IMPORTED/KNOWN**.
- Candidate as an `n=3` selector: **FALSIFIED**.
- Explicit R/C/H/O regression checks: **NUMERICALLY SUPPORTED**.
- PDT-native derivation of the Cycle 124 hypotheses: **OPEN**.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## Surviving next obligation

Derive, from PDT primitives rather than importing geometry, why physical distinction composition should provide a **nonzero same-sector bilinear operation with proper-rotation covariance but without a unital multiplicative-norm structure**. Alternatively, falsify that route and move to a different PDT-native composition mechanism.
