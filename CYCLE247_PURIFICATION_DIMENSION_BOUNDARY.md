# Cycle 247 — Purification is not a PDT-native composition or n=3 selector

## Question attacked

Can the operational **purification principle** close the two strongest PDT-II obligations: (i) a PDT-native composition law and/or (ii) a non-circular derivation of physical dimension `n=3`?

## Exact hypotheses tested

Take the standard operational purification requirement: every mixed state of A is the marginal of a pure state of a larger composite AB, with purifications unique up to reversible transformations on the purifying system. Ask whether this condition, without inserting a dimension-specific constant or an already-quantum tensor rule as a PDT axiom, uniquely fixes the PDT composite or selects n=3.

## Result 247A — dimension-selector no-go

**Status: PROVED (within ordinary finite-dimensional complex quantum theory); FALSIFIED as an n=3 selector.**

For every finite n>=1 and every density operator rho on C^n with spectral decomposition

rho = sum_i p_i |i><i|,

the vector

|Psi_rho> = sum_i sqrt(p_i) |i>_A |i>_B

in C^n tensor C^n is pure and satisfies Tr_B |Psi_rho><Psi_rho| = rho. Therefore the existence of purification holds uniformly for n=1,2,3,... . It cannot logically privilege n=3.

The regression `tests/test_cycle247_purification_dimension_boundary.py` checks exact rational spectra for n=1,...,12. This is a regression witness, not the proof; the displayed Schmidt construction is the proof for arbitrary finite n.

Smallest decisive competitor to n=3: n=2. A mixed qubit state has a purification, so purification does not exclude n=2.

## Result 247B — composition-law provenance boundary

**Status: IMPORTED/KNOWN; FALSIFIED as PDT-native if adopted without an independent PDT derivation; OPEN as a source from which a genuinely new PDT restriction might later be derived.**

Purification is established operational-probabilistic-theory machinery. Chiribella, D'Ariano and Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), study exactly the principle that every mixed state has a purification unique up to reversible channels on the purifying system and show major consequences including reversible dilation and a Choi-Jamiolkowski-type state-transformation correspondence. Their later *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311 (2011), uses purification together with five additional informational axioms to derive finite-dimensional quantum theory. Therefore importing purification and its known consequences cannot count as a PDT-native breakthrough.

A second prior-art guard is important: Chiribella and Scandolo, *Entanglement as an axiomatic foundation for statistical mechanics* (2016), define sharp theories with purification and explicitly include both complex and real quantum theory (and a suitable extension of classical probability theory). Thus purification-based thermodynamic structure is not automatically a unique selector of complex QM either.

## Same-input prediction audit

**Status: OPEN.**

No same-input PDT-vs-QM probability difference follows from purification alone. If PDT simply adopts the standard purification structure, the construction supplies no new P_PDT(O|I,R). Claiming a deviation would require an independently specified PDT dynamical/probabilistic rule under the same microscopic input I and resource window R.

## Composition audit

**Status: OPEN.**

Purification constrains composites strongly, but this cycle does not prove that the axiom alone uniquely fixes an admissible tensor cone. More importantly for PDT novelty, the principle and its major structural consequences are prior art. A surviving PDT composition law must be derived from PDT primitives rather than relabeling purification, reversible dilation, or the Choi correspondence.

## Stress/edge cases

- n=1: degenerate and purifiable; no selector information.
- n=2: decisive non-3 survivor.
- n=3: survives, but not uniquely.
- n=4,...,12: exact rational-spectrum regression survivors.
- arbitrary finite n: covered analytically by Schmidt purification.
- pure states: trivial purification with a one-dimensional/uncorrelated ancilla.
- mixed states: Schmidt purification as above.
- controlled environment: already part of the established reversible-dilation interpretation of purification; therefore not PDT-native by itself.
- thermodynamics: sharp-theory-with-purification literature is an explicit prior-art boundary.

## Classification ledger

| Claim | Classification |
|---|---|
| Every finite-dimensional complex quantum state admits purification | IMPORTED/KNOWN; exact construction reproduced |
| Purification selects n=3 | FALSIFIED |
| Purification alone is a PDT-native composition breakthrough | FALSIFIED as provenance claim |
| Purification gives a same-input PDT != QM prediction | OPEN / not derived |
| A stronger PDT-native joint-admissibility law exists | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Consequence for the next cycle

Do not spend another cycle merely renaming purification or reversible dilation as "distinction conservation." The strongest remaining target is still an independently derived PDT joint-admissibility predicate J_PDT(A,B,R), followed by a genuinely dimension-sensitive feasibility condition C(n,R) that excludes n=2 and n>=4 without encoding 3 in its assumptions.
