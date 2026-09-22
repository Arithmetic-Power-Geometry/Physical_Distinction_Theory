# PDT-II Cycle 325 — Resource-revelation / distinguishability monotonicity audit

## Target
Attack the strongest surviving PDT-II route using a quantity intrinsic to distinction/refinement operations rather than another reconstruction axiom: can monotonic loss of operational distinguishability under restricted resources supply (i) a unique composite law, (ii) a non-circular n=3 selector, or (iii) a same-input PDT/QM prediction?

## Candidate principle
For a declared measurement/resource family R, define the operational distinction seminorm of a signed state difference X by

D_R(X) = sup_{M in R} || M(X) ||_1,

up to the conventional factor 1/2. If R1 subset R2 then D_R1(X) <= D_R2(X). If a physical map Phi sends every allowed post-measurement test back into R (equivalently the relevant resource family is closed under precomposition), then D_R(Phi X) <= D_R(X).

This formulation is deliberately operational: refinement of the admissible test set can only reveal, never erase, optimal distinguishability.

## Proof
1. Resource refinement: R1 subset R2 implies sup over R1 <= sup over R2. Hence D_R is monotone nondecreasing under enlargement of the allowed measurement family.
2. Processing contraction: if for every M in R, M o Phi is again an allowed test in R, then
   D_R(Phi X) = sup_{M in R} ||M(Phi X)||_1
                = sup_{M in R} ||(M o Phi)(X)||_1
                <= D_R(X).
3. Equality need not hold. A channel or coarse graining may erase all distinction.

Classification of these statements: PROVED, but the mathematical mechanism is IMPORTED/KNOWN (data processing / distinguishability norms), not a PDT novelty claim.

## Smallest decisive counterexample to conservation
Take a classical binary state space, p=(1,0), q=(0,1). Their total-variation distinction is maximal. Apply the constant stochastic channel Phi that maps both inputs to r=(1,0). Then

D(p-q) > 0, but D(Phi(p-q)) = 0.

Thus any unconditional law 'physical evolution conserves distinction' is FALSIFIED already at n=2. The same construction embeds into every n>=2 by making all columns of a stochastic map identical.

## Exact dimension stress n=1..12
- n=1: all normalized states coincide; distinction is identically zero (degenerate edge case).
- n=2..12: choose e1 and e2 as distinct simplex vertices and the constant channel Phi(x)=e1. Input total variation is 1 (or norm 2 before the 1/2 convention); output total variation is 0.
- Therefore strict loss exists for every n>=2 and there is no distinguished behavior at n=3.

This proof extends to arbitrary finite n and does not rely on sampling.

## Composite/resource-window stress
For a bipartite system, different declared resource windows (global measurements, LOCC, local/product measurements, etc.) induce different operational distinguishability norms. Enlarging the measurement class gives a monotone hierarchy, but the hierarchy does not itself choose which resource family is physically fundamental. Known local/global state-discrimination and data-hiding results explicitly exhibit gaps between these norms.

Therefore 'distinction is what the available resource window can reveal' is operationally sound but does NOT close the PDT composite law: the missing object has merely moved into the choice of R.

## Same-input QM/GPT comparison
If PDT uses the same microscopic states, dynamics, and admissible measurement family R as QM, the operational supremum above reproduces the corresponding QM distinguishability statistic by definition. A PDT/QM numerical deviation requires an independently derived PDT change to the state cone, effect set, dynamics, composition rule, or resource family. Resource monotonicity alone cannot produce P_PDT(O|I,R) != P_QM(O|I,R).

## Prior-art guard
Distinguishability norms induced by restricted measurement classes, trace/base-norm contraction under admissible channels, and local-vs-global discrimination gaps are established quantum-information / ordered-vector-space machinery. In particular, Lancien and Winter analyze distinguishability norms defined by local measurement classes, while Reeb, Kastoryano and Wolf formulate contraction/distinguishability results using cones and base norms. No novelty is claimed for those mechanisms.

## Surviving PDT-native theorem candidate
A useful PDT-II structural statement survives, but only as a bookkeeping theorem:

**Resource Revelation Monotonicity.** For a fixed state/effect model and two declared resource windows R1 subset R2, operational distinction satisfies D_R1(X) <= D_R2(X). For resource-preserving processing Phi, D_R(Phi X) <= D_R(X).

Status: PROVED / IMPORTED-KNOWN mechanism. It is not a BREAKTHROUGH CANDIDATE because it is standard supremum monotonicity/data processing.

## Decisive consequences
- Unconditional distinction conservation: FALSIFIED (smallest nontrivial witness n=2).
- Resource refinement can only increase operationally accessible distinction: PROVED under stated nested-resource definition.
- Resource-preserving processing cannot increase operational distinction: PROVED under stated closure hypothesis.
- These laws select n=3: FALSIFIED; the same statements hold for every finite n.
- These laws uniquely determine composite distinction: FALSIFIED as an inference; different resource families induce different composite norms.
- These laws force a same-input PDT/QM deviation: FALSIFIED as an inference.

## PDT-II ledger after cycle 325
- PDT-native correlated-composite selector: OPEN
- Non-circular PDT-native n=3 derivation: OPEN
- Same-input parameter-free PDT/QM prediction: OPEN
- Resource Revelation Monotonicity: PROVED / IMPORTED-KNOWN mechanism
- Unconditional distinction conservation: FALSIFIED
- n=1..12 conservation stress: PROVED analytically
- Resource hierarchy as unique composition selector: FALSIFIED as an inference
- Breakthrough candidate: NO

## Next strongest attack
Search for a genuinely PDT-native *closure equation on resource refinement itself* whose fixed point is derived rather than chosen. It must survive adversarial replacement of R by global, LOCC/local, injective/projective extremes and restricted quotients, and it must not reduce to a generic supremum/data-processing theorem. If no independently fixed closure exists, record that underdetermination rather than tuning one to obtain n=3.
