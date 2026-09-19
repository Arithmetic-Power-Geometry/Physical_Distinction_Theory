# Cycle 254 — No-hiding selector boundary

## Candidate
Test whether a PDT-native conservation/revelation principle of the form “a distinction erased from an accessible subsystem must be recoverable in its environment rather than residing only in correlations” can (i) determine the composite rule or (ii) non-circularly select n=3.

## Exact hypotheses
Let S carry an arbitrary finite-dimensional quantum state and let an isometric/unitary dilation encode it into S+E. Suppose the final reduced state of S is independent of the input. Candidate selector: the missing input distinction is wholly recoverable from E and cannot be stored only in S:E correlations.

## Prove-or-falsify result
**FALSIFIED as an n=3 selector.** Braunstein and Pati's no-hiding theorem is dimension-independent. A particularly transparent survivor family exists for every finite n: take dim(S)=dim(E)=n, initialize E in |0>, and apply SWAP. Then |psi>_S|0>_E -> |0>_S|psi>_E. The S output is input-independent and the entire unknown state is recoverable from E. This works unchanged for n=1,2,3,...; n=2 is already a decisive nontrivial competitor to n=3.

**FALSIFIED as a unique composition selector.** The statement presupposes an S:E composite Hilbert space, a partial trace/reduced-state notion, and a unitary/isometric dilation. Those are composition/dynamics ingredients rather than consequences of no-hiding. Therefore using the standard theorem to derive the PDT tensor/composition rule would be circular. The no-hiding condition can constrain information flow inside an already-specified composite but cannot by itself specify the full admissible composite state/effect cones.

## Dimension and edge stress
`experiments/cycle254_no_hiding_dimension_stress.py` checks n=1..12 exactly at the basis/permutation level. For each n it verifies: (1) SWAP is an involution; (2) all basis inputs leave S in label 0; and (3) E exactly recovers the input basis label. Linearity extends the displayed SWAP identity from basis states to every pure state, and density-matrix linearity extends it to mixed states. Thus the witness is analytic for arbitrary finite n; the script is a regression check rather than the proof of the full no-hiding theorem.

Edge cases: n=1 is degenerate but consistent. n=2 is the smallest nontrivial counterexample to dimension selection. The construction includes a controlled environment record and is reversible globally, so apparent local erasure is exactly transfer, not destruction.

## Prior-art boundary
- S. L. Braunstein & A. K. Pati, *Quantum Information Cannot Be Completely Hidden in Correlations: Implications for the Black-Hole Information Paradox*, Phys. Rev. Lett. 98, 080502 (2007), DOI 10.1103/PhysRevLett.98.080502. They prove the no-hiding theorem and emphasize its dimension-independent robustness.
- H. Zhu, *Hiding and masking quantum information in complex and real quantum mechanics*, Phys. Rev. Research 3, 033176 (2021), DOI 10.1103/PhysRevResearch.3.033176, strengthens hiding/masking boundaries and also shows restricted real-state sets have subtleties; therefore broad hiding slogans must not be promoted as PDT novelty.

Therefore the standard no-hiding/conservation route is **IMPORTED/KNOWN**, not PDT-native novelty.

## Status ledger
- SWAP survivor for every finite n: **PROVED** analytically; n=1..12 exact regression implemented.
- General quantum no-hiding theorem: **IMPORTED/KNOWN**.
- No-hiding as unique n=3 selector: **FALSIFIED**; smallest nontrivial competitor n=2.
- No-hiding as unique composition selector: **FALSIFIED** / circular if standard tensor-product dilation is assumed.
- “Local erasure implies global destruction”: **FALSIFIED** by the SWAP witness.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input P_PDT(O|I,R) != P_QM(O|I,R): **OPEN**.
- PDT-native experimentally distinctive inequality: **OPEN**.
- Gravity/capacity law: **OPEN**; no import permitted.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving requirement
A PDT-II conservation/revelation theorem must be stated without silently assuming the quantum tensor product, partial trace, or unitary dilation it seeks to explain. To advance the same-input prediction target, PDT must first supply an independently defined operational state/effect/dynamics rule under a declared resource window; otherwise P_PDT is not mathematically distinct from the imported quantum model.
