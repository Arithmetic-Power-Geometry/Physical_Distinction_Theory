# Cycle 267 — Resource-additivity capacity no-go

## Target
Attack the missing PDT-II upper-bound/capacity side identified in Cycle 266, with priority on a PDT-native resource-refinement law that might select exact `n=3`.

## Candidate principle under test
A natural candidate is to identify a PDT distinction capacity `C_R(S)` with a resource monotone and demand:

1. normalization/nonnegativity;
2. monotonicity under declared free/resource-nonincreasing maps;
3. tensor additivity `C_R(A ⊗ B)=C_R(A)+C_R(B)`;
4. refinement monotonicity: enlarging the admissible resource window cannot reduce operational distinguishability/capacity.

Question: can these properties, without inserting a dimension-dependent normalization or ceiling, imply `n<=3` and hence close the exact-`n=3` obligation?

## Theorem — additive-resource axioms do not create a finite ambient-dimension ceiling
Let `{S_n}` be a nested family of finite-dimensional operational systems with resource-preserving embeddings `i_{n,m}:S_n→S_m` for `m>=n`. Let `C_R` be any capacity/resource functional such that:

- `C_R` is monotone under the embeddings (or invariant when the embedding and its restriction are free), and
- tensor composition is additive whenever defined.

Then these axioms alone cannot imply a strict universal ceiling `n<=N` for any finite `N` while admitting `S_N` and all resource-preserving embeddings.

### Proof
Assume `S_N` is admissible. By hypothesis there is a resource-preserving embedding `i_{N,N+1}:S_N→S_{N+1}`. Monotonicity/invariance gives a valid realization of every `S_N` resource task inside `S_{N+1}`. Additivity constrains how `C_R` behaves on composites but supplies no contradiction with the existence of the extra orthogonal/operational sector in `S_{N+1}`. Therefore a conclusion `n<=N` cannot follow from monotonicity plus additivity alone. Any such finite ceiling must enter through an additional non-hereditary premise that fails for `S_{N+1}` (for example a separately derived global budget/maximality law). QED.

This is a structural no-go: additivity can govern resource *scaling* after composition is specified, but it does not by itself bound the size of the ambient carrier.

## Stronger counterexample to naive additivity
Even treating exact additivity as a universal resource principle is unsafe. Standard quantum resource theories contain legitimate monotones that are strictly subadditive. In stabilizer/magic theory, the relative entropy of magic has known strict-subadditivity examples, motivating regularization. Thus `C(A⊗B)=C(A)+C(B)` cannot be promoted as a generic PDT resource law merely from monotonicity/refinement.

Conversely, special resource measures can be additive under tensor products (e.g. particular max-relative-entropy/channel quantities), so observing additivity does not uniquely select a composition theory or ambient dimension.

## Exact dimension stress n=1..12
For the dimension family itself, take the standard additive information capacity `C(n)=log n`. Then
`C(nm)=C(n)+C(m)`
for every positive integer pair. The law is valid at `n=1,2,...,12` and arbitrarily higher `n`; it has no special point at 3. Any monotone reparameterization that singles out 3 by an externally inserted cap simply assumes the missing upper-bound information.

Smallest decisive competitor to a proposed `additivity => n=3` rule: `n=2` already satisfies the same logarithmic composition law, and `n=4` demonstrates that the law continues above 3.

## Edge/composite/resource checks
- `n=1`: `C=0`, additive identity/degenerate carrier.
- `n=2,3,...,12`: exact algebraic equality under multiplicative dimension composition.
- composites: `n_A n_B` preserves log-additivity for all finite dimensions.
- restricted windows: monotonicity under window refinement can order capacities but does not supply an absolute dimension ceiling unless a global budget is independently postulated/derived.
- pure/mixed states: state-level resource monotones may have different additivity behavior; therefore carrier-level dimension selection cannot be inferred from generic state-resource additivity.
- dynamics/environment: allowing catalysts, correlations, records, or non-Markovian environments makes universal one-shot additivity still less defensible; such structure must be declared in `R` rather than hidden in a dimension selector.

## Prior-art boundary
Resource monotonicity, tensor additivity/subadditivity, regularization, catalytic resource conversion, and relative-entropy resource measures are established resource-theory machinery. In particular, the resource theory of stabilizer quantum computation records strict subadditivity of relative entropy of magic for some states and uses regularization asymptotically. Wilming, Gallego & Eisert characterize quantum relative entropy/free energy using axioms including tensor additivity and superadditivity. These facts are **IMPORTED/KNOWN**, not PDT discoveries.

The PDT-specific value of this cycle is negative/architectural: it blocks an invalid route from generic resource refinement/additivity to the missing exact-dimension upper bound.

## Classification
- Resource monotonicity/additivity as general machinery: **IMPORTED/KNOWN**.
- `C(n)=log n` exact tensor-additive dimension family: **PROVED**.
- Generic monotonicity + tensor additivity => finite ambient-dimension ceiling: **FALSIFIED** under the stated embedding hypotheses.
- Generic resource monotone must be exactly additive: **FALSIFIED** by known strict-subadditivity examples.
- Resource-window refinement alone => `n<=3`: **FALSIFIED / underdetermined** without a separately derived global budget or non-hereditary condition.
- PDT-native global budget/maximality law: **OPEN**.
- PDT-native composition law: **OPEN**.
- Same-input `P_PDT != P_QM` with an explicitly changed operational primitive: **OPEN**.
- BREAKTHROUGH CANDIDATE: **NO**.

## Next attack
Do not use generic resource monotonicity or tensor additivity as the missing upper-bound axiom. Attack whether PDT's own distinction bookkeeping can derive a *global finite budget* from first principles. The candidate must be non-hereditary, composition-consistent, resource-window explicit, and must fail above 3 for a reason not equivalent to inserting `3` into a normalization, rank cap, cross-product/Jacobi assumption, or microscopic input.
