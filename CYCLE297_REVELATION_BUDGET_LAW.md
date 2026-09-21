# Cycle 297 — Revelation budget law

Target: PDT-II resource refinement, revelation and conservation.

Fix one microscopic input family I and one operational distinguishability score. For an admissible operation family A define D_I(A) as the supremum of the score over operations in A.

## Theorem
Let A_0 be a subset of A_1, and so on through A_m. Define Delta_k = D_I(A_k) - D_I(A_{k-1}). Then:

1. Delta_k is nonnegative for every k.
2. The sum of all Delta_k equals D_I(A_m) - D_I(A_0).
3. Any two nested refinement paths with the same endpoints have the same total revelation, although their individual step gains may differ.

## Proof
Set inclusion preserves every previously available operation. Therefore optimizing the same score over A_k cannot produce a value below the optimum over A_{k-1}; each Delta_k is nonnegative. Summing the definitions cancels every interior D_I(A_k), leaving only D_I(A_m) - D_I(A_0). Applying this identity to two paths with common endpoints proves equality of their total gains. QED.

## Boundary and adversarial checks
Strict set refinement need not give positive gain: adding an operationally redundant procedure gives Delta_k = 0. Thus Cycle 296 remains decisive. Individual gains are path-dependent because an informative operation can be introduced early or late. Only the endpoint total is path-independent. Non-nested changes retain an algebraic signed telescoping identity but lose the interpretation as nonnegative revelation. Changing I, the score, or admissibility semantics between stages violates the hypotheses.

The proof is dimension-free, hence covers n=1 through n=12 and arbitrary higher finite dimension. It also covers degenerate cases. Classical, quantum, GPT, pure/mixed, composite, Markovian/non-Markovian, controlled-record and thermodynamic cases are covered only when their compared resource stages are genuinely nested under the same score.

## Novelty boundary
The mechanism is elementary optimization monotonicity plus telescoping and is not claimed as new mathematics. Resource theories and comparison of statistical experiments already use monotones under allowed transformations/refinements. PDT-specific value is architectural: the defensible conservation statement is conservation of total incremental revelation along a fixed-endpoint nested refinement, not local additive conservation and not strict revelation.

## Status
Weak refinement monotonicity: PROVED / IMPORTED-KNOWN mechanism.
Endpoint revelation-budget identity: PROVED, elementary, no novelty claim.
Path independence of total gain at fixed endpoints: PROVED.
Strict refinement implies strict revelation: FALSIFIED in Cycle 296.
Local additive distinction conservation: FALSIFIED in Cycle 294.
PDT-native criterion predicting informative refinements: OPEN.
Same-input quantitative PDT versus QM deviation: OPEN.
BREAKTHROUGH CANDIDATE: NO.
