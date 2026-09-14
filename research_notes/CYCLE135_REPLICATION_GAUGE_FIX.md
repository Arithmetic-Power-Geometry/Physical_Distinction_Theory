# Cycle 135 — Replication Gauge Fix

## Result

**Classification:** PROVED (conditional), FALSIFIED (doubling-only sufficiency), IMPORTED/KNOWN (real-analysis period argument), NUMERICALLY SUPPORTED, OPEN (PDT-native derivation of replication extensivity).

Assume the surviving scalar ambiguity after quadratic revelation accounting has the form

\[
R=f(Q),\qquad Q\ge 0,
\]

with continuous `f`, normalization `f(1)=1`, and identical-copy extensivity for both two and three independent copies:

\[
f(2q)=2f(q),\qquad f(3q)=3f(q).
\]

Then necessarily

\[
\boxed{f(q)=q}.
\]

For `q=e^t`, define `h(t)=f(e^t)/e^t`. The two replication identities make `ln 2` and `ln 3` periods of `h`. Their ratio is irrational, since a rational ratio would imply an impossible equality `2^m=3^n` for positive integers. Integer combinations of two incommensurate real periods form a dense subgroup of the real line; continuity therefore makes `h` constant. Calibration fixes the constant to one.

This is useful because it weakens the previous open bridge. Full pairwise resolved-channel additivity is sufficient but is not necessary for fixing the scalar resource gauge. It is enough, within the scalar reparameterization class, to derive operational extensivity of identical independent replication at multiplicities 2 and 3 plus continuity.

## Decisive falsification: doubling alone is insufficient

For `0<epsilon<1/sqrt(1+(2*pi/ln2)^2)`, define

\[
f_\epsilon(q)=q\left[1+\epsilon\sin(2\pi\log_2 q)\right],\quad q>0,
\]

and `f_epsilon(0)=0`.

It is continuous, positive and strictly increasing. Its derivative is bounded below by

\[
1-\epsilon\sqrt{1+(2\pi/\ln 2)^2}>0.
\]

It obeys exact doubling extensivity,

\[
f_\epsilon(2q)=2f_\epsilon(q),
\]

while it is nonlinear and fails three-copy extensivity generically. With `epsilon=0.05`, the derivative lower bound is approximately `0.5440143812`.

Therefore

\[
\boxed{\text{continuity + monotonicity + 2-copy extensivity does not fix the resource gauge}.}
\]

The 3-copy condition removes this explicit log-periodic freedom because `ln 2/ln 3` is irrational.

## Stress audit

Dimensions tested: `1..12, 16, 24, 32, 48, 64, 96, 128`, 20 seeded random matrices per dimension (`380` cases).

- linear gauge 2-copy failures: `0`
- linear gauge 3-copy failures: `0`
- log-periodic gauge 2-copy failures: `0`
- log-periodic gauge 3-copy violations: `380/380`
- maximum relative 2-copy residual: `8.77e-16`
- maximum relative 3-copy residual: `0.10136`

These computations are regression evidence only; the theorem and counterexample are analytic.

## Prior-art boundary

The mathematical mechanism is standard real analysis/functional-equation machinery: a continuous real function with two incommensurate periods is constant after the logarithmic change of variables. No novelty is claimed for that theorem. The PDT-specific content is only the proposed operational interpretation of 2-copy and 3-copy independent replication as a possible gauge-fixing bridge.

## PDT-II implication

The strongest surviving obligation is now narrower:

\[
\boxed{\text{Can PDT primitives derive identical-copy extensivity for 2 and 3 independent replicas?}}
\]

If yes, and if the prior cycles' reduction to a continuous scalar reparameterization `R=f(Q)` is retained, the numerical resource gauge is fixed to the quadratic ledger without assuming arbitrary pairwise additivity.

**BREAKTHROUGH CANDIDATE: NO.** The replication laws themselves are not yet PDT-native derivations.
