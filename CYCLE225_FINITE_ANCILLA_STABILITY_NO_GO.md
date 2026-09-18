# Cycle 225 — Finite-Ancilla Stability No-Go

## Target attacked
PDT-II (1) PDT-native composition law and (2) non-circular n=3 derivation.

## Candidate principle
A subsystem operation is physically admissible when it remains positive/admissible after extension by all ancillas up to some fixed size k. Could bounded extension-stability select the composite law or force n=3?

## Exact hypotheses
Work in finite-dimensional complex matrix state spaces M_d(C). A linear map Phi is k-positive when id_k tensor Phi maps positive semidefinite operators to positive semidefinite operators. Complete positivity (CP) requires this for every ancillary dimension. For maps M_d(C)->M_m(C), Choi's theorem implies d-positivity is sufficient for CP.

## Result
**FALSIFIED / IMPORTED-KNOWN boundary.** Stability only through ancilla size k<d is not, in general, sufficient for complete extension stability. The hierarchy P_1 superset P_2 superset ... superset P_d=CP is nontrivial in matrix theory. Thus a PDT rule that checks only a dimension-independent bounded ancilla family cannot infer unrestricted composite admissibility in arbitrary dimension.

For d=3 this is directly relevant: checking positivity only on the isolated system or on a qubit ancilla does not by itself justify complete extension stability. A 3-dimensional ancilla is sufficient in ordinary complex matrix theory by Choi's theorem, but invoking that theorem imports the complex-quantum matrix composition structure; it is not a PDT-native derivation of n=3.

## Exact witness for failure of 1-extension
The transpose T_d(X)=X^T is positive for every d, but is not 2-positive for every d>=2. On the maximally entangled two-level vector |Omega_2>=(|00>+|11>)/sqrt(2),

(id_2 tensor T_d)(|Omega_2><Omega_2|)

contains the two-level partial transpose block with eigenvalues {1/2,1/2,1/2,-1/2}. Hence a local positivity test can certify an operation that fails immediately under a 2-dimensional reference extension. This witness embeds in every d>=2.

## n=1..12 stress statement
- d=1: degenerate; transpose is CP.
- d=2,...,12: the embedded two-level witness has minimum eigenvalue -1/2 exactly, so transpose is positive but not 2-positive.
- Higher d: the same 2x2 principal embedding gives the same obstruction; no random search is needed for this witness.

## Stronger surviving theorem
For ordinary complex matrix systems of input dimension d, d-positivity is sufficient for complete positivity (Choi). This is a finite stopping theorem, but it is **IMPORTED/KNOWN** and depends on the matrix/tensor structure PDT is trying to derive. Therefore it cannot non-circularly select PDT composition or explain why physical spatial/state dimension should be n=3.

## Consequence for same-input prediction
A purported PDT-vs-QM deviation obtained by declaring an operation admissible after testing only small ancillas is not yet a same-input physical prediction. In QM, physical channels are CP precisely to remain valid on arbitrary reference extensions. PDT must derive a different extension rule and expose a concrete microscopic implementation before such a discrepancy is experimentally meaningful.

## Prior-art boundary
This is standard operator-algebra/quantum-information structure: positivity versus complete positivity, Choi's d-positivity criterion, and positive-but-not-CP maps such as transposition are established. Therefore **BREAKTHROUGH CANDIDATE: NO**.

## Status ledger
- Bounded-ancilla stability uniquely fixes unrestricted admissibility: **FALSIFIED**.
- Positive implies physically valid under arbitrary extension: **FALSIFIED**.
- d-positivity implies CP for M_d complex matrix inputs: **IMPORTED/KNOWN (PROVED in prior art)**.
- PDT-native reason selecting the required extension depth: **OPEN**.
- PDT-native composition law: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT != QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Derive, rather than assume, what class of reference/ancillary extensions a physical distinction operation must survive. Any candidate must avoid presupposing the Hilbert-space tensor product whose emergence PDT-II is supposed to explain.
