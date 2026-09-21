# PDT-II Cycle 289 — the binary cross-product route selects n=3 only conditionally

## Status

- **CONDITIONAL:** if PDT postulates a nonzero bilinear antisymmetric distinction-composition operation `x : V x V -> V` on a real `n`-dimensional Euclidean distinction space satisfying the ordinary vector-cross-product norm identity `||u x v||^2 = ||u||^2||v||^2 - <u,v>^2` for all `u,v`, then the classical classification restricts `n` to `0,1,3,7`; for nontrivial `n>1`, only `3` and `7` survive.
- **FALSIFIED:** these hypotheses alone do **not** derive `n=3`, because the octonionic cross product supplies an exact `n=7` countermodel.
- **IMPORTED/KNOWN:** the classification of real vector cross products and the octonionic `R^7` construction are classical mathematics (Brown--Gray/Hurwitz lineage), not PDT discoveries.
- **OPEN:** a genuinely PDT-native, independently physical hypothesis that excludes the `n=7` survivor without inserting associativity/three-dimensionality merely to force the answer.
- **OPEN:** same-input quantitative PDT/QM deviation.
- **BREAKTHROUGH CANDIDATE:** NO.

## Why attack this route

Cycle 288 proved that generic tensor/composition consistency does not select `n=3`. A stronger possible route is to demand that *two distinction directions compose into a third distinction direction* by a rotation-covariant antisymmetric operation with magnitude equal to oriented area. In ordinary three-space this is the vector cross product, so this is a natural candidate for a non-circular dimension selector.

The correct prove-or-falsify result is that the route gets close, but not all the way: dimension seven survives exactly.

## Candidate hypotheses

Let `V` be a finite-dimensional real inner-product space. Assume a bilinear operation `x: V x V -> V` with:

1. antisymmetry: `u x v = -(v x u)`;
2. orthogonality: `<u x v,u>=<u x v,v>=0`;
3. norm/area law: `||u x v||^2 = ||u||^2||v||^2 - <u,v>^2`;
4. nontriviality for some linearly independent `u,v`.

These are the standard real vector-cross-product axioms. They imply the familiar three-dimensional operation, but also the octonionic seven-dimensional one.

## Exact countermodel at n=7

Identify `V` with the imaginary octonions `Im(O) ~= R^7`. For imaginary octonions define

`u x v = Im(uv) = (uv-vu)/2`.

This operation is bilinear and antisymmetric. The normed-division-algebra identity gives

`||uv|| = ||u|| ||v||`,

and decomposition of `uv` into scalar and imaginary parts yields

`||u x v||^2 = ||u||^2||v||^2 - <u,v>^2`.

Hence the same area law that holds in `R^3` holds exactly in `R^7`. Therefore the candidate implication

`binary antisymmetric norm-preserving distinction composition => n=3`

is false.

## Dimension stress n=1,...,12

Classical cross-product classification gives the exact status:

| n | ordinary binary vector cross product satisfying the hypotheses? |
|---:|:---:|
| 1 | degenerate/trivial |
| 2 | no |
| 3 | yes |
| 4 | no |
| 5 | no |
| 6 | no |
| 7 | yes |
| 8 | no |
| 9 | no |
| 10 | no |
| 11 | no |
| 12 | no |

Thus, after excluding the trivial one-dimensional case, the hypotheses reduce the finite-dimensional search from arbitrary `n` to `{3,7}`, but they do not uniquely select three.

## Stronger surviving theorem

A defensible conditional statement is:

> If PDT independently derives an ordinary real binary vector-cross-product structure on distinction directions, then nontrivial finite distinction dimension is restricted to `n in {3,7}`.

This is much stronger than generic composition consistency, but it is **IMPORTED/KNOWN mathematics plus a PDT-conditional premise**, not a PDT-native derivation.

## Can associativity eliminate n=7?

The tempting repair is to require an associative underlying multiplication. Octonions are nonassociative, while quaternions are associative and generate the `R^3` cross product. This would remove the seven-dimensional survivor.

However, simply adding associativity is not yet acceptable as a PDT breakthrough: it risks selecting quaternions by importing exactly the algebraic property needed to exclude octonions. PDT must derive why physical distinction composition should obey the relevant associativity law, and the law must be stated operationally on measurable distinction processes rather than chosen because it returns three.

Accordingly:

- `cross-product axioms + independently justified associative composition => n=3` is at best **CONDITIONAL** pending a precise operational theorem;
- `cross-product axioms alone => n=3` is **FALSIFIED** by `R^7`.

## Prior-art gate

This dimensional restriction is established mathematics. The classification of vector cross products is associated with Brown and Gray and with normed-division-algebra/Hurwitz structure. The seven-dimensional cross product from imaginary octonions is standard. Therefore PDT cannot claim novelty for `{3,7}` selection itself.

The possible PDT research question is narrower: can PDT derive, from its own operational distinction principles and without assuming the target geometry, a measurable composition law whose mathematical consequences satisfy the cross-product hypotheses plus an independently motivated condition that rejects the octonionic survivor?

## Same-input prediction gate

Nothing in this result changes quantum probabilities. Both `R^3` and `R^7` here are mathematical distinction-space candidates, not alternative microscopic probability rules. Therefore this cycle produces no same-input `P_PDT != P_QM` prediction and makes no experimental claim.

## Next obligation

Attack operational associativity rather than algebraic associativity by defining sequential distinction composition entirely in terms of admissible experiments/records. Test whether an experimentally meaningful reassociation invariance actually implies an algebraic identity strong enough to remove `R^7`; actively search for Moufang/alternative-algebra countermodels before claiming success. If the operational condition is already standard reconstruction theory or is satisfied by the octonionic model, record the failure rather than strengthening it ad hoc.
