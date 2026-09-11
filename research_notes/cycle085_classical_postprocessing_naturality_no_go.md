# Cycle 085 — Classical post-processing naturality no-go

## Target attacked

PDT-II targets (3) and (5): can a same-input deviation from QM be obtained by taking the *entire* unchanged quantum output probability vector and applying a new relational/resource-aware transformation, rather than the outcome-local scalar reweightings already excluded in Cycles 077–078?

This cycle attacks a broad but explicit class of such proposals.

## Exact hypothesis class

For every finite outcome number `n`, suppose a candidate law supplies

\[
F_n:\Delta_n\to\Delta_n,
\]

where `Delta_n` is the probability simplex.  For the unchanged microscopic state, measurement, and declared resource window, QM supplies `q` and the candidate PDT-output-only deformation supplies `F_n(q)`.

Require **classical post-processing naturality**: for every column-stochastic matrix

\[
T:\Delta_n\to\Delta_m,
\]

representing ordinary classical relabelling, splitting, randomization, or coarse-graining after the physical measurement,

\[
\boxed{F_m(Tq)=T F_n(q)}.
\]

No continuity, differentiability, convex-linearity, outcome-locality, power-law form, or analyticity is assumed.

## Theorem — stochastic naturality lock

Under the hypotheses above,

\[
\boxed{F_n(q)=q}\qquad\text{for every finite }n\text{ and every }q\in\Delta_n.
\]

### Proof

`Delta_1` contains only the normalized distribution `(1)`, hence necessarily

\[
F_1(1)=1.
\]

Now choose an arbitrary `q in Delta_n`.  Define the `n x 1` column-stochastic channel

\[
T_q=\begin{pmatrix}q_1\\ \vdots\\ q_n\end{pmatrix}.
\]

It maps the unique singleton distribution to `q`:

\[
T_q(1)=q.
\]

Naturality therefore gives

\[
F_n(q)=F_n(T_q1)=T_qF_1(1)=T_q1=q.
\]

Since `q` and `n` were arbitrary, the family is identically the identity. QED.

## What this proves — and what it does not

This is a genuine no-go for **output-only** same-input deformations that are required to be transparent to all subsequent classical stochastic processing.

It is stronger than Cycle 078 in one direction: `F_n` may depend on the *whole probability vector* and can be nonlinear, nonlocal across outcomes, and dimension-dependent. The theorem still forces identity.

It does **not** exclude models in which:

- the proposed PDT resource is an additional physical variable carried through the experiment and transformed jointly with the classical record;
- the microscopic state, effect, or dynamics is physically changed;
- only a restricted class of classical channels is declared operationally admissible;
- the candidate explicitly makes the post-processing apparatus part of the microscopic input.

Any such escape must state that extra physics explicitly; it can no longer be described as merely a new map of the unchanged QM output distribution.

## Small decisive counterexample to nonlinear candidates

Take

\[
q=(3/4,1/4)
\]

and the normalized-square map

\[
F(q)_i=\frac{q_i^2}{\sum_jq_j^2}.
\]

Then

\[
F_2(q)=(9/10,1/10).
\]

Classically split the first outcome into two equal labels with

\[
T=\begin{pmatrix}1/2&0\\1/2&0\\0&1\end{pmatrix}.
\]

The two orders give

\[
F_3(Tq)=(9/22,9/22,2/11),
\]

but

\[
TF_2(q)=(9/20,9/20,1/10).
\]

The maximum component discrepancy is

\[
\boxed{9/110\approx0.08181818}.
\]

So this candidate changes its prediction depending on whether an otherwise classical splitting is applied before or after the proposed deformation.

## Numerical/adversarial audit

`cycle085_classical_postprocessing_naturality_no_go.py` stress-tests

`n = 1..12, 16, 24, 32, 48, 64, 96, 128`

with 20 random distributions and random column-stochastic maps per dimension.

Frozen results:

- 380 total random cases;
- 347 nontrivial-output (`m>1`) cases;
- identity family: maximum naturality residual `0.0`;
- direct singleton proof construction: maximum residual `0.0`;
- normalized `q^2`, `sqrt(q)`, and `exp(q)-1` families: 347/347 failures on nontrivial random channels.

The random audit is regression evidence only. The theorem is exact and does not depend on these sampled nonlinear families.

## Prior-art boundary

This must **not** be advertised as a new probability-theory theorem. The framework of stochastic/Markov kernels and probability monads already treats classical probability distributions functorially under stochastic maps. In particular, the Giry monad formalizes probability measures and Markov kernels, and categorical probability literature develops naturality of probabilistic constructions. The proof here is an elementary finite-simplex specialization: the terminal one-outcome simplex plus all stochastic maps already forces the identity natural endomorphism on distributions.

Relevant prior-art context checked in this cycle includes the standard category of Markov kernels / Giry monad and Sturtz (2017), *The factorization of the Giry monad* (arXiv:1707.00488), which explicitly studies probability measures through natural transformations. These sources establish the surrounding categorical-probability territory; no novelty is claimed for the mathematical mechanism.

## Classification

- `PROVED`: full stochastic-postprocessing naturality forces `F_n = id`.
- `FALSIFIED`: a genuinely different output-only same-input probability law cannot satisfy the stated naturality hypothesis.
- `NUMERICALLY SUPPORTED`: dimension/random-channel stress audit agrees with the theorem.
- `IMPORTED/KNOWN BOUNDARY`: stochastic maps, probability monads, and naturality are established probability/category theory.
- `BREAKTHROUGH CANDIDATE`: **NO**.

## PDT-II consequence

The surviving target-(3) route is now narrower. A defensible `P_PDT != P_QM` cannot be an after-the-fact deformation of the complete unchanged QM probability vector while remaining invariant under all ordinary classical post-processing. It must introduce a genuinely physical PDT variable or dynamics *before* the final classical probability record, and that new variable must then survive no-signalling, refinement, composition, calibration, and prior-art tests.
