# PDT-II Cycle 069 — No Universal Finite Trace-Word Cutoff

## Target attacked

Primary target: **(1) PDT-native composition law**.  This cycle tests whether the operator-complete trace-word construction from Cycles 067–068 can be compressed to a **dimension-independent finite maximum word length** while remaining operationally complete.

## Result

**Classification: PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED.**

The following candidate is falsified:

> There exists a fixed finite word-length cutoff `L`, independent of Hilbert-space dimension, such that all traces of words of length at most `L` in `(rho,sigma)` form an operator-complete distinction state for every finite dimension.

### Theorem

For every finite `L>=1`, there exist dimension `d=L+1`, faithful diagonal density matrices `rho != rho'`, and `sigma=I/d` such that

`Tr[w(rho,sigma)] = Tr[w(rho',sigma)]`

for every noncommutative word `w` of total length at most `L`, while `rho` and `rho'` are not unitarily equivalent and an allowed measurement effect gives different outcome probabilities.

### Proof

Choose `d=L+1` distinct positive numbers `lambda_1,...,lambda_d` summing to one, and let

`p(t)=prod_i (t-lambda_i)`.

Perturb only the constant coefficient: `p_epsilon(t)=p(t)+epsilon`.  Because the original roots are simple and strictly positive, for sufficiently small nonzero `epsilon` the perturbed polynomial has `d` simple positive real roots `mu_1,...,mu_d` continuously close to the originals.

All coefficients except the constant term are unchanged.  Therefore the elementary symmetric functions `e_1,...,e_{d-1}` of `lambda` and `mu` agree, while `e_d` differs.  Newton identities then imply

`sum_i lambda_i^k = sum_i mu_i^k` for every `k=1,...,d-1=L`,

but `prod_i lambda_i != prod_i mu_i`.  The first identity also preserves normalization.

Set `rho=diag(lambda)`, `rho'=diag(mu)`, and `sigma=I/d`.  Since `sigma` commutes with both states and is scalar, any word of total length at most `L` containing `a` copies of `rho` and `b` copies of `sigma` reduces to

`Tr[w(rho,sigma)] = d^{-b} Tr(rho^a)`.

Because `a<=L`, all such trace words agree for `rho` and `rho'`.  But the determinants differ, so their spectra differ and the states are not unitarily equivalent.  In the common diagonal basis, a coordinate projector onto any index where `lambda_i != mu_i` gives distinct measurement probabilities.  Hence the truncated trace-word data are not operationally complete.

This proves that **the finite completeness boundary from Cycle 068 must have a dimension-dependent cutoff**.  A universal bounded trace-word alphabet cannot be the sought PDT-native composition object.

## Numerical stress audit

`cycle069_no_universal_traceword_cutoff.py` instantiates the proof numerically.  Dimensions `d=2,...,12` use cutoff `L=d-1`; `d=1` is recorded as degenerate.  The largest observed matching-moment residual is at floating-point roundoff scale while every witness has a nonzero coordinate-probability separator and a changed determinant.

For higher dimensions `16,24,32,48,64,96,128`, a fixed `L=6` witness is embedded by appending an identical positive tail to both spectra.  The first six moments continue to agree to floating-point precision while the operational separator remains nonzero.

The exact algebraic theorem, not the numerical audit, carries the proof burden.

## Prior-art boundary

This result uses standard mathematics: Newton identities, continuity of simple polynomial roots, classical truncated-moment non-uniqueness, and matrix invariant theory.  Procesi/Razmyslov-type results establish dimension-dependent finite generating bounds for simultaneous-conjugation invariants, while Specht-type trace-word criteria characterize unitary equivalence.  Therefore **no historical novelty is claimed** for the mathematical fact that the required invariant degree grows with dimension or that finitely many low-order moments can be incomplete.

Relevant external prior-art checks for this cycle include invariant-ring results reporting trace-word generation with dimension-dependent degree bounds (including the `n^2` Razmyslov bound) and Specht/multivariable-Specht trace criteria.

## PDT-II consequence

Cycles 067–069 now give a sharper composition boundary:

1. scalar/spectral/Petz summaries are too compressed;
2. full trace-word data are operator-complete but imported/known;
3. fixed dimension admits finite trace-word generation;
4. **no dimension-independent finite maximum word length is complete across all finite dimensions**.

Accordingly, a viable PDT-native composition law must either be dimension/resource adaptive, retain an operator object directly, or introduce a new physically derived quotient/filtration whose sufficiency is proved for the declared resource window.  Merely choosing a fixed finite list of low-order trace words is now closed.

## Status

- Universal dimension-independent finite trace-word cutoff: **FALSIFIED**.
- Dimension-dependent finite trace-word completeness: **IMPORTED/KNOWN**.
- Algebraic no-go theorem above: **PROVED**.
- Numerical witness suite: **NUMERICALLY SUPPORTED**.
- Breakthrough candidate: **NO**.
