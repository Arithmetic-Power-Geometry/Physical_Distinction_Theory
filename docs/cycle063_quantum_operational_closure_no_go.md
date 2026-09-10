# Cycle 063 — Quantum operational-closure no-go

## Status

**PROVED + IMPORTED/KNOWN mathematics + DECISIVE FALSIFICATION of a PDT-II route.**

This is not a historical novelty claim and is not a `BREAKTHROUGH CANDIDATE`.

## Target attacked

PDT-II target (3): obtain a same-input quantitative prediction

\[
P_{\rm PDT}(O\mid I,R)\ne P_{\rm QM}(O\mid I,R)
\]

under identical microscopic inputs `I` and the same declared resource window `R`.

## Operational-closure theorem

Fix a finite-dimensional experiment, possibly multi-partite or multi-time. Suppose PDT retains all of the following ingredients of the QM comparator:

1. the same density operators / initial quantum state;
2. the same tensor-product composition of systems;
3. the same quantum channels or, more generally, the same process tensor / quantum comb;
4. the same interventions and POVM effects;
5. the same Born/generalized-Born probability pairing;
6. the same classical conditioning, marginalization and stochastic post-processing used to define resource window `R`.

Then for every outcome record `O`, microscopic input `I` and resource window `R`,

\[
\boxed{P_{\rm PDT}(O\mid I,R)=P_{\rm QM}(O\mid I,R).}
\]

Therefore a bookkeeping-only PDT extension cannot generate a same-input empirical deviation from QM.

## Proof

For a one-time measurement, identical state `rho` and POVM effect `E_o`, together with the same Born pairing, imply directly

\[
p_{\rm PDT}(o\mid I)=\operatorname{Tr}(\rho E_o)=p_{\rm QM}(o\mid I).
\]

For a multi-time experiment, the generalized Born rule contracts the same process tensor/comb with the same intervention sequence. Equal tensors and equal interventions therefore produce the same joint record distribution. This includes Markovian and non-Markovian dynamics.

Let `K_R` be any common classical stochastic map implementing the declared resource restriction, coarse-graining, detector relabeling, retained-record map, or other classical post-processing. Linearity gives

\[
P_{\rm PDT}(\cdot\mid I,R)
 =K_R P_{\rm PDT}(\cdot\mid I)
 =K_R P_{\rm QM}(\cdot\mid I)
 =P_{\rm QM}(\cdot\mid I,R).
\]

Conditioning on an event of nonzero probability also preserves equality because the same numerator and denominator are used. Tensor products do not open a loophole: equal component states/channels/effects and the same tensor rule give equal composite operators before the same generalized Born contraction.

Hence at least one closure ingredient must change for a genuine same-input deviation.

## Exact surviving alternatives

A defensible target-(3) candidate must explicitly change at least one of:

- physical state assignment;
- composite/tensor rule;
- microscopic dynamics/process;
- admissible intervention/effect set in a way not already represented by the same QM resource restriction;
- probability law / state-effect pairing;
- physical coupling to the resource window itself.

Changing only notation, hidden bookkeeping, phenomenological fitting, classical coarse-graining, non-Markovian labels, ensemble decomposition labels, or a statistic computed from the same QM experiment cannot suffice.

## Why this is stronger than the earlier local no-go entries

Earlier branch results separately excluded classical coarse-graining, affine mixed-state-only deviations, nonlinear ensemble labels under ordinary steering, and non-Markovianity with the same process tensor. The present theorem closes their common parent class: **unchanged quantum operational primitives imply unchanged operational probabilities**.

This does not rule out PDT as a modified physical theory. It rules out claiming new same-input predictions while all operational primitives remain those of standard QM.

## Numerical regression audit

`cycle063_quantum_operational_closure_audit.py` independently evaluates the Born probabilities in two implementations (direct trace and spectral decomposition), then tests common stochastic resource maps and common unitary dynamics.

The committed audit specification covers:

- dimensions `n=1,...,12`, 100 trials each;
- higher dimensions `16,24,32,48,64`, 20 trials each;
- alternating pure and mixed states;
- random three-outcome POVMs;
- random unitary dynamics;
- random stochastic resource-window maps.

Local reproduction of the committed algorithm with seed `63063` produced 1,300 cases, zero failures, maximum direct implementation gap `1.11e-15`, maximum post-processed gap `1.33e-15`, maximum unitary-sector gap `1.11e-15`, and maximum normalization error `4.66e-15`. These numerical checks are regression evidence only; the theorem is algebraic.

## Prior-art boundary

The ingredients are established quantum operational mathematics. Process tensors/quantum combs encode multi-time experiments through generalized Born rules; standard finite-dimensional quantum theory uses density operators, quantum channels and POVMs, with probabilities fixed by the Born pairing. Therefore no historical novelty is claimed for the closure theorem itself.

Relevant prior-art anchors include:

- Milz, Sakuldee, Pollock & Modi, *Kolmogorov extension theorem for (quantum) causal modelling and general probabilistic theories*, **Quantum 4, 255 (2020)**, DOI: `10.22331/q-2020-04-20-255`.
- Berk, Garner, Yadin, Modi & Pollock, *Resource theories of multi-time processes: A window into quantum non-Markovianity*, **Quantum 5, 435 (2021)**, DOI: `10.22331/q-2021-04-20-435`.
- White et al., *What can unitary sequences tell us about multi-time physics?*, **Quantum 9, 1695 (2025)**.
- Nakahira, *Two Operational Principles Single Out Quantum Theory* (2026 preprint), arXiv:`2605.23217`, as a recent reconstruction-oriented comparison point.

## Consequence for the breakthrough search

Target (3) is now more sharply constrained. The next candidate must specify an explicit new physical primitive and calculate a nonzero same-input probability gap while passing positivity, normalization, no-signalling/causality, composition, resource-window and prior-art tests. A correction term without such a changed primitive is rejected before simulation.
