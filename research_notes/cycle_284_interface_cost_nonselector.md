# Cycle 284 — interface-cost principle does not select composition

## Target
PDT-II target (1): test whether adding an explicit finite interface cost to the enriched resource object can uniquely select the joint interface/composite.

## Candidate statement attacked
Given fixed local implementation data `(R_A, Lambda_A)`, `(R_B, Lambda_B)` and a scalar interface budget `C`, suppose admissible joint interfaces are those whose implementation cost is at most `C`. Does the tuple of locals plus `C` determine a unique `J_AB` or unique joint admissible measurement family?

## Exact counterexample
Take two qubits with identical complete local controls and equal interface budget. Consider two distinct two-body couplings

`J_ZZ = g Z tensor Z`,
`J_XX = g X tensor X`,

with the same scalar coupling-strength/time cost under any cost functional that depends only on the chosen norm of the interaction generator and duration (for example `C = tau ||J||`, since `||Z tensor Z|| = ||X tensor X||` for every unitarily invariant matrix norm). They are physically different interfaces relative to a fixed local control frame, yet have identical scalar interface cost. If full arbitrary local SU(2) controls are declared free they can become locally equivalent; therefore choose restricted local implementation structure, e.g. local Z controls only. Then no allowed local frame change maps ZZ to XX, while the scalar cost remains identical.

Thus `(R_A,Lambda_A),(R_B,Lambda_B),C` does not determine a unique joint interface. The obstruction already occurs for 2 x 2 systems and embeds into larger dimensions by acting on a two-level subspace.

## Stronger surviving theorem
A scalar interface-cost budget can define a feasible *set* of interfaces,

`J(C) = {J : cost(J) <= C}`,

but cannot in general select a unique interface. Consequently a PDT-native composition principle cannot be only an interface-cost scalar. It must either retain implementation-resolved joint structure or derive a nontrivial equivalence/selection rule from the distinction primitive.

For a fixed implementation model and nested budgets `C1 <= C2`, feasible-interface inclusion `J(C1) subseteq J(C2)` is immediate, and any supremal operational distinction optimized over these feasible sets is monotone. This is a resource-refinement fact, not a unique-composition theorem.

## Prior-art gate
Measurement and operation costs depending on concrete apparatus/control models are established. Existing work studies time-energy costs of quantum measurements, finite-resource limitations of ideal projective measurements, thermodynamically consistent measurement costs, and entanglement cost/localization of joint measurements. Therefore `cost(J)` and finite-resource measurement implementation are not PDT inventions. The PDT question is whether finite-resource distinction itself derives additional joint structure beyond those implementation theories.

Relevant prior-art families checked 2026-09-21:
- Fung & Chau, Phys. Rev. A 89, 052306 (2014), time-energy costs of quantum measurements.
- Guryanova, Friis & Huber, Quantum 4, 222 (2020), ideal projective measurements require infinite resources in their model.
- Latune & Elouard, Quantum 9, 1614 (2025), thermodynamically consistent energy costs of quantum measurements.
- Pauwels et al., Phys. Rev. X 15, 021013 (2025), joint measurements classified via finite entanglement-localization cost.

## Status
- Scalar interface budget + complete local data -> unique `J_AB`: **FALSIFIED**.
- Smallest witness: two qubits with restricted local control frame and equal-cost inequivalent `ZZ`/`XX` interfaces: **PROVED counterexample**.
- Higher-dimensional embedding: **PROVED** by two-level subspace embedding.
- Nested interface budget -> nested feasible interface sets: **PROVED** (definition-level monotonicity).
- Measurement/interface resource costs as a general idea: **IMPORTED/KNOWN**.
- PDT-native selector of joint interface: **OPEN**.
- Non-circular PDT-native `n=3`: **OPEN**.
- Same-input `P_PDT != P_QM`: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest attack
Replace scalar interface cost by the full resource-feasible interface set and ask whether a PDT-native closure axiom can constrain that set without reducing to ordinary reachability/control theory or GPT/circuit composition. In parallel, test whether resource refinement admits any nontrivial quantitative inequality beyond set inclusion/data processing that survives same-input quantum comparison.