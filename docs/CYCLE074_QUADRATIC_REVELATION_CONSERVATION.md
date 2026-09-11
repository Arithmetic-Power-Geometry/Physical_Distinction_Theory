# Cycle 074 — Quadratic revelation conservation under orthogonal resource refinement

## Status

**PROVED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED.**  
**DECISIVE FALSIFICATION** of a universal extension to nonquadratic `l_p` geometries.  
**Not a BREAKTHROUGH CANDIDATE.**

## Setup

Let `V` be a finite-dimensional real or complex inner-product distinction space, let `x` denote a distinction vector (for quantum applications one may take `x = rho-sigma` in Hilbert–Schmidt geometry), and let

`S_0 subset S_1 subset ... subset S_m`

be nested accessible-resource subspaces. Write `P_k` for the orthogonal projector onto `S_k`, and define quadratic accessible distinction

`E_k(x) = ||P_k x||_2^2`.

## Theorem 1 — exact revelation conservation

For every nested chain,

`E_m(x)-E_0(x) = sum_{k=0}^{m-1} ||(P_{k+1}-P_k)x||_2^2`.

Every increment is nonnegative. Thus the total revealed quadratic distinction depends only on the endpoints, even though its allocation among intermediate resource steps depends on the chosen refinement path.

### Proof

For nested orthogonal projections, `P_k P_{k+1}=P_k=P_{k+1}P_k`. Hence `Q_k=P_{k+1}-P_k` is itself the orthogonal projector onto `S_{k+1} intersect S_k^perp`, and

`P_{k+1}x = P_k x + Q_k x`

with orthogonal summands. Pythagoras gives

`||P_{k+1}x||_2^2 = ||P_k x||_2^2 + ||Q_k x||_2^2`.

Summing over `k` proves the result.

This sharpens Cycle 073. Generic operational distinguishability increments are path-dependent and need not have a step-size-only conservation law. A quadratic Hilbert-space resource functional does possess an exact endpoint conservation identity because the refinement increments are orthogonal innovations.

## Theorem 2 — nonquadratic `l_p` extension fails

Suppose one tries to use `E_p(x)=||x||_p^2` and demands exact additivity over disjoint orthogonal coordinate resource blocks for every vector. Apply the demand to `x=(1,1)` split into the two coordinate axes. The whole-vector value is

`||(1,1)||_p^2 = 2^(2/p)`

for finite `p`, while the sum of the two one-coordinate contributions is exactly `2`. Equality therefore requires

`2^(2/p)=2`,

hence `p=2`. For `p=infinity`, the whole-vector value is `1`, again not `2`.

Therefore within the full `l_p` family, exact squared-norm revelation additivity selects the quadratic case `p=2`.

## Broader geometry boundary

This is not historically new mathematics. The general Jordan–von Neumann characterization says that a norm comes from an inner product iff it satisfies the parallelogram law; inner-product norms then obey Pythagorean orthogonal decompositions. See Encyclopedia of Mathematics, “Pre-Hilbert space”: https://encyclopediaofmath.org/wiki/Pre-Hilbert_space .

Accordingly, PDT must not claim that quadratic revelation conservation itself is novel. The branch contribution is its explicit resource-refinement interpretation and its use as a kill test: any proposed exact additive revelation law based only on squared norm innovations is forcing Hilbert/quadratic geometry (or an equivalent special structure), not deriving that geometry from PDT.

## Audit

`cycle074_quadratic_revelation_conservation.py` tests nested coordinate refinements in dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`.

There are 1,480 randomized chains, zero failures, and maximum floating-point endpoint error `5.684341886080802e-14`. The analytic proof, not the audit, establishes the theorem.

The same audit records the exact two-coordinate witness for `p=1, 1.5, 2, 3, 4, 8, infinity`; only `p=2` has zero additivity gap.

## PDT consequence

There is now a clean surviving target-(4) statement:

> If PDT can independently justify orthogonal innovation sectors and a physically meaningful quadratic distinction budget, then resource revelation obeys an exact nonnegative conservation law.

But using this identity to *derive* Hilbert geometry would be circular unless the orthogonality/quadratic assumptions themselves come from independent PDT principles. It does not select `n=3`, does not change Born probabilities, and does not by itself produce a new experiment.
