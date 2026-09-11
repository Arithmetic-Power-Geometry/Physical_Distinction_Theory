# Cycle 071 — Correlated-composite nonclosure of local resource quotients

## Classification

**PROVED + FALSIFIED + IMPORTED/KNOWN + NUMERICALLY SUPPORTED**

**Not a BREAKTHROUGH CANDIDATE.** The quantum-marginal problem, correlation tensors, and the general fact that local marginals do not determine a global correlated state are established quantum-information mathematics.

## Target attacked

PDT-II target (1): a PDT-native composition law.

Cycle 070 established an exact product-state identity for restricted operational states,

\[
q_{AB}(\rho_A\otimes\rho_B)=q_A(\rho_A)\otimes q_B(\rho_B).
\]

The present cycle asks whether the pair of local quotient states can determine the resource-restricted state of an **arbitrary correlated composite**.

## Theorem — local-only composition is impossible in the presence of accessible correlations

Let `S_A` and `S_B` be local accessible Hermitian observable spaces. Suppose each contains a nonzero traceless observable, respectively `A` and `B`. Normalize them so that

\[
\operatorname{Tr}(A^2)=\operatorname{Tr}(B^2)=1.
\]

On dimensions `d_A,d_B >= 2`, define

\[
\rho_\pm=\frac{I}{d_A d_B}\pm\epsilon A\otimes B,
\]

with `epsilon>0` small enough that both states remain positive semidefinite.

Because `Tr(A)=Tr(B)=0`,

\[
\operatorname{Tr}_B\rho_+=\operatorname{Tr}_B\rho_-=\frac{I_A}{d_A},
\qquad
\operatorname{Tr}_A\rho_+=\operatorname{Tr}_A\rho_-=\frac{I_B}{d_B}.
\]

Hence the two states have identical **full** local marginals and therefore identical local resource quotients for every choice of local accessible subspaces.

But the accessible product observable `A tensor B` separates them:

\[
\operatorname{Tr}[(\rho_+-\rho_-)A\otimes B]
=2\epsilon\operatorname{Tr}(A^2)\operatorname{Tr}(B^2)
=2\epsilon>0.
\]

Therefore there cannot exist a universal function `F_R` satisfying

\[
q_{AB}(\rho_{AB})=F_R(q_A(\rho_A),q_B(\rho_B))
\]

for all correlated bipartite states whenever the joint resource window can access such a product correlation.

This is a proof, not an inference from the numerical audit.

## Smallest decisive witness

At `d_A=d_B=2`, choose

\[
A=B=\frac{1}{\sqrt 2}\operatorname{diag}(1,-1),
\qquad \epsilon=1/4.
\]

Then both `rho_+` and `rho_-` are valid mixed states, their two local density matrices are exactly `I/2`, but

\[
\left|\langle A\otimes B\rangle_{\rho_+}-\langle A\otimes B\rangle_{\rho_-}\right|=1/2.
\]

Dimension 1 is correctly recorded as degenerate because it has no nonzero traceless local observable.

## Surviving composition object

The exact restricted joint state must contain an independent correlation sector.  A useful bookkeeping decomposition is

\[
q_{AB}=q_A\otimes q_B+\Gamma_R,
\]

where `Gamma_R` vanishes for product states but in general is not determined by `q_A` and `q_B`.

This equation is a decomposition/definition, **not** yet a new PDT law.  A genuine PDT-native advance would have to derive the allowed structure, resource scaling, dynamics, or composition rule of `Gamma_R` from PDT principles and obtain a consequence beyond standard quantum/operator-system theory.

## Stress audit

The explicit diagonal family is checked for local dimensions

`1,2,...,12,16,24,32,48,64,96,128`.

For every tested nondegenerate dimension, the local marginals agree to machine precision, both constructed states remain positive, and the joint product-observable separation is positive and agrees with the analytic value `2/d^2` for the symmetric `d x d` audit.

## Prior-art boundary

This result is deliberately not promoted as historically novel. The general phenomenon belongs to the established quantum-marginal/global-correlation literature; correlation-matrix/tensor descriptions likewise explicitly retain information that is absent from local Bloch vectors or marginals. Relevant prior-art classes include the quantum marginal problem and Bloch/correlation-tensor treatments of bipartite states.

## Consequence for PDT-II

The Cycle-070 product-state quotient law survives exactly, but its unrestricted correlated extension is **FALSIFIED**. Any viable PDT-native composition law must carry a correlation/coupling sector (or an equivalent operator-level object) that cannot be reconstructed from the local quotient states alone.
