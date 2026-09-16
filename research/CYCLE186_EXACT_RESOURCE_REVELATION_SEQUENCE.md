# Cycle 186 — Exact Resource-Revelation Sequence

## Status

**PROVED (finite-dimensional linear operational model)**; **CONDITIONAL** on representing a declared resource window by a linear span of accessible effects; **IMPORTED/KNOWN mathematics** (quotients, kernels, rank-nullity, exact sequences); **OPEN** as a uniquely PDT-native physical postulate; **BREAKTHROUGH CANDIDATE: NO**.

## Setup and exact hypotheses

Let `V` be a finite-dimensional real operational state/record vector space. For a declared resource window `R`, let `E_R <= V*` be the linear span of effects/tests accessible under `R`. Define the evaluation map

`T_R : V -> E_R*`, `T_R(v)(e)=e(v)`.

Define the resource-indistinguishable sector

`K_R := ker(T_R) = intersection_{e in E_R} ker(e)`

and the observable quotient

`Q_R := V / K_R`.

Suppose resource refinement is nested: `R <= R'` means `E_R <= E_R'`.

## Theorem 186.1 — Exact revelation sequence

If `E_R <= E_R'`, then `K_R' <= K_R` and there is a canonical surjective linear map

`pi_{R',R}: Q_R' -> Q_R`, `[v]_{K_R'} |-> [v]_{K_R}`.

Its kernel is canonically isomorphic to `K_R/K_R'`. Hence

`0 -> K_R/K_R' -> Q_R' -> Q_R -> 0`

is a short exact sequence.

### Proof

Because every effect in `E_R` also belongs to `E_R'`, any vector annihilated by all effects in `E_R'` is annihilated by all effects in `E_R`; hence `K_R' <= K_R`. The displayed quotient map is therefore well-defined and plainly surjective. Its kernel consists of classes `[v]_{K_R'}` with `v in K_R`; this is exactly `K_R/K_R'`. Exactness follows. QED.

## Corollary 186.2 — Exact dimension revelation law

Define observable distinction dimension

`D(R):=dim Q_R = rank(T_R)`.

Then

`D(R')-D(R) = dim(K_R/K_R') >= 0`.

Thus nested resource refinement can reveal but cannot erase linearly observable distinction dimensions.

This is stronger than a bare monotonicity statement: it identifies the exact newly revealed sector.

## Corollary 186.3 — Path-independent revelation conservation

For any nested chain `R0 <= R1 <= ... <= Rm`,

`D(Rm)-D(R0) = sum_{j=0}^{m-1} [D(R_{j+1})-D(R_j)]`

and equivalently

`dim(K_R0/K_Rm) = sum_j dim(K_Rj/K_R{j+1})`.

Therefore total linear revelation between fixed endpoints is path independent even though intermediate decompositions may differ.

This is a finite-dimensional conservation/accounting identity, not a claim of energetic conservation.

## Corollary 186.4 — Saturation criterion

A refinement `R <= R'` reveals no new linear distinction iff

`K_R'=K_R`, equivalently `D(R')=D(R)`, equivalently every new accessible effect in `E_R'` is redundant on the current operational quotient.

## Degenerate and edge cases

- Zero resource: `E_R={0}` gives `K_R=V`, `Q_R=0`, `D(R)=0`.
- Tomographically complete resource: if `E_R` separates `V`, then `K_R=0`, `Q_R=V`, `D(R)=dim V`.
- Linearly dependent added effects produce zero revelation increment.
- A single added independent effect can increase `D` by at most one.
- The theorem is norm-independent: no norm enters the proof.
- It is covariant under invertible changes of operational coordinates.

## Dimension stress test n=1,...,12

For `V=R^n`, choose nested effect matrices `A_k` whose rows span `E_k`. Then `K_k=null(A_k)` and `D(k)=rank(A_k)`. For every `n=1,...,12` and every nested row-span chain, rank-nullity gives exactly

`rank(A_{k+1})-rank(A_k)=dim(null(A_k))-dim(null(A_{k+1})) >= 0`.

No numerical approximation is required. Randomized tests in higher finite dimensions can only regression-test implementations; they do not strengthen the analytic proof.

## Adversarial falsification attempts and boundaries

1. **Non-nested resources.** If `E_R` and `E_S` are incomparable, neither kernel need contain the other. There is no canonical monotone revelation map. Therefore monotonicity is explicitly restricted to nested refinement.
2. **Nonlinear tests.** If accessible tests are not represented by a linear effect span, this theorem does not automatically apply. A separate operational quotient must be defined and proved compatible.
3. **Changing microscopic model.** Comparing different `V` spaces is not resource refinement under this theorem.
4. **Probability law.** The theorem determines equivalence classes/dimensions, not probabilities on them. It does not solve the PDT-native n=3 probability derivation.
5. **QM discrepancy.** Since QM/GPT operational models also admit effect-induced equivalence quotients, the theorem alone cannot yield `P_PDT != P_QM` under same inputs.
6. **Thermodynamics/gravity.** No energetic, entropic, gravitational, or capacity law follows without additional physical hypotheses.
7. **Markovian/non-Markovian dynamics.** At a fixed declared window the quotient theorem remains algebraic. A dynamical conservation claim requires compatibility of time evolution with the nested effect filtration and is not asserted here.
8. **Controlled-environment records.** Enlarging the effect window to include environment records fits the theorem only when the enlarged effects act on the same declared operational `V`; enlarging the underlying state space is a different construction.

## Composition compatibility with Cycle 185

Under Cycle-185 hypotheses `V_AB=V_A tensor V_B` and product-generated effect windows, `Q_AB(R_A,R_B) ~= Q_A(R_A) tensor Q_B(R_B)`. If both local windows refine, Cycle 186 gives canonical surjections on each factor, and their tensor product is the composite revelation map. Thus resource revelation and the conditional quotient tensor composition law commute.

## Prior-art boundary

The proof is ordinary finite-dimensional linear algebra and quotient-space theory. Operational equivalence under restricted measurements/effects and information/resource monotonicity are established themes in operational theories, statistical experiment comparison, and resource theories. Therefore **no novelty claim is made for the abstract theorem**. Any PDT novelty would have to come from an independently motivated physical identification of `V`, `E_R`, and resource windows that yields a new falsifiable consequence not already present in those frameworks.

## PDT-II ledger impact

1. **PDT-native composition law:** CONDITIONAL progress only; Cycle 185 remains the exact product-window theorem.
2. **PDT-native n=3 derivation:** OPEN; this result supplies no probability selector.
3. **Same-input PDT/QM quantitative gap:** OPEN; cannot be inferred from quotient dimension alone.
4. **Resource refinement/revelation/conservation:** **PROVED conditionally** as an exact short-exact-sequence and path-independent dimension-accounting law.
5. **Experimentally distinctive inequalities:** OPEN; `D(R')>=D(R)` is not PDT-distinctive because it is generic rank monotonicity.
6. **Gravity/capacity:** OPEN; do not import.

## Next strongest attack

Test whether a physically justified PDT resource filtration can impose a **non-generic constraint on revelation increments** (for example submodularity, strict bottleneck bounds, or composition-dependent deficit) that is not merely matrix-rank/subspace theory. First attempt falsification using two incomparable resource additions, composite hidden sectors, and non-product global effects before promoting any candidate.
