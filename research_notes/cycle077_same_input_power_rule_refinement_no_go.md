# Cycle 077 — Same-input power-rule deviation fails operational refinement

## Target attacked

PDT-II target (3): obtain a defensible same-input quantitative prediction
`P_PDT(O|I,R) != P_QM(O|I,R)` under identical microscopic input `I` and declared
resource window `R`, without changing the input or smuggling in an undeclared
measurement context.

## Candidate family

Let the fixed microscopic quantum weights for a POVM be

\[
q_i = \mathrm{Tr}(\rho E_i), \qquad \sum_i q_i=1.
\]

Attack the normalized power family

\[
p_i^{(\alpha)}=\frac{q_i^{\alpha}}{\sum_j q_j^{\alpha}}, \qquad \alpha>0.
\]

For `alpha != 1` this gives a literal same-input deviation from the Born
probabilities. It must therefore survive operational-equivalence tests before it
can count as a PDT prediction.

## Exact refinement theorem

Split one outcome of weight `q>0` into two classically labelled sub-outcomes
with weights `t q` and `(1-t)q`, where `0<t<1`, and then forget the label again.
The combined numerator for that physical event changes from

\[
q^\alpha
\]

to

\[
[t^\alpha+(1-t)^\alpha]q^\alpha.
\]

For any nontrivial split, the bracket equals one for all `t` iff `alpha=1`.
If at least one competing event has positive weight, the normalized probability
of the coarse physical event therefore changes whenever `alpha != 1`.

Hence within this family:

\[
\boxed{\text{refinement consistency} \iff \alpha=1}
\]

apart from degenerate one-event/zero-competitor cases.

## Smallest decisive witness

Take the same qubit state and projective measurement throughout:

\[
\rho=\mathrm{diag}(3/4,1/4), \qquad q=(3/4,1/4).
\]

For `alpha=2`, before any split the first event has probability

\[
\frac{(3/4)^2}{(3/4)^2+(1/4)^2}=\frac{9}{10}.
\]

Now only relabel the first detector event into two equiprobable classical
sub-labels. The microscopic coarse event is unchanged; the weights are

\[
(3/8,3/8,1/4).
\]

After recombining the two labels, the candidate gives

\[
\frac{2(3/8)^2}{2(3/8)^2+(1/4)^2}=\frac{9}{11}.
\]

Thus the same coarse event shifts from `9/10` to `9/11` solely because an
irrelevant classical label was introduced.

## Stress audit

The executable audit tests dimensions 1–12 and 16, 24, 32, 48, 64, 96, 128,
20 random positive outcome distributions per dimension, and
`alpha in {0.5,0.75,1,1.5,2,3}`.

Generated result ledger:

- alpha=1 refinement failures: **0**
- maximum alpha=1 numerical residual: **1.11e-16**
- strict shifts for alpha != 1: **1900 / 1900**

The analytic argument is the proof; random tests are regression evidence only.

## Prior-art boundary

This is not a novelty claim about alternative power rules. Quartic/contextual
alternatives to the Born rule are already discussed in the foundations
literature, and Gleason/POVM-frame-function results delimit when noncontextual
probability assignments reduce to the trace rule. The PDT-specific value of
this cycle is as a kill test: a proposed same-input deviation that depends on
arbitrary outcome splitting is not a defensible resource-window prediction.

Relevant prior-art anchors include Gleason-type noncontextual probability
results and modern operational analyses of alternative outcome probability
functions. No claim of inventing those results is made.

## Classification

- **PROVED**: normalized power family is refinement-consistent for all
  nontrivial splits only at `alpha=1`.
- **FALSIFIED**: `alpha != 1` power rules as PDT same-input replacement laws
  under operational refinement equivalence.
- **NUMERICALLY SUPPORTED**: finite-dimensional stress audit.
- **IMPORTED/KNOWN BOUNDARY**: Gleason/POVM noncontextuality and previously
  studied quartic alternatives.
- **OPEN**: a genuinely PDT-native same-input deviation that survives
  refinement/coarse-graining, composition, no-signalling, and prior-art review.

## Consequence for PDT-II

Target (3) remains open. This cycle narrows it substantially: merely replacing
Born weights with a nonlinear normalized function is not enough. Any surviving
PDT probability law must depend only on operationally meaningful resource
structure and must be invariant under irrelevant classical refinements of the
same physical event. No BREAKTHROUGH CANDIDATE is promoted.
