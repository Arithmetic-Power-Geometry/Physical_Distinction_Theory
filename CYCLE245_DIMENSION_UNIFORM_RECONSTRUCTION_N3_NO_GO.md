# Cycle 245 — Dimension-uniform reconstruction cannot derive n=3

## Target
Strongest unresolved PDT-II items: PDT-native composition and a non-circular PDT-native derivation of n=3.

## Candidate route attacked
After Cycle 244, a tempting repair is to add a Hardy-style selector (simplicity/minimal exponent, continuity of reversible transformations, or another dimension-uniform reconstruction postulate) to the multiplicative hierarchy K(N)=N^r, and then interpret the selected scaling as a derivation of the physically preferred n=3.

## Theorem (dimension-uniform selector blindness)
Let H be a reconstruction package whose hypotheses are asserted uniformly for every positive operational capacity N, and suppose H derives a law K(N)=F(N) on its domain without an additional predicate that distinguishes one value N=N*. Then H cannot, by that law alone, derive N=N* as the unique physically admissible capacity.

### Proof
The conclusion K(N)=F(N) is conditional on N and holds for every N in the stated domain. Therefore every N in that domain satisfying the common hypotheses remains a model of the derived law. If N=3 is to be the unique survivor, some additional hypothesis must fail for every N != 3 or explicitly constrain N. That additional hypothesis—not the uniform scaling law—is doing the selection. QED.

For the Cycle-244 family F(N)=N^r, all positive integers N are in the domain. Even choosing r=2 leaves N=1,2,3,... admissible. Thus selecting the quantum exponent is logically different from selecting N=3.

## Exact stress check
`cycle245_uniform_reconstruction_n3_no_go.py` verifies with exact integers that for r=1,...,8 and n=1,...,12 the unit, strict-monotonicity and multiplicativity conditions all survive. In particular r=2 survives simultaneously for every n=1,...,12 rather than only n=3. The algebraic identities extend this to every positive integer n.

This script is a regression check, not an empirical simulation and not evidence for a new physical law.

## Prior-art boundary
Hardy's 2001 reconstruction derives K=N^r from subspace/composite assumptions and uses further assumptions including simplicity and continuous reversible transformations to recover the complex-quantum case K=N^2. The reconstruction is formulated for arbitrary finite N; it does not select N=3 as a unique system capacity. Hardy's later operational reconstruction likewise applies system/composite postulates generally. Therefore importing simplicity/continuity can at most reproduce a known quantum-reconstruction selector; it does not constitute a PDT-native n=3 derivation.

References checked:
- L. Hardy, *Quantum Theory From Five Reasonable Axioms*, arXiv:quant-ph/0101012 (2001).
- L. Hardy, *Reformulating and Reconstructing Quantum Theory*, arXiv:1104.2066 (2011).

## Consequences
- **PROVED:** a dimension-uniform capacity/reconstruction law cannot by itself single out n=3.
- **FALSIFIED:** the proposal that selecting r (including r=2) thereby derives n=3.
- **IMPORTED/KNOWN:** Hardy-style simplicity/continuity as a route to complex quantum scaling.
- **OPEN:** a PDT-native physical predicate whose admissibility genuinely changes with n and uniquely survives at n=3 without encoding 3 in its definition or constants.
- **OPEN:** PDT-native composition law.
- **OPEN:** same-input quantitative P_PDT != P_QM.
- **BREAKTHROUGH CANDIDATE:** NO.

## Stronger surviving obligation
Any future n=3 claim must exhibit an independently motivated PDT-native quantity or feasibility condition C(n,R) and prove both C(3,R) and failure of C(n,R) for every competing n under the same resource semantics. A dimension-independent reconstruction axiom, parameter-count exponent, or relabelled quantum postulate is insufficient.
