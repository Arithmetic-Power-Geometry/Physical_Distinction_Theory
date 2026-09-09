# Cycle 017 — Transitive reversible norm spheres force Euclidean geometry

## Status

**PROVED (finite-dimensional theorem) / CONDITIONAL PDT INTERPRETATION / IMPORTED-KNOWN mathematics.**

This is not promoted as a breakthrough candidate.

## Statement

Let `V` be a finite-dimensional real normed space and let `G` be a compact group of linear isometries of the norm. If `G` acts transitively on the norm unit sphere, then the norm is induced by an inner product, up to an overall scale.

In PDT language: if every pure distinction direction can be reached reversibly from every other pure distinction direction by linear norm-preserving controls, then the distinction body is necessarily an ellipsoid; after a linear change of coordinates it is a Euclidean ball.

## Proof

Choose any positive-definite inner product `<.,.>_0` on `V` and average it over normalized Haar measure on `G`:

`<x,y>_G = integral_G <g x, g y>_0 dg`.

This is positive definite and `G`-invariant. Therefore its Euclidean norm `|x|_G=sqrt(<x,x>_G)` is constant on every `G` orbit. By transitivity it is a single constant `c>0` on the entire original norm unit sphere `S={x: ||x||=1}`. For arbitrary nonzero `x`, write `u=x/||x||`. Homogeneity gives

`|x|_G = ||x|| |u|_G = c ||x||`,

hence `||x|| = |x|_G/c`. So the original norm is Euclidean.

No connectedness assumption is needed.

## Adversarial norm tests

For `l_p^n`, compare two vectors on the `l_p` unit sphere:

- axis point `e_1`, whose standard Euclidean radius is `1`;
- equal-coordinate point `u=n^(-1/p)(1,...,1)`, whose Euclidean radius is `n^(1/2-1/p)`.

For every `n>=2`, these radii agree iff `p=2`. Thus the standard `l_p` families with `p!=2` visibly retain directional anisotropy and cannot satisfy full transitive linear reversibility. The branch audit checks `p in {1,1.5,2,3,4,10}` for `n=2..12`; tests extend the exact witness through `n=100`.

## What this does and does not solve

This materially simplifies the PDT geometry chain: Euclidean geometry can follow from a single strong operational symmetry hypothesis instead of being separately assumed. But it does **not** select spatial dimension `n=3`: Euclidean spheres are transitively reversible in every finite dimension. It also does not imply TPI for the actual reversible subgroup; proper transitive groups such as unitary families remain relevant to the earlier kill tests.

Therefore the result sharpens the boundary:

`transitive linear reversibility => Euclidean norm`,

but

`transitive linear reversibility !=> n=3`.

## Prior-art discipline

The averaging argument is standard compact-group/finite-dimensional Banach-space mathematics and belongs to the finite-dimensional side of the rotation-problem literature. Historical novelty is not claimed. The PDT contribution here is only the explicit placement of this theorem into the distinction/reversibility dependency graph and its executable norm-family kill tests.
