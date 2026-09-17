# Cycle 211 — Sequential-operational-equivalence no-go

## Target
PDT-II target (1): can a full *restricted sequential* intervention/decision profile select a unique resource-relative quotient when static Blackwell equivalence cannot?

## Status
- **PROVED (conditional no-go)**
- **FALSIFIED:** uniqueness from microscopic dynamics + full sequential decision equivalence under a declared restricted intervention/resource window
- **IMPORTED/KNOWN:** sequential operational equivalence, probabilistic bisimulation/process-tensor/quantum-comb ideas are established neighboring machinery
- **OPEN:** PDT-native principle that derives the admissible intervention algebra/resource window rather than presupposing it
- **BREAKTHROUGH CANDIDATE:** NO

## Exact construction
Let the microscopic state be

\[
X=(T,N_1,N_2)\in\{0,1\}^3,
\]

with deterministic microscopic dynamics

\[
F(T,N_1,N_2)=(T,N_1,0).
\]

Define two quotients

\[
q_A(T,N_1,N_2)=(T,N_1),\qquad q_B(T,N_1,N_2)=(T,N_2).
\]

Their autonomous quotient maps are

\[
\bar F_A(t,n)=(t,n),\qquad \bar F_B(t,n)=(t,0).
\]

Thus A has four fixed operational states and B has two. They are not dynamically isomorphic.

Now declare the resource window explicitly. At each time step the admissible controller may: (i) choose an intervention `do(T:=a)` with a in {0,1}, or do nothing; (ii) observe only the declared task coordinate T; and (iii) receive an arbitrary bounded reward depending on the finite history of chosen T-interventions and observed T-values. Nuisance coordinates are neither intervention targets nor reward/observation arguments.

## Theorem (restricted sequential profile does not select the quotient)
For every finite horizon h, every adaptive policy over the above admissible interventions, every initial distribution whose T-marginal is shared, and every bounded history-dependent reward functional of the admissible action/observation history, q_A and q_B induce exactly the same distribution over admissible histories and therefore exactly the same optimal sequential decision value. Nevertheless their autonomous quotient dynamics are non-isomorphic.

### Proof
The T-coordinate is invariant under F except when the controller itself sets T. Neither N_1 nor N_2 feeds into T. Therefore, conditional on any admissible history and chosen next action, the next observed T-value is determined solely by the previous T and the chosen T-intervention, identically under q_A and q_B. Induction on the horizon gives equality of the complete probability law of every admissible action/observation history for every adaptive policy. Equality of expected reward follows for every bounded functional of that history, hence equality of optimal values. But the quotient maps have respectively 4 and 2 fixed points, an isomorphism invariant. QED.

## Consequence
Even replacing static task-value matching by the *entire finite-horizon sequential decision profile* does not identify the operational quotient when the intervention/resource algebra leaves some coordinates operationally silent. The missing datum has moved again: PDT must independently derive why a particular intervention/observation algebra is physically admissible. If that algebra is stipulated, it can hide quotient-dynamical differences by construction.

This theorem is intentionally restricted. It does **not** claim equivalence under arbitrary interventions on N_1 or N_2, arbitrary full-state observations, or rewards that explicitly depend on nuisance coordinates. Such enlarged resource windows can distinguish the quotients and therefore are counterexamples to any unrestricted version of the claim.

## Dimension stress test
Embed the witness into n-bit microscopic spaces for every n>=3 by adjoining spectator bits S_1,...,S_{n-3} that neither affect T nor enter the admissible intervention/observation/reward algebra. The induction proof is unchanged. Exact tests cover n=3,...,12 and horizons 1,...,8; larger n follow analytically by spectator extension.

## Edge/degenerate cases
- n=1,2: this particular three-coordinate witness is unavailable; no claim.
- horizon 0: equivalence is vacuous.
- arbitrary initial nuisance correlations: allowed, provided the T-marginal used for comparing admissible histories is the same; nuisance never feeds T.
- Markovian versus hidden-memory nuisance dynamics: the theorem survives any nuisance evolution that cannot causally affect T inside the declared resource window.
- enlarging the admissible intervention algebra to probe nuisance coordinates destroys the theorem in general; this is a useful falsification boundary, not a defect.

## Prior-art boundary
The mathematical idea that processes are equivalent relative to an allowed tester/intervention class is established in probabilistic bisimulation, Markov decision/process abstraction, quantum combs and process tensors. Process-tensor distinguishability explicitly depends on physically admissible testers and obeying data-processing structure. Therefore the result is recorded as a PDT-II no-go boundary, not as a novelty claim.

## Next strongest attack
Test whether an independently motivated PDT resource-refinement law can force enlargement of the admissible tester algebra until all dynamically relevant distinctions become revealable, and whether such refinement admits a nontrivial monotone/conservation theorem rather than collapsing to full microscopic access.
