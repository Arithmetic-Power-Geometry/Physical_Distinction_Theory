# Cycle 079 — Calibrated resource-map Born lock

## Target attacked

PDT-II targets (3) and (5): seek a same-input quantitative prediction

\[
P_{\rm PDT}(O\mid I,R)\neq P_{\rm QM}(O\mid I,R)
\]

that survives the Cycle-078 no-go against positive outcome-local reweightings.

The natural next escape route is to let the declared resource window induce a transformation of the *whole operational state/effect pairing*, rather than reweight each Born outcome independently.

## Hypotheses

For fixed resource window `R`, let `p_R(E|rho)` assign a probability to every quantum effect `0 <= E <= I` and density operator `rho`. Assume:

1. **Effect coarse-graining / refinement consistency.** If `E,F >= 0` and `E+F <= I`, then

   \[
   p_R(E+F\mid\rho)=p_R(E\mid\rho)+p_R(F\mid\rho).
   \]

2. **Normalization.** `p_R(I|rho)=1`.

3. **Preparation convexity.** For `0 <= t <= 1`,

   \[
   p_R(E\mid t\rho+(1-t)\sigma)
   =t p_R(E\mid\rho)+(1-t)p_R(E\mid\sigma).
   \]

4. **Universal pure-state calibration.** For every rank-one projector `P`,

   \[
   p_R(P\mid P)=1.
   \]

The fourth condition says that an identically prepared sharp eigenstate remains certain for its identically specified sharp verification effect. If PDT changes this calibration, then the deviation is experimentally meaningful but is no longer an invisible re-description of the same calibrated microscopic input.

## Theorem — calibrated affine resource-map Born lock

Under hypotheses 1–4, in every finite dimension,

\[
\boxed{p_R(E\mid\rho)=\operatorname{Tr}(\rho E)}.
\]

### Proof

For each fixed `rho`, hypotheses 1–2 make `E -> p_R(E|rho)` a normalized additive probability assignment on effects. By the POVM/effect version of Gleason's theorem (Busch 2003; independently Caves, Fuchs, Manne & Renes 2004), there is a density operator `Phi_R(rho)` such that

\[
p_R(E\mid\rho)=\operatorname{Tr}[\Phi_R(\rho)E].
\]

This representation applies also to dimension two when all effects/POVMs are admitted.

Hypothesis 3 implies

\[
\Phi_R(t\rho+(1-t)\sigma)
=t\Phi_R(\rho)+(1-t)\Phi_R(\sigma),
\]

because equality of traces against all effects separates Hermitian operators. Thus `Phi_R` is affine on the state space.

Now take any rank-one projector `P`. Hypothesis 4 gives

\[
1=\operatorname{Tr}[\Phi_R(P)P].
\]

Since `Phi_R(P)` is a density operator, the expectation of a rank-one projector reaches one iff the state itself is `P`. Therefore

\[
\Phi_R(P)=P
\]

for every pure state projector. Every density operator is a convex combination of rank-one projectors, so affinity yields

\[
\Phi_R(\rho)=\rho
\]

for every density operator. Substitution gives the Born rule.

QED.

## What was falsified

The broad candidate claim

> A nonidentity affine resource map can produce a same-input probability deviation while retaining effect refinement, convex preparation mixing, and universal pure-state calibration.

is **FALSIFIED**.

Three standard nonidentity candidates were attacked numerically:

- depolarizing map,
- transpose map,
- nontrivial unitary conjugation.

All preserve affine preparation mixing; all yield additive probabilities in the effect variable when paired through the trace. But each fails universal pure-state calibration in every tested nondegenerate dimension. Dimension `d=1` is correctly degenerate.

## Regression audit

Dimensions tested:

`1..12, 16, 24, 32, 48, 64`

with five random trials per dimension and four maps (identity plus three nonidentity candidates), for 340 map cases total.

Recorded maxima:

- effect-additivity residual: `5.561946577567963e-17`,
- convex-preparation residual: `2.2458787007190695e-16`,
- identity-map calibration residual: `8.883072752094841e-16`.

Calibration failures above `1e-10`:

- identity: `0`,
- depolarizing: `80`,
- transpose: `80`,
- unitary conjugation: `80`.

The theorem is analytic; these numbers are regression/stress evidence only.

## Prior-art boundary

This is **not** promoted as a breakthrough. The central mathematical lock is a direct consequence of established effect/POVM Gleason-type results. Relevant prior art includes:

- P. Busch, *Quantum States and Generalized Observables: A Simple Proof of Gleason's Theorem*, Physical Review Letters 91, 120403 (2003), DOI 10.1103/PhysRevLett.91.120403.
- C. M. Caves, C. A. Fuchs, K. Manne, J. M. Renes, *Gleason-Type Derivations of the Quantum Probability Rule for Generalized Measurements*, Foundations of Physics 34 (2004), preprint quant-ph/0306179.
- V. J. Wright and S. Weigert, *Gleason-Type Theorems from Cauchy's Functional Equation*, Foundations of Physics 49, 594–606 (2019).
- J. Zhang, *Summing to uncertainty: On the necessity of additivity in deriving the Born rule*, Physical Review A, accepted 4 August 2026. This recent work explicitly emphasizes that additivity is an indispensable assumption in several Born-rule derivations.

## Classification

- **PROVED** — calibrated affine resource-map Born lock.
- **FALSIFIED** — nonidentity affine same-input resource map under all four hypotheses.
- **NUMERICALLY SUPPORTED** — regression audit across the stated dimensions.
- **IMPORTED/KNOWN BOUNDARY** — effect-Gleason representation is established prior art.
- **BREAKTHROUGH CANDIDATE: NO**.

## Surviving PDT-II route

Any genuine same-input PDT deviation must now relinquish at least one explicit assumption above. The scientifically clean possibilities are therefore sharply exposed rather than hidden:

1. a failure of effect coarse-graining/refinement additivity;
2. non-affinity under classical preparation mixing;
3. failure of exact pure-state calibration;
4. restricted measurement/effect domains insufficient for the effect-Gleason lock;
5. an additional dynamical/history/environment variable that means the compared operational input is genuinely richer than `(rho,E)`.

Routes 1–3 immediately create strong experimental or operational consequences and must be tested rather than assumed. Route 4 requires a physically derived PDT restriction, not an ad hoc deletion of measurements. Route 5 must declare the added microscopic variable explicitly before any claim of `P_PDT != P_QM` can count as a same-input prediction.
