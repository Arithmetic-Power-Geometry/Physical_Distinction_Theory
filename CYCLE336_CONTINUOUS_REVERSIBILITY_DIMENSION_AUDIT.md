# Cycle 336 — Continuous-reversibility dimension audit

## Target
Attack the strongest unresolved PDT-II obligations by testing whether continuous reversible interconvertibility of pure distinction states can non-circularly select n=3, determine the correlated composite, or force a same-input deviation from complex quantum theory.

## Exact candidate principle
For a finite system S with pure-state set P(S) and allowed reversible transformations G(S), impose:

**CR:** for every x,y in P(S), there is a continuous path g_t in G(S), t in [0,1], with g_0 = identity and g_1 x = y.

No rank, qutrit, Bloch-3-vector, complex Hilbert tensor product, or n=3 seed is included.

## Result 336A — CR does not select n=3 (FALSIFIED)
For ordinary complex quantum theory in every finite Hilbert dimension n >= 2, pure states are rays in CP^{n-1}. The connected group SU(n) acts transitively on these rays. Given pure rays [psi] and [phi], choose U in SU(n) taking one ray to the other; because SU(n) is path-connected, there is a continuous path U_t from identity to U. Therefore CR holds for every n >= 2. For n=1 the pure-state space is a singleton and CR is trivial.

Hence CR is satisfied for n=1,2,3,... and cannot single out n=3. The smallest nontrivial countermodel to `CR implies n=3` is n=2.

### Exact n=1..12 stress
| n | pure space | connected transitive reversible action | CR | n=3 selected? |
|---:|---|---|---|---|
|1|singleton|trivial|yes|no|
|2|CP^1|SU(2)|yes|no|
|3|CP^2|SU(3)|yes|no|
|4|CP^3|SU(4)|yes|no|
|5|CP^4|SU(5)|yes|no|
|6|CP^5|SU(6)|yes|no|
|7|CP^6|SU(7)|yes|no|
|8|CP^7|SU(8)|yes|no|
|9|CP^8|SU(9)|yes|no|
|10|CP^9|SU(10)|yes|no|
|11|CP^10|SU(11)|yes|no|
|12|CP^11|SU(12)|yes|no|

This is an analytic all-finite-n counterfamily, not merely numerical evidence.

## Result 336B — CR is even less dimension-selective at the single-system GPT level (PROVED counterfamily)
For each real d >= 2, take a normalized Euclidean-ball state space with pure states S^{d-1}. The connected rotation group SO(d) acts transitively on S^{d-1} for d >= 2, so the same CR principle holds across an infinite family of local dimensions. In particular, d=3 is not selected by CR itself.

This statement is deliberately local: a choice of bipartite cone/tensor rule is additional structure. That is exactly the point relevant to PDT-II composition: CR on local pure states does not specify that missing correlated-composite structure.

## Result 336C — CR does not determine a PDT composition law (FALSIFIED as an inference)
CR constrains the orbit structure of reversible transformations on each local pure-state set. It does not, by itself, specify the positive cone/effect set of AB, the admissible entangled states/effects, or a tensor norm. Therefore a correlated-composite selector cannot be inferred from CR alone without an additional composition postulate.

The complex-quantum family is already a direct countermodel to uniqueness across n: all finite n obey CR while using the ordinary quantum composite. Hypersphere GPT work further demonstrates that local hypersphere systems require separate bipartite choices and that imposing or violating continuous reversibility interacts with, rather than defines, those choices.

## Result 336D — no same-input PDT/QM deviation follows (PROVED implication failure)
Complex quantum theory itself satisfies CR for every finite n. Therefore CR cannot logically entail

P_PDT(O | I,R) != P_QM(O | I,R)

for identical microscopic input I and declared resource window R. Selecting the complex-QM realization gives equality and is a direct countermodel. A deviation requires an independently specified PDT rule that changes an operational probability under the same I and R.

## Prior-art rejection
This candidate is not PDT-native novelty.

1. L. Hardy, *Quantum Theory From Five Reasonable Axioms*, arXiv:quant-ph/0101012 (2001), explicitly uses continuous reversible transformations between pure states as an axiom separating his quantum reconstruction from classical probability theory.
2. S. Massar, S. Pironio and D. Pitalua-Garcia, *Hyperdense coding and superadditivity of classical capacities in hypersphere theories*, New J. Phys. 17, 113002 (2015), studies hypersphere GPTs and explicitly discusses continuous reversibility as a reconstruction condition; their composite constructions show that local hypersphere geometry and composite structure are distinct ingredients.

Accordingly, CR must be classified IMPORTED/KNOWN rather than promoted as PDT novelty.

## Adversarial checks
- **Dimension circularity:** no n=3/rank-3/qutrit seed was allowed.
- **Composition circularity:** no quantum tensor product was used to prove CR; only the local SU(n) action was needed.
- **Smallest counterexample:** n=2 already defeats `CR => n=3`.
- **Higher dimensions:** analytic SU(n) argument covers every finite n, stronger than randomized stress.
- **Alternative local geometry:** Euclidean-ball/SO(d) family independently defeats dimension uniqueness.
- **Same-input check:** because QM is itself a CR model, CR cannot force PDT != QM.

## Classification
- Continuous reversibility principle: **IMPORTED/KNOWN**.
- SU(n) all-finite-n CR counterfamily: **PROVED**.
- Euclidean-ball/SO(d) local counterfamily: **PROVED**.
- `CR => n=3`: **FALSIFIED**.
- `CR => unique PDT correlated composition`: **FALSIFIED as an inference**.
- `CR => parameter-free same-input PDT/QM deviation`: **FALSIFIED as an inference**.
- PDT-native correlated-composite selector: **OPEN**.
- Non-circular PDT-native n=3 derivation: **OPEN**.
- Same-input quantitative PDT prediction distinct from QM: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Surviving obligation
Do not spend further cycles treating generic reconstruction axioms as PDT primitives. The next viable candidate must be a mathematically explicit PDT-native functional or operation on *correlated distinctions* whose composite value is fixed before choosing a Hilbert/Jordan/GPT tensor product. It must then survive at least the n=2 versus n=3 versus n>=4 adversarial comparison and produce either a theorem or a fully specified same-input experimental probability difference.