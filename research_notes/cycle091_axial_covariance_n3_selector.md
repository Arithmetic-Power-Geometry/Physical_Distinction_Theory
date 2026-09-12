# Cycle 091 — Axial O(n) Covariance Repairs the Orientation Boundary

## Target
PDT-II target (2): non-circular PDT-native elementary `n=3` derivation.

## Why this cycle was necessary
Cycle 090 proved that a **polar-vector-valued** alternating closure cannot be equivariant under all of `O(3)`: a reflection reverses the 3D volume form.  That result is correct, but it leaves an important representation-type boundary.  The ordinary cross product is physically an **axial vector / pseudovector**, not a polar vector.

This cycle asks whether full unoriented `O(n)` isotropy can coexist with alternating closure when the output is typed correctly as axial.

## Exact hypothesis
Let `V = R^n` be Euclidean.  Let

`B : V x V -> V_ax`

be bilinear and alternating, with the output carrying the determinant-twisted standard representation:

`B(Rx,Ry) = det(R) R B(x,y)` for every `R in O(n)`.

Equivalently, `V_ax = V tensor det` as an `O(n)` representation.

## Theorem
For nontrivial finite Euclidean `V`,

`Hom_O(n)(Lambda^2 V, V tensor det) != 0`

if and only if

`n = 3`.

### n = 3 existence
The usual cross product, interpreted as axial, obeys

`(Rx) x (Ry) = det(R) R (x x y)`.

Thus it is covariant under both proper and improper orthogonal transformations.  No globally chosen handed coordinate system is needed in the covariance statement; the parity character is carried by the output representation.

### n > 3 no-go
Define

`T(x,y,z) = <B(x,y),z>`.

The axial covariance law implies

`T(Rx,Ry,Rz) = det(R) T(x,y,z)`.

So `T` is a determinant-twisted alternating 3-form.  Pick any coefficient `T(e_i,e_j,e_k)`.  Because `n>3`, choose an unused basis index `l`.  Let `R` be the pi rotation that flips `e_k` and `e_l` and fixes all other basis vectors.  Then `det(R)=+1`, while

`T(Re_i,Re_j,Re_k) = -T(e_i,e_j,e_k)`.

Covariance requires equality because `det(R)=+1`.  Hence that coefficient is zero.  Every coefficient is killed this way, so `T=0`, and therefore `B=0`.

### n = 2 and n = 1
For `n=1`, alternation is identically zero.

For `n=2`, `Lambda^2 V` carries the determinant representation.  A map into `V tensor det` would, after cancelling the determinant character, require an `O(2)`-equivariant map from the trivial representation to `V`, i.e. an `O(2)`-fixed nonzero vector.  None exists.

Therefore only `n=3` survives.

## Exact reflection witness
Take

`R = diag(-1,1,1)`, `x=e_2`, `y=e_3`.

Then `x cross y = e_1` and

- polar RHS: `R e_1 = -e_1`, while the transformed-input cross product is `+e_1`; residual norm = `2`;
- axial RHS: `det(R) R e_1 = (+e_1)`; residual = `0`.

Thus Cycle 090's polar no-go and Cycle 091's axial survival are perfectly compatible.

## Dimension and numerical audit
The analytic classification was frozen for

`n = 1..12, 16, 24, 32, 48, 64, 96, 128`.

Only `n=3` survives the stated hypothesis.  A fixed-seed numerical regression over 1,000 random `O(3)` transformations contained 514 proper and 486 improper transformations; the maximum axial-covariance residual was

`6.962667462125256e-15`.

The theorem is analytic; this numerical sweep is regression evidence only.

## Prior-art / rediscovery check
This is **not new mathematics**.  Standard tensor/exterior-algebra treatments identify the 3D cross product as an axial vector (pseudovector), with transformation law `det(R) R`.  Standard Hodge duality identifies 3D bivectors with axial vectors.  Useful prior-art boundaries include:

- E. W. Weisstein, *Pseudovector*, MathWorld: a pseudovector transforms with the extra determinant factor under improper orthogonal transformations.
- E. W. Weisstein, *Hodge Star*, MathWorld: Hodge duality maps alternating `k`-forms to `(n-k)`-forms on an oriented inner-product space.
- Doran & Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2007), for polar/axial and exterior-algebra representation structure.
- Arfken, Weber & Harris, *Mathematical Methods for Physicists*, for pseudotensors and axial-vector transformation laws.

The orthogonal-group split into determinant `+1` and `-1` components is classical; the determinant twist is therefore an established representation, not a PDT invention.

## Classification
- `PROVED`: under the stated determinant-twisted covariance hypothesis, nonzero alternating closure exists iff `n=3`.
- `CONDITIONAL`: applying this theorem to PDT requires an independent PDT derivation of the axial/parity-odd output character.
- `IMPORTED/KNOWN`: pseudovectors, determinant twists, Hodge duality and the representation-theoretic boundary are standard mathematics.
- `NUMERICALLY SUPPORTED`: 1,000 random `O(3)` covariance checks plus the frozen dimension ledger.
- `OPEN`: derive the parity type of primitive distinction closure from PDT operational primitives.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## What this changes
Cycle 090's statement that PDT must introduce an explicit orientation-preserving reversible group was too strong as a physical necessity.  A cleaner surviving route is

`full O(n) isotropy + PDT-native axial alternating closure -> n=3`.

This does **not** finish target (2), because declaring the closure axial merely to obtain three dimensions would be circular.  The next prove-or-falsify obligation is whether a pre-existing PDT notion—ordered distinction, reversible commutator, oriented record, or sequential composition—forces the determinant parity character without assuming dimension three.
