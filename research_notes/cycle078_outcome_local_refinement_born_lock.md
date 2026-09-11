# Cycle 078 — Outcome-local refinement Born lock

## Question attacked

Can PDT obtain a same-input quantitative deviation from quantum mechanics by applying an arbitrary nonlinear positive score to the unchanged microscopic Born weights

\[
q_i=\operatorname{Tr}(\rho E_i)
\]

and normalizing the scores?

The candidate class is

\[
P_i^{\rm cand}=\frac{f(q_i)}{\sum_j f(q_j)},
\qquad f:[0,1]\to[0,\infty),\quad f(0)=0,\quad f(x)>0\;(x>0).
\]

This strictly contains the power family attacked in Cycle 077.

## Exact hypotheses

1. The microscopic state, effects and declared resource window are unchanged relative to the QM comparison.
2. The candidate law is outcome-local: an outcome score depends only on its own QM weight `q_i` through one common function `f`.
3. `f(0)=0` and `f(x)>0` for every `x>0`.
4. Purely classical splitting of an outcome into labelled sub-outcomes, followed by forgetting that label, cannot change the probability of the original coarse physical event.

## Theorem

Under the four hypotheses above,

\[
f(x+y)=f(x)+f(y),\qquad x,y\ge0,\ x+y\le1.
\]

Because `f` is nonnegative, additivity makes it monotone: if `0<=x<=y`, then

\[
f(y)-f(x)=f(y-x)\ge0.
\]

For rational `m/n` in `[0,1]`, additivity gives

\[
f(m/n)=\frac{m}{n}f(1).
\]

Monotonicity and rational approximation then imply for every real `x in [0,1]`

\[
\boxed{f(x)=c x},\qquad c=f(1)>0.
\]

The normalization cancels `c`, so

\[
\boxed{P_i^{\rm cand}=q_i=\operatorname{Tr}(\rho E_i)}.
\]

### Why refinement invariance forces additivity

Let a coarse outcome have weight `q=x+y` and let the other outcomes contribute positive total score `C`. Before splitting,

\[
P_{q}=\frac{f(x+y)}{f(x+y)+C}.
\]

After splitting and recoarsening,

\[
P_{x\lor y}=\frac{f(x)+f(y)}{f(x)+f(y)+C}.
\]

Equality for the same coarse physical event and `C>0` implies

\[
f(x+y)=f(x)+f(y).
\]

## Small decisive witness when the condition is violated

For the nonlinear score `f(q)=q^2`, use the unchanged qubit weights

\[
q=(3/4,1/4).
\]

The candidate coarse probability of the first event is

\[
\frac{(3/4)^2}{(3/4)^2+(1/4)^2}=\frac{9}{10}.
\]

Classically split that first event into two half-labelled copies, so the refined weights are

\[
(3/8,3/8,1/4).
\]

Recoarsening the first two labels gives

\[
\frac{2(3/8)^2}{2(3/8)^2+(1/4)^2}=\frac{9}{11}.
\]

Therefore the same coarse physical event changes probability solely because an irrelevant classical label was introduced.

## Stress audit

The executable regression audit covers dimensions

`1..12, 16, 24, 32, 48, 64, 96, 128`

with 20 random positive probability vectors/splits per dimension (380 random cases total). Representative score functions were

- `f(q)=q`;
- `q^2`;
- `sqrt(q)`;
- `exp(q)-1`;
- `q + 0.5 q(1-q)`.

Results frozen in `results/cycle078_outcome_local_refinement_born_lock.json`:

- linear score: 0/380 failures, maximum numerical residual `1.1102230246251565e-16`;
- each sampled nonlinear score: 380/380 strict refinement shifts.

The numerical audit is regression evidence only. The theorem is analytic and is not inferred from the sampled families.

## Counterexample search / scope boundary

The theorem deliberately does **not** eliminate every imaginable same-input modification. It does not cover:

- explicitly measurement-context-dependent assignments;
- resource-dependent assignments that cannot be reduced to a function of one scalar `q_i`;
- genuinely multipartite/nonlocal operational laws;
- models that alter the microscopic state/effect dynamics, which would no longer satisfy the stated same-input protocol.

Those routes must be attacked separately for no-signalling, composition, refinement and prior-art consistency.

## Prior-art boundary

This result must not be sold as a new derivation of the Born rule. Its mathematical mechanism is the classical additive Cauchy functional equation: a bounded/nonnegative additive function on a finite interval is linear. Gleason-type and generalized-measurement results independently establish much broader noncontextual probability constraints. In particular, Busch (Phys. Rev. Lett. 91, 120403, 2003) obtains a Gleason-type result using generalized observables/effects, and Caves, Fuchs, Manne and Renes (2003) derive the quantum rule from POVM frame functions including the qubit case. The Cycle-078 contribution is therefore a PDT **kill test** specialized to outcome-local same-input scalar deformations, not a novelty claim.

## Classification

- `PROVED`: refinement consistency forces additivity and hence a linear score under the stated hypotheses.
- `FALSIFIED`: every genuinely nonlinear outcome-local normalized-score candidate is excluded under those hypotheses.
- `NUMERICALLY SUPPORTED`: dimension/family stress audit agrees with the theorem.
- `IMPORTED/KNOWN BOUNDARY`: Cauchy additivity and generalized Gleason/POVM constraints are established mathematics/quantum foundations.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## Consequence for PDT-II

A defensible target-(3) deviation can no longer come from a nonlinear scalar reweighting of each unchanged Born weight while retaining arbitrary classical split/recoarse invariance. The surviving search must introduce a genuinely PDT-derived relational/resource variable whose operational meaning survives irrelevant relabellings and whose law is then tested against no-signalling, composition, convex mixing and existing GPT/resource-theory results.
