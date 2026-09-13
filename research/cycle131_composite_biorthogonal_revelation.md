# Cycle 131 — Composite Biorthogonal Revelation Boundary

## Question
Can the local quadratic revelation law already present in PDT (Cycle 074) be lifted, without a new assumption, to the composite parallelogram/quadratic law used in Cycle 130?

## Result A — exact conditional selector theorem
Let `W = V_A tensor V_B` be represented as a real matrix space. Assume a composite resource norm `N` has:

1. product calibration: `N(x y^T) = ||x||_2 ||y||_2`;
2. positive homogeneity (automatic for a norm);
3. composite biorthogonal quadratic revelation: whenever
   `A = sum_k s_k u_k v_k^T` with `{u_k}` and `{v_k}` orthonormal,
   `N(A)^2 = sum_k N(s_k u_k v_k^T)^2`.

Take an SVD `A = sum_k s_k u_k v_k^T`. By homogeneity and product calibration,
`N(s_k u_k v_k^T)^2 = s_k^2`. Hence

`N(A)^2 = sum_k s_k^2 = ||A||_F^2`,

so `N(A) = ||A||_F` for every composite. The Cycle 130 parallelogram law is therefore a consequence of this stronger operational-looking composite revelation hypothesis rather than an independent assumption.

**Status:** PROVED (elementary once the hypotheses are stated), CONDITIONAL, IMPORTED/KNOWN mathematics. This is not claimed as a new matrix-analysis theorem.

## Result B — local-to-composite lift is false
The local Cycle 074 law does not by itself imply Result A's composite revelation axiom, even after adding rank-one/product calibration and local orthogonal covariance.

Counterfamily: Schatten `p` norms. They are functions of singular values, are invariant under left/right orthogonal transformations, and all agree on rank-one products because a rank-one matrix has a single nonzero singular value. Nevertheless, for rank >= 2 they obey quadratic channel additivity only at `p=2`.

### Smallest decisive witness
In dimension 2,

`I_2 = E_11 + E_22`,

where the two summands are biorthogonal rank-one product channels. Quadratic revelation would require

`N(I_2)^2 = N(E_11)^2 + N(E_22)^2 = 2`.

The gaps `N(I_2)^2 - 2` are:

- Schatten 1: `+2`;
- Schatten 2 / Frobenius: `0` (floating implementation residual about `4.44e-16`);
- Schatten 4: `sqrt(2)-2 = -0.5857864376...`;
- Schatten infinity / spectral: `-1`.

Thus the implication

`local quadratic revelation + product calibration + local reversible covariance => composite quadratic revelation`

is **FALSIFIED**. Dimension 1 and rank <= 1 cannot distinguish the Schatten family, so `n=2`, rank 2 is the minimal nontrivial witness.

## Stress audit
Seed: `131011`.
Dimensions: `1..12, 16, 24, 32, 48, 64, 96, 128`.
Norms: Schatten `p = 1,2,4,infinity`.

- 4,540 norm/gap evaluations;
- 0 `p=2` tolerance failures;
- all 2,970 generated rank>=2 non-`p=2` cases distinguished from quadratic revelation;
- 0 rank<=1 indistinguishability failures;
- 924 SVD reconstruction checks, maximum relative residual `7.41e-16`.

These computations are regression/stress evidence only; the theorem and counterexample are exact.

## Prior-art boundary
SVD, Frobenius geometry, Schatten norms and their orthogonal/unitary invariance are classical matrix-analysis facts. Therefore neither the singular-value calculation nor the Schatten counterfamily is claimed as PDT novelty. The PDT-specific research question is whether a *physical* composite-biorthogonal revelation principle can be derived independently from PDT primitives rather than inserted to select the Frobenius/Schatten-2 geometry.

## Classification
- PROVED
- CONDITIONAL
- IMPORTED/KNOWN
- NUMERICALLY SUPPORTED
- FALSIFIED
- OPEN

**BREAKTHROUGH CANDIDATE: NO.**

## Surviving obligation
Derive, falsify, or operationally motivate from PDT primitives the bridge:

`mutually resolvable composite product channels => quadratic resource additivity across those channels`.

Until that bridge is independently obtained, Frobenius composite geometry remains conditional rather than PDT-native.
