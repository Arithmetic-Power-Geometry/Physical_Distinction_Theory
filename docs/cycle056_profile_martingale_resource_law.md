# Cycle 056 — Distinction-Profile Martingale Resource Law

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT structural bridge.**

This is not a historical novelty claim and is not promoted to BREAKTHROUGH CANDIDATE.

## Hypotheses

Let `P,Q` be finite probability distributions with `Q_i>0`. Let `K(j|i)` be a finite stochastic resource map. Draw `I~Q` and then `J~K(.|I)`. Define the likelihood-ratio distinction variable

\[
L(I)=\frac{P_I}{Q_I}.
\]

The degraded experiment is `P'=KP`, `Q'=KQ`, with likelihood ratio

\[
L'(j)=\frac{P'_j}{Q'_j}.
\]

## Theorem 1 — resource degradation is conditional expectation

For every accessible output `j`,

\[
\boxed{L'(j)=\mathbb E_Q[L\mid J=j].}
\]

Proof:

\[
\mathbb E_Q[L\mid J=j]
=\frac{\sum_i Q_i K(j|i)(P_i/Q_i)}{\sum_iQ_iK(j|i)}
=\frac{\sum_iK(j|i)P_i}{\sum_iK(j|i)Q_i}
=\frac{P'_j}{Q'_j}.
\]

Thus a stochastic resource restriction is a martingale projection of the full distinction profile, not an arbitrary scalar contraction.

## Corollary 1 — simultaneous contraction of all convex distinction functionals

For every convex `phi`, Jensen gives

\[
\boxed{\mathbb E_{Q'}\phi(L')\le \mathbb E_Q\phi(L).}
\]

Hence the entire family of finite binary f-divergence-type functionals contracts at once. Total variation is recovered from `phi(x)=|x-1|/2`.

The exact loss is the Jensen gap

\[
\boxed{
\Delta_\phi(K;P,Q)
=\mathbb E_Q\phi(L)-\mathbb E_{Q'}\phi(L')\ge0.
}
\]

This is a non-tautological resource-revelation accounting law because both terms are independently defined operational functionals of the pre- and post-resource experiments.

## Theorem 2 — local resource maps commute with independent composition

For independent binary experiments `(P_A,Q_A)` and `(P_B,Q_B)`, their profile variable composes multiplicatively:

\[
L_{AB}=L_A L_B.
\]

For local resource maps `K_A,K_B`,

\[
(K_AP_A)\otimes(K_BP_B)=(K_A\otimes K_B)(P_A\otimes P_B)
\]

and similarly for the reference distributions. Therefore

\[
\boxed{
L'_{AB}=\mathbb E[L_A L_B\mid J_A,J_B]
=\mathbb E[L_A\mid J_A]\,\mathbb E[L_B\mid J_B].
}
\]

So composition and local resource degradation are exactly compatible at the profile level.

## Why this matters for PDT-II

Cycle 055 established that scalar distinction does not close under composition, whereas the full likelihood-ratio distinction profile does. Cycle 056 now shows that the same profile also carries stochastic resource refinement naturally: coarse resource access is conditional expectation, refinement restores dispersion in convex order, and independent composition is compatible with local resource maps.

This gives one exact mathematical object supporting both target (1) composition and target (4) resource revelation. It does **not** yet provide a PDT-native nonclassical state/effect composition law.

## Prior-art boundary

The ingredients are established statistical-experiment and probability theory: likelihood-ratio representations, Blackwell comparison, martingale/convex-order characterizations, Jensen/data-processing, and f-divergences. Therefore PDT should claim only the structural synthesis/application unless a genuinely PDT-native nonclassical extension is derived.

## Exact audit

Deterministic exact-rational tests used 200 randomized full-support experiments/resource kernels for every input dimension `n=1,...,12` (2400 cases). Results:

- conditional-expectation identity failures: **0**;
- tested convex-functional contraction failures: **0**.

Regression tests additionally verify compatibility of local resource maps with independent tensor composition.

## Remaining kill tests

1. Extend carefully to singular supports using Radon–Nikodym/infinite likelihood components rather than silently dividing by zero.
2. Test whether a profile object richer than the classical binary likelihood-ratio law can be derived from PDT primitives for nonclassical states/effects.
3. Determine whether a PDT-native admissibility axiom restricts profile composition beyond ordinary Blackwell/statistical-experiment theory.
4. Do not promote this result as a breakthrough unless those nonclassical/PDT-native steps survive prior-art and counterexample search.
