# PDT-II Cycle 286 — two scalar interface invariants still do not select composition

## Status

- **PROVED (two-qubit coupling model):** even fixing both the quadratic interaction magnitude `I2(J)=tr(J^T J)` and quartic invariant `I4(J)=tr[(J^T J)^2]` does not select a unique nonlocal interaction orbit under full local `SU(2) x SU(2)` control.
- **FALSIFIED:** `complete local controls + (I2,I4) => unique joint interaction orbit`.
- **IMPORTED/KNOWN:** singular-value/local-orbit classification and finite moment non-uniqueness.
- **OPEN:** a PDT-native operational principle selecting a complete nonlocal orbit/equivalence class rather than appending ad hoc invariants.
- **BREAKTHROUGH CANDIDATE:** NO.

## Exact counterexample

Write the two-qubit interaction as

`H(J)=sum_{i,j in {x,y,z}} J_ij sigma_i tensor sigma_j`.

Under arbitrary local unitaries, `J -> R_A J R_B^T` with `R_A,R_B in SO(3)`, so the singular values of `J` are local-orbit invariants.

Take diagonal nonnegative coupling matrices whose squared singular values are

`x_A = (1/2, 1/2, 0)`

and

`x_B = (2/3, 1/6, 1/6)`.

Equivalently,

`J_A = diag(1/sqrt(2), 1/sqrt(2), 0)`

and

`J_B = diag(sqrt(2/3), 1/sqrt(6), 1/sqrt(6))`.

They agree exactly on the first two power-sum invariants:

`I2 = sum_i x_i = 1`,

`I4 = sum_i x_i^2 = 1/2`.

But the next invariant differs:

`I6(J_A)=sum_i x_i^3 = 1/4`,

`I6(J_B)=sum_i x_i^3 = 11/36`.

Since their singular-value multisets differ, they are not locally equivalent despite identical `I2` and `I4`.

Thus upgrading Cycle 285 from one scalar interaction cost to two natural scalar invariants still does not determine composition.

## Why this matters for the PDT-II route

The result blocks the obvious repair `add one more scalar invariant`. In a rank-three two-qubit coupling sector, the first two power sums leave the third elementary/spectral degree of freedom unresolved. A complete local-orbit specification needs enough independent nonlocal information (subject to the standard canonical identifications), or a physical principle that selects it.

This does **not** establish that every finite invariant family fails: in fixed finite dimension a complete finite invariant set can exist. The defensible no-go is narrower: low-order scalar resource summaries such as magnitude plus one shape invariant are insufficient, and merely appending ad hoc invariants is not a PDT-native derivation.

## Dimension stress

The exact obstruction already occurs for local dimension 2. It embeds into larger local Hilbert spaces by adjoining spectator levels, so dimensions `n=2,...,12` cannot rescue uniqueness from the pair `(I2,I4)` alone.

## Prior-art gate

The mathematical mechanism is established invariant/spectral-moment structure, not PDT novelty. The PDT value of this cycle is the negative design constraint on the proposed composition programme.

Representative established background retained from Cycle 285:

- Zhang, Vala, Sastry & Whaley, *Geometric theory of nonlocal two-qubit operations*, Phys. Rev. A 67, 042313 (2003), DOI 10.1103/PhysRevA.67.042313.
- Bullock & Brennen, *Canonical decompositions of n-qubit quantum computations and concurrence*, J. Math. Phys. 45, 2447 (2004), DOI 10.1063/1.1723701.

## Surviving target

Do not search for PDT composition by accumulating arbitrary scalar costs. Search instead for an independently motivated PDT operational axiom that constrains or selects the nonlocal equivalence class, and then ask whether its same-input predictions differ from standard QM/GPT/control theory.