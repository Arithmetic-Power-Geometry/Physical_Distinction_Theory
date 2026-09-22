# PDT-II Cycle 322 — Thermodynamic record-cost selector

## Target
Test whether a PDT-native-looking thermodynamic requirement — that physically erased/released distinctions carry a minimum record-reset cost — can select n=3, determine composition, or force a same-input deviation from quantum mechanics.

## Candidate principle
For an n-valued record with distribution p=(p_1,...,p_n), reset into one standard state while coupled to an equilibrium bath at temperature T. Under the standard Landauer assumptions, the reversible lower bound is

Q_min >= k_B T H(p),

with H(p)=-sum_i p_i ln p_i (nats). For the maximally uncertain n-record, p_i=1/n,

Q_min >= k_B T ln n.

This is deliberately tested as a possible dimension/arity selector rather than assumed to be PDT-native.

## Prove-or-falsify assessment

### Claim A
`Minimum irreversible record cost singles out n=3.`

**Status: FALSIFIED.**

For every integer n>=1 the maximally uncertain record has H=ln n, hence normalized cost C_n := Q_min/(k_B T)=ln n. C_n is strictly increasing for n>0 and has no interior extremum, kink, fixed point, or algebraic singularity at n=3. Thus the thermodynamic erasure floor supplies no non-circular preference for n=3.

Exact symbolic stress for n=1,...,12 is simply C_n=ln n. Edge case n=1 gives C_1=0; binary, ternary, and all higher finite arities lie on the same smooth family.

### Claim B
`Landauer record cost supplies a PDT-native composition law.`

**Status: FALSIFIED as a PDT-native route / IMPORTED-KNOWN.**

For independent records p and q, Shannon additivity gives H(p tensor q)=H(p)+H(q), so the corresponding reversible erasure lower bound is additive. This is inherited from standard information thermodynamics, not derived uniquely from PDT. For correlated records the joint entropy includes mutual-information corrections, again standard information theory/thermodynamics. Therefore this route imports an established composition structure rather than deriving the missing PDT correlated-composite selector.

### Claim C
`Thermodynamic record cost forces a parameter-free same-input P_PDT != P_QM.`

**Status: FALSIFIED as an inference.**

Quantum mechanics is compatible with Landauer erasure bounds, with von Neumann entropy replacing classical Shannon entropy for quantum states. Therefore the candidate constraint is jointly satisfiable with ordinary QM. It does not alter a state, effect, Born probability, dynamics, or declared resource window and hence cannot by itself force P_PDT(O|I,R) != P_QM(O|I,R).

### Claim D
`A universal conservation law for distinction follows from the erasure bound.`

**Status: FALSIFIED as an inference.**

Landauer is a lower bound on thermodynamic cost under specified physical assumptions; it is not a conservation equation for an abstract distinction quantity. Correlations and side information change the relevant entropy accounting, and generalized formulations use conditional entropy. Equality additionally requires ideal reversible/quasistatic conditions. Thus a PDT conservation law cannot be inferred without new hypotheses.

## Edge/composite/resource audit
- n=1: zero information to erase, normalized lower bound 0.
- n=2,...,12: normalized lower bound ln n; no special n=3 feature.
- Independent composites: additive entropy/cost lower bound.
- Correlated composites: joint/conditional entropy matters; naive local additivity is not universal.
- Pure quantum state: von Neumann entropy zero; maximally mixed d-level state: entropy ln d.
- Rank-deficient/mixed states: cost tracks entropy, not Hilbert-space dimension alone.
- Controlled environment/side information: conditional entropy is the relevant generalized quantity; this blocks interpreting local entropy loss as a universal conserved PDT scalar.
- Finite-time/non-equilibrium implementations can exceed the reversible floor, so equality cannot be elevated to a universal dynamics law.

## Prior-art audit
Landauer's principle and its Shannon/von-Neumann entropy generalizations are established information thermodynamics. Experimental and theoretical quantum tests already connect erasure to entropy change. Generalized treatments with correlations/side information use conditional entropy. Therefore none of these ingredients may be claimed as PDT novelty.

## Surviving theorem/no-go boundary
**Thermodynamic arity no-go:** Any selector whose only n-dependence for a maximally uncertain finite record is the standard reversible erasure cost k_B T ln n cannot uniquely select n=3. More generally, any strictly monotone function f(ln n) with no externally supplied target value cannot select an interior finite n. A ternary preference would require an additional independently derived PDT scale, extremality condition, compositional obstruction, or resource threshold; inserting such a target solely to obtain n=3 would be circular.

This closes a tempting thermodynamic route while preserving thermodynamic settings as a future arena only after PDT independently derives a nonstandard operational quantity or constraint.

## Classification
- Standard Landauer erasure bound: **IMPORTED/KNOWN**.
- C_n=ln n for uniform n-record, all finite n: **PROVED / IMPORTED-KNOWN**.
- Landauer cost => n=3: **FALSIFIED**.
- Landauer cost as PDT-native composition law: **FALSIFIED as a native route**.
- Landauer cost => same-input PDT/QM deviation: **FALSIFIED**.
- Erasure bound => universal distinction conservation: **FALSIFIED as an inference**.
- Thermodynamic arity no-go stated above: **PROVED (conditional on stated selector class)**.
- PDT-native correlated-composite selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Parameter-free same-input PDT/QM prediction: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## References
1. R. Landauer, “Irreversibility and Heat Generation in the Computing Process,” IBM Journal of Research and Development 5, 183–191 (1961).
2. C. H. Bennett, “The Thermodynamics of Computation — a Review,” International Journal of Theoretical Physics 21, 905–940 (1982).
3. D. Reeb and M. M. Wolf, “An improved Landauer principle with finite-size corrections,” New Journal of Physics 16, 103011 (2014).
4. Generalized information-thermodynamic treatments with correlations formulate erasure cost using conditional entropy; this is prior art and not PDT-native.
