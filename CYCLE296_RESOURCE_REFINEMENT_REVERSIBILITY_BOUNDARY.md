# Cycle 296 — Strict resource refinement is not strictly revelatory

## Target
Attack PDT-II targets (3) and (4): same-input quantitative prediction and resource-refinement/revelation laws. After Cycle 295 established that a scalar budget does not identify the admissible operational family, test the stronger candidate claim that a genuine enlargement of the admissible family must reveal strictly more distinction for a fixed microscopic input.

## Candidate principle under test
Let A subsetneq B be two admissible operational families and define, for a fixed binary input I=(I0,I1),

D(I;A)=sup_{a in A} d(p_a(.|I0),p_a(.|I1)).

The tempting strengthening of refinement monotonicity is

A subsetneq B  =>  D(I;A) < D(I;B).

This cycle tests strictness, not the already-proved weak monotonicity.

## Smallest decisive classical counterexample
Take a binary microscopic input H in {0,1} with equal priors. Let family A contain one perfect readout a with outcome Y=H. Hence D(I;A)=1.

Let B=A union {b}, where b is any genuinely additional operation, for example a fair coin output independent of H. Then A subsetneq B, but

D(I;B)=max(1,0)=1=D(I;A).

Thus strict inclusion of admissible operations does not imply strict revelation for a fixed input. The failure already occurs in the smallest nontrivial classical binary experiment and therefore cannot be repaired by quantum structure, higher dimension, entanglement, or a different norm once the old family already attains the relevant optimum.

## Non-saturated counterexample
The failure is not merely a ceiling effect. Let the two input-conditioned distributions under operation a be Bernoulli(0.75) and Bernoulli(0.25), giving TV=0.5. Add a distinct operation b whose two conditional distributions are both Bernoulli(0.5), giving TV=0. Then A={a}, B={a,b}, A subsetneq B, yet D(I;A)=D(I;B)=0.5<1.

Therefore strict resource enlargement can be operationally redundant on the declared input even away from maximal distinction.

## Exact surviving law
For every fixed input I,

A subseteq B => D(I;A) <= D(I;B)

by optimization-domain inclusion. Equality occurs exactly when the newly admitted operations fail to exceed the old support value for that input. Consequently a PDT revelation law cannot infer strict increase from set inclusion alone.

A defensible strict-revelation statement must include an input-relative witness condition: there exists b in B such that

d(p_b(.|I0),p_b(.|I1)) > D(I;A).

Under that hypothesis D(I;B)>D(I;A) is immediate. But this is a criterion for strict revelation, not a PDT-native dynamical law.

## Resource equivalence quotient
For a declared input class C, define A ~_C B when D(I;A)=D(I;B) for every I in C (or, more strongly, when they induce the same attainable statistical experiments on C). Then physical resource refinement relevant to PDT should be studied on operational equivalence classes rather than raw set cardinality/inclusion. Strict syntactic enlargement can be null in the quotient.

This quotient idea is structurally aligned with established Blackwell/Le Cam comparison and restricted-measurement/resource-theory notions, so it is not claimed as PDT novelty.

## Quantum embedding and dimension stress
The classical witness embeds diagonally into quantum theory: use rho_0=|0><0| and rho_1=|1><1|. Let A contain the Z measurement; let B additionally contain X. A is a strict subset of B, while D(I;A)=D(I;B)=1 because Z already perfectly distinguishes the inputs. For a non-saturated version use rho_0=(I+0.5 Z)/2 and rho_1=(I-0.5 Z)/2: Z gives TV=0.5, X gives 0, so strict inclusion again leaves the optimum unchanged.

These qubit witnesses embed into every finite Hilbert dimension n>=2 by spectator dimensions, covering n=2 through n=12 and arbitrary higher n. The classical binary witness also exists independently of Hilbert dimension.

## Pure/mixed, records, dynamics, and thermodynamic interpretation
The pure and mixed examples above show that the no-go is not purity-specific. Adding a controlled environment record that is statistically independent of the hypothesis is another strict operational enlargement with zero additional revelation. Likewise, adding an allowed channel or thermodynamic operation that is a post-processing/garbling of an already available experiment need not increase distinction. Hence a resource count can increase while decision-relevant revelation remains unchanged.

## Prior-art boundary
Data processing/contractivity and Blackwell-style comparison of statistical experiments already formalize that post-processing cannot create distinguishability and that operational comparison depends on informativeness/simulability rather than the number of available procedures. Quantum channel comparison similarly characterizes post-processing order through discrimination tasks. These mechanisms are IMPORTED/KNOWN, not PDT novelty.

## Consequence for same-input PDT-vs-QM prediction
A proposed PDT deviation cannot be obtained merely by declaring that PDT has a strictly larger resource family than a QM benchmark. The extra PDT operations must be specified and must possess an explicit same-input witness that improves or changes the predicted outcome statistics. Otherwise the enlargement may be operationally null on the test input.

## Status ledger
- strict admissible-family inclusion implies strict distinction increase for every fixed input: **FALSIFIED**.
- smallest binary classical counterexample: **PROVED**.
- non-saturated strict-inclusion/equal-distinction counterexample: **PROVED**.
- weak refinement monotonicity under A subseteq B: **PROVED / IMPORTED-KNOWN**.
- input-relative witness criterion for strict revelation: **PROVED** (taut consequence of the supremum definition; not novel).
- qubit pure/mixed embeddings and n=2..12/higher spectator embeddings: **PROVED**.
- Blackwell/Le Cam/channel post-processing comparison mechanism: **IMPORTED/KNOWN**.
- PDT-native law predicting when a newly available physical resource is nonredundant on a microscopic input: **OPEN**.
- fully specified same-input PDT-vs-QM quantitative deviation: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next obligation
Do not equate resource growth with revelation growth. Search for a PDT-native, microscopic rule that maps a physical resource/interface specification to an operational equivalence class and predicts when refinement crosses an input-relative distinction boundary. Any candidate must then be tested against classical/quantum garblings, redundant controls, controlled records, pure/mixed states, and n=1..12 before it can support a same-input deviation or distinctive inequality.
