# PDT-II Cycle 329 — Local-tomography uniqueness no-go

## Target attacked
1. PDT-native composition law.
2. Non-circular PDT-native n=3 derivation.
3. Same-input quantitative PDT-vs-QM prediction.

## Candidate principle
Assume finite operational systems have a parameter count K and composites satisfy local tomography:

K(AB) = K(A) K(B).

Ask whether this condition can uniquely determine PDT composition, select n=3, or force a PDT/QM probability deviation.

## Exact counterfamilies
Two inequivalent theories satisfy the same local-tomography parameter law for every finite n:

* Classical n-level system: K_C(n)=n. Hence K_C(mn)=mn=K_C(m)K_C(n).
* Complex quantum n-level system: K_Q(n)=n^2. Hence K_Q(mn)=(mn)^2=m^2 n^2=K_Q(m)K_Q(n).

They have inequivalent state spaces and correlated-composite structure, but satisfy the same multiplicative tomography identity. Therefore local tomography alone cannot select a unique composition law.

The smallest nontrivial witness is n=2: K_C(2)=2 and K_Q(2)=4, while both satisfy the same composite multiplicativity rule. The ambiguity persists at n=3 and at every finite n. Exact checks for n=1..12 are recorded separately.

## Theorem (selector no-go)
If a proposed PDT selector uses only finite local parameter counts and the identity K(AB)=K(A)K(B), then it cannot distinguish the classical family K(n)=n from the complex-quantum family K(n)=n^2. Consequently it cannot, without an additional independently derived PDT-native hypothesis, imply a unique correlated composition, select n=3, or entail P_PDT(O|I,R) != P_QM(O|I,R).

### Proof
For all positive integers m,n, both K_1(n)=n and K_2(n)=n^2 satisfy K_i(mn)=K_i(m)K_i(n). Since K_1 and K_2 disagree for every n>1, the multiplicativity constraint has at least two inequivalent solutions. Thus uniqueness is false. Since n=2,3,4,... all occur in both families, n=3 is not selected. Since complex finite-dimensional quantum theory itself realizes K_2 and local tomography, the condition cannot logically imply a deviation from quantum probabilities. QED.

## Adversarial/edge checks
* n=1: both families collapse to K=1; this degenerate case cannot discriminate them.
* n=2..12: exact integer identities hold in both families.
* Higher n: proof is algebraic, so randomized/asymptotic testing is unnecessary for the theorem.
* Pure/mixed states: local tomography is a statement about reconstructing arbitrary composite states from local statistics; it does not itself choose the state cone.
* Correlated states: precisely where the underdetermination matters; equal dimension-factorization does not specify positivity/effect cones or allowed correlations.
* Alternative norms/reversible groups: not fixed by the parameter-count identity, so they remain free rather than repairing uniqueness.

## Prior-art guard
Local tomography is established reconstruction/GPT machinery, not PDT-native. Hardy and Wootters discuss complex quantum theory as locally tomographic and real-vector-space quantum theory as bilocally rather than locally tomographic (arXiv:1005.4870). Barnum and Wilce obtain complex quantum structure only when local tomography is combined with additional Jordan/homogeneity/self-duality and qubit assumptions (arXiv:1202.4513). Hence this cycle claims only the elementary no-go consequence above, not novelty for local tomography.

## Status ledger
| Claim | Status |
|---|---|
| Classical K(n)=n obeys local tomography parameter multiplicativity | PROVED / IMPORTED-KNOWN model |
| Complex quantum K(n)=n^2 obeys local tomography parameter multiplicativity | PROVED / IMPORTED-KNOWN model |
| Local tomography alone => unique PDT composition | FALSIFIED |
| Local tomography alone => n=3 | FALSIFIED |
| Local tomography alone => same-input PDT/QM probability deviation | FALSIFIED |
| PDT-native correlated-composite selector | OPEN |
| BREAKTHROUGH CANDIDATE | NO |

## Consequence for next cycle
Do not stack local tomography onto PDT merely as a selector. A viable route must constrain correlated distinctions beyond parameter-count factorization and must be derived from PDT primitives rather than imported reconstruction axioms.