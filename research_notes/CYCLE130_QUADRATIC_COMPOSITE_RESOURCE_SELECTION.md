# Cycle 130 — Quadratic composite-resource selection

## Status

- **PROVED (conditional theorem):** on `M_n(R)`, the Frobenius norm is the unique norm satisfying the parallelogram law, independent left/right orthogonal covariance, and Euclidean normalization on all simple tensors.
- **CONDITIONAL:** PDT-II has not yet derived the full composite parallelogram law from its native primitives; importing it would be circular if used merely to recover a Hilbert geometry.
- **IMPORTED/KNOWN:** the Jordan–von Neumann characterization of inner-product norms and standard orthogonal/Frobenius facts are classical mathematics.
- **NUMERICALLY SUPPORTED:** deterministic stress audit in `results/cycle130_quadratic_composite_resource_selection.json`.
- **FALSIFIED:** the `p=1`, `p=4`, and `p=infinity` Schatten alternatives from Cycle 129 violate the parallelogram law already at `n=2`.
- **OPEN:** derive, weaken, or falsify a PDT-native composite quadratic revelation/conservation principle strong enough to imply the required parallelogram identity without assuming Hilbert structure.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Why this cycle matters

Cycle 129 proved that product normalization plus `O(n) x O(n)` covariance leaves many composite resource norms. Cycle 130 identifies a precise additional hypothesis that removes that ambiguity. This is progress because the extra hypothesis is transparent and falsifiable rather than an arbitrary choice of `p=2`.

## Theorem

Let `N` be a norm on the real matrix space `M_n(R)`. Assume:

1. **Parallelogram law** for all `A,B`:

   `N(A+B)^2 + N(A-B)^2 = 2 N(A)^2 + 2 N(B)^2`.

2. **Independent local reversible covariance**:

   `N(U A V^T) = N(A)` for every `U,V in O(n)`.

3. **Simple-tensor normalization**:

   `N(x y^T) = ||x||_2 ||y||_2` for every `x,y in R^n`.

Then

`N(A) = ||A||_F`

for every `A in M_n(R)`.

## Elementary proof

By the Jordan–von Neumann theorem, the parallelogram law implies that `N` is induced by an inner product `<.,.>_N` recovered through polarization.

Let `E_ij` denote the matrix units.

### Step 1 — distinct rows are orthogonal

Choose a diagonal orthogonal sign matrix `D` that flips row `i` and leaves row `k` unchanged. Invariance of the norm implies invariance of its polarized inner product. Hence, for `i != k`,

`<E_ij,E_kl>_N = <D E_ij, D E_kl>_N = <-E_ij,E_kl>_N = -<E_ij,E_kl>_N`,

so the inner product is zero.

### Step 2 — distinct columns are orthogonal

The same argument using a right-side diagonal sign flip gives zero whenever `j != l`.

Thus the complete matrix-unit family `{E_ij}` is pairwise orthogonal.

### Step 3 — all matrix units have the same length

Left and right permutation matrices send any `E_ij` to any `E_kl`. Orthogonal covariance therefore forces all `N(E_ij)` to be equal.

### Step 4 — normalization fixes that length

Each matrix unit is the simple tensor `e_i e_j^T`, so simple-tensor normalization gives

`N(E_ij)=||e_i||_2 ||e_j||_2=1`.

Therefore for `A=sum_ij a_ij E_ij`,

`N(A)^2 = sum_ij a_ij^2`,

which is exactly the Frobenius norm squared. QED.

## Smallest decisive witness against the Cycle-129 alternatives

At `n=2`, let `A=E_11` and `B=E_22`. For a Schatten-`p` norm,

`N_p(A+B)=N_p(A-B)=2^(1/p)`

for finite `p`, while `N_p(A)=N_p(B)=1`. Therefore the parallelogram gap is

`2*2^(2/p)-4`.

It vanishes at `p=2`. Explicitly:

- `p=1`: gap `4`;
- `p=2`: gap `0`;
- `p=4`: gap `2 sqrt(2)-4`;
- `p=infinity`: gap `-2`.

So the competing norms are separated already in the smallest nontrivial local dimension.

## Stress audit

Dimensions:

`1..12, 16, 24, 32, 48, 64, 96, 128`.

Deterministic seed: `130`.

Across **860 random matrix-pair/covariance cases**:

- Frobenius parallelogram failures above `1e-10`: **0**;
- Frobenius local orthogonal-covariance failures above `1e-10`: **0**;
- maximum relative parallelogram residual: `1.794573123523998e-15`;
- maximum relative covariance residual: `6.160050785910573e-16`.

The theorem does not depend on these numerical checks.

## Prior-art boundary

The norm-to-inner-product implication is the classical Jordan–von Neumann theorem. The Frobenius norm and its left/right orthogonal invariance are standard. Therefore this cycle makes no novelty claim for those mathematical facts. The PDT-specific value is diagnostic: it gives an exact extra premise that would resolve Cycle 129's underdetermination if PDT can derive that premise independently.

## Connection to earlier PDT work

Cycle 074 already audited an exact quadratic revelation-conservation identity under orthogonal refinement and showed that nonquadratic `l_p` alternatives fail squared block additivity. That result does **not** by itself prove the present composite parallelogram law. The next prove-or-falsify obligation is therefore:

> Can PDT's native refinement/revelation axioms force the composite parallelogram identity, rather than merely assuming Euclidean/Hilbert resource accounting?

If yes, Cycle 129's composite norm ambiguity collapses to Frobenius geometry. If no, the remaining non-Hilbert composite alternatives stay admissible.
