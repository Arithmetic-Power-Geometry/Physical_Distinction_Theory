# Cycle 349 — Purification dimension boundary

## Target attacked
PDT-II target (2): non-circular PDT-native derivation of n=3, while also testing whether purification can supply the missing composition selector.

## Candidate principle
Purification: every mixed state of system A admits a pure bipartite extension on AB whose marginal on A is the original state, with purifications unique up to reversible transformations on the purifying system (in the standard operational formulation).

## Exact hypotheses
1. Finite-dimensional complex quantum state space of Hilbert dimension n.
2. Composite supplied by the ordinary complex Hilbert-space tensor product.
3. Purifying ancilla may have dimension at least rank(rho).
4. Reversible transformations on the purifying subsystem are unitary.

## Proof / counterexample family
Let rho be any density operator on C^n. Spectrally decompose

rho = sum_i lambda_i |i><i|,

where r = rank(rho) <= n. On C^n tensor C^r define

|Psi_rho> = sum_i sqrt(lambda_i) |i>_A |i>_B.

Then Tr_B |Psi_rho><Psi_rho| = rho. Standard purification uniqueness gives equivalence of purifications by an isometry/unitary on a sufficiently large purifying system. Nothing in this construction requires n=3. It works for every finite n.

Hence the implication

    purification => n=3

is false. The smallest nontrivial quantum counterexample is n=2: every qubit mixed state is purifiable, so purification cannot uniquely select n=3.

## n=1..12 stress
The attached CSV records the exact maximal ancilla rank needed for a generic full-rank n-level quantum state. Every n from 1 through 12 passes the existence construction. There is no n=3 singularity.

## Composition boundary
Purification is genuinely compositional because it refers to pure extensions. However, using the standard quantum purification construction already assumes a tensor-product composite and therefore cannot be advertised as a PDT-native derivation of that composite. Operational reconstructions can use purification together with additional axioms to characterize quantum theory, but that is established reconstruction machinery, not a new PDT-native composition law.

## Prior-art check
Chiribella, D'Ariano and Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), develops purification as an operational principle and proves major structural consequences. Their *Informational derivation of quantum theory*, Phys. Rev. A 84, 012311 (2011), derives finite-dimensional quantum theory from purification together with five other informational axioms. Therefore purification as a quantum reconstruction principle is IMPORTED/KNOWN.

## Status ledger
- Finite-dimensional complex-QM purification for every n: PROVED / IMPORTED-KNOWN.
- Purification => n=3: FALSIFIED. Smallest nontrivial counterexample n=2.
- Purification alone => PDT-native unique composition: OPEN as a PDT claim; standard quantum construction cannot establish it without importing the composite structure.
- Purification => same-input P_PDT != P_QM: FALSIFIED as an inference, because ordinary quantum theory itself satisfies purification.
- Purification as reconstruction machinery: IMPORTED/KNOWN.
- PDT-native intrinsically joint selector: OPEN.
- BREAKTHROUGH CANDIDATE: NO.

## Guardrail
No gravity/capacity claim is made. No experimental deviation is claimed. No novelty is claimed for purification or its standard consequences.
