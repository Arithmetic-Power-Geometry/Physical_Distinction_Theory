# PDT-II Breakthrough Lab — Cycle 332

## Target attacked
1. PDT-native composition law
2. Non-circular PDT-native n=3 derivation
3. Same-input PDT/QM discriminator

## Candidate principle
**Purification selector:** every mixed state has a purification by adjoining an environment; purifications of the same state are equivalent up to a reversible transformation on the purifying system.

## Exact hypotheses
For each finite system dimension n >= 1:
- states are density operators on C^n;
- composites use the ordinary complex Hilbert-space tensor product;
- reversible transformations include unitaries;
- every density operator rho admits a pure state |psi> on system+environment with Tr_E |psi><psi| = rho;
- any two minimal purifications of rho are related by a unitary on E (and nonminimal purifications by an isometry, after padding as needed).

## Proof / counterfamily
Let rho = sum_i lambda_i |i><i| be the spectral decomposition of any density operator on C^n. Define

|psi_rho> = sum_i sqrt(lambda_i) |i>_S |i>_E.

Then Tr_E |psi_rho><psi_rho| = rho. Hence purification exists for every finite n, including n=1,...,12 and all higher finite n. Unitary freedom of purification follows from the Schmidt decomposition / unitary equivalence on the purifying support.

Therefore purification is satisfied by an infinite family of dimensions. It has no exceptional closure, singularity, extremum, or consistency event at n=3.

### Smallest decisive witness
n=2 already satisfies purification. For rho = diag(p,1-p),

|psi> = sqrt(p)|00> + sqrt(1-p)|11>

purifies rho for every p in [0,1]. Thus any implication `purification => n=3` is false.

## Same-input consequence
Complex quantum theory itself satisfies purification. Therefore purification alone cannot logically entail a prediction P_PDT(O|I,R) != P_QM(O|I,R) under identical microscopic input I and resource window R. Any deviation requires an additional PDT-native operational law not already satisfied by ordinary quantum theory.

## Composition consequence
Purification is a strong constraint on an operational theory, but it is not by itself a derivation of a specifically PDT-native tensor/composition rule. Importing the standard quantum tensor product to demonstrate purification would be circular if that tensor product were then claimed as a PDT derivation.

## n=1..12 exact stress
See `cycle_332_purification_n1_n12.csv`. Every n is a pass. The CSV is not empirical data; it records the exact finite-dimensional construction above.

## Edge cases
- n=1: trivial pure state; purification holds.
- rank-deficient rho: omit zero Schmidt coefficients; purification still holds.
- pure rho: environment can be one-dimensional.
- maximally mixed rho: maximally entangled purification exists for every n.
- degenerate spectra: purification is basis-nonunique but remains valid.

## Prior-art audit
Purification as an operational principle and its role in reconstructions of quantum theory are established prior art, especially Chiribella, D'Ariano and Perinotti, *Probabilistic theories with purification*, Phys. Rev. A 81, 062348 (2010), DOI 10.1103/PhysRevA.81.062348, and the later reconstruction literature. The finite-dimensional purification theorem is standard quantum information. No PDT novelty is claimed for purification or unitary freedom of purification.

## Status ledger
| Claim | Status |
|---|---|
| Finite-dimensional complex QM admits purification for every n | IMPORTED/KNOWN |
| Explicit spectral/Schmidt construction above | PROVED |
| Purification selects n=3 | FALSIFIED |
| Purification uniquely derives PDT composition | FALSIFIED as an inference |
| Purification alone forces same-input PDT/QM deviation | FALSIFIED as an inference |
| PDT-native correlated-composite selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Surviving strengthened statement
Any proposed n=3 derivation whose hypotheses are all satisfied by ordinary finite-dimensional complex quantum theory for every n cannot select n=3 without an additional dimension-sensitive PDT-native axiom. The next attack must therefore target a genuinely PDT-defined distinction/refinement invariant rather than another generic reconstruction axiom.
