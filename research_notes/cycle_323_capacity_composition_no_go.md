# PDT-II Cycle 323 — capacity/composition arity no-go

## Target
Attack the strongest unresolved PDT-II obligations: PDT-native composition and a non-circular n=3 selector.

## Candidate principle
Let N be operational distinguishability capacity (maximum perfectly distinguishable alternatives) and K(N) the finite number of real fiducial coordinates required to specify a state. Assume:

H1. K:N+ -> N+ is strictly increasing.
H2. Independent composition is locally tomographic at the parameter-count level: K(mn)=K(m)K(n).
H3. Capacity composes multiplicatively: N_AB=N_A N_B.
H4. No dimension-specific constant or target value is inserted.

Question: can H1-H4 select physical arity n=3, or provide a PDT-native composite selector?

## Result
**FALSIFIED as an n=3/composition selector.**

The hypotheses are dimension-uniform. Established operational-reconstruction prior art already contains the stronger conclusion that strictly increasing completely multiplicative finite parameter counts have the hierarchy

K(N)=N^r,  r=1,2,3,...

under the corresponding regularity/integrality assumptions. Every member of this hierarchy is defined for every positive integer N. Thus neither multiplicative capacity nor multiplicative fiducial dimension singles out N=3. In particular, r=1 (classical scaling) and r=2 (complex quantum scaling) both satisfy the multiplicative equations for N=1,...,12 and for arbitrary finite N. Selecting r=2 in Hardy's reconstruction requires additional assumptions (continuity plus simplicity); this is imported prior art, not a PDT-native result, and still does not select N=3.

## Exact stress table
For N=1,...,12 the two smallest established hierarchy members are:

| N | K_r=1 | K_r=2 |
|---:|------:|------:|
|1|1|1|
|2|2|4|
|3|3|9|
|4|4|16|
|5|5|25|
|6|6|36|
|7|7|49|
|8|8|64|
|9|9|81|
|10|10|100|
|11|11|121|
|12|12|144|

For every m,n in 1..12, (mn)^r=m^r n^r exactly for r=1,2; the same identity is algebraic for all finite m,n and every integer r>=1. Degenerate capacity N=1 is also admitted. No singularity, extremum, closure failure, or distinguished fixed point occurs at N=3.

## Smallest decisive counterexample to uniqueness
At N=2, K=2 and K=4 already realize distinct parameter-count laws satisfying the same multiplicative form. Therefore multiplicativity cannot uniquely determine even the local state-space scaling, much less correlated composite geometry. N=3 merely gives K=3 versus K=9 and is not selected.

## Consequence for same-input prediction
H1-H4 contain no probability rule beyond parameter counting. Hence they cannot entail a parameter-free same-input inequality P_PDT(O|I,R) != P_QM(O|I,R). Quantum scaling K=N^2 is itself an admissible member.

## Prior-art gate
Lucien Hardy, *Quantum Theory From Five Reasonable Axioms*, quant-ph/0101012, explicitly derives K=N^r from subspace/composition assumptions and then uses additional continuity/simplicity assumptions to select quantum scaling. Therefore the hierarchy and its use as a reconstruction route are IMPORTED/KNOWN and must not be promoted as PDT novelty.

## Status
- Multiplicative capacity/parameter composition -> n=3: **FALSIFIED**.
- Multiplicative capacity/parameter composition -> unique composite law: **FALSIFIED**.
- K=N^r hierarchy under the cited reconstruction hypotheses: **IMPORTED/KNOWN**.
- Exact N=1..12 multiplicativity stress: **PROVED** (elementary identity).
- Same-input PDT/QM deviation from H1-H4: **FALSIFIED as an inference**.
- PDT-native correlated-composite selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
A viable next candidate must add genuinely PDT-native structure that constrains correlated composite directions rather than only product capacity/parameter counts, and it must be checked against operational/GPT reconstruction prior art before any novelty claim.
