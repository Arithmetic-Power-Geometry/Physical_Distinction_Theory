# Cycle 169 — A scalar resource budget does not determine the admissible recombination algebra

Status: **PROVED / CONDITIONAL / IMPORTED-KNOWN / FALSIFIED / OPEN**

## Targets attacked
PDT-II (1) PDT-native composition law and (4) resource-refinement/revelation laws, with consequences for (3) same-input PDT-vs-QM predictions and (5) distinctive inequalities.

## Candidate principle under test
Following Cycle 168, suppose PDT assigns every deterministic joint witness f a nonnegative cost c(f), and a declared resource window B admits exactly witnesses satisfying c(f) <= B. Could the scalar budget B plus natural cost axioms determine the composite witness algebra?

Natural axioms tested:
1. c(constant)=0;
2. local coordinate witnesses have unit cost;
3. monotonicity under a larger budget;
4. relabeling symmetry among coordinates;
5. deterministic postprocessing cannot increase cost when the postprocessing is declared free.

## Theorem 169A — scalar-budget underdetermination
These axioms do not uniquely determine the admissible joint witness family.

Proof by smallest decisive countermodel. Let the joint record be two bits (x1,x2), with B=1. Define two symmetric cost models that agree on constants and coordinate witnesses.

Model L (linear/affine closure): cost 0 for constants, cost 1 for every nonconstant affine Boolean function a0 xor a1 x1 xor a2 x2, and cost 2 for the remaining Boolean functions.

Model J (junta closure): cost 0 for constants, cost 1 for every Boolean function depending on at most one coordinate, and cost 2 for every function depending essentially on both coordinates.

Both models assign unit cost to x1 and x2, are invariant under swapping coordinates, and generate nested admissible families as B grows. Yet parity x1 xor x2 is admitted at B=1 in Model L and excluded at B=1 in Model J. Therefore identical local costs and the same scalar resource budget do not determine which relational distinctions are physically admissible. QED.

The postprocessing clause must be interpreted relative to the declared free-operation set: if *all* deterministic postprocessing of the paired record is free, Cycle 168 applies and every Boolean witness is free once the full pair is available. Thus a nontrivial resource-bounded theory must specify its free operations rather than infer them from B alone.

## Theorem 169B — exact n-dimensional stress family
For every n>=2, define:
- L_n: all affine Boolean functions on n bits have cost <=1;
- J_n: all functions depending on at most one input coordinate have cost <=1.

Both are permutation-symmetric and agree on all constants and coordinate projections. They disagree on n-bit parity: L_n admits parity at budget 1 while J_n excludes it for every n>=2. Hence the underdetermination is exact for n=2,...,12 and all higher finite n. No randomized test can repair the missing axiom.

Counts at B=1 also separate the families: L_n has 2^(n+1) affine Boolean functions, whereas J_n contains the two constants plus, for binary inputs/outputs, the nonconstant one-coordinate functions x_i and not-x_i, giving 2+2n distinct functions. They coincide only at n=1; for n>=2 the gap grows exponentially versus linearly.

## Surviving theorem — budget filtration
Once a specific cost functional c and free-operation set F are independently fixed, A_B={f:c(f)<=B} is automatically monotone in B: B<=B' implies A_B subseteq A_B'. This is a valid resource-refinement filtration, but it does not derive c or F.

If composition of admissible witnesses is required, additional closure/subadditivity hypotheses must be stated explicitly. They are not consequences of a scalar budget.

## Prior-art boundary
The ingredients are not claimed as new mathematics. Resource-bounded computation, communication complexity, thermodynamics of information processing, and quantum resource theories already formalize task-dependent costs and restricted operations. In particular, minimal work costs of logical processes and complexity-constrained quantum thermodynamics show that physical cost depends on the process and allowed implementation class, not merely on a single undifferentiated budget. Cycle 169's value is an internal PDT no-go boundary: a scalar `distinction resource` cannot by itself supply the missing composition law.

## Consequences for PDT-II
- A resource-bounded recombination law must contain at least two independently derived objects: a task/process cost functional and a declared free-operation/implementation class.
- Choosing either object merely to obtain PDT != QM would be circular.
- Therefore no same-input PDT-vs-QM prediction follows yet.
- No experimentally distinctive inequality follows yet.
- No gravity/capacity law is imported or asserted.

## Classification
- Scalar-budget uniqueness of composite witness algebra: **FALSIFIED**.
- Counterexample family n=2,...,12 and all n>=2: **PROVED**.
- Budget filtration after fixing c: **PROVED / CONDITIONAL**.
- Resource/thermodynamic mechanism as general concept: **IMPORTED/KNOWN**.
- PDT-native derivation of c and free operations: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT != QM prediction: **OPEN**.
- Experimentally distinctive PDT inequality: **OPEN**.
- Gravity/capacity law: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next strongest obligation
Attack whether PDT's existing primitive notion of a distinction supplies a non-arbitrary *operational cost functional* from distinguishability geometry itself. Candidate costs must be invariant under reversible relabelings, monotone under declared free operations, composable/subadditive where justified, and independently measurable. Before promotion, compare any surviving functional against established communication/query complexity, statistical distinguishability, quantum resource monotones, and thermodynamic work costs to reject rediscovery.