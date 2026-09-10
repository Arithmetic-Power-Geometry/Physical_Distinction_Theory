# Cycle 057 — Singular-support repair of the distinction profile

## Status

- Unaugmented likelihood-ratio profile beyond full support: **FALSIFIED**.
- Augmented singular-support profile: **PROVED**.
- Historical novelty: **IMPORTED/KNOWN mathematics + PDT structural repair**.
- Breakthrough candidate: **NO**.

## Smallest decisive counterexample

Take `P=(0,1)` and `Q=(1,0)`. The Q-weighted finite likelihood-ratio profile contains only lambda=0 with unit Q-weight. Therefore the unaugmented formula gives

`(1/2) E_Q |lambda-1| = 1/2`,

while the true total-variation distance is `TV(P,Q)=1`.

Hence the Cycle-055 full-support representation cannot simply be extended to singular supports without an additional singular component.

## Repaired object

Let

`s(P||Q) = P({i : Q_i=0})`

and, on the Q-supported outcomes, let `mu_{P|Q}` be the Q-weighted distribution of the finite likelihood ratio `lambda_i=P_i/Q_i`.

Then

`TV(P,Q) = 1/2 [ s(P||Q) + integral |lambda-1| d mu_{P|Q}(lambda) ]`.

This follows by splitting the L1 sum into indices with `Q_i=0` and `Q_i>0`.

## Exact independent composition

For independent pairs `(P,Q)` and `(R,S)`, the singular mass composes as

`s_AB = 1-(1-s_A)(1-s_B)`

because a product draw from `P x R` is QxS-regular iff both local draws lie in the corresponding reference supports.

On the regular sector, likelihood ratios multiply, so

`mu_AB = mu_A circledast_x mu_B`,

where `circledast_x` denotes multiplicative convolution.

Thus the augmented object `(s,mu)` closes exactly under ordinary independent composition, including zero-probability and mutually singular edge cases.

## Why this matters for PDT-II

This is a correction, not a breakthrough. It blocks an invalid extension of the full-support distinction-profile law and identifies the minimal extra datum needed for singular-support closure. Any PDT-native nonclassical profile candidate must handle analogous singular sectors explicitly rather than hiding them in an infinite likelihood ratio convention.

## Verification

Exact rational tests cover 200 deterministic-seed cases for each dimension n=1,...,12, including distributions with zeros. The stored audit has zero TV-recovery failures and zero augmented-profile composition failures.

## Prior-art boundary

The repair is an application of standard Radon-Nikodym/Lebesgue decomposition ideas and total-variation measure theory. No historical novelty is claimed for separating absolutely continuous and singular parts.
