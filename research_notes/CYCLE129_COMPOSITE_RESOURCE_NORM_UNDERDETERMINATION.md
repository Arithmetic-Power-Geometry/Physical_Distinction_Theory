# Cycle 129 — Composite resource-norm underdetermination

## Status

- **PROVED:** rank-one/product-state multiplicativity plus independent local orthogonal covariance does not uniquely determine a norm on a tensor composite.
- **FALSIFIED:** the candidate uniqueness principle stated below.
- **IMPORTED/KNOWN:** Schatten norms, singular-value invariance, and tensor/matrix identifications are standard matrix-analysis machinery; no novelty is claimed for them.
- **NUMERICALLY SUPPORTED:** deterministic dimension stress audit recorded in `results/cycle129_composite_resource_norm_underdetermination.json`.
- **OPEN:** a PDT-native composite-sensitive resource law that selects the composite geometry without importing the answer.
- **BREAKTHROUGH CANDIDATE:** **NO**.

## Candidate principle attacked

Let local real distinction spaces be Euclidean spaces `V_A = V_B = R^n`.  Suppose a candidate PDT composition route uses the algebraic tensor carrier

`W = V_A \otimes V_B \cong M_n(R)`

and asks a resource norm `N` on `W` to satisfy:

1. **Product-state multiplicativity**
   `N(x \otimes y) = ||x||_2 ||y||_2` for all local `x,y`.
2. **Independent local reversible covariance**
   `N((U \otimes V)w) = N(w)` for all `U,V in O(n)`.
3. **Norm axioms** on the full composite carrier.

Tempting but false claim: these conditions uniquely determine the composite resource norm.

## Exact counterfamily

Identify a simple tensor `x \otimes y` with the rank-one matrix `x y^T`.  For every `p in [1,infinity]`, define the Schatten norm

`N_p(M) = ||sigma(M)||_p`,

where `sigma(M)` is the vector of singular values.

### Product multiplicativity

A rank-one matrix `x y^T` has exactly one nonzero singular value,

`||x||_2 ||y||_2`.

Therefore for **every** Schatten index `p`,

`N_p(x y^T) = ||x||_2 ||y||_2`.

Thus all members of the counterfamily agree exactly on every simple/product tensor.

### Local reversible covariance

For orthogonal `U,V`,

`(U M V^T)^T(U M V^T) = V M^T M V^T`.

The two positive matrices are orthogonally similar, so they have the same eigenvalues and hence `M` and `U M V^T` have the same singular values.  Consequently

`N_p(U M V^T) = N_p(M)`

for every `p`.

### Smallest decisive counterexample

At `n=1` all these norms coincide, so no separation is possible.  At `n=2`, take the non-product composite direction `I_2`.  Its singular values are `(1,1)`, hence

- `N_1(I_2) = 2`,
- `N_2(I_2) = sqrt(2)`,
- `N_4(I_2) = 2^(1/4)`,
- `N_infinity(I_2) = 1`.

All four norms satisfy the same local product multiplicativity and the same `O(2) x O(2)` covariance, yet they assign different composite resources.  Therefore the uniqueness claim is false already in the smallest nontrivial local dimension.

## Surviving theorem

> **Composite-resource underdetermination theorem (within the tensor-carrier candidate route).**  Product-state multiplicativity and independent local orthogonal covariance constrain the resource norm on rank-one local product orbits but do not uniquely extend that resource geometry to the full composite carrier for any `n >= 2`.

The result is deliberately scoped: it does **not** derive the tensor product from PDT, does not identify entanglement with any particular matrix rank, and does not select a quantum norm.  It only proves that, even after granting this candidate composite carrier, local/product resource data are insufficient to select the full composite resource law.

## Stress audit

Deterministic seed: `129`.

Dimensions:

`1..12, 16, 24, 32, 48, 64, 96, 128`.

Norm family:

`p = 1, 2, 4, infinity`.

Recorded checks:

- rank-one multiplicativity: **564 checks, 0 failures**;
- local orthogonal invariance: **564 checks, 0 failures**;
- maximum rank-one relative residual: `9.102237472961577e-16`;
- maximum invariance relative residual: `1.1187137799664875e-15`;
- smallest exact norm-separation witness: `n=2`, `I_2`.

These numerical checks are regression evidence only.  The counterexample and theorem above are exact.

## Prior-art boundary

Schatten norms and their unitary/orthogonal invariance are standard matrix analysis.  Unitarily invariant norms, including Schatten-p norms, are widely established in the literature.  The present cycle therefore makes **no novelty claim** for the counterfamily itself.  Its role is as a PDT falsification guard: local product multiplicativity plus local reversible covariance must not be mistaken for a derivation of a unique PDT composite resource geometry.

## Consequence for PDT-II

A defensible PDT-native composite-resource derivation needs at least one principle that is sensitive to genuinely composite directions rather than only simple tensors/local reversible orbits.  Candidate forms include a PDT-derived spectral/gauge selection rule, a composite revelation/refinement law, or an operational inequality whose value distinguishes the surviving norm families.  Such a principle must be derived independently rather than chosen to reproduce the desired quantum structure.
