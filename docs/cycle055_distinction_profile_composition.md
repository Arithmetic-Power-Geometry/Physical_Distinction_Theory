# Cycle 055 — Exact distinction-profile composition

## Status

**PROVED + IMPORTED/KNOWN mathematics + PDT structural candidate.** Not a BREAKTHROUGH CANDIDATE.

## Hypotheses

Let `P,Q` and `R,S` be finite probability distributions. For the theorem below assume the reference distributions `Q,S` have full support. Define the likelihood-ratio distinction profile

\[
\mu_{P|Q}=\sum_i Q_i\,\delta_{P_i/Q_i}.
\]

It is a probability measure on nonnegative likelihood-ratio values and has first moment one.

## Exact composition theorem

For ordinary independent composition,

\[
(P,Q)\otimes(R,S)=(P\otimes R,Q\otimes S),
\]

its distinction profile obeys

\[
\boxed{\mu_{P\otimes R\mid Q\otimes S}=\mu_{P|Q}\circledast_\times\mu_{R|S}},
\]

where multiplicative convolution is

\[
(\mu\circledast_\times\nu)(A)=\iint 1_{xy\in A}\,d\mu(x)d\nu(y).
\]

Proof: under `Q\otimes S`, the composite likelihood ratio factorizes pointwise,

\[
\frac{P_iR_j}{Q_iS_j}=\frac{P_i}{Q_i}\frac{R_j}{S_j},
\]

and the reference weight also factorizes as `Q_i S_j`. Grouping equal products gives the stated convolution exactly.

Equivalently, for the log-likelihood profile `L=log(P_i/Q_i)`, independent composition is ordinary additive convolution because `L_AB=L_A+L_B`.

## Recovery of scalar distinction

Total variation is a projection of the profile:

\[
D_{TV}(P,Q)=\frac12\int |\lambda-1|\,d\mu_{P|Q}(\lambda).
\]

Hence

\[
D_{TV}(P\otimes R,Q\otimes S)=\frac12\iint |\lambda\eta-1|\,d\mu_{P|Q}(\lambda)d\mu_{R|S}(\eta).
\]

This explains the earlier scalar non-closure result: `D_A,D_B` discard the shape of the two profiles, whereas exact product composition depends on that retained likelihood-ratio geometry.

## Algebraic consequences

The profile product is associative and commutative, with identity `delta_1`. Thus the full profile provides an exact closed composition object for finite full-support classical binary experiments, whereas scalar total variation does not.

## Stress test

Exact rational arithmetic was used on 200 randomized full-support four-distribution constructions for each dimension `n=1,...,12`, plus 50 trials each for `n=16,24,32,48,64`. No profile-composition or total-variation recovery failure was observed. This computation checks the implementation; the theorem itself is algebraic and does not depend on numerical evidence.

## Prior-art boundary

This construction is rooted in standard likelihood-ratio / binary-experiment / f-divergence mathematics. In particular, f-divergences are expectations of functions of `dP/dQ` under `Q`, and comparison-of-experiments theory routinely represents binary experiments through likelihood-ratio or posterior distributions. PDT therefore must not claim historical novelty for likelihood-ratio sufficiency or convolution under independent products.

The PDT-specific value is structural: it identifies a minimal-looking richer object that survives the scalar-composition no-go and gives an exact composition candidate to test against resource quotients, nonclassical state/effect cones, and experimentally meaningful PDT extensions.

## Remaining kill tests

1. Extend rigorously to singular supports using an extended likelihood-ratio profile including mass at infinity.
2. Determine whether resource coarse-graining acts on profiles by a monotone Markov transformation and characterize equality.
3. Test whether a nonclassical PDT analogue exists that is not merely a restatement of classical binary experiment theory.
4. Do not infer a unique quantum/GPT composite, `n=3`, Born rule, or same-input PDT!=QM prediction from this theorem alone.
