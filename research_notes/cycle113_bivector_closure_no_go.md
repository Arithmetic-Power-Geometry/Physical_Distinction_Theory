# Cycle 113 — Bivector-sector closure no-go for an `n=3` selector

## Question
Can PDT obtain a non-circular `n=3` result from an alternating primitive composition that is fully rotation covariant and obeys the exact Euclidean area law?

## Decisive countermodel
Let `V` be any finite-dimensional real Euclidean space and take

\[
B(x,y)=x\wedge y\in\Lambda^2V.
\]

This composition is bilinear and alternating. Naturality of exterior powers gives

\[
(Rx)\wedge(Ry)=(\Lambda^2R)(x\wedge y)
\]

for every orthogonal `R`; in the antisymmetric-matrix realization,

\[
W(Rx,Ry)=R W(x,y)R^T.
\]

The induced exterior-power inner product also gives the exact Gram area law

\[
\|x\wedge y\|^2=\|x\|^2\|y\|^2-\langle x,y\rangle^2.
\]

Therefore **alternation + full rotational covariance + the exact Euclidean area law do not imply `n=3`** if the output is allowed to live in the bivector sector. This candidate implication is FALSIFIED; the smallest nontrivial witness is already `n=2`.

## What actually selects three

\[
\dim\Lambda^2V=\binom n2=\frac{n(n-1)}2.
\]

If PDT independently requires an isomorphic identification `Λ²V ≅ V`, dimension matching gives

\[
\frac{n(n-1)}2=n,
\]

with nonnegative solutions `n=0,3`; the only positive nontrivial solution is `n=3`. But this makes the unresolved premise explicit: PDT must derive why pairwise composition closes back into the same primitive state sector. That closure cannot be assumed simply because it produces three dimensions. In standard 3D Euclidean geometry the Hodge star supplies a bivector/vector identification only after metric and orientation structure are supplied, so importing it would not be a PDT-native derivation.

## Composite and dimensional stress tests
For direct-sum systems,

\[
\Lambda^2(A\oplus B)\cong\Lambda^2A\oplus(A\otimes B)\oplus\Lambda^2B.
\]

The corresponding dimension identity was checked for every `a,b=1,…,12`: 144/144 passed. Dimensions `1,…,12,16,24,32,48,64,96,128` were audited. Exhaustive basis-pair Gram checks through `n=12` and analytic certificates above it had zero failures. A seeded 585-case integer-vector audit using determinant-`+1` signed-permutation rotations had zero Gram-law failures and zero equivariance failures, with maximum residual `0` in these exact tests. Local regression tests: 7/7 passed.

## Norm boundary
The area identity is Hilbert/Euclidean structure, not a generic norm statement. For `x=(1,1)` and `y=(1,-1)`, the standard bivector coefficient norm gives `||x∧y||²=4`, while a naive replacement of Euclidean norms by `ℓ1` in the Gram expression gives `16`. Thus arbitrary-norm transport of this selector is also FALSIFIED.

## Prior-art boundary
Exterior powers, wedge-product naturality, induced Gram inner products, Hodge duality, and the 3D bivector/vector identification are standard mathematics; none is claimed as novel. Useful references checked in this cycle:

- Brian Conrad, Stanford Math 210A, *Tensor algebras, tensor pairings, and duality*: https://math.stanford.edu/~conrad/210APage/handouts/tensoralg.pdf
- MathWorld, *Exterior Algebra*: https://mathworld.wolfram.com/ExteriorAlgebra.html
- Standard Hodge-star/Gram construction: https://en.wikipedia.org/wiki/Hodge_star_operator

## Status
- `x∧y` countermodel: **PROVED / IMPORTED-KNOWN**.
- “alternation + full rotation covariance + area law ⇒ n=3” without closure: **FALSIFIED**.
- `dim Λ²V=dim V` gives nontrivial positive `n=3`: **PROVED**.
- PDT-native vector-valued closure `Λ²V≅V`: **OPEN / CONDITIONAL**.
- arbitrary-norm version of the Euclidean area law: **FALSIFIED**.
- stress tests: **NUMERICALLY SUPPORTED**.
- **BREAKTHROUGH CANDIDATE: NO.**

## Next obligation
Before adding further generic symmetry axioms to a vector cross product, prove or falsify the PDT-native claim that composition of two primitive distinctions must remain in the same primitive distinction sector rather than in a pair/bivector sector. Any proposed derivation must survive exterior-algebra countermodels, subsystem decompositions, resource quotients and reversible-group covariance without importing Hodge duality or the desired dimension.
