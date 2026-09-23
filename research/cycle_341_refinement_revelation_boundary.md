# Cycle 341 — Resource refinement: strictness criterion and quotient boundary

## Status
PROVED (elementary operational theorem); novelty status: IMPORTED/KNOWN in relation to Blackwell/randomization and distinguishability preorders. Not a breakthrough candidate.

## Setup
For states/hypotheses x,y and an admissible measurement resource set R, define

D_R(x,y) = sup_{M in R} TV(p_M(.|x),p_M(.|y)).

Let R1 subseteq R2.

## Theorem 341.1 — exact strict-revelation criterion
D_R2(x,y) > D_R1(x,y) iff there exists M in R2 whose induced total-variation separation exceeds D_R1(x,y).

Proof: If such M exists, the supremum over R2 is at least its value and hence exceeds D_R1. Conversely, if D_R2>D_R1, by the defining property of a supremum there is an M in R2 with value >D_R1 (choose epsilon smaller than D_R2-D_R1). QED.

Corollary: set-theoretic strict refinement R1 proper-subset R2 is neither necessary nor sufficient for positive revelation about a fixed pair. What matters is operational nonequivalence relative to that pair.

## Definition — pair-relative operational quotient
R ~_{x,y} R' iff D_R(x,y)=D_R'(x,y). Resource windows should therefore be compared after quotienting away additions that do not improve the decision-relevant distinction.

## Theorem 341.2 — saturation obstruction
If D_R1(x,y)=1, every refinement R2 superset R1 has zero revelation increment because TV<=1. Hence universal strict revelation under every proper resource refinement is impossible in any theory admitting a perfectly distinguishable pair.

Smallest decisive witness: n=2. Take x,y perfectly distinguishable and R1 containing a distinguishing measurement; append any genuinely new measurement to form R2. Then R1 proper-subset R2 but D_R1=D_R2=1.

## Dimension stress
The witness embeds in classical n-level and complex quantum n-dimensional systems for every n>=2 by using two basis states. Therefore it applies exactly for n=2,...,12 and arbitrarily high finite n. n=1 is degenerate: no distinct state pair exists.

## Dynamics / records
Any Markovian or non-Markovian preprocessing, environment record, or thermodynamic setting can be absorbed into the admissible experiment/measurement family when the final comparison is performed on the same hypotheses. The set-inclusion theorem survives unchanged. This does not assert that physical dynamics always increases distinguishability; CPTP processing can contract it.

## Composition and n=3 consequences
These results do not select a tensor/composition rule and do not select n=3. They also provide no same-input PDT-vs-QM probability difference, because the theorem is representation-independent and ordinary classical/quantum theories satisfy it.

## Prior-art boundary
The operational content overlaps established Blackwell/randomization/channel-comparison and distinguishability-resource theory. Accordingly, the monotonicity/quotient idea is not claimed as PDT novelty. The useful PDT-II consequence is negative: any future native revelation law must be formulated on decision-relative operational resource classes and must add structure beyond mere resource inclusion.

## Classifications
- Refinement monotonicity: PROVED; IMPORTED/KNOWN operational structure.
- Exact strict-revelation criterion: PROVED.
- Universal strict revelation from proper set inclusion: FALSIFIED.
- Saturation obstruction: PROVED.
- n=3 selection from refinement/revelation: FALSIFIED.
- Unique PDT composition from this route: OPEN / not implied.
- Same-input PDT/QM discriminator from this route: OPEN / not implied.
- BREAKTHROUGH CANDIDATE: NO.
