# Cycle 366 — No-restriction hypothesis does not select PDT composition or n=3

## Target attacked
Priority (1) PDT-native composition law, then (2) a non-circular n=3 derivation and (3) a same-input PDT/QM probability gap.

## Candidate principle
Let a finite-dimensional operational theory have a closed pointed state cone C and order unit u. Impose the **no-restriction hypothesis (NRH)**: every mathematically valid normalized affine effect is physically allowed, i.e. the physical effect interval is [0,u] inside the dual cone C*. Candidate inference under test:

> NRH, possibly together with quantum self-duality, determines the composite and/or selects n=3.

## Exact quantum counterfamily
For complex quantum theory in Hilbert-space dimension d, take C_d = PSD_d, u=I, and pairing <E,rho>=Tr(E rho). The positive-semidefinite cone is self-dual under the Hilbert-Schmidt pairing:

    C_d* = C_d.

Consequently the full mathematically allowed normalized effect interval is exactly

    0 <= E <= I,

which is the ordinary quantum effect set. Thus finite-dimensional complex QM satisfies NRH for every d >= 1. There is no exceptional d=3 step.

### Dimension audit
For d=1,...,12 the real vector-space dimension of Hermitian operators is K(d)=d^2, state-cone and effect-cone dimensions agree, and NRH is satisfied. Therefore d=2 is the smallest nontrivial counterexample to `NRH => d=3`; d=4 already defeats uniqueness above three. The construction is analytic and extends to every finite d, so the finite audit is not the basis of the proof.

## Composition attack
NRH is a single-system state/effect relation. It does **not**, by itself, uniquely specify a composite tensor cone. In GPT language, admissible composites can lie between suitable minimal and maximal tensor constructions, subject to the chosen consistency assumptions. Hence importing NRH cannot fill PDT's missing composition rule. Any PDT composition law must add genuinely compositional structure rather than infer it from the availability of all dual effects.

For ordinary quantum theory, selecting the standard PSD cone on H_A tensor H_B recovers the usual quantum composite in every finite pair of dimensions. That supplies another all-dimensional counterfamily to any inference `NRH + ordinary quantum composition => d=3`.

## Same-input prediction check
If PDT uses the same quantum state rho, the same allowed effect E, and the same resource window R that contains E, NRH yields the same Born probability

    P(O|I,R) = Tr(E rho).

Therefore NRH alone cannot imply P_PDT(O|I,R) != P_QM(O|I,R). A numerical gap requires an additional PDT-native rule that changes the admissible states, effects, transformations, composition, or resource-conditioned probability assignment.

## Adversarial/edge checks
- d=1: trivial cone; NRH holds.
- d=2: nontrivial quantum counterexample; NRH holds.
- d=3: NRH holds, but nothing singular occurs.
- d=4,...,12: NRH continues identically.
- Pure and mixed states: both use the same PSD cone/effect duality.
- Degenerate/rank-deficient states and effects: included because PSD self-duality does not require full rank.
- Reversible unitary conjugation preserves both cones and the effect interval.
- Composite dimensions d_A,d_B are not selected by NRH; ordinary quantum tensor composition remains available for arbitrary finite d_A,d_B.

## Prior-art boundary
NRH is established GPT terminology and structure, not PDT novelty. Janotta and Lal, *Phys. Rev. A* 87, 052131 (2013), explicitly formulate GPTs without the no-restriction hypothesis and emphasize that the standard framework commonly assumes it; they also study consequences for joint states/tensor products. Later work on operational restrictions and Gleason-type GPTs further analyzes NRH and its relaxation. Therefore neither NRH nor the observation that quantum theory satisfies it is novel here.

References checked:
- P. Janotta and R. Lal, “Generalized Probabilistic Theories Without the No-Restriction Hypothesis,” Phys. Rev. A 87, 052131 (2013), DOI: 10.1103/PhysRevA.87.052131.
- T. Heinosaari, L. Leppäjärvi and M. Plávala, “No-free-information principle in general probabilistic theories,” Quantum 3, 157 (2019), DOI: 10.22331/q-2019-07-08-157.
- V. J. Wright and S. Weigert, “General Probabilistic Theories with a Gleason-type Theorem,” Quantum 5, 588 (2021), DOI: 10.22331/q-2021-11-25-588.

## Status ledger
| Claim | Status | Reason |
|---|---|---|
| PSD cone self-duality in finite-dimensional complex QM | IMPORTED/KNOWN | Standard finite-dimensional operator theory |
| Quantum NRH for every finite d | PROVED / IMPORTED-KNOWN | C_d*=C_d and effects are 0<=E<=I |
| NRH => n=3 | FALSIFIED | d=2 is a nontrivial counterexample; all d work |
| NRH uniquely determines composition | FALSIFIED as an inference | single-system duality does not fix a unique composite rule |
| NRH => same-input PDT/QM probability gap | FALSIFIED as an inference | identical rho,E,R gives identical Tr(E rho) |
| PDT-native composition selector beyond NRH | OPEN | requires an additional PDT-specific axiom/law |
| BREAKTHROUGH CANDIDATE | NO | candidate is known and dimension-uniform |

## Surviving requirement
A viable PDT-II composition principle must constrain **joint physical distinctions** in a way not already fixed by single-system cone duality/NRH, survive arbitrary finite-dimensional embeddings, and either prove a dimension-sensitive theorem without assuming n=3 or generate a declared-resource same-input probability differing quantitatively from QM.
