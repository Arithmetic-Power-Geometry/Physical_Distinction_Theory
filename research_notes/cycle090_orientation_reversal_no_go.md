# Cycle 090 — Orientation-Reversal No-Go for the n=3 Selector

## Target
PDT-II target (2): non-circular PDT-native elementary `n=3` derivation.

## Exact hypothesis tested
Let `V = R^3` with its Euclidean inner product. Let

`B : V x V -> V`

be bilinear and alternating. Strengthen Cycle 089's covariance requirement from `SO(3)` to the full orthogonal group `O(3)`:

`B(Rx,Ry) = R B(x,y)` for every `R in O(3)`.

## Theorem — orientation-reversal no-go
Under these hypotheses, `B = 0`.

### Proof
Define `T(x,y,z)=<B(x,y),z>`. Because `B` is alternating and equivariant and the inner product is orthogonally invariant, `T` is an `O(3)`-invariant alternating 3-form. Every alternating 3-form on `R^3` is a scalar multiple `c vol` of the oriented volume form. For any reflection `R` with `det R=-1`,

`vol(Rx,Ry,Rz) = -vol(x,y,z)`.

But `O(3)` invariance would require equality. Hence `c=-c`, so `c=0`; therefore `T=0` and nondegeneracy of the inner product gives `B=0`.

A concrete witness is `R=diag(-1,1,1)`. It reverses every nonzero Levi-Civita component.

## Consequence for Cycle 089
The Cycle-089 selector does **not** follow from unoriented isotropy. The statement

`full O(n) reversible isotropy + nonzero alternating equivariant binary closure => n=3`

is false in the intended existence sense: at `n=3` the required closure is killed by reflections. To retain the selector, PDT must independently justify an **orientation-preserving** reversible group (`SO(n)` or an equivalent handed structure), rather than merely isotropy under all Euclidean reversible transformations.

This is a substantive circularity/assumption audit: orientation is now an explicit physical premise that cannot be hidden inside the word “isotropy.” It does not by itself invalidate the conditional Cycle-089 theorem.

## Classification
- `PROVED`: the O(3) no-go.
- `FALSIFIED`: the strengthened O(n)-isotropy version of the Cycle-089 selector.
- `IMPORTED/KNOWN`: cross products/volume forms are standard multilinear geometry.
- `OPEN`: PDT-native derivation of orientation-preserving isotropy and alternating closure.

## Counterexample / boundary catalog
- `n=3`, `SO(3)`: ordinary cross product survives.
- `n=3`, `O(3)`: reflection covariance fails for a vector-valued cross product; the cross product transforms as a pseudovector.
- Restricted groups can admit other structures; Cycle 089 already records the dimension-7/G2 boundary.

## Novelty discipline
No breakthrough claim. The mathematical fact is known. Its role here is to eliminate an unjustified strengthening of the PDT n=3 route and to expose the exact additional physical premise required.
