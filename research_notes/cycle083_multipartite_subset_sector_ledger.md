# Cycle 083 — Multipartite subset-sector quadratic ledger

## Target attacked
PDT-II targets (1) composition law and (4) resource/revelation/conservation law.

## Exact hypotheses
Let the system have finite local dimensions `d_1,...,d_N`, total dimension `D=prod_i d_i`, and a density operator `rho`.  On the Hilbert--Schmidt operator space of subsystem `i`, define

- `P_i(X) = Tr_i(X) tensor I_i/d_i` (with the identity reinserted at site `i`),
- `Q_i = I - P_i`.

For each subset `S` of parties define the orthogonal tensor-sector projector

`Pi_S = tensor_{i in S} Q_i tensor_{j notin S} P_j`

and `rho_S = Pi_S(rho)`.  Define the normalized quadratic sector energy

`C_S(rho) = D ||rho_S||_2^2`.

The empty sector is `rho_empty = I_D/D`.

## Theorem 083-A — exact subset-sector decomposition
**Classification: PROVED; IMPORTED/KNOWN mathematical structure.**

The local maps `P_i,Q_i` are mutually commuting Hilbert--Schmidt orthogonal projections.  Hence the `2^N` projectors `Pi_S` are pairwise orthogonal, resolve the identity superoperator, and

`rho = sum_S rho_S`.

Therefore Pythagoras gives

`Tr(rho^2) = 1/D + sum_{S nonempty} ||rho_S||_2^2`, so with

`E_D(rho)=D Tr(rho^2)-1`

we have the exact ledger

`E_D(rho) = sum_{S nonempty} C_S(rho)`, with every `C_S >= 0`.

This is an operator-space identity. It is not an entanglement decomposition: nonempty joint sectors can be populated by product states.

## Theorem 083-B — exact product factorization
**Classification: PROVED; IMPORTED/KNOWN boundary.**

For a product state `rho = tensor_i rho_i`, write `delta_i = rho_i-I_i/d_i` and `E_i=d_i Tr(rho_i^2)-1=d_i||delta_i||_2^2`. Then

`rho_S = tensor_{i in S} delta_i tensor_{j notin S} I_j/d_j`,

hence

`C_S(rho) = prod_{i in S} E_i`.

Summing all nonempty subsets immediately recovers

`1+E_D(rho)=prod_i (1+E_i)`.

Thus Cycle 075's scalar product law is exactly the generating-function sum of the subset ledger.

## Theorem 083-C — no subset-sector transfer under local bistochastic dynamics
**Classification: PROVED; IMPORTED/KNOWN operator-theory boundary.**

Let `Phi=tensor_i Phi_i`, where every `Phi_i` is completely positive, trace preserving, and unital. Trace preservation and unitality imply

`P_i Phi_i = Phi_i P_i = P_i`,

so `Q_i Phi_i = Phi_i Q_i`. Therefore every subset sector is invariant as a subspace:

`rho'_S = Phi(rho_S)`.

For a unital completely positive map, Kadison--Schwarz plus trace preservation gives Hilbert--Schmidt contraction,

`||Phi(X)||_2 <= ||X||_2`.

Consequently

`C_S(Phi(rho)) <= C_S(rho)`

for every subset `S`. Local unitaries give equality sector by sector.

This strengthens Cycle 082 conceptually: bistochastic local dynamics cannot move quadratic distinction between subset labels; nonunital dynamics can mix the identity and traceless sectors and therefore can populate sectors, as the local-reset counterexample already demonstrated.

## Numerical stress audit
The deterministic audit in `cycle083_multipartite_subset_sector_ledger.py` checks:

- dense bipartite pure and mixed states for every equal local dimension `n=1,...,12` (24 cases),
- dense correlated tripartite mixed states for `n=1,...,4` (4 cases),
- three-party product factorization for `n=1,...,12,16,24,32,48,64,96,128` (19 cases),
- local-unitary invariance of every nonempty bipartite sector for `n=2,...,6` (15 sector checks),
- the degenerate `n=1` boundary.

Frozen maxima:

- decomposition residual: `2.842170943040401e-14`,
- reconstruction norm: `6.297555910327939e-17`,
- cross-sector Hilbert--Schmidt inner product: `2.7755575615628914e-17`,
- product-factorization residual: `2.842170943040401e-14`,
- local-unitary sector residual: `7.771561172376096e-16`.

These computations are regression evidence only; the results above are proved algebraically.

## Prior-art rejection of a breakthrough claim
The decomposition is in established generalized Bloch/correlation-tensor territory. In particular:

1. Hassan & Joag, *Phys. Rev. A* **77**, 062334 (2008), use norms of multipartite Bloch correlation tensors: https://doi.org/10.1103/PhysRevA.77.062334
2. Hassan & Joag, *Phys. Rev. A* **80**, 042302 (2009), extend correlation-tensor methods to N-qudit states: https://doi.org/10.1103/PhysRevA.80.042302
3. de Vicente & Huber (2011), arXiv:1106.5756, develop arbitrary-dimensional multipartite correlation-tensor methods: https://arxiv.org/abs/1106.5756
4. Wyderka & Guhne (2019), arXiv:1905.06928, explicitly study multipartite sector lengths: https://arxiv.org/abs/1905.06928
5. The 2024 Physics Reports review on randomized measurements explicitly records purity decomposition into sector lengths and the product convolution property: https://doi.org/10.1016/j.physrep.2024.09.009

Accordingly, this cycle **must not** be promoted as a PDT breakthrough. Its value is organizational: it exposes exactly where a genuinely PDT-native law would have to enter.

## Surviving PDT-II target
The exact known ledger supplies coordinates, not new physics. A PDT-native advance now requires an independently derived constraint on the allowed subset-sector distribution or flow, e.g. a resource-cost inequality, dynamical selection rule, experimentally falsifiable cross-sector bound, or nontrivial composition restriction that is not already implied by positivity, Hilbert--Schmidt geometry, or standard quantum mechanics.

## Status
- Exact subset-sector decomposition: **PROVED / IMPORTED-KNOWN**
- Product subset factorization: **PROVED / IMPORTED-KNOWN**
- Local bistochastic sector monotonicity: **PROVED / IMPORTED-KNOWN**
- Numerical stress audit: **NUMERICALLY SUPPORTED**
- PDT-native novelty: **OPEN**
- BREAKTHROUGH CANDIDATE: **NO**
