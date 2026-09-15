# Cycle 156 — Affine/CP Escape Boundary for PDT-vs-QM Dynamics

## Status

- **PROVED (conditional structural implication):** If a deterministic PDT state-update law respects operational equivalence of classical preparation mixtures, then its action on density operators is affine on the convex state space. If, in addition, the law is required to act consistently on arbitrary untouched quantum reference systems, positivity of the joint output requires complete positivity of the affine/linear extension. Trace preservation then places the law inside the ordinary CPTP quantum-channel set.
- **FALSIFIED:** `make Lambda_R nonlinear/non-CP` is by itself a defensible route to a beyond-QM PDT prediction while retaining ordinary mixture equivalence and arbitrary-reference consistency.
- **IMPORTED/KNOWN:** convex operational state spaces; complete positivity/ancilla extension; Choi/Kraus/Stinespring channel theory; literature on nonlinear quantum evolution and signaling.
- **OPEN:** a PDT-native operational principle that changes one of these assumptions and yields a quantitative, internally consistent, experimentally distinctive prediction not reducible to a standard quantum channel/process description.
- **BREAKTHROUGH CANDIDATE:** NO.

## Theorem A — classical randomization forces affinity

Let `T_R` be a deterministic PDT transformation at fixed declared resource window `R`. Suppose a laboratory can prepare `rho1` with classical probability `p` and `rho2` with probability `1-p`, and suppose PDT respects the ordinary operational identification of that randomized preparation with density operator

`rho = p rho1 + (1-p) rho2`.

If forgetting the classical preparation flag cannot alter subsequent unconditioned outcome statistics, then for every effect `E`,

`Tr[E T_R(rho)] = p Tr[E T_R(rho1)] + (1-p) Tr[E T_R(rho2)]`.

Because effects separate density operators,

`T_R(p rho1 + (1-p) rho2) = p T_R(rho1) + (1-p) T_R(rho2)`.

Hence `T_R` is affine on the convex state space. Iteration gives finite-mixture affinity; continuity gives the usual real convex extension. A deterministic nonlinear map that assigns different unconditioned outputs to two ensemble decompositions of the same density operator therefore violates this preparation-mixture equivalence assumption.

## Theorem B — arbitrary-reference consistency forces CP

Take the affine map's standard linear extension on operators. Suppose the PDT transformation acts locally on system `A` while an arbitrary finite reference `B` is untouched. Requiring

`(T_R \otimes id_B)(omega_AB) >= 0`

for every positive joint state `omega_AB` and every finite reference dimension is exactly complete positivity. With normalization preserved, `T_R` is CPTP.

Therefore, under both operational assumptions,

`mixture equivalence + arbitrary-reference positivity + normalization => CPTP`.

Cycle 155 then applies: the transformation is already quantum mechanically admissible.

## Smallest decisive counterexamples to naive escape routes

### 1. Nonlinear ensemble-sensitive map

Consider a normalized nonlinear rule such as `N(rho)=rho^2/Tr(rho^2)`. It fixes pure states. But the maximally mixed qubit has many pure-state decompositions. Evolving the density matrix directly and evolving flagged ensemble components before forgetting the flag need not define the same operational procedure for general nonlinear rules. Thus nonlinearity is not a free escape: PDT must explicitly replace ordinary preparation-mixture equivalence and state what observable consequence follows.

### 2. Positive but non-CP map

Matrix transposition is positive and trace preserving on an isolated system, but `transpose \otimes id` applied to half of an entangled two-qubit state produces a non-positive operator. Thus isolated-state positivity is insufficient if arbitrary entangled references are admitted.

## Consequence for PDT-II target (3)

The search tree is now narrower.

1. Same state/channel/effect: Cycle 154 forces identical probabilities.
2. Different but CPTP PDT channel: Cycle 155 remains inside QM.
3. Deterministic nonlinear PDT map while preserving ordinary forgotten-mixture equivalence: excluded by Theorem A.
4. Linear/affine positive but non-CP map while allowing arbitrary untouched entangled references: excluded by Theorem B.
5. A legitimate PDT deviation must therefore identify and physically motivate the exact operational assumption it changes: preparation equivalence, reference-system composition, state/effect space, process structure, or another explicitly testable primitive.

This does **not** prove that every nonlinear theory signals or is inconsistent. Literature contains nonlinear evolutions designed to satisfy weaker no-signaling-related conditions. The defensible statement is only the conditional closure theorem above: retaining the stated mixture and arbitrary-reference assumptions closes the route back to CPTP quantum dynamics.

## Experimental inequality direction

A useful PDT experiment should therefore target the changed primitive itself. For example, if PDT predicts preparation-context dependence, compare two experimentally distinct randomized ensembles with the same reconstructed density matrix and pre-register a PDT-predicted probability gap. If PDT instead restricts reference composition, formulate an ancilla-assisted inequality. No numerical gap is claimed until PDT derives its magnitude without fitting the observed outcome.

## Dimension stress status

The implications are structural and dimension-independent for finite dimensions. They cover `n=1..12` and higher dimensions without Monte Carlo evidence. The smallest nontrivial ancilla witness for positivity-vs-complete-positivity occurs already for a qubit with a two-dimensional reference (e.g. transposition on half of an entangled pair). Numerical stress testing cannot replace or overturn these exact implications.

## Prior-art boundary

No novelty is claimed for affinity of operational transformations, complete positivity, or nonlinear-evolution signaling discussions. These are established quantum-foundations/quantum-information structures. Relevant boundary literature includes Choi/Kraus/Stinespring quantum operations and modern analyses of nonlinear quantum evolution and signaling. PDT novelty, if any, must be a newly derived physical reason to alter one closure assumption plus a quantitative prediction surviving existing experimental constraints.
