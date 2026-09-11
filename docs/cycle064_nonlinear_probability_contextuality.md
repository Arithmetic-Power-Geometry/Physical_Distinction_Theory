# Cycle 064 — nonlinear probability deformation is contextual

## Target

PDT-II target (3): seek a genuine same-input quantitative prediction
`P_PDT(O|I,R) != P_QM(O|I,R)` without silently changing the operational
meaning of the input or resource window.

## Candidate route tested

Keep the standard quantum microscopic state `rho` and POVM effects `E_i`, form
the ordinary Born weights

`b_i = Tr(rho E_i)`,

but replace the Born rule by a completion-normalized nonlinear transform

`p_i = g(b_i) / sum_j g(b_j)`.

This is an attractive-looking way to obtain a numerical deviation while
retaining the same state and effects. The question is whether it can remain
noncontextual with respect to the physical effect being measured.

## Smallest explicit witness

Take a qubit in `rho = |0><0|` and retain the same effect

`E = diag(1/2,0)`.

Two legitimate POVM completions are

- `M2 = {E, I-E}`, with Born weights `(1/2,1/2)`;
- `M3 = {E,F,G}`, where `F=G=diag(1/4,1/2)`, with Born weights
  `(1/2,1/4,1/4)`.

For `g(x)=x^2`,

`p(E|M2)=1/2`,

while

`p(E|M3)=(1/2)^2/[(1/2)^2+2(1/4)^2]=2/3`.

Hence

`p(E|M3)-p(E|M2)=1/6`.

The density operator, retained effect, and microscopic Born weight of that
effect are identical; only the other effects completing the measurement have
changed. Therefore this nonlinear rule is measurement contextual.

## General surviving theorem

Assume a probability assignment to quantum effects is noncontextual in the
sense that the probability assigned to an effect depends only on that effect
(and the fixed preparation), not on which POVM contains it. Assume further
that probabilities are normalized on every POVM. Then generalized
Gleason/Busch-type theorems imply that the assignment is linear on effects and
is representable as

`p(E)=Tr(rho_* E)`

for a density operator `rho_*`.

Consequently, if PDT also insists on the *same* microscopic density operator
`rho_*=rho`, then the probability assignment is exactly the Born rule. A
same-input deviation while retaining the same quantum effect algebra must
therefore change at least one substantive operational assumption: the state
assignment, effect space, measurement noncontextuality, normalization/additive
structure, dynamics/composition, or the physical resource interaction.

For the narrower transform family

`p_i = g(b_i)/sum_j g(b_j)`,

completion invariance under arbitrary refinements forces additivity of `g` on
`[0,1]`; nonnegativity/regularity then forces `g(x)=c x`, and normalization
cancels `c`. Thus the Born weights are recovered. The power family
`g(x)=x^alpha` is therefore contextual for generic refinements whenever
`alpha != 1`.

## Stress tests

`cycle064_nonlinear_probability_contextuality.py` contains the exact rational
qubit witness and randomized split-completion tests. The construction embeds
in every larger finite dimension, so dimensions `1..12` are scanned as labels
of the ambient stress family and additional runs use `16,24,32,48,64,96,128`.
The algebraic witness, not random testing, establishes the falsification.

## Prior-art boundary

This is not claimed as a novel Born-rule theorem. Generalized effect/POVM
versions of Gleason's theorem are established prior art, including P. Busch,
"Quantum States and Generalized Observables: A Simple Proof of Gleason's
Theorem," *Physical Review Letters* 91, 120403 (2003), and C. M. Caves,
C. A. Fuchs, K. Manne, and J. M. Renes, "Gleason-Type Derivations of the
Quantum Probability Rule for Generalized Measurements," *Foundations of
Physics* 34, 193–209 (2004). The PDT contribution here is a target-specific
kill test and explicit minimal contextuality witness for a tempting nonlinear
same-input escape route.

## Status

- nonlinear completion-normalized deformation as a noncontextual same-input
  PDT route: **FALSIFIED**;
- explicit qubit witness: **PROVED**;
- generalized Born-rule uniqueness under effect noncontextuality/POVM
  normalization: **IMPORTED/KNOWN**;
- genuine same-input PDT deviation: **OPEN**.

This is not a BREAKTHROUGH CANDIDATE.
