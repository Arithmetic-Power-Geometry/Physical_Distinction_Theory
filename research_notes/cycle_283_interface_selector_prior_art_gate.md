# Cycle 283 — joint-interface selector: prior-art gate before theorem search

## Target
PDT-II target (1), following Cycle 282: determine whether the missing joint interface `J_AB` can be selected from distinction principles without silently importing a standard composite axiom.

## Current logical boundary
Cycle 282 proved that complete local implementation/control data do not determine the joint reachable family: identical local qubit controls give Lie closure dimension 6 without an interaction and 15 after adding an entangling `ZZ` coupling. Thus a composition theorem must either (a) take genuinely joint/interface data as input or (b) derive that joint structure from an additional physical principle.

## Candidate route audited
A tempting route is to choose `J_AB` by demanding a generic information/distinction principle (for example no-signalling, local consistency, or an information-processing constraint) and then regard the selected composite as PDT-native.

This route is **not presently promotable**. GPT prior art already treats local systems as compatible with multiple composite state/effect spaces between minimal and maximal tensor constructions, and information-theoretic principles have explicitly been proposed to constrain those composites. Consequently, merely imposing such a principle would not constitute a PDT-native derivation unless the principle itself follows from the finite-resource distinction primitive and yields a theorem stronger/different from the existing GPT/operational reconstruction literature.

## Prior-art collision checked this cycle
- GPT composite non-uniqueness and minimal/maximal tensor constructions are established.
- Information-causality-style principles have already been used to constrain/rationalize quantum composition.
- Operational/circuit frameworks already encode composition through explicit wiring/interface structure.

These facts do **not** prove that no PDT-native selector exists. They do rule out claiming novelty for the generic move “add an information principle to choose a composite.”

## Status
- Local implementation data -> unique joint interface: **FALSIFIED** (Cycle 282).
- Generic information principle -> novel PDT composition merely by relabelling it in distinction language: **IMPORTED/KNOWN route; REJECT AS NOVELTY CLAIM**.
- The theorem “no PDT-native selector can exist”: **NOT PROVED; do not claim**.
- PDT-native derivation of `J_AB` from finite-resource distinction: **OPEN**.
- Non-circular PDT-native `n=3`: **OPEN**.
- Same-input `P_PDT != P_QM`: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Stronger next attack
Search for a specifically resource-relative composition constraint that is absent from ordinary GPT composition: a theorem relating *joint admissible experiment closure* to independently specified implementation resources, with explicit interface costs and monotonicity under resource refinement. Any candidate must first be tested against minimal/maximal GPT tensors, ordinary quantum tensor composition, circuit/process theories, and controllability. A useful result must survive those collisions and must not obtain `n=3` by inserting local tomography or an equivalent known reconstruction axiom.
