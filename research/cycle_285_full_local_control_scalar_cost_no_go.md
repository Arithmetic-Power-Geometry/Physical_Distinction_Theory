# PDT-II Cycle 285 — scalar interface cost fails even with full local control

## Status

- **PROVED (finite-dimensional control model):** equal scalar interaction cost does not select a unique two-system interaction even when *all* local one-qubit unitaries are freely admissible.
- **IMPORTED/KNOWN:** two-qubit local-unitary/KAK canonical classification and its nonlocal invariants.
- **FALSIFIED:** `complete local controls + one scalar interface norm/cost => unique joint interface up to local equivalence`.
- **OPEN:** a PDT-native principle selecting the nonlocal interaction orbit from distinction/resource data.
- **BREAKTHROUGH CANDIDATE:** NO.

## Stronger counterexample than Cycle 284

Cycle 284 used restricted local controls. Here local control is maximal: `SU(2) x SU(2)`.

Write a two-qubit interaction Hamiltonian as

`H(J) = sum_{i,j in {x,y,z}} J_ij sigma_i tensor sigma_j`.

Under local unitaries, the real coupling matrix transforms as `J -> R_A J R_B^T`, with `R_A,R_B in SO(3)`. Therefore the singular values of `J` are invariants of the local orbit (up to the familiar canonical/Weyl identifications).

Take

`J_1 = diag(1,0,0)`

and

`J_2 = diag(1/sqrt(2),1/sqrt(2),0)`.

They have the same Frobenius scalar cost:

`||J_1||_F = ||J_2||_F = 1`.

But their singular-value multisets are respectively

`{1,0,0}` and `{1/sqrt(2),1/sqrt(2),0}`,

so no local rotations `R_A,R_B` can map one to the other. Hence no full local-unitary pre/post processing can erase the distinction between these interaction orbits.

Thus even with complete local implementation data and maximal local control,

`(Lambda_A, Lambda_B, C_scalar)`

is insufficient to determine the composite interaction orbit.

## Exact algebraic witness

A polynomial invariant avoiding numerical SVD is

`I_4(J) = tr[(J^T J)^2]`.

For the examples,

`I_4(J_1)=1`, while `I_4(J_2)=1/2`,

even though the quadratic scalar cost `I_2(J)=tr(J^T J)=1` agrees. This is an exact obstruction.

The construction embeds into larger local dimensions by adjoining spectator levels, so the failure is not a qubit-only rescue for dimension selection.

## Prior-art gate

This mechanism is not PDT novelty. Canonical/KAK decompositions and local invariants of two-qubit nonlocal operations are established quantum-control/quantum-information mathematics. The PDT contribution here is only the negative design constraint: a scalar interface budget cannot be promoted to a PDT-native composition selector, even after granting full local control.

Representative prior art checked in this cycle:

- Zhang, Vala, Sastry & Whaley, *Geometric theory of nonlocal two-qubit operations*, Phys. Rev. A 67, 042313 (2003), DOI 10.1103/PhysRevA.67.042313.
- Bullock & Brennen, *Canonical decompositions of n-qubit quantum computations and concurrence*, J. Math. Phys. 45, 2447 (2004), DOI 10.1063/1.1723701.

## Surviving PDT-II target

The composition object must retain nonlocal orbit information, e.g. a structured joint/interface datum `J_AB` or its complete operational equivalence class. Merely enriching a scalar resource tuple by another scalar interaction cost cannot solve composition.

A genuinely PDT-native advance would need to derive constraints selecting an allowed nonlocal orbit/equivalence class from independently motivated distinction principles, and then survive comparison with the same-input quantum/GPT/control description.
