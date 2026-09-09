# Cycle 019 — finite record-information capacity

## Status

**PROVED as a conditional PDT corollary; IMPORTED/KNOWN quantum-information mathematics.**

This cycle does **not** introduce a PDT-vs-QM deviation and is **not** a breakthrough candidate. It supplies a measurement-independent kill test for any PDT rule that interprets a finite-dimensional environment record as revealing classical branch identity.

## Theorem (record-information ceiling)

Let a classical branch label `X` take `k` values with prior probabilities `p_i`, encoded into quantum record states `rho_i` supported on a Hilbert space of dimension `d`. For any measurement of the record with classical outcome `Y`,

`I(X:Y) <= chi({p_i,rho_i}) <= min(H(X), log2 d)`.

The first inequality is the Holevo bound. The second follows because

`chi = S(sum_i p_i rho_i) - sum_i p_i S(rho_i) <= S(sum_i p_i rho_i) <= log2 d`,

while mutual information cannot exceed `H(X)`.

For `k` equiprobable branches this gives the explicit residual-uncertainty floor

`H(X|Y) = log2 k - I(X:Y) >= max(0, log2(k/d))`.

Hence, if `k>d`, **perfect branch revelation is impossible for every measurement**, independent of pairwise overlap proxies and independent of how the POVM is optimized.

## Exact saturation family

When `k=q d`, assign `q` distinct classical labels to each vector of an orthonormal basis of `C^d`, all labels equiprobably. A basis measurement reveals the basis coordinate exactly but cannot distinguish duplicate labels. It yields

`I(X:Y)=log2 d`,

`H(X|Y)=log2(k/d)=log2 q`.

Thus the dimension-only bound is sharp for this infinite family.

## Relation to Cycle 018

Cycle 018 used the Welch bound to show unavoidable average pairwise overlap when more branch records than dimensions are present. The present theorem is stronger in a different operational sense: it bounds the **maximum classical information recoverable by any measurement**, even when no particular pairwise distinguishability measure is declared.

The two statements should not be conflated:

- Welch controls aggregate pairwise Hilbert-space geometry.
- Holevo controls measurement-accessible classical information.

Neither is historically new.

## PDT implication

Any PDT revelation variable intended to mean operationally recoverable branch information from the same `d`-dimensional quantum record must satisfy the ceiling above unless PDT explicitly changes the physical state space, measurement rule, probability law, or resource interaction. A formula that assigns more than `log2 d` accessible branch-information bits to the unchanged record would therefore be a same-input disagreement with standard QM, but it would also require a genuinely new physical law and cannot be justified by bookkeeping alone.

## Numerical/adversarial audit

The implementation `pdt_record_information_capacity.py` checks uniform pure-state ensembles. Fixed-seed random ensembles were sampled for `d=1..12` with `k=d+3`; all computed Holevo quantities obeyed `chi<=log2 d` to floating-point tolerance. Unit tests repeat randomized checks and exact saturation constructions, and scan formula-level edge cases through dimension 100.

## Prior art

The core bound is established quantum-information theory and must be classified as imported/known. Relevant prior-art pointers include:

- A. S. Holevo's accessible-information/Holevo bound (standard theorem; see modern summaries and Holevo's texts).
- M. Dall'Arno, *Hierarchy of Bounds on Accessible Information and Informational Power*, Phys. Rev. A 92, 012328 (2015), arXiv:1504.04429.
- R. Jain and A. Nayak, *Accessible versus Holevo Information for a Binary Random Variable*, arXiv:quant-ph/0603278.

No novelty claim is made for the information inequality itself.
