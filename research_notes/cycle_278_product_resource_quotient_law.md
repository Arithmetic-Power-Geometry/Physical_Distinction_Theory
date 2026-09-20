# Cycle 278 — Product-resource quotient dimension law

Status: **PROVED under explicitly factorized test-span hypothesis; IMPORTED/KNOWN linear algebra; NOT a breakthrough candidate**

## Question attacked
Can PDT obtain a composition constraint from resource-admissible tests rather than from a preselected scalar divergence?

## Setup
Let finite-dimensional local state-difference spaces be `V_A,V_B`. Let the linear spans of locally admissible effects be `W_A subseteq V_A*` and `W_B subseteq V_B*`. Define operational null spaces

`N_A = W_A^perp`, `N_B = W_B^perp`.

Assume the joint resource window admits **exactly the linear span of product effects**,

`W_AB = W_A tensor W_B subseteq (V_A tensor V_B)*`.

This is a hypothesis about the resource window, not a theorem that all physical composites must have this form.

## Theorem 278.1 — factorized product-resource quotient law
Under the stated finite-dimensional factorized test-span hypothesis,

`N_AB = N_A tensor V_B + V_A tensor N_B`.

Consequently there is a canonical vector-space isomorphism

`(V_A tensor V_B)/N_AB ~= (V_A/N_A) tensor (V_B/N_B)`.

If `r_A = dim(V_A/N_A)` and `r_B = dim(V_B/N_B)`, then

`r_AB = r_A r_B`.

### Proof
The quotient maps `q_A:V_A->V_A/N_A` and `q_B:V_B->V_B/N_B` induce `q_A tensor q_B`. Standard tensor-product exactness over finite-dimensional real/complex vector spaces gives

`ker(q_A tensor q_B)=N_A tensor V_B + V_A tensor N_B`.

The product test span `W_A tensor W_B` separates exactly the quotient tensor product, so its annihilator is this kernel. The first isomorphism theorem yields the quotient identity, and finite-dimensional tensor dimensions multiply. QED.

## Exact dimension stress test n=1,...,12
For arbitrary local dimensions `n_A,n_B` and resolved ranks `0<=r_A<=n_A`, `0<=r_B<=n_B`, the theorem predicts

`dim N_AB = n_A n_B - r_A r_B`.

Equivalently, inclusion-exclusion on the two null summands gives

`(n_A-r_A)n_B + n_A(n_B-r_B) - (n_A-r_A)(n_B-r_B) = n_A n_B-r_A r_B`.

This is an exact polynomial identity, so it covers every rank choice for dimensions 1 through 12 and all higher finite dimensions without numerical tolerance. Degenerate cases: if either `r=0`, no product distinction is resolved; if both local windows are tomographically complete, `N_AB={0}`.

## Adversarial boundary — why this does not solve PDT composition
The hypothesis `W_AB=W_A tensor W_B` excludes entangled/global joint effects by construction. Enlarging the joint admissible span to `W_AB' supersetneq W_A tensor W_B` can strictly shrink `N_AB` and reveal joint directions invisible to all product tests. Conversely a restricted joint apparatus may realize a proper subspace of the product span. Therefore local resource windows alone do not determine the joint test span.

A minimal abstract witness is `V_A=V_B=R^2` with one resolved local functional on each side (`r_A=r_B=1`). Product-only resolution has rank 1 in the four-dimensional tensor space. Adding any independent joint functional raises the resolved rank while leaving both local windows unchanged. Hence local resolved ranks do not fix joint resolved rank.

## Consequences for PDT-II targets
- A resource-native composition theorem can be exact **conditional on a declared joint test-generation rule**.
- The quotient functor commutes with tensor product for the factorized rule above.
- The law does not derive the physical joint rule from local PDT data.
- `r_AB=r_A r_B` is dimension-independent and cannot select `n=3`.
- It supplies no same-input `P_PDT != P_QM` prediction.
- It strengthens the target: PDT must derive or physically constrain the joint admissible-effect generator, not merely choose a scalar divergence or quotient notation.

## Prior-art boundary
The kernel/quotient identity is standard tensor-product linear algebra. Product-vs-global measurement freedom is also familiar from operational/GPT and quantum-information frameworks. The result is therefore **not new mathematics**. Its PDT value is architectural: it identifies the exact missing object as the resource-window rule generating admissible joint effects.

## Classification
- factorized quotient identity: **PROVED (conditional on W_AB=W_A tensor W_B)**
- resolved-rank multiplication: **PROVED (same hypothesis)**
- local resource windows uniquely determine joint admissible effects: **FALSIFIED**
- product-rank law implies `n=3`: **FALSIFIED**
- theorem as mathematical novelty: **IMPORTED/KNOWN infrastructure**
- PDT-native physical selector for joint effects: **OPEN**
- same-input PDT/QM deviation: **OPEN**
- breakthrough candidate: **NO**
