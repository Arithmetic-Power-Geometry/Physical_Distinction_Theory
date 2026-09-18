# Cycle 232 — Refinement / Revelation Conservation No-Go

## Target
PDT-II target (4): determine whether a PDT-native **scalar conservation law of accessible distinction** follows from refinement/revelation primitives alone.

## Candidate attacked
A tempting candidate is that for a closed reversible system-environment evolution, a scalar distinction quantity carried by the observed subsystem should be conserved under refinement/revelation.

## Exact counterexample
Take a classical bit system S and bit environment E. Compare two microscopic preparations

- H0: (S,E)=(0,0)
- H1: (S,E)=(1,0).

Initially S perfectly distinguishes H0 from H1. Apply the reversible CNOT permutation

    U(s,e)=(s,e xor s).

Now discard S and retain E. E perfectly distinguishes the hypotheses. Conversely, if the controlled operation is chosen as

    V(s,e)=(s xor e,e)

with E initially fixed at 0, E retains zero local distinction while S retains it. More generally, reversible global dynamics can redistribute distinguishability among S, E and correlations. Therefore no nontrivial **local scalar conservation law** follows from reversibility alone.

A sharper erasure witness uses the reversible SWAP map with E initially fixed: local distinction can move completely from S to E while global microscopic distinguishability is unchanged. Hence a claim such as

    D_S(before) = D_S(after)

is false even for finite classical reversible dynamics.

## Dimension stress test
The binary witness embeds into every finite alphabet n >= 2 by restricting dynamics to labels {0,1}; n=1 is degenerate. Thus the obstruction applies exactly to n=2,...,12 and algebraically to every n>=2. It is independent of Euclidean/trace/TV norm choice whenever the chosen distinguishability separates the two deterministic point states.

## Surviving theorem
What survives is conditional:

> If D is a divergence invariant under reversible bijections/unitaries on the **full declared closed system**, then D(global before)=D(global after). After restriction/coarse-graining to a subsystem, only a data-processing inequality can generally be asserted for contractive divergences.

This is not a PDT-native conservation theorem. It is inherited from the selected divergence and transformation class.

## Controlled-environment / Markovian boundary
The counterexample is already deterministic, reversible and Markovian at the global level, so adding stochastic, non-Markovian, mixed-state, or thermodynamic structure cannot rescue unconditional local conservation. Environment records must be explicitly included in the declared resource window if one wants a global accounting identity.

## Prior-art boundary
This surviving statement lies inside established information theory / quantum information: distinguishability measures such as relative entropy obey data processing under channels; equality is tied to sufficiency/recovery (Petz-type results), and resource theories of distinguishability already treat distinguishability as an operational resource. Therefore PDT must not claim ordinary DPI, reversible invariance, or recoverability as new.

## Consequence for same-input prediction
A PDT-vs-QM difference cannot be manufactured by letting PDT count an environment record while the QM comparator traces it out (or vice versa). The microscopic preparation, controlled environment, retained algebra/records, measurement and resource window must be identical on both sides.

## Status
- Local scalar distinction conservation from reversibility alone: **FALSIFIED**.
- Global reversible invariance for an explicitly invariant divergence: **CONDITIONAL / IMPORTED-KNOWN**.
- Contractive coarse-graining law (DPI): **IMPORTED/KNOWN**.
- PDT-native refinement/revelation conservation law stronger than these: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next obligation
Search for a PDT-native **accounting identity with an explicit record/correlation term**, derived from PDT primitives rather than chosen entropy/divergence machinery; then test whether it collapses to chain rules, mutual information, Blackwell order, sufficiency/recovery, or standard resource-theory monotones before assigning novelty.
