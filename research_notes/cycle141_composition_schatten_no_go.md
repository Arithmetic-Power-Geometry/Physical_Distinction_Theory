# PDT Cycle 141 — Composition-law Schatten power-sum no-go

## Question
Do direct-sum additivity, tensor-product multiplicativity, reversible left/right covariance, and rank-one calibration uniquely select the quadratic/Frobenius-squared resource law?

## Counterfamily
For finite p>=1 define

R_p(A) = sum_i sigma_i(A)^p.

For every p:

1. R_p(U A V^T)=R_p(A) for orthogonal U,V.
2. R_p(A direct-sum B)=R_p(A)+R_p(B), because singular values concatenate.
3. R_p(A tensor B)=R_p(A) R_p(B), because tensor-product singular values are all pairwise products sigma_i(A)sigma_j(B).
4. For rank-one A=x y^T, R_p(A)=(||x|| ||y||)^p.
5. R_p(0)=0 and R_p(A)>=0.

Thus the composition package is compatible with a full p-family and does not select p=2.

## Exact same-input witness
For A=diag(1,2):

- R_1(A)=3
- R_2(A)=5
- R_3(A)=9
- R_4(A)=17

The resource values are inequivalent even though each member obeys the tested composition and reversible-symmetry laws.

## What survives
A separate PDT-native principle fixing degree-two scaling, or an operational continuous-mixing/resolved-channel law strong enough to imply it, is still required to exclude p!=2. Composition alone is insufficient.

## Computational audit
Seed 141; dimensions n=1..12,16,24,32,48,64,96,128; p=1,2,3,4; 664 p-cases. Zero failures for orthogonal invariance, direct-sum additivity, tensor multiplicativity, and rank-one behavior. Maximum relative residual among the four audited identities was 2.8815e-15. Five regression tests passed locally.

## Prior-art boundary
The singular-value and Schatten-norm machinery is standard matrix analysis and is not claimed as PDT novelty. Relevant prior art includes Fosner, Huang, Li & Sze, *Linear Maps Preserving Ky Fan Norms and Schatten Norms of Tensor Products of Matrices*, SIAM Journal on Matrix Analysis and Applications 34(2), 2013, DOI 10.1137/120891794, and standard definitions of Schatten p norms as p-power sums of singular values. A 2026 operator-valued Schatten-norm treatment also states natural tensor multiplicativity (Communications in Mathematical Physics, DOI 10.1007/s00220-026-05567-8).

## Classification
- PROVED: the stated R_p identities, by singular-value algebra.
- FALSIFIED: composition + reversible symmetry + rank-one calibration/formula uniquely select p=2.
- IMPORTED/KNOWN: Schatten norms/power sums and singular-value direct-sum/tensor rules.
- NUMERICALLY SUPPORTED: seeded stress audit through n=128.
- OPEN: PDT-native principle that excludes p!=2 without importing the desired quadratic law.
- BREAKTHROUGH CANDIDATE: NO.
