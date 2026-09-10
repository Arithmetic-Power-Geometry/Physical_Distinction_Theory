# PDT-II Cycle 048 — Resource refinement, revelation, and conservation boundary

## Status

- **Resource-refinement monotonicity:** PROVED; IMPORTED/KNOWN mathematics.
- **Naive conservation of accessible distinction under refinement:** FALSIFIED.
- **PDT-native breakthrough claim:** none.

## Setup

Let `p` and `q` be two probability laws over a fine outcome space and let `K` be any stochastic coarse-graining kernel. Define operational distinction by total variation

\[
D(p,q)=\frac12\sum_i |p_i-q_i|.
\]

The coarse observer sees `Kp` and `Kq`; the refined observer sees `p` and `q`.

## Theorem 048-A — refinement monotonicity

For every stochastic kernel `K`,

\[
D(Kp,Kq)\le D(p,q).
\]

### Proof

For output index `j`,

\[
|(Kp)_j-(Kq)_j|
=\left|\sum_i K_{ij}(p_i-q_i)\right|
\le \sum_i K_{ij}|p_i-q_i|.
\]

Summing over `j` and using `sum_j K_ij=1` gives

\[
\sum_j |(Kp)_j-(Kq)_j|
\le \sum_i |p_i-q_i|.
\]

Dividing by two proves the claim.

If resource level `R_2` refines `R_1` and the `R_1` record is obtained from the `R_2` record by such a stochastic map, then

\[
D_{R_1}\le D_{R_2}.
\]

Thus additional admissible record resolution can reveal distinction that was inaccessible at the coarser resource level.

## Theorem 048-B — revelation increment bound

Define

\[
\Delta_{R_2\leftarrow R_1}=D_{R_2}-D_{R_1}.
\]

Then

\[
0\le \Delta_{R_2\leftarrow R_1}\le 1-D_{R_1}.
\]

The lower bound is Theorem 048-A and the upper bound follows from `D_R <= 1`. Both bounds are sharp.

## Decisive falsification — accessible distinction is not conserved

Take two fine outcomes and

\[
p=(1,0),\qquad q=(0,1).
\]

At the refined level,

\[
D(p,q)=1.
\]

Now merge both fine outcomes into one coarse outcome. Then

\[
Kp=Kq=(1),
\]

so

\[
D(Kp,Kq)=0.
\]

Therefore the proposed equality

\[
D_{R_1}=D_{R_2}
\]

for every resource refinement is false. The smallest counterexample has two fine outcomes. A nontrivial three-outcome version is obtained by merging only the first two outcomes and leaving the third separately visible.

The reveal can be maximal:

\[
\Delta=1.
\]

Accordingly PDT-II must not call accessible distinction itself a conserved quantity under resource refinement. Any genuine conservation law needs an enlarged quantity that explicitly includes hidden/environmental records or another independently defined complement; otherwise the equality is unsupported.

## Exact audit

`cycle048_resource_refinement_monotonicity.py` uses exact `Fraction` arithmetic. It checks dimensions/outcome counts `n=1,...,12` with 200 deterministic pseudo-random rational pairs and stochastic kernels per `n`. The maximum exact data-processing violation is zero in every tested dimension. The embedded witness gives fine TV `1` and coarse TV `0` for every `n>=2`.

See `results/cycle048_resource_refinement_audit.csv` and `tests/test_cycle048_resource_refinement_monotonicity.py`.

## Prior-art boundary

The contraction of statistical distance under stochastic processing is standard data-processing mathematics, and the broader information-order interpretation is closely related to Blackwell garbling. This cycle therefore claims no novelty for the inequality itself. The PDT-specific value is a disciplined boundary: **resource refinement supports monotone revelation, not conservation of accessible distinction.**

## Consequence for remaining PDT-II targets

A defensible PDT-native target is now narrower: derive, from PDT primitives rather than by definition, either (i) a conserved *total* distinction containing accessible plus inaccessible/environmental components with a non-tautological exchange law, or (ii) a quantitative resource-revelation law stricter than ordinary data processing and carrying a falsifiable prediction.
