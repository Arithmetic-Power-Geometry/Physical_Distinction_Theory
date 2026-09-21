# Cycle 295 — Scalar resource budgets do not identify operational distinction

## Target
Attack PDT-II targets (1), (3), and (4): composition, same-input quantitative prediction, and resource refinement. Test whether a scalar declared resource budget R is sufficient to define a unique operational distinguishability or probability law.

## Candidate principle under test
Suppose a physical input I is fixed microscopically and an observer is assigned a scalar resource level R (cost, cardinality, rank, time, or another one-number budget). A tempting PDT formulation writes a unique prediction P_PDT(O|I,R), implicitly assuming that I and the scalar R identify the admissible operational interface strongly enough to determine outcome statistics/distinguishability.

This cycle tests that identifiability assumption. It is a candidate only, not a PDT axiom.

## Exact qubit counterexample
Fix the same microscopic binary input ensemble with equal priors:

rho_0 = |0><0|,
rho_1 = |1><1|.

Consider two resource implementations having the same scalar measurement count/cost: each permits exactly one binary projective measurement.

Implementation Z permits the computational-basis measurement { |0><0|, |1><1| }.
Implementation X permits the Hadamard-basis measurement { |+><+|, |-><-| }.

For the fixed inputs rho_0,rho_1:

- Under Z, the two outcome distributions are disjoint, so total-variation distinguishability D_Z = 1 and equal-prior discrimination succeeds with probability 1.
- Under X, both rho_0 and rho_1 give outcome distribution (1/2,1/2), so D_X = 0 and equal-prior discrimination succeeds only with probability 1/2.

Both implementations have the same naive scalar resource descriptor R = one binary projective measurement, yet their operational predictions differ maximally.

Therefore a scalar R that records only resource amount/cardinality/cost does not determine P(O|I,R) or operational distinguishability. The geometry/identity of the admissible operation set matters.

## Stronger abstract statement
Let M_R denote the admissible measurement/operation set. Operational distinction has the form

D(I; M_R) = sup_{M in M_R} d(p_M(.|I_0), p_M(.|I_1)).

If R does not uniquely determine M_R up to operational equivalence on the relevant inputs, then D(I;R) is not a well-defined single-valued quantity. Two sets M_R and M'_R can carry the same scalar budget label and yield different support functions/restricted distinguishability norms.

Thus a claimed same-input comparison

P_PDT(O|I,R) != P_QM(O|I,R)

is not yet falsifiable if R denotes only a scalar budget while the operational resource implementation is underspecified. A defensible comparison must hold fixed the full admissible instrument/measurement/channel class (or derive it from PDT), not merely a resource number.

## Resource-refinement law that survives
If the resource is represented by nested admissible sets M_R subseteq M_R' for R <= R', then by optimization-domain inclusion

D(I;M_R) <= D(I;M_R').

This monotonicity is exact but generic and not PDT novelty. A scalar ordering R <= R' alone is insufficient unless it is accompanied by, or proved to induce, this set inclusion/Blackwell-type operational refinement.

## Dimension stress
The decisive counterexample is a qubit. It embeds into every Hilbert dimension n >= 2 by using a fixed two-dimensional subspace and spectator dimensions. Hence the non-identifiability survives n=2 through n=12 and arbitrary higher finite n. Dimension n=1 is operationally degenerate for a binary orthogonal-state discrimination witness.

## Pure/mixed and noisy variants
The obstruction is not tied to perfect purity. For rho_0=(I+a Z)/2 and rho_1=(I-a Z)/2 with 0<a<=1, Z measurement yields TV=a while X measurement yields TV=0. Thus the same-resource non-identifiability persists continuously for mixed states and under reduced contrast.

## Prior-art boundary
Restricted-measurement distinguishability and the statistical norms induced by allowed measurement families are established quantum-information ideas; comparison/refinement of statistical experiments is also classical Blackwell/Le Cam territory. Therefore the counterexample mechanism and set-inclusion monotonicity are IMPORTED/KNOWN mathematics, not PDT novelty. The PDT value is the audit boundary: a scalar resource window is insufficient specification for a unique theory-vs-QM prediction.

## Status ledger
- scalar resource amount/cardinality alone uniquely determines operational distinction: **FALSIFIED**.
- same microscopic input + same scalar resource amount uniquely determines outcome/discrimination prediction: **FALSIFIED** unless the operational resource implementation is also fixed or derived.
- qubit Z-vs-X witness with D_Z=1, D_X=0: **PROVED**.
- mixed-state witness D_Z=a, D_X=0 for 0<a<=1: **PROVED**.
- embedding into n=2..12 and arbitrary higher finite dimension: **PROVED**.
- monotonicity under inclusion of admissible measurement sets: **PROVED / IMPORTED-KNOWN**.
- restricted-measurement norms and Blackwell/Le Cam comparison: **IMPORTED/KNOWN**.
- PDT-native derivation of the admissible operational resource family from a scalar/microscopic resource description: **OPEN**.
- fully specified same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next obligation
Do not write P_PDT(O|I,R) with R as an unspecified scalar budget and treat it as a unique prediction. Replace R operationally by a declared admissible family A_R (instruments, controls, measurements, channels, records, environment access, time/energy constraints), or derive A_R from PDT. Then search for a same-input deviation after QM and PDT are given exactly the same A_R. The strongest next target remains a PDT-native rule that determines or constrains A_R/interface composition without importing QM/GPT/resource-theory structure.