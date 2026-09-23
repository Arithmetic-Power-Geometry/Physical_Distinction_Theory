# Cycle 347 — No-restriction hypothesis boundary

Status date: 2026-09-23

## Target
Test whether the no-restriction hypothesis (NRH)—taking the physically allowed effects to be the full positive dual interval of the state cone—can serve as the missing PDT-native selector for (i) composite structure, (ii) a non-circular n=3 derivation, or (iii) a same-input PDT/QM probability deviation.

## Exact hypotheses
For a finite-dimensional ordered state space `(V,V_+,u)`, NRH takes every affine effect `e` satisfying `0 <= e <= u` on normalized states as physically allowed. Candidate inference under attack: NRH plus local PDT distinction structure uniquely selects the composite and/or n=3.

## Proof / counterexample
The inference is false.

1. Classical n-level theory: normalized states form the simplex `Delta_n`; the full dual interval gives all response vectors `e_i in [0,1]`. Hence NRH holds for every finite n.
2. Complex quantum n-level theory: normalized states are density operators on `C^n`; the full dual interval is exactly the POVM-effect interval `0 <= E <= I`. Hence NRH also holds for every finite n.
3. These two theory families are operationally inequivalent for every nontrivial n, yet both satisfy NRH. Therefore NRH does not select complex quantum theory, does not select n=3, and cannot by itself entail a PDT/QM probability difference.
4. More strongly, NRH fixes the local effect set relative to a chosen state cone; it does not by itself supply a unique correlated composite cone. Thus it cannot repair the composition underdetermination established in Cycle 345.

The smallest nontrivial witness is n=2: a classical bit and a qubit both satisfy NRH but have inequivalent state geometry. The same construction holds exactly for n=2..12 and all finite n. n=1 is degenerate and also satisfies NRH.

## Adversarial checks
- Edge case n=1: both constructions collapse to a one-state theory; no dimension selection.
- n=2: smallest decisive inequivalent pair.
- n=3: nothing singular occurs in either family.
- n=4..12: same algebraic construction.
- Higher n: proof is dimension-independent.
- Pure/mixed states: NRH concerns the entire normalized convex state space and its dual effect interval, so restricting attention to pure states does not rescue uniqueness.
- Alternative composites: because the hypothesis is local state/effect duality, a separate joint-state rule is still required.

## Prior-art boundary
NRH is standard GPT/convex-operational structure, not PDT-native. It is therefore classified IMPORTED/KNOWN. The Cycle-347 contribution is only the explicit PDT-II rejection test and theorem-status boundary; no novelty is claimed for NRH itself.

## Classification
- No-restriction hypothesis: **IMPORTED/KNOWN**.
- Classical all-finite-n NRH family: **PROVED**.
- Complex-quantum all-finite-n NRH family: **PROVED**.
- `NRH => n=3`: **FALSIFIED**.
- `NRH => unique PDT composition`: **FALSIFIED**.
- `NRH => P_PDT(O|I,R) != P_QM(O|I,R)`: **FALSIFIED as an inference**.
- PDT-native intrinsically joint selector: **OPEN**.
- Breakthrough candidate: **NO**.

## Consequence for the search
Do not spend further cycles trying to derive PDT-II from unrestricted local effects alone. Any surviving composition candidate must add a genuinely joint, non-circular constraint and must then be checked against classical, quantum, and GPT countermodels before promotion.
